# BỘ QUY CHUẨN TRÍCH DẪN & THAM CHIẾU IEEE TỔNG THỂ (IEEE CITATION & REFERENCE MASTER SUITE)
**Version**: 2.0 (Kiến trúc Đa Kỹ năng Chuyên biệt - Modular Architecture)  
**Mã tài liệu**: `IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0`  
**Trạng thái**: Áp dụng chính thức cho toàn bộ 5 Role AI Agents  
**Ngày ban hành**: 23/09/2026  
**Thay thế**: `IEEE_CITATION_REFERENCE_SKILL_v1.3.md` (Đã chuyển vào `00_SKILL/archive/` làm tài liệu tra cứu mở rộng)  
**Quyết định kiến trúc**: **ADR-012** (Tách nguyên khối thành 4 Sub-Skills chuyên biệt & Khóa cửa ải chống link ảo)  

---

## 1. TỔNG QUAN KIẾN TRÚC MODULAR SUITE

Để khắc phục triệt để tình trạng quá tải ngữ cảnh của tệp nguyên khối cũ (2.204 dòng) và giải quyết tận gốc nguy cơ AI suy đoán link ảo (404), hệ thống trích dẫn IEEE của Real Group được tái cấu trúc thành **Bộ 4 Sub-Skills độc lập, khép kín theo đúng vòng đời bài viết**:

```text
                                  ┌────────────────────────────────────────────────────────┐
                                  │   IEEE CITATION & REFERENCE MASTER SUITE v2.0          │
                                  └────────────────────────────────────────────────────────┘
                                                               │
          ┌─────────────────────────────┬───────────────────────┴───────────────────────┬─────────────────────────────┐
          ▼                             ▼                                               ▼                             ▼
┌─────────────────────────┐   ┌─────────────────────────┐                     ┌─────────────────────────┐   ┌─────────────────────────┐
│ IEEE-01: SOURCE IDENT & │   │ IEEE-02: IN-TEXT        │                     │ IEEE-03: REFERENCE      │   │ IEEE-04: CITATION       │
│ LIVE URL CHECK          │   │ CITATIONS & LOCATORS    │                     │ NAMING & CKEDITOR STYLE │   │ AUDIT PROTOCOL          │
├─────────────────────────┤   ├─────────────────────────┤                     ├─────────────────────────┤   ├─────────────────────────┤
│ • 10 loại hình kỹ thuật │   │ • Đánh số tuyến tính [n]│                     │ • Khuôn mẫu 10 loại hình│   │ • 6 Cửa ải kiểm định    │
│ • LIVE-CHECK URL 200    │   │ • Cú pháp rời [1], [2]  │                     │ • Standards/Manuals đầu │   │ • Test 100% link sống   │
│ • CẤM TUYỆT ĐỐI LINK ẢO │   │ • CẤM gạch nối [1]–[3]  │                     │ • Reports/Blogs ngoặc kép│  │ • Fact-check tài liệu   │
│ • Trích xuất Metadata   │   │ • Locator (p., eq., Tab)│                     │ • Link bấm được <a>     │   │ • Gate 5: VỊ TRÍ CUỐI CÂU│
│                         │   │ • VỊ TRÍ LUÔN Ở CUỐI CÂU│                     │                         │   │ • Chữ ký duyệt PASS/FAIL│
├─────────────────────────┤   ├─────────────────────────┤                     ├─────────────────────────┤   ├─────────────────────────┤
│ Phụ trách:              │   │ Phụ trách:              │                     │ Phụ trách:              │   │ Phụ trách:              │
│ ➔ RESEARCH AGENT        │   │ ➔ DRAFTING AGENT        │                     │ ➔ DRAFTING & PUBLISHER  │   │ ➔ TECH REVIEW AGENT     │
└─────────────────────────┘   └─────────────────────────┘                     └─────────────────────────┘   └─────────────────────────┘
```

---

## 2. DANH MỤC 4 SUB-SKILLS & LIÊN KẾT TRUY CẬP

| Mã Sub-Skill | Tên tệp kỹ năng | Agent chính | Nhiệm vụ cốt lõi |
|:---|:---|:---|:---|
| **`IEEE-01`** | [IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.1.md) | **Research Agent** | Nhận diện 10 loại hình nguồn tài liệu; bắt buộc dùng tool kiểm tra URL sống (HTTP 200); **Cửa ải Điều hướng Trực tiếp (ADR-015)**: link sâu/link tải trực tiếp, cấm dùng link trang chủ hay thư viện chung chung, đối chiếu khớp tiêu đề trang. |
| **`IEEE-02`** | [IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md) | **Drafting Agent** | Đánh số tăng dần liên tục trong bài viết; cú pháp ngoặc rời `[1], [2], [3]` (cấm gạch nối `[1]–[3]`); gắn bộ định vị chi tiết; **100% trích dẫn bắt buộc đặt ở CUỐI CÂU** (trước dấu chấm hoặc dấu hai chấm). |
| **`IEEE-03`** | [IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL_v1.1.md) | **Drafting & Publisher** | Áp dụng cấu trúc đặt tên IEEE chuẩn cho 10 loại tài liệu; quy chuẩn xuất bản CKEditor 3.6.6.2 (thụt lề treo, tạo link bấm trực tiếp `<a href="..." target="_blank">`, chuẩn responsive đa thiết bị ADR-016 với `word-break: break-all;` chống vỡ layout mobile). |
| **`IEEE-04`** | [IEEE_04_CITATION_AUDIT_PROTOCOL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_04_CITATION_AUDIT_PROTOCOL_v1.1.md) | **Tech Review Agent** | Quy trình kiểm duyệt 6 cửa ải (Gate 1: Live URL 200, Gate 2: Tác giả thật, Gate 3: Fact-Check, Gate 4: Naming Pattern, Gate 5: Bracket Syntax & Vị trí Cuối câu, Gate 6: Locator). |

---

## 3. TÀI LIỆU TRA CỨU MỞ RỘNG (EXHAUSTIVE ARCHIVE DICTIONARY)

Khi gặp các trường hợp trích dẫn hiếm gặp (Bằng sáng chế - Patents, Luận án tiến sĩ nước ngoài, Băng ghi âm, Luật và văn bản quy phạm pháp luật...), các Agent có thể tra cứu toàn văn trong tệp lưu trữ:
- **Tệp từ điển mở rộng**: [00_SKILL/archive/IEEE_CITATION_REFERENCE_SKILL_v1.3.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/archive/IEEE_CITATION_REFERENCE_SKILL_v1.3.md) (2.204 dòng, đồng bộ đầy đủ toàn bộ IEEE Reference Guide V 3.28.2025).

---

## 4. HỢP ĐỒNG LIÊN TẦNG (INTER-AGENT CITATION CONTRACT)

1. **Khâu Nghiên cứu (Research)**: Research Agent **chỉ được phép bàn giao** các nguồn đã được xác thực link sống (HTTP 200) và locator trong `evidence_dossier.md` (Tuân thủ `IEEE-01`).
2. **Khâu Soạn thảo (Drafting)**: Drafting Agent **không được tự bịa nguồn mới** ngoài `evidence_dossier.md`; đánh số tuyến tính, gắn đúng locator và **bắt buộc 100% trích dẫn nằm ở CUỐI CÂU**, không ngắt quãng mạch văn (Tuân thủ `IEEE-02 v1.1` & `IEEE-03`).
3. **Khâu Kiểm duyệt (Review)**: Tech Review Agent **click kiểm tra 100% URL**, kiểm tra cú pháp ngoặc và vị trí cuối câu; nếu phát hiện bất kỳ link nào 404 hoặc đặt sai vị trí giữa câu, bài viết lập tức bị từ chối phê duyệt (Tuân thủ `IEEE-04 v1.1`).
4. **Khâu Xuất bản (Publishing)**: Publisher Agent **bắt buộc bọc mọi URL trong thẻ `<a>`** có `target="_blank"` để người đọc click mở trực tiếp bài gốc trong 1 giây (Tuân thủ `IEEE-03`).
