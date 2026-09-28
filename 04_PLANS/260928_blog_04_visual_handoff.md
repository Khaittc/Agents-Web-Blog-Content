# BÁO CÁO BÀN GIAO THỊ GIÁC (VISUAL HANDOFF REPORT) — BLOG_04

**Mã bài viết**: `BLOG_04`  
**Tiêu đề bài viết**: *VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải*  
**Thể loại bài viết**: `BLOG-T04` — Comparison  
**Tác nhân thực hiện**: Visual Agent (`visual_agent`) — Real Group  
**Ngày thực hiện**: 28/09/2026  
**Căn cứ pháp lý & quy chuẩn**:
- `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md`
- `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` (Mục 14: $1 \le n \le 3$)
- `ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md` (Cổng 2: Visual Handoff)
- `ADR-010` (Phân tách Prompt AI & Khung placeholder HTML)
- `ADR-016` (Chuẩn Responsive đa thiết bị)

---

## 1. XÁC NHẬN TIỀN ĐIỀU KIỆN (PREREQUISITE CONFIRMATION)

Visual Agent đã thẩm tra tính toàn vẹn và hợp lệ của bài viết trước khi thực hiện:
- **Trạng thái bài viết (`article_status.json`)**: `status == "TECH_APPROVED"`, `is_locked == false` (Đạt).
- **Phán quyết Cổng 1 (`audit.json`)**: `gate == "TECHNICAL_REVIEW_GATE"`, `verdict == "PASS"`, `revision_request_file == null` (Đạt).
- **Hồ sơ kiểm định (`technical_audit_report.md`)**: Phần III đã ghi nhận toàn bộ 9 issue (`REV-001` đến `REV-009`) đạt trạng thái `VERIFIED_RESOLVED`.
- **Ranh giới bất biến (Strict Read-Only)**: Toàn bộ bản thảo kỹ thuật `draft_review_package.md`, `claim_source_map.json`, `evidence.json`, `audit.json` được giữ nguyên vẹn 100%, không bị sửa đổi hay diễn giải lại.

---

## 2. CHIẾN LƯỢC THỊ GIÁC CHO THỂ LOẠI BLOG-T04 (BLOG-T04 VISUAL STRATEGY)

`BLOG-T04` là thể loại bài viết so sánh kỹ thuật công nghiệp chuyên sâu. Chiến lược thị giác được thiết kế xoay quanh 3 mục tiêu:
1. **Minh họa sự đối lập công nghệ (Technology Contrast)**: Thể hiện trực quan nguyên lý biến đổi tần số phức hợp (AC-DC-AC) của VFD đối chiếu với nguyên lý điều khiển pha điện áp RMS đơn giản, chạy mát qua bypass của Soft Starter.
2. **Kỷ luật dữ liệu thực nghiệm (Data Discipline)**: Trực quan hóa chính xác các điểm đo rời rạc từ Bảng 1 của Rockwell Automation, loại bỏ nguy cơ vẽ đường cong võ đoán hoặc tạo dữ liệu giả định cho VFD.
3. **Hướng dẫn quyết định khách quan (Conditional Decision Flow)**: Trình bày lưu đồ lựa chọn tuần tự với văn phong có điều kiện, tránh tư duy áp đặt giải pháp duy nhất.

---

## 3. DANH MỤC TÀI SẢN THỊ GIÁC (ASSET INVENTORY)

Visual Agent đã thiết lập bộ 4 tài sản thị giác hoàn chỉnh ($01\text{ Featured} + 03\text{ Content Images}$):

| Mã Tài sản | Tên tệp xuất bản | Vai trò & Mục tiêu | Tỷ lệ & Kích thước | Phương pháp thực hiện | Trạng thái kỹ thuật |
|:---|:---|:---|:---:|:---|:---:|
| **`IMG-FEATURED`** | `featured-vfd-vs-soft-starter-808x500.webp` | Ảnh đại diện bài viết / OpenGraph | 16:10 (`808 × 500 px`) | 5-Tier AI Generative Prompt | Sẵn sàng tạo ảnh |
| **`IMG-001`** | `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp` | Sơ đồ so sánh cấu trúc công suất | 16:9 (`1200 × 675 px`) | Controlled Vector Diagram | Yêu cầu dựng vector |
| **`IMG-002`** | `hinh-2-dong-va-mo-men-khoi-dong.webp` | Biểu đồ thực nghiệm dòng - mô-men | 16:9 (`1200 × 675 px`) | Deterministic Data Chart | Khóa dữ liệu EVD-003 |
| **`IMG-003`** | `hinh-3-khung-lua-chon-vfd-soft-starter.webp` | Lưu đồ khung quyết định lựa chọn | 16:9 (`1200 × 675 px`) | Controlled Vector Flowchart | Yêu cầu dựng vector |

---

## 4. QUYẾT ĐỊNH THIẾT KẾ FEATURED IMAGE (`IMG-FEATURED`)

- **Bố cục**: Bố cục đối xứng hai bên trong không gian tủ điện công nghiệp (MCC). Bên trái là biến tần VFD hiện đại, bên phải là bộ khởi động mềm bán dẫn nhỏ gọn; trung tâm phía dưới là động cơ không đồng bộ ba pha rô-to lồng sóc kết nối cáp công nghiệp gọn gàng.
- **Bảng màu thương hiệu**: Nền xám kỹ thuật (`#f8fafc`), xanh navy Real Group (`#0f2b46`), xanh kỹ thuật (`#0284c7`), đèn báo LED màu hổ phách (`#d97706`).
- **Khống chế**: Không chứa text phức tạp, không gắn logo giả mạo, không có dây nối nguy hiểm hay tia lửa điện. Đạt chuẩn tỷ lệ vàng `808 × 500 px`.

---

## 5. QUYẾT ĐỊNH THIẾT KẾ CONTENT IMAGE 1 (`IMG-001`)

- **Vị trí**: Đặt sau **Mục 2** của bài viết.
- **Nội dung kỹ thuật**:
  - Nhánh trái: Cấu trúc VFD với chuỗi chuyển đổi gián tiếp: `Lưới xoay chiều 50/60 Hz` $\rightarrow$ `Chỉnh lưu (Diode Rectifier)` $\rightarrow$ `Dàn tụ lọc DC Bus` $\rightarrow$ `Nghịch lưu IGBT` $\rightarrow$ `Động cơ (f = 0 - 250 Hz)`.
  - Nhánh phải: Cấu trúc Soft Starter: `Lưới xoay chiều 50/60 Hz` $\rightarrow$ `3 cặp Thyristor phản song song` $\rightarrow$ `Động cơ (f = 50/60 Hz, điện áp RMS tăng dần)` kèm `Nhánh Contactor Bypass AC-1` song song.
- **Ranh giới**: Ngăn chặn AI tự vẽ linh kiện sai định hướng phân cực của diode/thyristor; gán cờ `ASSET_REQUIRES_CONTROLLED_RENDERING`.

---

## 6. QUYẾT ĐỊNH THIẾT KẾ CONTENT IMAGE 2 (`IMG-002`)

- **Vị trí**: Đặt sau **Bảng số liệu thực nghiệm Mục 3.2**.
- **Nội dung kỹ thuật**: Minh họa chính xác 4 trường hợp khảo sát rời rạc của Rockwell Automation (`EVD-003`):
  1. *DOL*: Dòng $600\%$, Điện áp $100\%$, Mô-men $100\%$.
  2. *Soft Start Điểm 1*: Giới hạn dòng $150\%$, Điện áp $25\%$, Mô-men sụt xuống $6\%$.
  3. *Soft Start Điểm 2*: Giới hạn dòng $300\%$, Điện áp $50\%$, Mô-men đạt $25\%$.
  4. *Soft Start Điểm 3*: Giới hạn dòng $450\%$, Điện áp $75\%$, Mô-men đạt $56\%$.
- **Ranh giới**: Cấm tuyệt đối việc vẽ đường cong spline liên tục (tránh gây hiểu lầm đây là dải phổ quát); cấm vẽ cột dòng khởi động cho VFD vì chưa có approved evidence; gán cờ `DATA_FIGURE_REQUIRES_DETERMINISTIC_RENDERING`.

---

## 7. QUYẾT ĐỊNH THIẾT KẾ CONTENT IMAGE 3 (`IMG-003`)

- **Vị trí**: Đặt tại đầu **Mục 10** (Khung quyết định lựa chọn).
- **Nội dung kỹ thuật**: Lưu đồ 3 bước rẽ nhánh tuần tự:
  - Bước 1: Yêu cầu điều chỉnh tốc độ liên tục? $\rightarrow$ Có: Cân nhắc chọn VFD; Không: sang Bước 2.
  - Bước 2: Yêu cầu đầy đủ mô-men tại $0\text{ rpm}$? $\rightarrow$ Có: Cân nhắc chọn VFD; Không: sang Bước 3.
  - Bước 3: Đánh giá tổng hợp các ràng buộc dòng khởi động, kích thước tủ điện, sóng hài PCC (IEEE Std 519) và CAPEX.
- **Ranh giới**: Sử dụng câu chữ tiếng Việt chuẩn xác, văn phong có điều kiện, cấm áp đặt giải pháp duy nhất; gán cờ `ASSET_REQUIRES_CONTROLLED_RENDERING`.

---

## 8. TRUY XUẤT NGUỒN GỐC CHỨNG CỨ KỸ THUẬT (EVIDENCE TRACEABILITY)

Tất cả các hình ảnh đều được bảo chứng bởi hệ thống chứng cứ đã phê duyệt:
- `IMG-FEATURED`: `EVD-001`, `EVD-002`, `EVD-005`.
- `IMG-001`: `EVD-001` (AC-DC-AC, 0-250 Hz), `EVD-002` (Thyristor phản song song, 50/60 Hz), `EVD-005` (Giới hạn tốc độ), `EVD-007` (Contactor bypass AC-1).
- `IMG-002`: `EVD-003` (Bảng 1 Table 1 Rockwell, $T \propto U^2$, các điểm 150%, 300%, 450%).
- `IMG-003`: `EVD-003`, `EVD-004` (Mô-men 100% tại 0 rpm), `EVD-005`, `EVD-009` (TDD 5.0% tại PCC), `EVD-010` (CAPEX tương đối), `EVD-014` (IEEE 519 cấp hệ thống), `EVD-015` (Kích thước tủ điện).

---

## 9. BIỆN PHÁP CHỐNG ẢO GIÁC THỊ GIÁC (ANTI-HALLUCINATION CONTROLS)

Visual Agent đã thiết lập bộ kiểm soát nghiêm ngặt:
1. Không đưa thương hiệu, logo hay part number giả vào ảnh.
2. Không cho phép AI tự suy diễn dải dòng khởi động của VFD.
3. Không biến các điểm khảo sát rời rạc thành đường cong phổ quát cho mọi loại Soft Starter.
4. Không ngụ ý sai lệch rằng mọi biến tần đều bắt buộc phải có bộ lọc sóng hài riêng lẻ.

---

## 10. KIỂM THỬ KHUNG PLACEHOLDER RESPONSIVE (RESPONSIVE VERIFICATION)

Tất cả 3 khung thẻ HTML tại Mục 9 của `image_specifications.md` đều đáp ứng đầy đủ tiêu chuẩn ADR-016:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_N]" alt="[ALT_TEXT]" style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình N:</strong> [CAPTION]
    </p>
</div>
```
- Co giãn đa thiết bị (Desktop, Laptop, Mobile).
- Triệt tiêu hiện tượng méo ảnh dọc bằng `height: auto !important;`.
- Căn giữa trang với `display: block; margin: 0 auto;`.

---

## 11. KẾT QUẢ KIỂM TOÁN TÀI SẢN THỊ GIÁC (ASSET QA RESULTS)

- **Hồ sơ quy cách `image_specifications.md`**: Đã khởi tạo hoàn chỉnh, cấu trúc 14 mục đầy đủ theo giao thức.
- **Khả năng kết xuất vật lý trực tiếp trong môi trường sandbox**: Môi trường hiện tại không có các thư viện đồ họa vector chuyên dụng (Pillow, Matplotlib, Figma CLI) để kết xuất tự động các biểu đồ và lưu đồ vector đạt chất lượng xuất bản công nghiệp.
- **Nguyên tắc Fail-Closed**: Không giả mạo tệp nhị phân rỗng hay tạo ảnh kém chất lượng. Đặt trạng thái bàn giao theo đúng quy chuẩn: `SPECIFICATION_READY_ONLY`.

---

## 12. QUYẾT ĐỊNH VÒNG ĐỜI (LIFECYCLE DECISION)

- Theo Mục 33 (Case B) và Mục 38 của giao thức nhiệm vụ:
  - Do tài sản hình ảnh vật lý cuối cùng đang ở trạng thái chờ kết xuất đồ họa chính xác (`ASSET_GENERATION_PENDING`), trạng thái bài viết trong `article_status.json` **tiếp tục duy trì `TECH_APPROVED`**.
  - **KHÔNG** chuyển sang `VISUAL_READY` khi các tệp ảnh nhị phân chưa được kết xuất và kiểm chứng trực tiếp.
  - Cập nhật trường `notes` trong `article_status.json` để phản ánh trung thực tiến độ hoàn thành đặc tả thị giác.

---

## 13. SẴN SÀNG CHO PACKAGING AGENT (PACKAGING READINESS)

- **Ready for Packaging Agent**: **NO** (Bản thảo chưa có các tệp hình ảnh vật lý để đóng gói vào HTML cuối cùng).
- **Packaging Agent invoked**: **NO** (Visual Agent dừng lại tại đây, không gọi Packaging Agent).
- **Kế hoạch bàn giao tiếp theo**:
  1. Kỹ sư trưởng / Người dùng sử dụng các câu lệnh Prompt và bộ thông số tại `image_specifications.md` để kết xuất 4 tệp hình ảnh `.webp`.
  2. Tải 4 tệp ảnh lên hệ thống CDN hoặc thư mục bài viết.
  3. Kích hoạt Cổng bàn giao tiếp theo để hoàn tất quy trình Visual và chuyển giao cho Packaging Agent.

---
*Báo cáo được lập bởi: Visual Agent — Real Group*  
*Chữ ký điện tử: `visual_agent:blog_04:spec_ready`*
