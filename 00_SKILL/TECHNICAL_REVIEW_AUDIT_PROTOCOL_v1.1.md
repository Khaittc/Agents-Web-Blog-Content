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

## 2. KIẾN TRÚC 2 CỔNG KIỂM ĐỊNH ĐỘC LẬP (TWO-GATE AUDIT ARCHITECTURE)

Nhằm tối ưu hóa luồng kiểm duyệt, tránh lãng phí thời gian tạo đồ họa khi bản thảo kỹ thuật chưa đạt chuẩn, quy trình kiểm duyệt được chia tách thành **2 CỔNG ĐỘC LẬP TÁCH BẠCH**:

```text
Drafting Agent Hoàn thành Bản thảo & Claim Map
                     │
                     ▼
┌────────────────────────────────────────────────────────┐
│ CỔNG 1: TECHNICAL REVIEW GATE (Kiểm Định Chuyên Môn)   │
│ ├── Trụ cột 1: Citation Audit (IEEE, Gate 5 Cuối câu)  │
│ ├── Trụ cột 2: Formula Audit (LaTeX & Đơn vị SI)       │
│ └── Trụ cột 3: Claim & Logic Audit (Khớp evidence.json)│
│ (LƯU Ý: KHÔNG kiểm tra responsive tại Cổng 1)          │
└────────────────────────────┬───────────────────────────┘
                             │ PASS (TECH_APPROVED)
                             ▼
              Visual Agent (Hoàn thiện ảnh)
                             │
                             ▼
              Packaging Agent (HTML Packaging & Manifest)
                             │
                             ▼
┌────────────────────────────────────────────────────────┐
│ CỔNG 2: PRESENTATION & RESPONSIVE REVIEW GATE          │
│ └── Trụ cột 4: Presentation & Responsive Audit         │
│     ├── Hiển thị Laptop (>= 1200px)                    │
│     ├── Hiển thị Mobile Smartphone (360px - 480px)     │
│     ├── Chống méo dọc ảnh (height: auto !important)    │
│     ├── Bảng chống nén ép (overflow-x + min-width)     │
│     ├── Link tham khảo không tràn viền (word-break)    │
│     └── Vệ sinh mã nguồn sạch tuyệt đối (Output Clean) │
└────────────────────────────┬───────────────────────────┘
                             │ PASS
                             ▼
            Human Review & Manual CMS Publish
```

---

### TRỤ CỘT 1: CITATION & SOURCE POLICY AUDIT (Theo IEEE Master Suite v2.0 & ADR-024)

- [ ] **Thẩm tra Chính sách Nguồn & Ngoại lệ Thẩm quyền Cao (Source Policy Check - ADR-024)**:
  - Mặc định: Đạt 4–7 nguồn kỹ thuật, tỷ lệ Tier 1 + Tier 2 ưu tiên $\ge 70\%$.
  - Nếu sử dụng 1–3 nguồn: Bắt buộc có cờ `source_policy_exception` trong `evidence.json`. Review Agent thẩm định tính chuyên sâu hẹp và thẩm quyền nguồn sơ cấp để ban hành phán quyết: `APPROVE_EXCEPTION` hoặc `REJECT_EXCEPTION`.
  - Không dùng số lượng nguồn làm thang điểm chất lượng bài viết (chất lượng đánh giá theo tính thẩm quyền, độ xác thực, độ tươi mới và độ bao phủ luận điểm).
- [ ] **Nhận định Đúng Loại Tài liệu (Source Type Classification Check - IEEE-01 v1.1)**:
  - Phân loại và gán nhãn đúng hệ thống phân loại nguồn mở trong `evidence_dossier.md` và `evidence.json`.
  - Cửa ải Điều hướng Trực tiếp (ADR-015): 100% link phải mở đúng tài liệu (Deep Link / Direct PDF / Launch URL), cấm link trang chủ hoặc link tìm kiếm chung chung. Tách bạch `canonical_url` và `retrieval_url`.
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

## 3. ĐÁNH GIÁ, VÒNG LẶP HIỆU CHỈNH VÀ RA QUYẾT ĐỊNH (AUDIT DECISIONS & REVISION LOOP)

### 3.1. Phán quyết tại từng Cổng Kiểm định
Tại mỗi cổng (`TECHNICAL_REVIEW_GATE` hoặc `PRESENTATION_REVIEW_GATE`), Review Agent xuất ra 1 trong 3 trạng thái:
1. **`PASS` (ĐẠT)**: 100% tiêu chí của cổng đạt chuẩn. Cho phép chuyển sang công đoạn tiếp theo.
2. **`REVISION_REQUIRED` (YÊU CẦU HIỆU CHỈNH)**: Phát hiện sai lệch cần sửa đổi. Bắt buộc lập tệp `revision_request.json`.
3. **`FAIL` (TỪ CHỐI)**: Vi phạm nghiêm trọng không thể khắc phục nhanh. Yêu cầu làm lại công đoạn.

### 3.2. Quy chế Vòng lặp Hiệu chỉnh có Cấu trúc (`revision_request.json`)
Khi ra phán quyết `REVISION_REQUIRED`, Review Agent bắt buộc tạo tệp `revision_request.json` tuân thủ `02_AGENT_TEMPLATES/contracts/revision_request.schema.json`:
- **Giới hạn phạm vi (Scope-limited)**: Phải chỉ định rõ `owner` (`RESEARCH`, `DRAFTING`, `VISUAL`, `PUBLISHER`), `artifact`, `claim_id` (nếu có), và `scope`. Agent được giao **CHỈ SỬA ĐÚNG PHẠM VI**, cấm rewrite toàn bài nếu lỗi chỉ ở một phần tử đơn lẻ.
- **Giới hạn tối đa 3 vòng lặp tự động (Max 3 Loops)**: Nếu sau 3 lần hiệu chỉnh tự động mà vẫn không đạt, Review Agent chuyển sang trạng thái `ESCALATED_TO_HUMAN` để Kỹ sư trưởng can thiệp trực tiếp.

---

## 4. BIỂU MẪU GIAO PHẨM KIỂM DUYỆT (DELIVERABLE ARTIFACTS)

Review Agent chịu trách nhiệm xuất song song:
1. **`audit.json`**: Bản ghi máy đọc canonical theo `02_AGENT_TEMPLATES/contracts/audit.schema.json`.
2. **`technical_audit_report.md`**: Báo cáo tổng hợp dành cho Kỹ sư trưởng:

```markdown
# BÁO CÁO KIỂM ĐỊNH KỸ THUẬT & RESPONSIVE ĐA THIẾT BỊ (AUDIT REPORT)
**Mã bài viết**: [MÃ_BÀI]
**Ngày kiểm duyệt**: [YYYY-MM-DD]
**Người kiểm duyệt**: Review Agent (Chief Technical Auditor)

## PHẦN 1: KẾT QUẢ CỔNG 1 — TECHNICAL REVIEW GATE
- **Trạng thái Cổng 1**: [PASS / REVISION_REQUIRED / FAIL]
- **Trụ cột 1 (Citation Audit)**: Chuẩn IEEE, 100% trích dẫn ở CUỐI CÂU (Gate 5).
- **Trụ cột 2 (Formula Audit)**: Thứ nguyên SI chuẩn xác, đầy đủ bảng biến số.
- **Trụ cột 3 (Claim & Logic Audit)**: Số liệu đối chiếu khớp 100% evidence.json.

## PHẦN 2: KẾT QUẢ CỔNG 2 — PRESENTATION & RESPONSIVE REVIEW GATE
- **Trạng thái Cổng 2**: [PASS / REVISION_REQUIRED / FAIL]
- **Đánh giá Laptop (>= 1200px)**: Bảng 100%, typography chuẩn CKEditor 3.6.6.2.
- **Đánh giá Mobile (360px - 480px)**:
  - [x] Hình ảnh: Có `height: auto !important; margin: 0 auto;`, không méo dọc.
  - [x] Bảng kỹ thuật: Bọc `overflow-x: auto;`, `min-width: 680px - 720px;`, cuộn ngang mượt.
  - [x] Link tham khảo: Bọc `word-break: break-all;`, không tràn màn hình điện thoại.
- **Vệ sinh mã nguồn**: Sạch 100% ghi chú nội bộ.

## PHẦN 3: KẾT LUẬN & CHỮ KÝ PHÊ DUYỆT
- [x] ĐÃ XÁC NHẬN BÀI VIẾT ĐẠT CHUẨN KỸ THUẬT VÀ HIỂN THỊ HOÀN HẢO TRÊN CẢ LAPTOP LẪN MOBILE.
```
