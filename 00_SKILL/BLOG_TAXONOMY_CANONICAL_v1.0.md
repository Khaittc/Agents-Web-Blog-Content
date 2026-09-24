# CANONICAL BLOG TAXONOMY STANDARD v1.0
**Mã tài liệu**: `00_SKILL/BLOG_TAXONOMY_CANONICAL_v1.0.md`
**Phiên bản**: 1.0
**Ngày ban hành**: 24/09/2026
**Trạng thái**: Nguồn Chuẩn Duy Nhất (Single Source of Truth) về Phân Loại Bài Viết Kỹ Thuật
**Phạm vi**: Toàn bộ Subagents, Kế hoạch, Cẩm nang, và Bài viết trong repository `Agents-Web-Blog-Content`.

---

## 1. NGUYÊN TẮC BẤT DI BẤT DỊCH (CANONICAL RULE)

1. **Nguồn chuẩn duy nhất**: Toàn bộ hệ thống (Research Agent, Drafting Agent, Visual Agent, Review Agent, Publisher Agent, Orchestrator) **BẮT BUỘC** phải tuân thủ và tham chiếu trực tiếp đến 5 mã thể loại chuẩn mực được định nghĩa trong tài liệu này.
2. **Tuyệt đối cấm định nghĩa riêng lẻ**: Không bất kỳ Agent nào được tự ý đặt tên, sửa đổi tên gọi, hoặc tạo ra định nghĩa loại bài riêng trong template của mình.
3. **Một bài viết - Một thể loại chủ đạo**: Mỗi bài viết kỹ thuật có thể tích hợp nhiều yếu tố phụ trợ (ví dụ: bài giải thích kỹ thuật có phần tính toán), nhưng **bắt buộc phải chọn đúng 1 mã thể loại chủ đạo** để định hình cấu trúc bài viết và ma trận kiểm duyệt.

---

## 2. BẢNG PHÂN LOẠI CANONICAL TAXONOMY (THE 5 CANONICAL TYPES)

| Code | Canonical Name | Tên Tiếng Việt Chuẩn | Purpose (Mục đích cốt lõi) | Typical Use (Trường hợp sử dụng điển hình) | Primary Structure Reference |
|---|---|---|---|---|---|
| **`BLOG-T01`** | **Technical Explanation** | Giải thích Kỹ thuật Chuyên sâu | Giải thích bản chất vật lý, cơ chế hoạt động, định luật, công thức toán học hoặc thuật ngữ kỹ thuật trừu tượng. | Bản chất hiện tượng sóng hài bậc cao, ý nghĩa vật lý của cos phi, nguyên lý điều khiển vector FOC, cơ chế bão hòa từ máy biến áp. | Section 6 trong `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` |
| **`BLOG-T02`** | **How-to / Measurement** | Hướng dẫn Kỹ thuật & Đo kiểm | Hướng dẫn quy trình đo lường, kiểm tra, tính toán đánh giá tình trạng thiết bị bằng công cụ thực tế và đưa ra quyết định kỹ thuật từ dữ liệu đo. | Cách phát hiện động cơ điện chạy non tải, cách đo độ lệch trở cuộn dây, cách kiểm tra mất cân bằng điện áp bằng máy phân tích công suất, đánh giá hệ số tải máy biến áp. | Section 7 trong `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` |
| **`BLOG-T03`** | **Troubleshooting** | Chẩn đoán & Khắc phục Sự cố | Cung cấp cây quyết định (decision tree), quy trình logic từng bước để cô lập nguyên nhân gốc (root cause) và xử lý sự cố thiết bị tại nhà máy. | Quy trình 4 bước chẩn đoán và khắc phục lỗi quá dòng (Overcurrent) biến tần, xử lý lỗi quá nhiệt động cơ, khắc phục sự cố nhảy Aptomat tổng không rõ nguyên nhân. | Section 8 trong `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` |
| **`BLOG-T04`** | **Comparison** | So sánh Đối đầu Công nghệ | Phân tích định lượng so sánh 2 hoặc nhiều công nghệ, giải pháp, dòng thiết bị dựa trên thông số kỹ thuật, hiệu suất năng lượng, chi phí TCO và giới hạn ứng dụng. | So sánh khởi động mềm (Soft Starter) và Biến tần (VFD), so sánh động cơ IE3 và IE4, so sánh phương pháp lọc sóng hài chủ động AHF và thụ động PHF. | Section 9 trong `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` |
| **`BLOG-T05`** | **Best Practice / Engineering Guide** | Thực hành Tốt nhất & Hướng dẫn Vận hành | Tổng hợp các khuyến nghị thiết kế, lắp đặt, bảo trì phòng ngừa theo tiêu chuẩn quốc tế và kinh nghiệm hiện trường để tối ưu độ tin cậy hệ thống. | Hướng dẫn lắp đặt dây cáp động lực biến tần chống nhiễu EMC, tiêu chuẩn bảo trì định kỳ tủ điện hạ thế, quy tắc vàng trong tính toán chọn dung lượng tụ bù công suất phản kháng. | Section 10 trong `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` |

---

## 3. CHI TIẾT ĐẶC TẢ TỪNG LOẠI BÀI VIẾT

### 3.1. `BLOG-T01` — Technical Explanation
* **Mục tiêu**: Độc giả hiểu sâu sắc "TẠI SAO" một hiện tượng kỹ thuật xảy ra, cơ sở toán học và bản chất vật lý nền tảng.
* **Cấu trúc cốt lõi**:
  1. Đặt vấn đề & Khái niệm/Định nghĩa chuẩn xác.
  2. Nguyên lý vật lý hoặc cơ chế vận hành.
  3. Mô hình toán học LaTeX & Phân tích thứ nguyên SI (`LATEX_FORMULA_SKILL_v1.0.md`).
  4. Worked Example / Ví dụ tính toán bằng số liệu thực tế.
  5. Ý nghĩa trong vận hành công nghiệp & Những hiểu lầm thường gặp.
  6. Kết luận & Danh mục tài liệu tham khảo IEEE.
* **Bài viết mẫu đã nghiệm thu**: `BLOG_02_He_so_cong_suat_va_Song_hai`.

---

### 3.2. `BLOG-T02` — How-to / Measurement
* **Mục tiêu**: Độc giả có thể "LÀM NHƯ THẾ NÀO" để đo lường, tính toán, và đưa ra quyết định kỹ thuật tự tin từ số liệu thu thập.
* **Cấu trúc cốt lõi**:
  1. Vấn đề cần kiểm tra & Nguy cơ nếu không phát hiện kịp thời.
  2. Các thông số kỹ thuật cần thu thập (dòng điện, điện áp, công suất, độ rung, nhiệt độ).
  3. Dụng cụ đo kiểm cần thiết & Yêu cầu an toàn điện.
  4. Quy trình từng bước thực hiện đo đạc và tính toán.
  5. Bảng tra cứu đối chiếu & Tiêu chí ra quyết định (Decision Matrix).
  6. Khuyến nghị giải pháp kỹ thuật sau đo kiểm.
  7. Kết luận & Danh mục tài liệu tham khảo IEEE.
* **Bài viết mẫu đã nghiệm thu**: `BLOG_01_Dong_co_non_tai`.

---

### 3.3. `BLOG-T03` — Troubleshooting
* **Mục tiêu**: Độc giả có thể "CÔ LẬP VÀ XỬ LÝ LỖI" nhanh nhất, có phương pháp khoa học, triệt tiêu tư duy "thay thế thử nghiệm may rủi".
* **Cấu trúc cốt lõi**:
  1. Mô tả triệu chứng sự cố & Mã lỗi kỹ thuật cụ thể.
  2. Biểu đồ cây quyết định chẩn đoán (Decision Tree Flowchart).
  3. Quy trình từng bước cô lập nguyên nhân: Kiểm tra ngoại vi $\rightarrow$ Kiểm tra tải cơ khí $\rightarrow$ Kiểm tra mạch công suất $\rightarrow$ Phân tích tham số cài đặt.
  4. Hướng dẫn đo nguội (Cold check) / Đo nóng (Live check) với chỉ số an toàn nghiêm ngặt.
  5. Bảng tổng hợp nguyên nhân gốc, triệu chứng đo đạc và biện pháp xử lý triệt để.
  6. Khuyến nghị bảo trì phòng ngừa tái diễn.
  7. Kết luận & Danh mục tài liệu tham khảo IEEE.
* **Bài viết mẫu đã nghiệm thu**: `BLOG_03_Chan_doan_qua_dong_bien_tan`.

---

### 3.4. `BLOG-T04` — Comparison
* **Mục tiêu**: Độc giả có đầy đủ dữ liệu so sánh công tâm, định lượng để "LỰA CHỌN CÔNG NGHỆ" tối ưu cho dự án.
* **Cấu trúc cốt lõi**:
  1. Bối cảnh bài toán kỹ thuật & Giới thiệu các đối tượng so sánh.
  2. Bảng so sánh ma trận thông số kỹ thuật trực quan (Feature Matrix).
  3. Phân tích chi tiết từng khía cạnh: Nguyên lý, Hiệu suất, Kích thước, Độ phức tạp điều khiển.
  4. Phân tích kinh tế: Chi phí đầu tư ban đầu (CAPEX) vs Chi phí vận hành (OPEX) / Tổng chi phí sở hữu (TCO).
  5. Vùng ứng dụng tối ưu cho từng giải pháp (When to use What).
  6. Kết luận & Khuyến nghị kỹ sư.

---

### 3.5. `BLOG-T05` — Best Practice / Engineering Guide
* **Mục tiêu**: Độc giả nắm vững các "QUY TẮC THỰC CHIẾN" chuẩn mực theo tiêu chuẩn quốc tế để thiết kế, thi công hoặc vận hành hệ thống bền bỉ nhất.
* **Cấu trúc cốt lõi**:
  1. Tầm quan trọng của việc tuân thủ quy chuẩn & Hậu quả của sai sót điển hình.
  2. Danh mục các quy tắc kỹ thuật chuẩn hóa (Quy tắc 1, Quy tắc 2, ...).
  3. Hướng dẫn chi tiết từng quy tắc kèm tiêu chuẩn tham chiếu (IEC/IEEE/NFPA).
  4. Sơ đồ lắp đặt hoặc kiến trúc phân bổ mẫu.
  5. Danh mục tự kiểm tra hiện trường (Commissioning Checklist).
  6. Kết luận & Danh mục tài liệu tham khảo IEEE.

---

## 4. QUY TRÌNH THAM CHIẾU DÀNH CHO CÁC AGENT

1. **Orchestrator Agent**: Khi nhận đề bài từ người dùng, bắt buộc map đề tài vào chính xác 1 trong 5 mã `BLOG-T01` đến `BLOG-T05` trong `article_brief.json`.
2. **Drafting Agent**: Bắt buộc đọc file này và `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` để triển khai đúng mạch cấu trúc tương ứng.
3. **Review Agent**: Bắt buộc sử dụng tiêu chí của loại bài tương ứng tại Trụ cột 3 (Claim & Logic Audit) để thẩm định tính mạch lạc của nội dung.
4. **Publisher Agent**: Ghi nhận chính xác mã thể loại vào `article_status.json` và `article_manifest.json`.
