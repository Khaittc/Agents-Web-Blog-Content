# BÁO CÁO VI VÁ NGỮ NGHĨA TRƯỚC KIỂM DUYỆT (PRE-REVIEW SEMANTIC MICRO-PATCH REPORT)
## BLOG_04 — VFD VÀ SOFT STARTER: SO SÁNH NGUYÊN LÝ, DÒNG KHỞI ĐỘNG, ĐIỀU KHIỂN TỐC ĐỘ VÀ PHẠM VI ỨNG DỤNG
**Thời điểm thực hiện**: 2026-09-25T16:37:00+07:00  
**Tác nhân thực hiện**: Drafting Agent / Quality & Architecture Guardian  
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`  
**Mã phân loại chuẩn**: `BLOG-T04` (Comparison)  
**Baseline Commit**: `42bbe3d — fix: finalize semantic evidence boundaries in BLOG_04`  

---

## 1. CÁC PHÁT BIỂU THỰC TẾ CÒN SÓT ĐÃ ĐỊNH VỊ (RESIDUAL FACTUAL CLAIMS FOUND)

Qua kiểm toán chi tiết từng câu trong bản thảo, các phát biểu thực tế vượt ra ngoài phạm vi trực tiếp của các `EVD-xxx` đã được nhận diện và xử lý triệt để:
1. **Mục 3.1 & 3.2**: Nhận định về hậu quả thứ cấp của dòng DOL ("gây sụt áp trên thanh cái, ảnh hưởng thiết bị điện tử nhạy cảm") và cách diễn đạt dải dòng Soft Starter như một dải định mức chung ("150% đến 450%").
2. **Mục 4**: Các ví dụ về van tiết lưu, cánh hướng gió, và suy luận "tiết kiệm điện năng trong ứng dụng bơm quạt khi giảm lưu lượng" chưa có bằng chứng trực tiếp trong EVD-005.
3. **Mục 6.3**: Các suy luận về kịch bản lưới điện mạnh/yếu, tỷ trọng VFD lớn/nhỏ đảm bảo tuân thủ, và khuyến nghị vị trí gắn bộ lọc thụ động/AHF tại thanh cái chính.
4. **Mục 8.1 (Bơm)**: Công thức $T_L \propto n^2$, giả định bơm khởi động nhẹ ở tốc độ thấp, các quy tắc chọn cứng ("chọn Soft Starter khi...", "chọn VFD khi...") và giả định điều tiết áp suất/tiết kiệm điện theo giờ tiêu thụ.
5. **Mục 8.2 (Quạt & Blower)**: Toàn bộ các phát biểu về quán tính cánh quạt lớn, đứt dây curoa, quạt thông gió hầm mỏ, hệ thống HVAC, quạt hút lò hơi, quy luật $P \propto n^3$, và cài đặt thời gian dốc 20–45 giây không có bằng chứng riêng trong hồ sơ đã duyệt.
6. **Executive Summary & Kết luận**: Các tính từ định tính chưa được trích dẫn ("toàn năng", "kinh tế", "hiệu quả", "vượt trội", ví dụ phụ tải chưa kiểm chứng).

---

## 2. LÀM SẠCH MỤC 4 — ĐIỀU KHIỂN TỐC ĐỘ LIÊN TỤC (SECTION 4 CLEANUP)

- **Căn cứ bằng chứng**: `EVD-005` (Soft Starter chỉ điều khiển dốc khởi động/dừng, sau đó chạy cố định theo tần số lưới; VFD điều khiển tốc độ liên tục) kết hợp `EVD-001` (dải tần số ngõ ra 0–250 Hz).
- **Hành động**:
  - Loại bỏ hoàn toàn các cơ cấu điều tiết cơ khí (van tiết lưu, cánh hướng gió).
  - Loại bỏ các khẳng định tiết kiệm năng lượng cho bơm/quạt.
  - Thu gọn câu văn: Khi quy trình công nghệ đòi hỏi điều chỉnh tốc độ liên tục trong quá trình vận hành, biến tần là phương án cần được xem xét [1, p. 16], [1, p. 17]. Soft Starter không có khả năng điều chỉnh tốc độ liên tục sau khi hoàn tất khởi động [1, p. 17].

---

## 3. LÀM SẠCH MỤC 6.3 — CHUẨN IEEE STD 519 VÀ GIẢI PHÁP SÓNG HÀI (SECTION 6.3 CLEANUP)

- **Căn cứ bằng chứng**: `EVD-009` (Bảng 2 IEEE Std 519-2022 giới hạn TDD 5.0% cho $I_{sc}/I_L < 20$) và `EVD-014` (IEEE 519 áp dụng tại điểm PCC cho toàn bộ cơ sở, không áp dụng cho thiết bị đơn lẻ và không bắt buộc mọi drive phải có lọc).
- **Hành động**:
  - Loại bỏ toàn bộ suy đoán kịch bản lưới mạnh/yếu (strong grid / weak grid scenarios).
  - Loại bỏ giả định tỷ trọng VFD nhỏ thì chắc chắn đạt chuẩn còn tỷ trọng lớn thì bắt buộc gắn AHF tại thanh cái chính.
  - Thu gọn mục 3 thành: Đánh giá sóng hài là bài toán cấp hệ thống tại điểm PCC dựa trên tỷ số $I_{sc}/I_L$ [4, p. 10], [5, p. 12]; tiêu chuẩn IEEE Std 519 không bắt buộc mọi biến tần phải lắp đặt bộ lọc riêng [4, p. 10].

---

## 4. LÀM SẠCH MỤC 8.1 — PHỤ TẢI BƠM LY TÂM (SECTION 8.1 CLEANUP)

- **Căn cứ bằng chứng**: `EVD-011` (Hiện tượng mài mòn và áp lực đường ống do sóng áp suất khi dừng quá nhanh; Soft Starter cung cấp giải pháp giảm áp qua dốc dừng êm).
- **Hành động**:
  - Loại bỏ công thức đặc tính tải $T_L \propto n^2$.
  - Loại bỏ các quy tắc chọn cứng ("Chọn Soft Starter khi...", "Chọn Biến tần khi...").
  - Loại bỏ các giả định tiết kiệm năng lượng, duy trì áp suất đường ống không đổi theo giờ tiêu thụ.
  - Thu gọn nội dung: Ghi nhận thách thức chính là hiện tượng sóng áp suất va đập (búa nước) khi dừng quá nhanh; tính năng dừng êm của Soft Starter giúp giảm thiểu hiện tượng này [1, p. 29]; nếu quy trình yêu cầu điều chỉnh tốc độ liên tục thì đối chiếu thêm nguyên lý của VFD [1, p. 16], [1, p. 17].

---

## 5. LÀM SẠCH MỤC 8.2 — PHỤ TẢI QUẠT VÀ BLOWER (SECTION 8.2 CLEANUP)

- **Nguyên nhân**: Hồ sơ bằng chứng kỹ thuật đã duyệt (`evidence.json`) **không có bất kỳ EVD nào chuyên biệt cho ứng dụng quạt**.
- **Hành động áp dụng Option A**:
  - Loại bỏ 100% các suy diễn kỹ thuật nền (quán tính lớn, đứt dây curoa, quạt hầm mỏ, hệ thống HVAC, lò hơi, tiết kiệm điện theo quy luật lập phương $P \propto n^3$, thời gian tăng tốc 20–45 giây).
  - Ghi nhận rõ ràng và trung thực trong bài viết: Hồ sơ bằng chứng hiện tại không thiết lập tài liệu chuyên biệt riêng cho quạt; do đó việc đánh giá hoàn toàn dựa trên 2 nguyên tắc cốt lõi:
    - Nếu cần điều chỉnh tốc độ liên tục: Cân nhắc VFD [1, p. 16], [1, p. 17].
    - Nếu chỉ cần khởi động/dừng ở tốc độ cố định: Khởi động mềm có thể được đánh giá tùy theo yêu cầu mô-men [1, p. 17], [2, Tab. 1, p. 6].
  - Việc cắt giảm hướng dẫn chuyên biệt cho quạt là hành vi tuân thủ kỷ luật bằng chứng đúng đắn, không phải lỗi kỹ thuật.

---

## 6. LÀM SẠCH MÔ TẢ DÒNG KHỞI ĐỘNG VÀ HẬU QUẢ THỨ CẤP CỦA DOL (DOL / CURRENT WORDING)

- **Hậu quả thứ cấp DOL**: Loại bỏ câu "gây sụt áp trên thanh cái phân phối, tác động xấu đến các thiết bị điện tử nhạy cảm cùng lộ cấp nguồn" vì không có trong `EVD-003`. Giữ đúng: Dữ liệu thực nghiệm của Rockwell ghi nhận trường hợp DOL tương ứng dòng khởi động khoảng $600\%$ ($6.0 \cdot I_n$) [2, Tab. 1, p. 6].
- **Dữ liệu dòng Soft Starter**: Thay vì mô tả như một dải định mức liên tục $150\%–450\%$, câu văn được chỉnh thành: Bảng 1 của Rockwell đưa ra các điểm khảo sát giới hạn dòng ở mức $150\%$, $300\%$ và $450\%$ dòng định mức [2, Tab. 1, p. 6].
- Cột đánh giá trong bảng số liệu Mục 3.2 được làm sạch, bám sát các số liệu thực nghiệm gốc.

---

## 7. KIỂM TOÁN BẢNG SO SÁNH TỔNG HỢP MỤC 9 (TABLE AUDIT)

Rà soát 11 hàng của bảng đối chiếu:
- **Dòng khởi động**: Ô Soft Starter ghi nhận các điểm khảo sát $150\%, 300\%, 450\%$ theo Bảng 1 Rockwell; ô VFD ghi nhận kiểm soát quá trình qua tần số/điện áp và hồ sơ không xác lập dải số liệu cụ thể.
- **Mô-men tại 0 rpm**: Ghi nhận chính xác VFD cấp full torque tại $0\text{ rpm}$ theo EVD-004; Soft Starter không thể cấp full torque tại $0\text{ rpm}$.
- **Hiệu suất**: Ghi nhận Soft Starter đóng bypass chạy mát hơn và hiệu suất cao hơn do không có bán dẫn công suất phát nhiệt theo EVD-006.
- **Bảo trì**: Ghi nhận hướng dẫn bảo trì VFD của Rockwell theo EVD-017; ghi chú rõ hồ sơ hiện tại không xác lập danh mục kiểm tra tương đương cho Soft Starter.
- **CAPEX**: So sánh định tính lịch sử dựa trên EVD-010 và chỉ số ABB EVD-016.

---

## 8. KIỂM TOÁN TÓM TẮT KỸ THUẬT (EXECUTIVE SUMMARY AUDIT)

Phần Tóm tắt Kỹ thuật ở đầu bài đã được viết lại hoàn toàn:
- Loại bỏ toàn bộ các khái niệm chưa được map: đặc tính mô-men thay đổi hay không đổi, nhu cầu điều chỉnh lưu lượng liên tục, hiện tượng búa nước trong phần tóm tắt.
- Chỉ giữ các nội dung đã map về `EVD-001`, `EVD-002`, `EVD-004`, `EVD-005`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`.

---

## 9. KIỂM TOÁN KẾT LUẬN (CONCLUSION AUDIT)

Mục 11 đã được loại bỏ toàn bộ các tính từ mang tính chủ quan hoặc chưa được chứng minh ("hoàn hảo", "toàn năng", "kinh tế", "hiệu quả", "vượt trội", "tải nặng ưu việt"):
- Tóm tắt súc tích, khách quan: Soft Starter phù hợp khi yêu cầu cốt lõi là kiểm soát quá trình khởi động/dừng êm và không đòi hỏi điều chỉnh tốc độ liên tục [1, p. 17]. Biến tần phù hợp khi cần điều chỉnh tốc độ liên tục [1, p. 16] hoặc tải đòi hỏi full torque tại zero speed [3].
- Mọi phát biểu đều truy vết trực tiếp về `EVD-004` và `EVD-005`.

---

## 10. ĐỒNG BỘ BẢN ĐỒ LUẬN ĐIỂM (CLAIM-MAP SYNCHRONIZATION)

Tệp `03_Articles/BLOG_04_VFD_vs_Soft_Starter/claim_source_map.json`:
- `CLM-003`: Cập nhật `claim_text` để thể hiện chính xác các điểm khảo sát $150\%, 300\%, 450\%$ theo Bảng 1 của Rockwell Automation.
- Toàn bộ 17 claims (`CLM-001` đến `CLM-017`) đều có chuỗi truy vết trực tiếp khép kín:
  `CLM-xxx` → `EVD-xxx` → `SRC-xxx` → `IEEE [n]`.
- Thứ tự xuất hiện đầu tiên của các nguồn không đổi:
  `SRC-001` [1], `SRC-002` [2], `SRC-003` [3], `SRC-005` [4], `SRC-004` [5], `SRC-006` [6].

---

## 11. TÍNH TOÀN VẸN CỦA HỒ SƠ NGHIÊN CỨU (RESEARCH ARTIFACT INTEGRITY)

Tuyệt đối không có bất kỳ sửa đổi nào đối với:
- `article_brief.json`
- `research_plan.json`
- `research_log.json`
- `evidence.json`
- `evidence_dossier.md`
- `research_handoff.json`

Không sửa schema hoặc CI scripts.

---

## 12. MỨC ĐỘ SẴN SÀNG CHO TECHNICAL REVIEW GATE (REVIEW READINESS)

- **Trạng thái bài viết (`article_status.json`)**: Duy trì **`TECH_REVIEW`**.
- Toàn bộ các câu văn thực tế trong bản thảo hiện đã được bao bọc $100\%$ bởi các bằng chứng đã phê duyệt. Không còn bất kỳ phát biểu thực tế nào đứng độc lập ngoài hồ sơ bằng chứng. Bản thảo đã hoàn toàn sẵn sàng cho Review Agent tiến hành quy trình độc lập tại **Technical Review Gate**.
