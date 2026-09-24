# QUY TRÌNH PHÂN TẦNG VÀ THẨM ĐỊNH BẰNG CHỨNG KỸ THUẬT (SOURCE TIER & EVIDENCE WORKFLOW)
Version: 1.0
Trạng thái: Áp dụng chính thức cho Research & Evidence Agent
Phạm vi: Toàn bộ bài viết kỹ thuật (Blog / Solution) cho Real Group (`real-group.org`)

---

## 1. MỤC ĐÍCH

Tài liệu này chuẩn hóa quy trình:
1. Phân loại và xếp tầng độ tin cậy của tài liệu tham khảo kỹ thuật (**Source Tiering**).
2. Xử lý và giải quyết mâu thuẫn số liệu kỹ thuật giữa các nguồn (**Data Conflict Resolution**).
3. Xác minh số định vị cụ thể (**Verified Locator Protocol** — số trang, số chương, bảng biểu).
4. Thiết lập hồ sơ bằng chứng (**Evidence Dossier**) trước khi chuyển giao cho Drafting Agent.

Tài liệu này phối hợp trực tiếp với [IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md) (đặc biệt là Sub-skill `IEEE-01`) để đảm bảo mọi tuyên bố kỹ thuật (technical claims) đều có thể truy nguyên 100%.

---

## 2. PHÂN CẤP TẦNG NGUỒN (SOURCE TIER HIERARCHY)

Mọi tài liệu phục vụ biên soạn bài viết bắt buộc phải được xếp vào một trong 3 tầng giá trị kỹ thuật sau:

```text
┌─────────────────────────────────────────────────────────────┐
│ TIER 1: TIÊU CHUẨN QUỐC TẾ & TÀI LIỆU CHÍNH HÃNG           │
│ (IEC, IEEE, ISO, NEMA, Datasheets/Manuals Siemens, ABB...)  │
└──────────────────────────────┬──────────────────────────────┘
                               │ Ưu tiên tuyệt đối
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TIER 2: SỔ TAY KỸ THUẬT & TỔ CHỨC NĂNG LƯỢNG QUỐC GIA       │
│ (US DOE, EPRI, Sách chuyên khảo đại học, Báo cáo kiểm định) │
└──────────────────────────────┬──────────────────────────────┘
                               │ Hỗ trợ ngữ cảnh thực nghiệm
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TIER 3: BÀI BÁO KHOA HỌC & PHÂN TÍCH CHUYÊN GIA WEB         │
│ (Tạp chí kỹ thuật, Whitepapers, Web kỹ thuật đã kiểm chứng) │
└─────────────────────────────────────────────────────────────┘
```

### 2.1. Tier 1 — Nguồn Chuẩn Quốc Tế & Nhà Sản Xuất (Primary Engineering Authority)
- **Bao gồm**:
  - Tiêu chuẩn quốc tế: IEC (ví dụ: IEC 60034 cho động cơ), IEEE (ví dụ: IEEE 519 cho sóng hài), ISO, NEMA.
  - Tài liệu kỹ thuật chính hãng: Nameplate, Catalog, Hardware Manual, Technical Guidebook do chính nhà sản xuất thiết bị phát hành (Siemens, ABB, Schneider Electric, Danfoss, Mitsubishi Electric, Rockwell Automation...).
- **Độ tin cậy**: Cao nhất. Số liệu, công thức và ngưỡng kỹ thuật từ Tier 1 được coi là chuẩn tham chiếu mặc định.

### 2.2. Tier 2 — Tài liệu Thể chế & Chuyên khảo Học thuật (Institutional & Textbook Authority)
- **Bao gồm**:
  - Tài liệu của các cơ quan năng lượng/chính phủ: US Department of Energy (DOE - ví dụ: Motor Systems Tip Sheets), Viện Nghiên cứu Điện năng EPRI, Trung tâm Khuyến nông Năng lượng Quốc gia.
  - Giáo trình kỹ thuật đại học chính quy (Electrical Machines, Power Systems Analysis của các NXB: Wiley, McGraw-Hill, Springer, NXB ĐHQG).
  - Báo cáo thử nghiệm độc lập của các phòng lab được công nhận (KEMA, UL, TÜV).
- **Độ tin cậy**: Rất cao. Phù hợp cho việc giải thích nguyên lý, phương pháp đo thực tế và kinh nghiệm vận hành.

### 2.3. Tier 3 — Báo cáo Ngành & Tạp chí Kỹ thuật (Industry Articles & Whitepapers)
- **Bao gồm**:
  - Bài viết chuyên sâu trên các tạp chí ngành: Plant Services, Efficient Plant, Electrical Engineering Portal (EEP), Control Engineering.
  - Whitepaper của các hãng tích hợp hệ thống uy tín.
- **Độ tin cậy**: Khá. Chỉ dùng để bổ sung ví dụ thực tế hoặc góc nhìn vận hành. Không dùng Tier 3 để phủ nhận thông số của Tier 1.

### 2.4. Nguồn Bị Cấm Tuyệt Đối (Unacceptable Sources)
- Bài viết SEO quảng cáo bán hàng chung chung, không có tác giả chuyên môn.
- Trang hỏi đáp không kiểm duyệt (Quora, Reddit, diễn đàn tự do không có trích dẫn tài liệu gốc).
- Nội dung do AI tự tạo ra mà không có trích dẫn nguồn gốc (AI Hallucinated Text).

---

## 3. NGUYÊN TẮC GIẢI QUYẾT XUNG ĐỘT SỐ LIỆU (DATA CONFLICT RESOLUTION)

Khi xuất hiện sự khác biệt về số liệu, công thức hoặc ngưỡng giữa các tài liệu, Agent áp dụng quy tắc:

1. **Quy tắc Phân tầng (Tier Override)**:
   ```text
   Tier 1 > Tier 2 > Tier 3
   ```
   *Ví dụ*: Nếu một bài blog Tier 3 ghi "động cơ dưới 60% là non tải", nhưng tài liệu Tier 2 của DOE xác định ngưỡng suy giảm hiệu suất rõ rệt là dưới 50% tải, Agent **bắt buộc tuân theo Tier 2 (DOE)** và nêu rõ điều kiện áp dụng.

2. **Quy tắc Đồng tầng (Same Tier Precedence)**:
   - **Phiên bản mới hơn ưu tiên hơn**: Tiêu chuẩn IEC 60034-30-1:2014 thay thế cho bản 2008.
   - **Đặc tính chuyên biệt ưu tiên hơn hướng dẫn tổng quát**: Manual cụ thể của dòng biến tần ABB ACS880 ghi đè tài liệu hướng dẫn biến tần chung của hãng.
   - **Nêu rõ giả thiết đo lường**: Nếu 2 nguồn Tier 1 đưa ra giá trị khác nhau do điều kiện thử nghiệm khác nhau (ví dụ: ở 40°C ambient vs 25°C ambient), Agent **bắt buộc phải ghi rõ điều kiện môi trường** thay vì chỉ đưa ra một con số duy nhất.

---

## 4. QUY TRÌNH XÁC MINH SỐ ĐỊNH VỊ (VERIFIED LOCATOR PROTOCOL)

Theo chuẩn [IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md):
1. **Không trích dẫn chung chung**: Một cuốn sách 500 trang hoặc tiêu chuẩn 100 trang không được trích dẫn chỉ bằng tên tài liệu nếu tuyên bố mang tính định lượng cụ thể.
2. **Cấu trúc Locator hợp lệ trong hồ sơ nghiên cứu**:
   - Số trang: `p. 45` hoặc `pp. 45–48`
   - Chương / Mục: `Sec. 3.2`
   - Bảng số liệu: `Tab. 4`
   - Công thức: `eq. (3)`
3. **Trường hợp chưa xác minh được trang cụ thể**: Đánh dấu cờ `LOCATOR_NOT_CHECKED` trong `evidence.json`. Drafting Agent khi đó chỉ được phép dùng trích dẫn số `[n]` đơn thuần ở cuối câu, **tuyệt đối không được tự suy đoán số trang**.

---

## 5. HỒ SƠ BẰNG CHỨNG SONG HÀNH (EVIDENCE DOSSIER & EVIDENCE.JSON)

Research Agent bắt buộc phải tạo song song:
1. **`evidence.json`**: Tệp dữ liệu máy đọc canonical tuân thủ `02_AGENT_TEMPLATES/contracts/evidence.schema.json`.
2. **`evidence_dossier.md`**: Báo cáo tổng hợp bằng chứng kỹ thuật dành cho Kỹ sư trưởng đọc và thẩm định.

> [!IMPORTANT]
> **QUY TẮC STABLE SOURCE ID & TÁCH BẠCH HTTP 200 (PHASE 2.5 ARCHITECTURE HARDENING)**:
> 1. **STABLE SOURCE ID (`SRC-xxx`)**: Nghiên cứu chỉ cấp phát mã định danh ổn định `SRC-001`, `SRC-002`, `SRC-003`,... Tuyệt đối KHÔNG gán số trích dẫn IEEE `[1]`, `[2]` ở giai đoạn này. Số IEEE sẽ do Drafting Agent gán dựa trên thứ tự xuất hiện đầu tiên trong bài viết.
> 2. **TÁCH BẠCH KIỂM CHỨNG**:
>    ```text
>    URL ACCESS (HTTP 200) ≠ CONTENT IDENTITY ≠ CLAIM VERIFIED ≠ LOCATOR VERIFIED
>    ```
>    HTTP 200 chỉ chứng minh đường truyền mạng hoạt động, **KHÔNG ĐƯỢC COI HTTP 200 LÀ BẰNG CHỨNG NỘI DUNG CLAIM ĐÃ ĐÚNG**. Phải có xác nhận đối chiếu văn bản gốc.

```markdown
# EVIDENCE DOSSIER — [MÃ BÀI VIẾT]

## 1. Danh sách Nguồn Ổn định (Stable Source Registry)
| Source ID | Phân tầng | Loại hình (Source Type) | Chuẩn trích dẫn IEEE chính thức (Official IEEE Reference) | Năm | Link Trực tiếp (Verified URL) | Trạng thái Mạng | Content ID | Claim Verified | Locator Verified |
|:---:|:---:|:---|:---|:---:|:---|:---:|:---:|:---:|:---:|
| `SRC-001` | Tier 1 | `STANDARD` | *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. | 2022 | `https://...` | HTTP 200 OK | YES | YES | YES (Tab. 1, p. 12) |
| `SRC-002` | Tier 1 | `MANUAL` | *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, 2018. | 2018 | `https://...` | HTTP 200 OK | YES | YES | YES (Sec. 3, p. 45) |
| `SRC-003` | Tier 2 | `TECH_REPORT` | “Improving motor and drive system performance: A sourcebook for industry,” US DOE, Rep. DOE/GO-102014-4421, 2014. | 2014 | `https://...` | HTTP 200 OK | YES | YES | YES (p. 24) |
| `SRC-004` | Tier 3 | `BLOG_POST` | J. Smith, “Understanding total harmonic distortion in industrial power,” *Schneider Electric Blog*, 2023. | 2023 | `https://...` | HTTP 200 OK | YES | YES | NO (LOCATOR_NOT_CHECKED) |

## 2. Bảng Trích xuất Dữ liệu (Fact Registry)
| Fact ID | Tuyên bố / Số liệu / Công thức | Nguồn (Source ID) & Locator | Tier | Trạng thái Thẩm định |
|:---:|:---|:---|:---:|:---:|
| F01 | Công thức tính hệ số tải từ công suất thực P_in | `SRC-002`, p. 2, eq. (2) | Tier 2 | VERIFIED |
| F02 | Hiệu suất động cơ duy trì gần như phẳng từ 50% đến 100% | `SRC-003`, p. 24 | Tier 2 | VERIFIED |

## 3. Các Xung đột Đã xử lý (Resolved Conflicts)
- Ghi nhận xung đột và lý do chọn số liệu.
```
