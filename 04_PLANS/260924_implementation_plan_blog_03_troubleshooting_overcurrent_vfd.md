# Kế hoạch Triển khai Bài viết Stress-test Thứ 3: BLOG_03 (Troubleshooting Overcurrent trên Biến tần)
**Mã kế hoạch**: `260924_implementation_plan_blog_03_troubleshooting_overcurrent_vfd`  
**Ngày lập**: 24/09/2026  
**Thuộc Giai đoạn**: Phase 2 — Stress-test & Standards Expansion ([ROADMAP.md](file:///d:/Agents_Tools/05_WebsiteTTC/ROADMAP.md))  
**Vị trí lưu trữ**: [04_PLANS/260924_implementation_plan_blog_03_troubleshooting_overcurrent_vfd.md](file:///d:/Agents_Tools/05_WebsiteTTC/04_PLANS/260924_implementation_plan_blog_03_troubleshooting_overcurrent_vfd.md) (Tuân thủ ADR-006 & ADR-014)  
**Trạng thái**: 🟡 **ĐANG CHỜ KỸ SƯ TRƯỞNG DUYỆT (PROPOSED FOR REVIEW)**  

---

## 1. MỤC TIÊU & BỐI CẢNH

Sau khi hoàn thành và khóa an toàn 2 bài viết nền tảng:
- `BLOG_01`: *Cách phát hiện động cơ điện đang chạy non tải trong nhà máy* (Dạng `BLOG-T02` — How-to / Measurement, Baseline đã khóa).
- `BLOG_02`: *Hệ số công suất cos phi và sóng hài trong nhà máy: Phân biệt bản chất và giải pháp xử lý triệt để* (Dạng `BLOG-T01` — Technical Explanation, Gold Standard đã khóa).

Kế hoạch này khởi động bài viết kiểm nghiệm kỹ thuật thứ 3 (**`BLOG_03`**), đại diện cho thể loại nội dung có lượng tìm kiếm kỹ thuật và giá trị thực chiến cao nhất trong nhà máy công nghiệp: **`BLOG-T03` — Troubleshooting (Chẩn đoán & Xử lý sự cố kỹ thuật)**.

### Mục tiêu Cốt lõi:
1. **Stress-test cấu trúc `BLOG-T03`**: Kiểm tra tính hiệu quả của quy trình 5 Agent khi giải quyết một bài toán chẩn đoán sự cố theo trình tự logic cô lập từ ngoài vào trong.
2. **Áp dụng toàn diện các quy chuẩn mới được nâng cấp**:
   - `IEEE_01 v1.0`: Nhận diện 10 loại nguồn & Cửa ải xác thực URL sống (HTTP 200 OK) trước khi đưa vào Dossier.
   - `IEEE_02 v1.1`: Đánh số tuần tự, ngoặc vuông rời `[1], [2]` và **100% trích dẫn bắt buộc đặt ở CUỐI CÂU** (ADR-013).
   - `IEEE_03 v1.0`: Cấu trúc đặt tên chuẩn hóa, thụt lề treo 25px và siêu liên kết click được trên CKEditor (`<a>`).
   - `IEEE_04 v1.1`: Ma trận kiểm định 6 cửa ải độc lập từ Tech Review Agent.
   - `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1`: Cung cấp Prompt AI 5 tầng, 2 hình ảnh nội dung kỹ thuật (1 Lưu đồ quyết định + 1 Sơ đồ đo kiểm IGBT), khung HTML placeholder `<img>` sạch.
   - `ADR-014`: 100% tệp tin được tạo và lưu trữ trực tiếp bên trong `d:/Agents_Tools/05_WebsiteTTC/`.

---

## 2. ĐỀ BÀI KỸ THUẬT: BLOG_03

- **Chủ đề**: *Quy trình chẩn đoán và khắc phục lỗi quá dòng (Overcurrent - F0001 / OC) trên biến tần công nghiệp*.
- **Loại bài**: `BLOG-T03` (Troubleshooting).
- **Thư mục làm việc**: [03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/).
- **Phạm vi kỹ thuật**:
  - Đối chiếu mã lỗi quá dòng của các hãng biến tần hàng đầu: Siemens (F0001 / F0004), Yaskawa (oC / oL2), ABB (Fault 2310 / Overcurrent), Danfoss (Alarm 13 / Overcurrent), Mitsubishi (E.OC1 / E.OC2 / E.OC3), Inovance (Err02 / Err03).
  - Phân tích điều kiện phát sinh: Quá dòng khi tăng tốc (Accel), khi giảm tốc (Decel), khi đang chạy tải ổn định (Steady-state), hoặc nổ/báo lỗi tức thì ngay khi vừa cấp lệnh Run.
  - Phân loại 4 nhóm nguyên nhân gốc:
    1. Tải cơ khí (kẹt cơ khí, bạc đạn vỡ, quán tính tải quá lớn so với dải biến tần).
    2. Cáp nguồn & động cơ (chập pha-pha, chạm đất cuộn dây, suy giảm cách điện theo IEEE 43-2013).
    3. Cài đặt tham số điều khiển (thời gian Acc/Dec quá dốc, đường đặc tính V/f Boost quá mức, nhận dạng động cơ Auto-tuning sai).
    4. Phần cứng khối công suất biến tần (chập van nghịch lưu IGBT, hỏng mạch kích lái Gate Driver, hỏng cảm biến dòng CT/Hall sensor).
  - Quy trình 4 bước cô lập & đo kiểm thực nghiệm (Đo điện trở cuộn dây, đo Megger kiểm tra cách điện, đo phân cực thuận/nghịch khối IGBT bằng thang đo Diode của đồng hồ VOM).
  - Cảnh báo an toàn điện: Điện áp bus một chiều DC Bus tích trữ 560V–800V DC trên dàn tụ lọc, quy trình xả điện an toàn và thử nghiệm đo áp dư trước khi chạm vào cầu đấu.

---

## 3. QUY TRÌNH PHỐI HỢP 5 AGENT & GIAO PHẨM DỰ KIẾN

```text
┌─────────────────────────┐
│ 1. RESEARCH AGENT       │ ──> Xuất evidence_dossier.md (Nguồn Tier 1 Siemens, Yaskawa, ABB, IEEE 43)
└─────────────────────────┘     (100% URL Live-Check HTTP 200 OK theo IEEE-01 v1.0)
             │
             ▼
┌─────────────────────────┐
│ 2. DRAFTING AGENT       │ ──> Soạn thảo draft_review_package.md chuẩn BLOG-T03
└─────────────────────────┘     (100% trích dẫn ở CUỐI CÂU theo IEEE-02 v1.1)
             │
             ▼
┌─────────────────────────┐
│ 3. VISUAL AGENT         │ ──> Thiết kế image_specifications.md theo Skill v1.1
└─────────────────────────┘     (Featured Image 808x500 + Hình 1 Lưu đồ + Hình 2 Sơ đồ đo IGBT)
             │
             ▼
┌─────────────────────────┐
│ 4. TECH REVIEW AGENT    │ ──> Thẩm định 4 trụ cột, xuất technical_audit_report.md
└─────────────────────────┘     (Chấm điểm 6 cửa ải trích dẫn theo IEEE-04 v1.1)
             │
             ▼
┌─────────────────────────┐
│ 5. PUBLISHER AGENT      │ ──> Đóng gói HTML CKEditor 3.6.6.2 & article_status.json
└─────────────────────────┘     (Link tham khảo clickable <a>, hanging indent 25px)
```

### Danh mục Tệp tin Bàn giao (100% trong `03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/`):
1. `evidence_dossier.md`: Nguồn tài liệu Tier 1/Tier 2 chính hãng kèm locator số trang chính xác và URL sống.
2. `draft_review_package.md`: Bản thảo nội dung kỹ thuật đầy đủ phần 1–12 chuẩn cấu trúc `BLOG-T03`.
3. `image_specifications.md`: Hồ sơ đặc tả hình ảnh, quy trình 5 bước và 3 bộ AI Prompts chuyên sâu.
4. `technical_audit_report.md`: Báo cáo kiểm định kỹ thuật 4 trụ cột (PASS).
5. `bai-viet-chan-doan-qua-dong-bien-tan-ckeditor.html`: Mã nguồn HTML sạch chuẩn CKEditor 3.6.6.2 sẵn sàng đăng tải.
6. `article_status.json`: Quản lý vòng đời bài viết (`status: "IN_REVIEW"`).

---

## 4. KẾ HOẠCH TRIỂN KHAI CHI TIẾT (TỪNG BƯỚC)

- **Bước 1**: Khởi tạo thư mục bài viết `03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/`.
- **Bước 2 (Research Agent)**: Thu thập và xác minh nguồn tài liệu Tier 1 từ Cẩm nang bảo trì & hướng dẫn khắc phục sự cố chính thức của Siemens (Sinamics S120/G120, Micromaster 440), Yaskawa (Technical Manual GA700/A1000), ABB (Firmware Manual ACS580/ACS880) và tiêu chuẩn thử nghiệm cách điện IEEE 43-2013. Chạy công cụ mạng kiểm tra mã HTTP 200 cho toàn bộ link trực tuyến và lập `evidence_dossier.md`.
- **Bước 3 (Drafting Agent)**: Soạn thảo bài viết kỹ thuật hoàn chỉnh theo form `BLOG-T03`, cấu trúc 8 mục nội dung mạch lạc, công thức tính toán thời gian tăng tốc tối thiểu, định luật Ohm bảo vệ quá dòng, và ép buộc 100% trích dẫn nội văn nằm ở cuối câu trước dấu chấm/hai chấm.
- **Bước 4 (Visual Agent)**: Lập hồ sơ `image_specifications.md` bao gồm:
  - Featured Image: Kỹ sư bảo trì đo kiểm biến tần trong tủ điện MCC (808×500 px).
  - Hình 1: Lưu đồ cây quyết định chẩn đoán lỗi OC 4 cấp độ (Tải $\rightarrow$ Cáp & Động cơ $\rightarrow$ Tham số $\rightarrow$ Khối IGBT).
  - Hình 2: Sơ đồ đo kiểm phân cực thuận/nghịch 6 van IGBT nghịch lưu bằng thang đo Diode đồng hồ vạn năng.
- **Bước 5 (Tech Review Agent)**: Thực hiện kiểm định 4 trụ cột, quét 6 cửa ải trích dẫn (`IEEE-04 v1.1`), kiểm tra vị trí trích dẫn cuối câu, đối chiếu công thức và xuất `technical_audit_report.md`.
- **Bước 6 (Publisher Agent)**: Đóng gói mã HTML CKEditor 3.6.6.2 sạch, định dạng bảng so sánh mã lỗi các hãng, semantic callouts (Lưu ý kỹ thuật, Cảnh báo an toàn điện áp cao DC bus), chèn placeholder ảnh `[URL_HINH_ANH_1]`, `[URL_HINH_ANH_2]`, định dạng danh mục tham khảo thụt lề 25px có thẻ `<a>` có thể click trực tiếp và khởi tạo `article_status.json`.
- **Bước 7**: Cập nhật tiến độ dự án vào [ROADMAP.md](file:///d:/Agents_Tools/05_WebsiteTTC/ROADMAP.md), [WORKLOG.md](file:///d:/Agents_Tools/05_WebsiteTTC/WORKLOG.md) và báo cáo [walkthrough.md](file:///d:/Agents_Tools/05_WebsiteTTC/walkthrough.md).

---

## 5. KẾ HOẠCH KIỂM TRA & NGHIỆM THU (VERIFICATION CRITERIA)

| Tiêu chí | Phương pháp kiểm tra | Điều kiện Đạt (PASS) |
|---|---|---|
| **Vị trí lưu trữ file** | Kiểm tra đường dẫn thư mục | 100% file nằm trong `05_WebsiteTTC/03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/` (ADR-014). |
| **Xác thực Link Sống** | Dùng `read_url_content` kiểm tra | 100% link tham khảo trả về HTTP 200 OK, 0 link 404/ảo giác (`IEEE-01`). |
| **Vị trí Trích dẫn Nội văn** | Quét regex `\[\d+.*?\]` | 100% trích dẫn nằm ở CUỐI CÂU (trước dấu `.` hoặc `:`), 0 trích dẫn ở đầu/giữa câu (`IEEE-02 v1.1`). |
| **Quy chuẩn Đặt tên IEEE** | So sánh với template | Đúng ngữ pháp IEEE từng loại hình, thụt lề treo 25px, link bấm trực tiếp (`IEEE-03`). |
| **Quy chuẩn Hình ảnh** | So khớp với Skill v1.1 | 1 Featured Image (808x500) + 2 hình nội dung kỹ thuật, prompt AI 5 tầng, khung `<img>` placeholder (`IMAGE_SPEC v1.1`). |
| **Tương thích CKEditor** | Quét mã HTML | 100% inline CSS, không thẻ cấm, không render SVG thô trong bài viết. |
