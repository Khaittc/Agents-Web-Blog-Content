# BÁO CÁO DỌN DẸP NGỮ NGHĨA VÀ RANH GIỚI BẰNG CHỨNG CUỐI CÙNG (FINAL SEMANTIC EVIDENCE CLEANUP REPORT)
## BLOG_04 — VFD VÀ SOFT STARTER: SO SÁNH NGUYÊN LÝ, DÒNG KHỞI ĐỘNG, ĐIỀU KHIỂN TỐC ĐỘ VÀ PHẠM VI ỨNG DỤNG
**Thời điểm thực hiện**: 2026-09-25T16:30:00+07:00  
**Tác nhân thực hiện**: Drafting Agent / Quality & Architecture Guardian  
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`  
**Mã phân loại chuẩn**: `BLOG-T04` (Comparison)  
**Baseline Commit**: `fa6be73 — fix: enforce evidence boundaries in BLOG_04 draft`  

---

## 1. CÁC LUẬN ĐIỂM DƯ THỪA / VƯỢT RANH GIỚI BẰNG CHỨNG ĐÃ PHÁT HIỆN (RESIDUAL UNSUPPORTED CLAIMS FOUND)

Qua quá trình rà soát chi tiết từng câu chữ trong bản thảo `draft_review_package.md` và bản đồ luận điểm `claim_source_map.json`, các luận điểm vượt ranh giới bằng chứng sau đã được định vị:
1. **Dòng khởi động VFD (Mục 3.1 & Bảng 9)**: Phát biểu dòng khởi động VFD không vượt quá 100%–150% dòng định mức ($1.0–1.5 \cdot I_n$). Approved evidence không chứa số liệu định lượng dải dòng khởi động cho VFD.
2. **Quy tắc ngưỡng chọn thiết bị theo dòng điện trong Decision Framework (Mục 10)**: Quy tắc suy diễn nếu nguồn không cấp được $>1.5 \cdot I_n$ thì chọn VFD, nếu nguồn chịu được $2.5–4.5 \cdot I_n$ thì chọn Soft Starter.
3. **Mô-men VFD duy trì ổn định trên toàn dải từ 0 rpm đến tốc độ danh định (Mục 2.1)**: EVD-001 và EVD-004 chỉ chứng minh VFD cấp full torque tại zero speed ($0\text{ rpm}$), không chứng minh "ổn định trên toàn dải từ 0 đến định mức".
4. **Cơ chế tổn hao nhiệt bán dẫn chi tiết (Mục 5.1–5.2)**: Giải thích tổn hao chuyển mạch, tổn hao dẫn liên tục và làm mát cưỡng bức vượt quá nội dung định tính của EVD-006.
5. **Trình tự đóng cắt tiếp điểm bypass (Mục 5.3)**: Các chi tiết về điện áp tiếp điểm vài Volt, kích dẫn lại thyristor trước khi soft stop, và ngắt hồ quang không có trong EVD-007.
6. **Yêu cầu bảo trì Soft Starter (Mục 7.3 & Bảng 9)**: Tuyên bố bảo trì Soft Starter đơn giản, siết bu-lông và vệ sinh bụi không có trong EVD-017 (vốn chỉ là danh mục bảo trì VFD của Rockwell).
7. **Chi tiết ứng dụng phụ tải băng tải (Mục 8.3)**: Phân loại băng tải ngắn/dài, chở vật liệu nhẹ/nặng, dốc, khởi động đầy tải vượt quá EVD-003 và EVD-004.
8. **Phần mở rộng trong CLM-017 (Mục 8.4)**: Cụm từ "để tránh hiện tượng sụt áp và quá nhiệt trong thời gian khởi động kéo dài" không có trong EVD-012.
9. **Khẳng định tuyệt đối về chi phí CAPEX (Mục 7.1)**: Nhận định "cấu trúc phần cứng phức tạp của biến tần luôn đặt ra mức vốn đầu tư ban đầu (CAPEX) cao hơn đáng kể" vượt quá bối cảnh so sánh định tính lịch sử của EVD-010 (vốn chỉ ra ở dải thấp chi phí có thể tương đương).

---

## 2. CÁC LUẬN ĐIỂM ĐÃ LOẠI BỎ (CLAIMS REMOVED)

- Loại bỏ hoàn toàn tuyên bố số liệu định lượng dòng khởi động VFD ($100\%–150\%$, $1.0–1.5 \cdot I_n$) khỏi Mục 3.1 và Bảng 9.
- Loại bỏ quy tắc ngưỡng chọn thiết bị dựa trên dòng điện nguồn cấp ($1.5 \cdot I_n$ vs $2.5–4.5 \cdot I_n$) trong Decision Framework.
- Loại bỏ các diễn giải chi tiết về cơ chế tổn hao bán dẫn (switching losses, conduction losses, forced cooling specifics) tại Mục 5.1.
- Loại bỏ các chi tiết trình tự thao tác tiếp điểm bypass (điện áp vài Volt, kích dẫn lại thyristor trước khi dừng, dập hồ quang) tại Mục 5.2.
- Loại bỏ khẳng định so sánh bảo trì Soft Starter đơn giản tại Mục 7.3 và ô so sánh tương ứng trong Bảng 9.
- Loại bỏ các phân nhánh phụ tải băng tải mang tính suy diễn ngoài bằng chứng (băng tải ngắn, băng tải dốc, tải vật liệu nhẹ) tại Mục 8.3.
- Loại bỏ các từ mang tính quy luật tuyệt đối ("luôn", "always", "vững chắc") trong phân tích chi phí CAPEX tại Mục 7.1.

---

## 3. CÁC LUẬN ĐIỂM ĐÃ THU GỌN VÀ ĐIỀU CHỈNH MỨC ĐỘ (CLAIMS DOWNGRADED)

- **Dòng khởi động VFD**: Chuyển thành phát biểu định tính: Biến tần có khả năng kiểm soát gia tốc và quá trình khởi động của động cơ qua điều khiển tần số và điện áp ngõ ra theo [1, p. 16]; hồ sơ bằng chứng hiện tại không xác lập số liệu dải dòng định lượng.
- **Mô-men tại 0 rpm**: Thu gọn phát biểu về đúng phạm vi EVD-004: Biến tần có thể cung cấp đầy đủ 100% mô-men định mức ngay tại tốc độ zero speed ($0\text{ rpm}$) cho các ứng dụng đòi hỏi mô-men bứt phá theo [3].
- **Hiệu suất và nhiệt năng bypass**: Thu gọn Section 5.1 về đúng nội dung EVD-006: Khi vận hành ở tốc độ định mức đầy tải có integrated bypass, dòng điện chuyển qua contactor giúp thiết bị chạy mát hơn và đạt hiệu suất cao hơn biến tần do không có bán dẫn công suất chủ động phát nhiệt [3].
- **Định mức AC-1 của bypass**: Thu gọn Section 5.2 về đúng EVD-007: Contactor bypass tích hợp thường có định mức AC-1 vì không bao giờ phải đóng hoặc cắt dòng điện trong vận hành bypass thông thường [2, p. 7].
- **Bảo trì vòng đời**: Nêu rõ tài liệu Rockwell cung cấp quy trình bảo trì chi tiết cho hệ thống biến tần [6, pp. 1–4]; ghi nhận rõ hồ sơ bằng chứng hiện tại không xác lập danh mục kiểm tra tương đương cho khởi động mềm.
- **Phụ tải băng tải**: Thu gọn về 2 nguyên tắc cơ bản: Nếu tải đòi hỏi full torque tại $0\text{ rpm}$ thì xem xét VFD [3]; nếu chỉ yêu cầu khởi động/dừng êm và chạy lưới trực tiếp thì Soft Starter có thể phù hợp tùy yêu cầu mô-men [1, p. 17], [2, Tab. 1, p. 6].
- **CLM-017 (Oversizing cho tải nặng)**: Thu gọn về đúng EVD-012: Đối với ứng dụng có mô-men quán tính rất lớn như máy nghiền, máy khuấy, tài liệu ABB cho biết Soft Starter thường được chọn lớn hơn một cấp công suất (oversizing: one size larger) so với công suất động cơ ($kW\text{ size}$) [1, p. 37].
- **Chi phí CAPEX**: Chuyển thành phân tích định tính lịch sử theo EVD-010: Ở dải thấp chi phí ban đầu có thể tương đương; khi dòng và công suất tăng thì chi phí biến tần tăng cao hơn [2, p. 15].

---

## 4. HIỆU CHỈNH KHUNG RA QUYẾT ĐỊNH (DECISION-FRAMEWORK CORRECTIONS)

Mục 10 (Decision Framework) đã được tái cấu trúc thành 3 câu hỏi đánh giá kỹ thuật độc lập, loại bỏ mọi ngưỡng số liệu võ đoán:
1. **Câu hỏi 1**: Quy trình công nghệ có đòi hỏi điều chỉnh tốc độ liên tục không?
   - Có: Cân nhắc chọn VFD [1, p. 16], [1, p. 17]. Soft Starter không hỗ trợ điều chỉnh tốc độ xác lập.
2. **Câu hỏi 2**: Phụ tải có đòi hỏi đầy đủ mô-men tại tốc độ zero speed ($0\text{ rpm}$) không?
   - Có: Cân nhắc chọn VFD [3]. Soft Starter bị sụt giảm mô-men theo bình phương điện áp [2, Tab. 1, p. 6] và không đáp ứng được yêu cầu full torque tại $0\text{ rpm}$ [3].
3. **Câu hỏi 3**: Đánh giá đa chiều về dòng khởi động, chi phí ban đầu, không gian tủ điện và tuân thủ sóng hài:
   - Dòng khởi động: Đối chiếu yêu cầu dòng/mô-men của tải với khả năng của từng phương án và dữ liệu OEM.
   - Chi phí & Footprint: Cân nhắc tương quan chi phí (thấp tương đương, lớn VFD cao hơn [2, p. 15]) và không gian tủ điện (Soft Starter nhỏ hơn [2, pp. 15–16]).
   - Chuẩn IEEE Std 519: Đánh giá méo dòng TDD tại ranh giới PCC theo tỷ số $I_{sc}/I_L$ [4, p. 10], [5, p. 12].

---

## 5. HIỆU CHỈNH BẢNG SO SÁNH KỸ THUẬT (COMPARISON-TABLE CORRECTIONS)

Bảng đối chiếu tại Mục 9 đã được làm sạch toàn bộ 11 hàng:
- **Dòng khởi động**: Ô VFD ghi rõ kiểm soát gia tốc qua tần số/điện áp; không tự ý gán số liệu dải dòng định lượng.
- **Mô-men tại 0 rpm**: Ghi nhận chính xác VFD cấp full torque tại $0\text{ rpm}$ theo EVD-004; Soft Starter không thể cấp full torque tại $0\text{ rpm}$.
- **Hiệu suất**: Ghi nhận định tính theo EVD-006: Soft Starter đóng bypass chạy mát hơn và hiệu suất cao hơn do không có bán dẫn công suất phát nhiệt.
- **Bảo trì**: Ghi nhận rõ hướng dẫn bảo trì chi tiết của Rockwell cho VFD (EVD-017) và ghi chú không có danh mục tương đương cho Soft Starter trong hồ sơ hiện tại.
- **CAPEX**: So sánh định tính lịch sử dựa trên EVD-010 và chỉ số ABB EVD-016, không dùng từ tuyệt đối.

---

## 6. ĐỒNG BỘ BẢN ĐỒ LUẬN ĐIỂM (CLM UPDATES)

Đã cập nhật tệp `03_Articles/BLOG_04_VFD_vs_Soft_Starter/claim_source_map.json`:
- `CLM-006`: `section_target` cập nhật thành `"Section 5.1"`.
- `CLM-007`: `section_target` cập nhật thành `"Section 5.2"`.
- `CLM-012`: `claim_text` chuẩn hóa tương quan chi phí dải thấp tương đương, dải cao VFD tăng cao hơn.
- `CLM-017`: `claim_text` cắt bỏ phần suy diễn ngoài bằng chứng về sụt áp và quá nhiệt, giữ đúng nội dung chọn lớn hơn một cấp (one size larger) theo ABB p. 37.

---

## 7. SỐ LƯỢNG LUẬN ĐIỂM CUỐI CÙNG (FINAL CLAIM COUNT)

- **Tổng số claims thực tế và có căn cứ xác thực**: **17 claims** (`CLM-001` đến `CLM-017`).
- Toàn bộ 17 claims đều có bằng chứng trực tiếp trong `evidence.json` (`EVD-001` đến `EVD-017`), không có claim rỗng, không có claim suy diễn.

---

## 8. XÁC MINH ÁNH XẠ NGUỒN VÀ MÃ IEEE (IEEE MAPPING VERIFICATION)

Thứ tự xuất hiện đầu tiên của các nguồn trong bản thảo đã được kiểm tra:
1. `SRC-001` xuất hiện tại Section 1 -> Mã IEEE **`[1]`**
2. `SRC-002` xuất hiện tại Section 3.1 -> Mã IEEE **`[2]`**
3. `SRC-003` xuất hiện tại Section 2.1 / 3.3 -> Mã IEEE **`[3]`**
4. `SRC-005` xuất hiện tại Section 6.2 -> Mã IEEE **`[4]`**
5. `SRC-004` xuất hiện tại Section 6.3 -> Mã IEEE **`[5]`**
6. `SRC-006` xuất hiện tại Section 7.3 -> Mã IEEE **`[6]`**

Ánh xạ `source_to_ieee_map` trong `claim_source_map.json` hoàn toàn trùng khớp với thứ tự xuất hiện tuyến tính và danh mục tài liệu tham khảo trong bản thảo.

---

## 9. TÍNH TOÀN VẸN CỦA HỒ SƠ NGHIÊN CỨU (RESEARCH ARTIFACT INTEGRITY)

Các tệp thuộc hồ sơ nghiên cứu gốc được bảo toàn tuyệt đối, không có bất kỳ thay đổi nào:
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/article_brief.json` (Unchanged)
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/research_plan.json` (Unchanged)
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/research_log.json` (Unchanged)
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/evidence.json` (Unchanged)
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/evidence_dossier.md` (Unchanged)
- `03_Articles/BLOG_04_VFD_vs_Soft_Starter/research_handoff.json` (Unchanged)

Không có tệp schema trong `02_AGENT_TEMPLATES/contracts/` hoặc script trong `scripts/` nào bị sửa đổi.

---

## 10. MỨC ĐỘ SẴN SÀNG CHO TECHNICAL REVIEW GATE (TECHNICAL REVIEW READINESS)

- **Trạng thái bài viết (`article_status.json`)**: Duy trì **`TECH_REVIEW`**.
- Bản thảo `draft_review_package.md` và bản đồ luận điểm `claim_source_map.json` đã được làm sạch triệt để về mặt ngữ nghĩa và ranh giới bằng chứng, đáp ứng đầy đủ tính khách quan kỹ thuật để sẵn sàng cho Review Agent tiến hành kiểm định độc lập tại **Technical Review Gate**.
