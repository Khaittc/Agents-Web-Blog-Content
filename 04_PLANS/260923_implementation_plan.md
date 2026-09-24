# Kế hoạch Triển khai Phase 2: Hoàn thiện Bộ Quy chuẩn Phụ trợ & Bài viết Stress-test BLOG_02
**Mã kế hoạch**: `260923_implementation_plan`  
**Ngày lập**: 23/09/2026  
**Trạng thái**: ✅ **ĐÃ THỰC THI HOÀN TẤT (EXECUTED & READY FOR USER REVIEW)**

Tài liệu này chi tiết hóa các bước thực hiện tiếp theo theo đúng [ROADMAP.md](file:///d:/Agents_Tools/05_WebsiteTTC/ROADMAP.md) nhằm hoàn thiện các tài liệu chuẩn hóa còn thiếu trong `00_SKILL/` trước khi tiến hành viết bài mẫu thứ 2.

---

## 1. MỤC TIÊU CẦN DUYỆT (USER REVIEW REQUIRED)

> [!IMPORTANT]
> **Kết quả thực hiện kế hoạch**:
> 1. [x] **Bước 1 (Xây dựng 3 quy chuẩn kỹ năng phụ trợ trong `00_SKILL/`) — ĐÃ HOÀN THÀNH**:
>    - [x] `SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md`: Quy định rõ nguồn cấp 1 (Tier 1), cấp 2 (Tier 2), cấp 3 (Tier 3), cách giải quyết mâu thuẫn số liệu kỹ thuật giữa các tài liệu.
>    - [x] `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md`: Quy chuẩn và bảng checklist ma trận để Tech Review Agent chấm điểm đạt/không đạt (*Citation Audit*, *Formula Audit*, *Fact-Check*).
>    - [x] `IMAGE_PROMPT_STYLE_GUIDE_v1.0.md`: Quy chuẩn tạo prompt cho hình ảnh Featured Image (808x500 px) và thông số kỹ thuật cho biểu đồ minh họa.
> 2. [x] **Bước 2 (Triển khai bài viết mẫu thứ 2 - Stress-test `BLOG-T01`) — ĐÃ HOÀN THÀNH**:
>    - Đã xuất bản trọn gói tại `03_Articles/BLOG_02_He_so_cong_suat_va_Song_hai/`:
>      - `evidence_dossier.md` (Research Agent)
>      - `draft_review_package.md` (Drafting Agent)
>      - `technical_audit_report.md` (Tech Review Agent - PASS)
>      - `bai-viet-he-so-cong-suat-va-song-hai-ckeditor.html` (Publisher Agent)
>      - `article_status.json` (`status: "IN_REVIEW"`)



---

## 2. CHI TIẾT CÁC THAY ĐỔI DỰ KIẾN (PROPOSED CHANGES)

Tất cả các thay đổi sẽ diễn ra **100% bên trong thư mục `d:/Agents_Tools/05_WebsiteTTC`**:

### Nhóm 1: Bổ sung 3 chuẩn kỹ năng trong `00_SKILL/`

#### [NEW] [00_SKILL/SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md)
- Định nghĩa phân cấp nguồn tài liệu kỹ thuật:
  - **Tier 1 (Nguồn gốc tối cao)**: Tiêu chuẩn IEC, IEEE, ISO; Nameplate & Datasheet chính thức của hãng sản xuất thiết bị (ABB, Siemens, Schneider...).
  - **Tier 2 (Nguồn chuyên gia / Tổ chức)**: Hướng dẫn kỹ thuật của Cục Năng lượng (US DOE), sách chuyên khảo đại học, báo cáo thử nghiệm độc lập.
  - **Tier 3 (Nguồn tham khảo phụ trợ)**: Bài báo kỹ thuật, bài phân tích kỹ sư trên web chuyên ngành.
- Quy tắc giải quyết xung đột dữ liệu: Tier cao hơn luôn ghi đè Tier thấp hơn; khi cùng Tier, ưu tiên tài liệu mới nhất hoặc điều kiện thử nghiệm tương đồng nhất.

#### [NEW] [00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md)
- Tiêu chí đánh giá kiểm duyệt kỹ thuật (Review Protocol):
  - Ma trận Audit Citation (100% nguồn có verified locator hoặc đánh dấu cảnh báo).
  - Ma trận Audit Formula (Kiểm tra thứ nguyên đơn vị SI, tính hợp lệ cú pháp LaTeX, định nghĩa biến số).
  - Ma trận Kiểm tra tính khách quan (Loại bỏ các từ ngữ tuyệt đối hóa, quảng cáo thương mại, tự bịa số liệu).
- Mẫu báo cáo kiểm duyệt `technical_audit_report.md`.

#### [NEW] [00_SKILL/IMAGE_PROMPT_STYLE_GUIDE_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IMAGE_PROMPT_STYLE_GUIDE_v1.0.md)
- Chuẩn hóa tỷ lệ và độ phân giải hình ảnh website:
  - Featured Image: tỷ lệ chuẩn `808 × 500 px`.
  - Bộ từ khóa phong cách nhận diện Real Group (Industrial, clean, professional engineering, high dynamic range, no blurry/distorted elements).
- Quy chuẩn tạo sơ đồ kỹ thuật (Technical Figures: Flowchart, biểu đồ vector, ma trận so sánh).

---

### Nhóm 2: Quản trị Tiến độ Dự án

#### [MODIFY] [ROADMAP.md](file:///d:/Agents_Tools/05_WebsiteTTC/ROADMAP.md)
- Đánh dấu hoàn thành các đầu mục tài liệu quy chuẩn mới tạo trong Phase 2.

#### [MODIFY] [WORKLOG.md](file:///d:/Agents_Tools/05_WebsiteTTC/WORKLOG.md)
- Cập nhật nhật ký phiên làm việc và các quyết định kiến trúc mới.

---

## 3. KẾ HOẠCH KIỂM TRA & XÁC NHẬN (VERIFICATION PLAN)

### Kiểm tra Tự động
- Kiểm tra toàn bộ file tạo mới bằng công cụ quét file trong workspace.
- Kiểm tra tính toàn vẹn của các liên kết markdown.

### Kiểm tra Kỹ thuật
- Đảm bảo các quy chuẩn mới ăn khớp 100% với 4 quy chuẩn cốt lõi đã có (`BLOG_CONTENT_STRUCTURE_STANDARD`, `IEEE_CITATION_REFERENCE_SKILL`, `LATEX_FORMULA_SKILL`, `REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE`).
