# QUY CHUẨN KIỂM DUYỆT VÀ PHẢN BIỆN KỸ THUẬT (TECHNICAL REVIEW & AUDIT PROTOCOL)
**Version**: 1.1  
**Trạng thái**: Áp dụng bắt buộc cho Tech Review Agent, Drafting Agent và Publisher Agent  
**Ngày ban hành**: 24/09/2026  
**Thay thế**: `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md` (Đã lưu trữ tại `00_SKILL/archive/`)  
**Căn cứ pháp lý & kỹ thuật**:
- `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md`
- `IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md` (Bộ 4 Sub-Skills IEEE-01 đến IEEE-04)
- `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md`
- `LATEX_FORMULA_SKILL_v1.0.md`
- `REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md`
- **ADR-016**: Tiêu chuẩn Responsive Đa thiết bị (Laptop & Mobile).
- **ADR-017**: Cửa ải Kiểm định Responsive Song song Bắt buộc trên Laptop và Mobile cho Tech Review Agent.

---

## 1. MỤC ĐÍCH & NGUYÊN TẮC KIỂM DUYỆT

Tech Review Agent hoạt động hoàn toàn độc lập với Drafting Agent. Mục tiêu không phải là "khen ngợi bài viết" mà là **tìm kiếm lỗi sai, lỗ hổng logic, công thức thiếu đơn vị, các trích dẫn thiếu căn cứ, và các lỗi vỡ layout hiển thị trên Laptop và Mobile**.

### Nguyên tắc bất di bất dịch:
1. **Không có bằng chứng = Từ chối duyệt**: Nếu một con số kỹ thuật hoặc công thức không truy nguyên được nguồn gốc trong `evidence_dossier.md`, bài viết không được thông qua.
2. **Sai toán học = Lỗi nghiêm trọng (Critical Defect)**: Công thức sai thứ nguyên (dimensional error) hoặc thiếu giải thích biến số lập tức bị đánh rớt (*FAIL*).
3. **Bài viết public phải sạch tuyệt đối**: Không để sót bất kỳ ghi chú Agent, nhắc nhở nội bộ hay đánh dấu kỹ thuật nào lọt vào mã HTML CKEditor công khai.
4. **Kiểm tra song song Laptop & Mobile (ADR-017)**: Bài viết phải hiển thị hoàn hảo, không méo hình, không ép nén cột bảng và không tràn lề trên cả 2 môi trường Laptop và Mobile trước khi ký duyệt.

---

## 2. 4 TRỤ CỘT KIỂM DUYỆT (4 AUDIT PILLARS)

Mọi bài viết trước khi xuất xưởng bắt buộc phải vượt qua 4 ma trận kiểm tra:

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
│ 4. PRESENTATION & RESPONSIVE AUDIT (Laptop & Mobile)   │
└────────────────────────────────────────────────────────┘
```

---

### TRỤ CỘT 1: CITATION AUDIT (Theo IEEE Master Suite v2.0)

- [ ] **Nhận định Đúng Loại Tài liệu (Source Type Classification Check - IEEE-01 v1.1)**:
  - Phân loại và gán nhãn đúng 1 trong 10 loại hình kỹ thuật trong `evidence_dossier.md`: `STANDARD`, `MANUAL`, `JOURNAL_PAPER`, `CONF_PAPER`, `BLOG_POST`, `WEB_ARTICLE`, `TECH_REPORT`, `BOOK`, `DATASHEET`, `THESIS`.
  - Cửa ải Điều hướng Trực tiếp (ADR-015): 100% link phải là Deep Link hoặc Direct PDF, cấm link trang chủ hoặc link tìm kiếm chung chung.
- [ ] **Cấu trúc Đặt tên Chuẩn IEEE theo Từng Loại (IEEE-03 v1.1)**:
  - `STANDARD`: *Tên tiêu chuẩn in nghiêng* đứng đầu, mã hiệu, năm. Cấm đặt tên tổ chức lên trước.
  - `MANUAL`: *Tên sổ tay in nghiêng* đứng đầu, tên hãng, địa điểm, năm. Cấm đặt tên hãng lên trước.
  - `TECH_REPORT`: Tên báo cáo trong ngoặc kép `"..."`, cơ quan ban hành, mã hiệu `Rep. xxx`.
  - `JOURNAL_PAPER`: Tác giả, tên bài trong ngoặc kép `"..."`, *Tên tạp chí in nghiêng viết tắt*, vol., no., pp., DOI.
  - `BLOG_POST`: Tác giả, tên bài trong ngoặc kép `"..."`, *Tên Blog in nghiêng*, ngày đăng, [Online]. Available: URL.
- [ ] **Cú pháp Ngoặc vuông & Locator (IEEE-02 v1.1)**:
  - Liệt kê từng cặp ngoặc vuông riêng biệt `[1], [2], [3]`. Tuyệt đối cấm gạch nối `[1]–[3]`.
  - Số thứ tự `[n]` tăng dần liên tục theo trật tự xuất hiện từ trên xuống dưới.
  - Đầy đủ locator kiểm chứng (`p. 45`, `Sec. 2.1`, `Tab. 5.1`).
- [ ] **Gate 5: Vị trí Trích dẫn Nội văn Bắt buộc ở CUỐI CÂU (IEEE-02 v1.1 & IEEE-04 v1.1)**:
  - 100% trích dẫn `[n]` phải đặt ở cuối câu văn (ngay trước dấu chấm `.` hoặc dấu hai chấm `:`).
  - Đánh rớt (FAIL) nếu phát hiện trích dẫn nằm giữa câu làm đứt đoạn mạch đọc.

---

### TRỤ CỘT 2: FORMULA AUDIT (Theo LaTeX Skill v1.0)

- [ ] **Cú pháp LaTeX chuẩn**: Sử dụng môi trường `\begin{equation}` hoặc `\begin{equation}\begin{aligned}...\end{aligned}\end{equation}`. Không dùng ký hiệu chém xiên dạng văn bản thô cho công thức chính.
- [ ] **Phân tích thứ nguyên (Dimensional Analysis)**: Đơn vị ở vế trái và vế phải đồng nhất (kW, W, V, A, \(\Omega\), \(\text{N}\cdot\text{m}\)).
- [ ] **Bảng giải thích biến số**: Nêu rõ tên biến, ý nghĩa và đơn vị đo lường theo chuẩn quốc tế SI ngay dưới công thức.
- [ ] **Visual Rule (Quy chuẩn giao diện)**:
  - Công thức nằm trên nền trắng/trong suốt, không đặt vào hộp có màu nền (colored box/card).
  - Không viền khung (border) trang trí. Bọc div ngoài có `overflow-x: auto;` để chống vỡ màn hình mobile khi công thức dài.
- [ ] **Worked Example Check**: Phân biệt rạch ròi giữa số liệu danh định (Nameplate), số liệu đo thực tế và giả thiết minh họa. Không trình bày ví dụ như khối code block đen xì.

---

### TRỤ CỘT 3: CLAIM & LOGIC AUDIT (Theo Blog Structure Standard v1.3)

- [ ] **Logic luồng kỹ thuật**: Bài viết đi đúng mạch: *Context → Problem → Technical Explanation → Practical Application → Decision/Action → Conclusion*.
- [ ] **Loại bỏ từ ngữ tuyệt đối hóa vô căn cứ**: Không dùng từ "chắc chắn", "luôn luôn", "bắt buộc phải thay mới", trừ khi có điều kiện ràng buộc kỹ thuật rõ ràng.
- [ ] **Kiểm tra ngưỡng kỹ thuật (Thresholds)**: Mọi con số định lượng (độ lệch trở \(\le 2\%\), cách điện \(\ge 5\text{ M}\Omega\), THD 5%) có nguồn trích dẫn từ Tier 1/Tier 2.
- [ ] **Tính phi thương mại**: Bài viết mang tính chia sẻ chuyên môn, không biến thành bài quảng cáo bán hàng lộ liễu.

---

### TRỤ CỘT 4: PRESENTATION & RESPONSIVE AUDIT ĐA THIẾT BỊ (LAPTOP & MOBILE) (Theo Master Style v1.0, ADR-016 & ADR-017)

Tech Review Agent **BẮT BUỘC** phải rà soát mã HTML CKEditor trên cả 2 độ phân giải:
- **Laptop / Desktop ($\ge 1200\text{ px}$)**: Cột hiển thị nội dung $\approx 750\text{ px} - 800\text{ px}$.
- **Mobile Smartphone ($360\text{ px} - 480\text{ px}$)**: Màn hình điện thoại thực tế của người dùng.

#### 4.1. Cửa ải Kiểm tra Hình ảnh (Laptop & Mobile Image Viewport Check):
- [ ] Thẻ `<img>` **BẮT BUỘC** có khai báo:
  ```html
  style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;"
  ```
- [ ] **Khóa méo tỷ lệ (Anti-Distortion Gate)**: Đảm bảo có `height: auto !important;`. Tuyệt đối không để thuộc tính chiều cao cố định (ví dụ `height: 675px`) làm biến dạng ảnh trên Mobile từ 16:9 thành 1:1.87 dọc.
- [ ] **Căn giữa trang nhã**: Bắt buộc có `display: block; margin: 0 auto;` để hình ảnh không bị dạt sang trái trên điện thoại di động.
- [ ] Có đầy đủ thẻ `alt` chuẩn SEO kỹ thuật và chú thích ảnh in nghiêng (`Hình n:`).

#### 4.2. Cửa ải Kiểm tra Bảng Kỹ thuật (Laptop & Mobile Table Layout Check):
- [ ] Thẻ `<table>` **BẮT BUỘC** được bao bọc trong thẻ `<div>` có:
  ```html
  <div style="margin:0 0 24px 0;overflow-x:auto;-webkit-overflow-scrolling:touch;border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  ```
- [ ] **Khóa độ rộng tối thiểu (Min-Width Gate)**: Thẻ `<table>` **BẮT BUỘC** có:
  - Bảng 4–5 cột: `min-width: 680px;` (hoặc từ 650px).
  - Bảng 6 cột trở lên: `min-width: 720px;` (hoặc đến 760px).
  - Đánh rớt (FAIL) nếu bảng chỉ có `width: 100%` mà thiếu `min-width`, vì trên điện thoại các cột sẽ bị ép chặt, chữ bị bẻ thành từng chữ cái đơn lẻ.
- [ ] Trên Laptop: Bảng tự động giãn nở đủ `100%` độ rộng cột bài viết.
- [ ] Trên Mobile: Bảng giữ nguyên cấu trúc đọc rõ ràng và cho phép người dùng cuộn vuốt ngang mượt mà.
- [ ] Có dòng ghi chú trợ năng phía trên bảng:
  ```html
  <div style="text-align:right;font-size:12px;color:#94a3b8;margin-bottom:4px;font-style:italic;">(Cuộn ngang trên điện thoại để xem trọn vẹn bảng)</div>
  ```

#### 4.3. Cửa ải Kiểm tra Đường dẫn Tham khảo (Mobile Link Word-Break Gate):
- [ ] Khung chứa từng mục tham khảo **BẮT BUỘC** có:
  ```html
  style="padding-left:28px;text-indent:-28px;margin-bottom:12px;line-height:1.6;font-size:14px;word-break:break-word;overflow-wrap:anywhere;"
  ```
- [ ] Thẻ liên kết `<a href="...">` **BẮT BUỘC** có `word-break: break-all;`:
  ```html
  style="color:#005a9c;text-decoration:underline;word-break:break-all;"
  ```
- [ ] Đánh rớt (FAIL) nếu các link dài (> 80 ký tự không dấu cách) thiếu thuộc tính bẻ dòng, vì sẽ đẩy toàn bộ layout trang web trên Mobile ra ngoài màn hình 360px gây rung lắc ngang.

#### 4.4. Cửa ải Kiểm tra Phân cấp Tiêu đề (Heading Hierarchy Gate):
- [ ] Nội dung CKEditor **BẮT BUỘC** bắt đầu từ thẻ `<h2>` cho các đề mục chính và `<h3>` cho các đề mục con.
- [ ] Tuyệt đối không lặp lại thẻ `<h1>` bên trong thân bài viết CKEditor (tránh xung đột SEO với tiêu đề chính của template web).
- [ ] Cỡ chữ `<h2>` (khoảng 20–22px) và `<h3>` (khoảng 17–18px) cân đối, dễ đọc trên cả máy tính và điện thoại.

#### 4.5. Output Hygiene & Callouts:
- [ ] Không còn thẻ placeholder chưa xử lý (ví dụ: `[URL_HINH_ANH_1]`).
- [ ] Không để lọt ghi chú nội bộ của Agent: "TODO", "Review note", "Skill version".
- [ ] Semantic Callouts đúng màu sắc: Technical Note (xanh lam `#0284c7`), Limitation (hổ phách `#d97706`), Safety Warning (đỏ `#dc2626`).

---

## 3. ĐÁNH GIÁ VÀ RA QUYẾT ĐỊNH (AUDIT DECISION)

Kết quả kiểm duyệt chỉ có 1 trong 3 trạng thái:

1. **PASS (ĐẠT)**: Toàn bộ 4 trụ cột đều đạt, bao gồm 100% tiêu chí hiển thị trên cả Laptop và Mobile. Cho phép chuyển sang khâu xuất bản HTML.
2. **REVISION_REQUIRED (YÊU CẦU HIỆU CHỈNH)**: Có từ 1 đến 3 lỗi nhỏ (ví dụ: thiếu `word-break: break-all;` trên link tham khảo, thiếu `min-width` trên 1 bảng, câu chữ hơi hướng quảng cáo). Trả về cho Drafting Agent chỉnh sửa cụ thể.
3. **FAIL (TỪ CHỐI)**: Có lỗi nghiêm trọng (sai công thức toán học, trích dẫn số liệu bịa đặt, ảnh bị méo dọc trên mobile, vỡ layout màn hình). Yêu cầu soạn thảo lại.

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
| Trụ cột | Trạng thái | Số lỗi phát hiện | Đánh giá Laptop | Đánh giá Mobile | Ghi chú |
|---|---|---|---|---|---|
| 1. Citation Audit | PASS / FAIL | 0 | Chuẩn IEEE | Chuẩn IEEE | ... |
| 2. Formula Audit | PASS / FAIL | 0 | Đầy đủ SI | Có overflow cuộn | ... |
| 3. Claim & Logic | PASS / FAIL | 0 | Logic chặt chẽ | Dễ lướt đọc | ... |
| 4. Presentation & Responsive | PASS / FAIL | 0 | Bảng 100%, ảnh 16:9 | Không méo ảnh, cuộn bảng mượt, URL không tràn | ... |

## 2. Chi tiết Cửa ải Responsive Đa Thiết bị (Laptop vs. Mobile)
- [x] Hình ảnh: Đã ép `height: auto !important;` và `margin: 0 auto;`, khóa tỷ lệ 16:9 tự nhiên.
- [x] Bảng kỹ thuật: Đã bọc `overflow-x: auto; -webkit-overflow-scrolling: touch;`, khai báo `min-width: 680px - 720px;`, không ép nén cột trên mobile.
- [x] Tài liệu tham khảo: Đã có `word-break: break-word;` và `word-break: break-all;`, không tràn khung màn hình điện thoại.
- [x] Phân cấp tiêu đề: Bắt đầu từ `<h2>` và `<h3>`, tương thích hoàn hảo với CMS.

## 3. Chữ ký Phê duyệt Kỹ thuật
- [x] ĐÃ XÁC NHẬN BÀI VIẾT ĐẠT CHUẨN KỸ THUẬT VÀ HIỂN THỊ HOÀN HẢO TRÊN CẢ LAPTOP LẪN MOBILE.
```
