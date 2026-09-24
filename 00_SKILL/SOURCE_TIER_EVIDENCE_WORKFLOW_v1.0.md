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

Theo chuẩn [IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0.md):
1. **Không trích dẫn chung chung**: Một cuốn sách 500 trang hoặc tiêu chuẩn 100 trang không được trích dẫn chỉ bằng tên tài liệu nếu tuyên bố mang tính định lượng cụ thể.
2. **Cấu trúc Locator hợp lệ**:
   - Số trang: `[1, p. 45]` hoặc `[1, pp. 45–48]`
   - Chương / Mục: `[2, Sec. 3.2]`
   - Bảng số liệu: `[3, Tab. 4]`
   - Công thức: `[1, eq. (3)]`
3. **Trường hợp chưa xác minh được trang cụ thể**: Chỉ ghi trích dẫn số `[1]` và đánh dấu cờ `LOCATOR_PENDING` trong báo cáo bằng chứng nội bộ để Tech Review Agent rà soát.

---

## 5. HỒ SƠ BẰNG CHỨNG (EVIDENCE DOSSIER CONTRACT)

Trước khi chuyển sang khâu viết, Research Agent phải tạo file `evidence_dossier.md` trong thư mục bài viết với cấu trúc bắt buộc có trường **Loại hình tài liệu (Source Type)** và **Trạng thái URL** tuân thủ [IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.0.md):

```markdown
# EVIDENCE DOSSIER — [MÃ BÀI VIẾT]

## 1. Danh sách Nguồn (Source Registry)
| ID | Phân tầng | Loại hình (Source Type) | Chuẩn trích dẫn IEEE chính thức (Official IEEE Reference) | Năm | Định danh / Mã chuẩn |
|---|---|---|---|---|---|
| [1] | Tier 1 | `STANDARD` | *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. | 2022 | IEEE Std 519-2022 |
| [2] | Tier 1 | `MANUAL` | *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, Rueil-Malmaison, France, 2018. | 2018 | Schneider Tech Guide |
| [3] | Tier 2 | `TECH_REPORT` | “Improving motor and drive system performance: A sourcebook for industry,” US Department of Energy (DOE), Washington, DC, USA, Rep. DOE/GO-102014-4421, 2014. | 2014 | DOE/GO-102014-4421 |
| [4] | Tier 3 | `BLOG_POST` | J. Smith, “Understanding total harmonic distortion in industrial power,” *Schneider Electric Blog*, Oct. 15, 2023. Accessed: Mar. 10, 2026. [Online]. Available: URL | 2023 | Blog kỹ thuật hãng |

## 2. Bảng Trích xuất Dữ liệu (Fact Registry)
| ID | Tuyên bố / Số liệu / Công thức | Nguồn & Locator | Tier | Trạng thái Thẩm định |
|---|---|---|---|---|
| F01 | Công thức tính hệ số tải từ công suất thực P_in | [2, p. 2, eq. (2)] | Tier 2 | VERIFIED |
| F02 | Hiệu suất động cơ duy trì gần như phẳng từ 50% đến 100% | [2, p. 1] & [1, p. 14] | Tier 1/2 | VERIFIED |

## 3. Các Xung đột Đã xử lý (Resolved Conflicts)
- Ghi nhận xung đột và lý do chọn số liệu.
```
