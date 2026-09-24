# QUY CHUẨN KIỂM DUYỆT VÀ PHẢN BIỆN KỸ THUẬT (TECHNICAL REVIEW & AUDIT PROTOCOL)
Version: 1.0  
Trạng thái: Áp dụng bắt buộc cho Tech Review Agent  
Mục tiêu: Đóng vai trò "Người gác cổng" (Gatekeeper) đảm bảo tính chính xác kỹ thuật 100% trước khi bài viết được trình ký hoặc xuất bản.

---

## 1. MỤC ĐÍCH & NGUYÊN TẮC KIỂM DUYỆT

Tech Review Agent hoạt động hoàn toàn độc lập với Drafting Agent. Mục tiêu không phải là "khen ngợi bài viết" mà là **tìm kiếm lỗi sai, lỗ hổng logic, công thức thiếu đơn vị, và các trích dẫn thiếu căn cứ**.

### Nguyên tắc bất di bất dịch:
1. **Không có bằng chứng = Từ chối duyệt**: Nếu một con số kỹ thuật hoặc công thức không truy nguyên được nguồn gốc trong `evidence_dossier.md`, bài viết không được thông qua.
2. **Sai toán học = Lỗi nghiêm trọng (Critical Defect)**: Công thức sai thứ nguyên (dimensional error) hoặc thiếu giải thích biến số lập tức bị đánh rớt (*FAIL*).
3. **Bài viết public phải sạch tuyệt đối**: Không để sót bất kỳ ghi chú Agent, nhắc nhở nội bộ hay đánh dấu kỹ thuật nào lọt vào mã HTML CKEditor công khai.

---

## 2. 4 TRỤ CỘT KIỂM DUYỆT (4 AUDIT PILLARS)

Mọi bài viết trước khi xuất xưởng phải trải qua 4 ma trận kiểm tra:

```text
┌────────────────────────────────────────────────────────┐
│ 1. CITATION AUDIT (Kiểm duyệt Trích dẫn & Nguồn IEEE) │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. FORMULA AUDIT (Kiểm duyệt Công thức Toán & LaTeX)  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. CLAIM & LOGIC AUDIT (Kiểm duyệt Logic & Ngữ cảnh)  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. PRESENTATION AUDIT (Kiểm duyệt Mã HTML CKEditor)   │
└────────────────────────────────────────────────────────┘
```

---

### TRỤ CỘT 1: CITATION AUDIT (Theo IEEE Skill v1.3)

- [ ] **Nhận định Đúng Loại Tài liệu (Source Type Classification Check)**:
  - Agent đã phân loại và gán nhãn đúng loại hình tài liệu trong `evidence_dossier.md` chưa?
  - Bắt buộc phân định rạch ròi 10 loại hình: `STANDARD`, `MANUAL`, `JOURNAL_PAPER`, `CONF_PAPER`, `BLOG_POST`, `WEB_ARTICLE`, `TECH_REPORT`, `BOOK`, `DATASHEET`, `THESIS`.
  - Nghiêm cấm quy đồng tài liệu PDF/báo cáo thành bài Web thông thường, hoặc ngược lại.
- [ ] **Cấu trúc Đặt tên Chuẩn IEEE theo Từng Loại (Per-Type IEEE Naming & Typography Check)**:
  - `BLOG_POST`: Tên bài trong ngoặc kép `"..."`, tên Blog in nghiêng `*...*`, ngày đăng cụ thể, ngày truy cập và URL.
  - `JOURNAL_PAPER`: Tên bài báo trong ngoặc kép `"..."`, tên tạp chí in nghiêng viết tắt chính thức `*...*`, đầy đủ vol., no., pp., và mã DOI.
  - `CONF_PAPER`: Tên bài trong ngoặc kép `"..."`, kỷ yếu hội nghị in nghiêng `in *Proc. ...*`, địa điểm, năm.
  - `STANDARD`: **Tên tiêu chuẩn in nghiêng `*...*` bắt buộc đứng đầu**, tiếp theo là mã hiệu (e.g. IEEE Std 519-2022) và năm. Tuyệt đối không đưa tên tổ chức ("IEEE PES,", "IEC,") lên trước tiêu đề.
  - `MANUAL`: **Tên sổ tay in nghiêng `*...*` bắt buộc đứng đầu**, tiếp theo là tên hãng, địa điểm và năm. Tuyệt đối không đưa tên hãng lên trước tiêu đề.
  - `TECH_REPORT`: **Tên báo cáo bắt buộc đặt trong ngoặc kép `"..."`** (không in nghiêng), tiếp theo là cơ quan ban hành và mã hiệu `Rep. xxx`.
  - `BOOK`: Tác giả đứng đầu, tên sách in nghiêng `*...*`, nơi xuất bản và nhà xuất bản.
- [ ] **Dải trích dẫn trong văn bản**: Liệt kê rõ từng cặp ngoặc vuông `[1], [2], [3]`. Tuyệt đối không dùng gạch nối `[1]–[3]`.
- [ ] **Tính nhất quán trích dẫn số**: Các mã `[1]`, `[2]`, `[3]` xuất hiện theo thứ tự tăng dần từ đầu đến cuối bài viết.
- [ ] **Kiểm tra nguồn thực tế**: Mọi mục trong danh mục Tài liệu tham khảo cuối bài đều phải được gọi tên ít nhất 1 lần trong bài viết. Không chèn nguồn "trang trí".
- [ ] **Verified Locator Check**:
  - Đối với các tài liệu dài (> 10 trang, sách, tiêu chuẩn): Đã xác minh số trang (`p. 45`), số chương (`Sec. 2.1`) hoặc số bảng/hình cụ thể chưa?
  - Nếu locator chưa kiểm chứng: Chỉ được ghi `[n]`, tuyệt đối không tự bịa số trang.
- [ ] **Vị trí đặt trích dẫn**: Trích dẫn đặt trong câu văn tự nhiên (prose), **tuyệt đối không chèn vào bên trong môi trường LaTeX** `\begin{equation}`.

---

### TRỤ CỘT 2: FORMULA AUDIT (Theo LaTeX Skill v1.0)

- [ ] **Cú pháp LaTeX chuẩn**: Sử dụng môi trường `\begin{equation}` hoặc `\begin{equation}\begin{aligned}...\end{aligned}\end{equation}`. Không dùng ký hiệu chém xiên dạng văn bản thô (e.g. `P = U*I*cos phi`) cho các công thức chính.
- [ ] **Phân tích thứ nguyên (Dimensional Analysis)**: Đơn vị ở vế trái và vế phải có đồng nhất không? (Ví dụ: Công suất tính ra kW hay W, có nhân thêm thừa số \(\sqrt{3}\) cho điện 3 pha không?).
- [ ] **Bảng giải thích biến số**: Nằm ngay sau công thức, nêu rõ tên biến, ý nghĩa và đơn vị đo lường theo chuẩn quốc tế SI.
- [ ] **Visual Rule (Quy chuẩn giao diện)**:
  - Công thức có bị đặt vào hộp có màu nền (colored box/card) không? *(Nếu có: BẮT BUỘC YÊU CẦU BỎ, công thức phải nằm trên nền trắng/trong suốt)*.
  - Công thức có bị viền khung (border) chỉ để trang trí không? *(Bắt buộc bỏ)*.
- [ ] **Worked Example Check**: Ví dụ thay số tính toán phải rõ ràng, phân biệt rạch ròi giữa số liệu danh định (Nameplate), số liệu đo thực tế và giả thiết minh họa. Không trình bày ví dụ như một khối code block đen xì.

---

### TRỤ CỘT 3: CLAIM & LOGIC AUDIT (Theo Blog Structure Standard v1.2)

- [ ] **Logic luồng kỹ thuật**: Bài viết có đi đúng mạch: *Context → Problem → Technical Explanation → Practical Application → Decision/Action → Conclusion* không?
- [ ] **Loại bỏ từ ngữ tuyệt đối hóa vô căn cứ**: Quét và loại bỏ các từ: "chắc chắn", "luôn luôn", "bắt buộc phải thay mới", trừ khi có điều kiện ràng buộc kỹ thuật rõ ràng.
- [ ] **Kiểm tra ngưỡng kỹ thuật (Thresholds)**:
  - Các con số như "dưới 50% tải", "độ lệch áp 2%", "THD 5%" có nguồn trích dẫn từ Tier 1/2 không?
  - Có nêu rõ giới hạn áp dụng và các trường hợp ngoại lệ (Exceptions) không?
- [ ] **Tính phi thương mại**: Bài viết mang tính chất chia sẻ giải pháp kỹ thuật, không biến thành bài quảng cáo bán hàng lộ liễu.

---

### TRỤ CỘT 4: PRESENTATION & OUTPUT HYGIENE AUDIT (Theo Master Style v1.0)

- [ ] **Tương thích CKEditor 3.6.6.2**: Toàn bộ nội dung bài viết được bao bọc trong thẻ gốc:
  ```html
  <div style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:1.7;color:#243447;">
  ```
- [ ] **Semantic Callout Check**:
  - Technical Note dùng viền xanh lam `#0284c7`, nền `#f0f9ff`.
  - Limitation dùng viền hổ phách `#d97706`, nền `#fffbeb`.
  - Safety Warning dùng viền đỏ `#dc2626`, nền `#fef2f2`.
  - Không lạm dụng callout tràn lan (mỗi bài chỉ từ 2–4 callouts thực sự quan trọng).
- [ ] **Public Output Hygiene**:
  - Không còn thẻ placeholder chưa xử lý (ví dụ: `[IMAGE_1]`).
  - Không lọt ghi chú nội bộ của Agent: "Ghi chú cho Reviewer", "TODO", "Skill version".

---

## 3. ĐÁNH GIÁ VÀ RA QUYẾT ĐỊNH (AUDIT DECISION)

Kết quả kiểm duyệt chỉ có 1 trong 3 trạng thái:

1. **PASS (ĐẠT)**: Không có lỗi nghiêm trọng, toàn bộ 4 trụ cột đều đạt. Cho phép chuyển sang khâu đóng gói xuất bản HTML.
2. **REVISION_REQUIRED (YÊU CẦU HIỆU CHỈNH)**: Có từ 1 đến 3 lỗi nhỏ (ví dụ: thiếu đơn vị của 1 biến số, câu chữ hơi hướng quảng cáo, citation chưa chuẩn IEEE). Trả về cho Drafting Agent chỉnh sửa cụ thể.
3. **FAIL (TỪ CHỐI)**: Có lỗi nghiêm trọng (sai công thức toán học, trích dẫn số liệu bịa đặt, vi phạm nghiêm trọng quy chuẩn Master Style). Yêu cầu soạn thảo lại.

---

## 4. BIỂU MẪU BÁO CÁO KIỂM DUYỆT (DELIVERABLE SCHEMA)

Báo cáo kiểm duyệt phải được xuất thành file `technical_audit_report.md` tại thư mục bài viết:

```markdown
# BÁO CÁO KIỂM DUYỆT KỸ THUẬT (TECHNICAL AUDIT REPORT)
**Mã bài viết**: [MÃ_BÀI]  
**Ngày kiểm duyệt**: [YYYY-MM-DD]  
**Người kiểm duyệt**: Tech Review Agent  
**Kết quả chung**: [PASS / REVISION_REQUIRED / FAIL]

## 1. Tổng kết 4 Trụ cột
| Trụ cột | Trạng thái | Số lỗi phát hiện | Ghi chú |
|---|---|---|---|
| 1. Citation Audit | PASS / FAIL | 0 | ... |
| 2. Formula Audit | PASS / FAIL | 0 | ... |
| 3. Claim & Logic | PASS / FAIL | 0 | ... |
| 4. Presentation | PASS / FAIL | 0 | ... |

## 2. Chi tiết các điểm cần hiệu chỉnh (nếu có)
- [Vị trí dòng / Heading]: [Mô tả lỗi & Yêu cầu chỉnh sửa cụ thể]

## 3. Chữ ký Phê duyệt Kỹ thuật
- [x] ĐÃ XÁC NHẬN BÀI VIẾT ĐẠT CHUẨN KỸ THUẬT VÀ SẴN SÀNG TRÌNH KÝ.
```
