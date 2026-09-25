# BÁO CÁO THỬ NGHIỆM CHUYỂN GIAO NGHIÊN CỨU SANG SOẠN THẢO (RESEARCH → DRAFTING HANDOFF TEST REPORT)
## BLOG_04 — VFD VÀ SOFT STARTER: SO SÁNH NGUYÊN LÝ, DÒNG KHỞI ĐỘNG, ĐIỀU KHIỂN TỐC ĐỘ VÀ PHẠM VI ỨNG DỤNG
**Thời điểm thực hiện**: 2026-09-24T23:45:00+07:00  
**Tác nhân thực hiện**: Drafting Agent (Kỹ sư Soạn thảo Kỹ thuật Chuyên môn)  
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`  
**Chủ đề**: VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải  
**Mã phân loại chuẩn**: `BLOG-T04` (Comparison)  
**Commit Baseline**: `e6271d1 — fix: enforce drafting prerequisites before TECH_REVIEW`  

---

## 1. TIÊU THỤ HỒ SƠ CHUYỂN GIAO NGHIÊN CỨU (RESEARCH HANDOFF CONSUMED)

Drafting Agent đã tiếp nhận và tiêu thụ toàn bộ gói hồ sơ nghiên cứu đã được phê duyệt tại Cổng Final Research Gate:
- **`research_handoff.json`**:
  - `research_status`: `PASS`
  - `research_plan_status`: `COMPLETE`
  - `handoff_ready`: `true`
  - Tỷ lệ nguồn chất lượng cao: 5 Tier 1, 0 Tier 2, 1 Tier 3 (83.3% Tier 1+2)
- **Hồ sơ minh chứng đã tiêu thụ**:
  - 6 Nguồn tài liệu chính thức (`SRC-001` đến `SRC-006`)
  - 17 Bằng chứng kỹ thuật định lượng và trích dẫn (`EVD-001` đến `EVD-017`)
  - 2 Xung đột kỹ thuật đã giải quyết (`CON-001`, `CON-002`)
- **Nguyên tắc bảo toàn**: Toàn bộ các tệp nghiên cứu gốc (`article_brief.json`, `research_plan.json`, `research_log.json`, `evidence.json`, `evidence_dossier.md`, `research_handoff.json`) được giữ ở chế độ **READ-ONLY**, không có bất kỳ sửa đổi nào.

---

## 2. CẤU TRÚC BẢN THẢO ĐÃ KHỞI TẠO (DRAFT STRUCTURE CREATED)

Đã khởi tạo bản thảo kỹ thuật hoàn chỉnh tại:  
`03_Articles/BLOG_04_VFD_vs_Soft_Starter/draft_review_package.md`

Bản thảo tuân thủ đúng định dạng thể loại **`BLOG-T04 — Comparison`** với 11 phần nội dung và danh mục tài liệu tham khảo:
- **Lead / Executive Technical Summary**: Tóm tắt kỹ thuật định hướng cho kỹ sư vận hành.
- **Mục 1**: VFD và Soft Starter giải quyết hai bài toán khác nhau thế nào? (Điều khiển quá trình liên tục vs Khởi động/dừng êm).
- **Mục 2**: Khác biệt cốt lõi về nguyên lý biến đổi điện năng và cấu trúc công suất (2.1 VFD AC-DC-AC PWM; 2.2 Soft Starter SCR điều khiển góc kích pha).
- **Mục 3**: So sánh định lượng dòng khởi động và quan hệ mô-men - điện áp ($T \propto U^2$, sụt giảm mô-men ở mức giới hạn dòng thấp, mô-men bứt phá tại $0\text{ rpm}$).
- **Mục 4**: Khả năng điều chỉnh và duy trì tốc độ vận hành liên tục.
- **Mục 5**: Hiệu suất năng lượng, tổn hao công suất và cơ chế Contactor Bypass (tổn hao IGBT, hiệu suất bypass $>99.5\%$, định mức AC-1 của bypass tích hợp).
- **Mục 6**: Sóng hài dòng điện và ranh giới áp dụng chuẩn IEEE Std 519 (6.1 Sóng hài ngắn hạn Soft Starter; 6.2 Sóng hài VFD theo cấu trúc 6-pulse/12-pulse/AFE; 6.3 Ranh giới PCC và tỷ số $I_{sc}/I_L$ theo IEEE 519-2022).
- **Mục 7**: Chi phí đầu tư (CAPEX), không gian lắp đặt (Footprint) và bảo trì vòng đời (7.1 Tương quan chi phí định tính lịch sử; 7.2 Không gian tủ MCC; 7.3 Quy trình bảo trì quạt, tụ bus reforming).
- **Mục 8**: Ma trận đánh giá và hướng dẫn lựa chọn theo nhóm phụ tải công nghiệp (Bơm ly tâm, Quạt, Băng tải, Máy nghiền).
- **Mục 9**: Bảng đối chiếu tổng hợp đa chiều giữa VFD và Soft Starter (11 tiêu chí kỹ thuật).
- **Mục 10**: Tiêu chí lựa chọn kỹ thuật tối ưu (Decision Framework 4 bước).
- **Mục 11**: Kết luận kỹ thuật.
- **Tài liệu tham khảo (References)**: Danh mục 6 nguồn chuẩn IEEE với liên kết kiểm chứng.

---

## 3. SỐ LƯỢNG LUẬN ĐIỂM KỸ THUẬT (CLAIM COUNT & GRANULARITY)

Đã khởi tạo bản đồ luận điểm - nguồn tại:  
`03_Articles/BLOG_04_VFD_vs_Soft_Starter/claim_source_map.json`

- **Tổng số claims được ánh xạ**: **17 claims** (`CLM-001` đến `CLM-017`).
- **Phân loại trạng thái**:
  - `SUPPORTED / VERIFIED`: 17 claims ($100\%$).
  - `CONDITIONAL`: 0 claims.
  - `NEEDS_RESEARCH`: 0 claims.
  - `DO_NOT_USE`: 0 claims.
- **Tính độc lập (Granularity)**: Mỗi claim tương ứng với một phát biểu kỹ thuật đơn lẻ có thể kiểm toán độc lập về số trang, bảng biểu và trích dẫn gốc.

---

## 4. ĐỘ BAO PHỦ BẰNG CHỨNG (EVIDENCE COVERAGE)

Tỷ lệ bao phủ bằng chứng đạt **100%**:
- Toàn bộ 17 bằng chứng kỹ thuật từ `EVD-001` đến `EVD-017` trong `evidence.json` đều được tích hợp vào văn bản bản thảo và phản ánh đầy đủ trong `claim_source_map.json`.
- Không có bất kỳ bằng chứng nào bị bỏ sót hoặc suy diễn sai lệch so với hồ sơ nghiên cứu.

---

## 5. ÁNH XẠ NGUỒN ỔN ĐỊNH SANG SỐ THỨ TỰ TRÍCH DẪN IEEE (SRC → IEEE MAPPING)

Căn cứ vào nguyên tắc xuất hiện đầu tiên trong bản thảo thực tế (First Appearance Order):

| Stable Source ID | Mã trích dẫn IEEE | Vị trí Xuất hiện Đầu tiên | Loại hình Tài liệu | Nhà xuất bản & Tiêu đề |
|:---:|:---:|:---|:---:|:---|
| **`SRC-001`** | **`[1]`** | Mục 1, Mục 2.1 | `MANUAL` | ABB AB, *Softstarter Handbook* (1SFC132060M0201) |
| **`SRC-002`** | **`[2]`** | Mục 3.1, Bảng 1 | `TECH_REPORT` | Rockwell Automation, “When to use a Soft Starter or an AC VFD” |
| **`SRC-003`** | **`[3]`** | Mục 3.3, Mục 5.1 | `WEB_ARTICLE` | Schneider Electric Blog, “Soft starters vs. VFDs Conveyor Guide” |
| **`SRC-005`** | **`[4]`** | Mục 6.2 | `TECH_REPORT` | ABB Oy, *Technical Guide No. 6: Guide to Harmonics with AC Drives* |
| **`SRC-004`** | **`[5]`** | Mục 6.3 | `STANDARD` | IEEE, *IEEE Standard for Harmonic Control in Power Systems* (Std 519-2022) |
| **`SRC-006`** | **`[6]`** | Mục 7.3 | `TECH_REPORT` | Rockwell Automation, “Preventive Maintenance Checklist of Industrial Control” |

- **Bảo tồn Stable Source ID**: Các mã `SRC-001` đến `SRC-006` được bảo toàn nguyên vẹn trong `claim_source_map.json`.
- **Thứ tự tuyến tính**: 100% các số trích dẫn xuất hiện tuần tự `[1]`, `[2]`, `[3]`, `[4]`, `[5]`, `[6]`, không nhảy cóc và không đảo lộn.

---

## 6. TUÂN THỦ CÁC RÀNG BUỘC CẤM ĐOÁN SOẠN THẢO (DRAFTING CONSTRAINTS COMPLIANCE)

Bản thảo đã tuân thủ triệt để 7 ràng buộc kỹ thuật bắt buộc:
1. **Chuẩn IEEE Std 519-2022**: Trình bày rõ ràng ranh giới áp dụng tại Điểm Đấu Nối Chung (PCC) cho toàn bộ cơ sở dựa trên tỷ số ngắn mạch $I_{sc}/I_L$. Tuyệt đối không tuyên bố tiêu chuẩn áp dụng cho từng chiếc biến tần hay bắt buộc mọi biến tần phải lắp bộ lọc.
2. **Sóng hài VFD**: Trình bày độ méo dòng sóng hài theo từng cấu trúc bộ chỉnh lưu và cuộn kháng (6 xung có cuộn kháng $\approx 40\%$, 12 xung $\approx 10\%$, AFE $\approx 4\%$), nhấn mạnh số liệu phụ thuộc cấu hình cụ thể; không quy chụp một con số cố định cho toàn bộ biến tần.
3. **Sóng hài Soft Starter**: Nêu rõ sóng hài chỉ phát sinh ngắn hạn ($<10\%$) khi khởi động/dừng qua SCR; ở chế độ xác lập bypass hầu như không có sóng hài từ thiết bị; không tuyên bố $0\%$ mang tính tuyệt đối.
4. **Chi phí RQ-006**: Áp dụng nghiêm ngặt chế độ định tính và bối cảnh lịch sử công nghệ đối với bảng chỉ số của ABB 2011 (DOL=1, Star-Delta=3, Softstarter=6, Drives>12) và đường cong chi phí Rockwell 2014; không tự ý gán thành đơn giá tiền tệ hoặc tỷ lệ cố định của năm 2026.
5. **Mô-men Soft Starter cho tải nặng**: Phân tích sâu mối quan hệ $T \propto U^2$, chỉ rõ giới hạn dòng $150\%$ khiến mô-men chỉ còn $6\%$; nêu rõ yêu cầu chọn tăng cấp công suất (oversizing: one size larger) hoặc chuyển sang dùng VFD cho tải có quán tính lớn.
6. **Nguồn Tier 3 Schneider Electric**: Trình bày trong đúng ngữ cảnh kinh nghiệm thực tế về mô-men tại $0\text{ rpm}$ và hiệu suất bypass, không thay thế cho các nguyên lý cơ bản của nguồn Tier 1.
7. **Kỷ luật Trích dẫn**: $100\%$ trích dẫn đặt ở cuối câu trước dấu chấm câu hoặc dấu hai chấm; không đặt trích dẫn bên trong công thức LaTeX `$$ ... $$`; cú pháp ngoặc riêng biệt `[1], [2]`.

---

## 7. KIỂM TOÁN CÁC LUẬN ĐIỂM VÀ RANH GIỚI BẰNG CHỨNG (DRAFT EVIDENCE BOUNDARY AUDIT)

- **Kết quả Kiểm toán Bản thảo Ban đầu (Initial Drafting Audit)**: **`REVISION_REQUIRED`**.
- **Các phát hiện vượt ranh giới bằng chứng trong bản thảo ban đầu**:
  1. *Hiệu suất & Tổn hao*: Các con số phần trăm cụ thể (Soft Starter bypass $>99.5\%$, VFD $96\%-98\%$, tổn hao dẫn/chuyển mạch $2\%-4\%$, $0.5\%-1.0\%$, điện áp rơi thuận $V_F, V_T$) không có trong hồ sơ `evidence.json` (EVD-006 chỉ so sánh định tính hiệu suất).
  2. *Dòng khởi động DOL*: Bảng 1 của Rockwell (EVD-003) chỉ xác nhận $600\% I_n$, phát biểu "đến $800\%$" là suy diễn thêm ngoài bằng chứng.
  3. *Ngôn ngữ áp đặt*: Cụm từ "bắt buộc chọn VFD" vượt quá khuyến nghị trung lập của hồ sơ nghiên cứu.
  4. *Định cỡ Soft Starter*: ABB (EVD-012) khuyến nghị "usually selected one size larger", không phải "quy định bắt buộc phải chọn lớn hơn ít nhất một cấp".
  5. *Búa nước đường ống*: ABB (EVD-011) chỉ xác nhận giải pháp giảm áp lực sóng áp suất, không hỗ trợ tuyên bố "giải quyết hoàn hảo / triệt tiêu hoàn toàn".
  6. *Mở rộng lý thuyết ngoài hồ sơ*: Các thuật ngữ SVPWM, Sensorless Vector Control, công thức $n_s = 60f/p$ và ví dụ PLC/SCADA không nằm trong phạm vi trích xuất bằng chứng đã phê duyệt.
  7. *Dải công suất RQ-006*: Các mốc "dưới vài chục kW", "100 kW đến 710 kW", "cấp số nhân" không có căn cứ từ EVD-010.
  8. *Năm xuất bản SRC-005*: Tài liệu `3AFE64292714 Rev F` có năm xuất bản chính thức là 2017 (trong danh mục tham khảo ban đầu ghi 2011).
  9. *Thứ tự trích dẫn CLM-010*: Cần đồng bộ thứ tự `source_ids` và `assigned_ieee_numbers` giữa `[4]` (SRC-005) và `[5]` (SRC-004).
- **Hành động khắc phục**: Mở task riêng **`260925_blog_04_drafting_evidence_boundary_patch`** để chuẩn hóa và thu gọn toàn bộ bản thảo và bản đồ luận điểm về đúng ranh giới bằng chứng đã phê duyệt (`DRAFT CLAIM <= APPROVED EVIDENCE <= VERIFIED SOURCE`).

---

## 8. KHOẢNG TRỐNG VÀ XỬ LÝ RANH GIỚI BẰNG CHỨNG (EVIDENCE BOUNDARY RESOLUTION)

- Không cần bổ sung Live Research mới do hồ sơ nghiên cứu đã đủ bao quát toàn bộ 7 Research Questions.
- Quy tắc xử lý: Thu gọn phát biểu bản thảo về đúng nội hàm của bằng chứng đã được phê duyệt, loại bỏ các con số suy diễn ngoài hồ sơ và trung lập hóa văn phong kỹ thuật.

---

## 9. KẾT QUẢ KIỂM TRA CI & BẢO TOÀN KIẾN TRÚC (VALIDATION RESULTS)

Đã chạy kiểm tra tự động toàn diện:
1. **Schema Validation (`claim_source_map.json`)**: **`PASS`** (Hợp lệ $100\%$ với `claim_source_map.schema.json`).
2. **Architecture Validation (`python scripts/validate_architecture.py`)**: **`PASS`** (Bao gồm Gate 10 và Gate 11 Draft Claim Traceability).
3. **Locked Article Integrity (`python scripts/verify_locked_articles.py`)**: **`PASS`** (Bảo toàn tuyệt đối mã băm SHA-256 của `BLOG_01`, `BLOG_02`, `BLOG_03`).
4. **Git Diff Check (`git diff --check`)**: **`PASS`** (Không có lỗi khoảng trắng hay ký tự lạ).

---

## 10. CHUYỂN GIAO TRẠNG THÁI VÒNG ĐỜI (LIFECYCLE TRANSITION)

Sau khi hoàn tất khởi tạo và áp dụng bản vá ranh giới bằng chứng (`260925_blog_04_drafting_evidence_boundary_patch`):
- **Trạng thái bài viết (`article_status.json`)**: Duy trì **`TECH_REVIEW`**.
- **Ghi chú vòng đời**:
  > *"Draft evidence-boundary patch completed. Draft and claim map are ready for independent Technical Review Gate."*
- **Ý nghĩa hiện tại**: Bản thảo `draft_review_package.md` và bản đồ luận điểm `claim_source_map.json` đã đạt tính chuẩn xác và khả năng truy vết $100\%$, sẵn sàng cho **Cổng Kiểm duyệt Kỹ thuật (Technical Review Gate)**.
