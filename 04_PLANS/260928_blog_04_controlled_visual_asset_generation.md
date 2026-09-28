# BÁO CÁO KHỞI TẠO TÀI SẢN THỊ GIÁC CÓ KIỂM SOÁT (CONTROLLED VISUAL ASSET GENERATION REPORT) — BLOG_04

**Mã bài viết**: `BLOG_04`  
**Tiêu đề bài viết**: *VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải*  
**Thể loại bài viết**: `BLOG-T04` — Comparison  
**Tác nhân thực hiện**: Visual Agent (`visual_agent`) — Real Group  
**Ngày thực hiện**: 28/09/2026  
**Baseline Git**: `c1065e6` — *fix: complete BLOG_04 visual traceability mapping*  

---

## 1. TIỀN ĐIỀU KIỆN & TRẠNG THÁI ĐẦU VÀO (BASELINE & PREREQUISITE)

Visual Agent đã thẩm định hiện trạng đầu vào trước khi tiến hành khởi tạo:
- **`article_status.json`**: `status == "TECH_APPROVED"`, `is_locked == false` (Đạt).
- **`audit.json`**: `gate == "TECHNICAL_REVIEW_GATE"`, `verdict == "PASS"`, `revision_request_file == null` (Đạt).
- **`image_specifications.md`**: Đã hoàn thiện 100%, vượt qua vi chỉnh ngữ nghĩa và đồng bộ hóa ma trận truy xuất chứng cứ.
- **Ranh giới bất biến (Strict Read-Only)**: 100% hồ sơ kỹ thuật (`draft_review_package.md`, `claim_source_map.json`, `evidence.json`, `audit.json`) được giữ nguyên vẹn tuyệt đối.

---

## 2. MÔI TRƯỜNG & CÔNG CỤ KHỞI TẠO (RENDERING ENVIRONMENT & TOOLS)

Visual Agent đã thiết lập quy trình kết xuất kết hợp (hybrid pipeline) bảo đảm tính chính xác kỹ thuật:
- **AI Generative Engine**: Sử dụng `generate_image` với câu lệnh Prompt 5 tầng chuẩn hóa cho `IMG-FEATURED` (tạo bối cảnh tủ điện công nghiệp MCC thực tế, trung thực, không vẽ vi mạch giả định).
- **Python Imaging Library (Pillow 12.3.0)**: Cắt cúp tỷ lệ vàng, tái lấy mẫu chất lượng cao `LANCZOS`, đóng gói chuẩn `.webp` chất lượng cao (quality=95).
- **Deterministic Vector & Chart Engine (Matplotlib 3.11.2 & Python)**: Dựng đồ họa kỹ thuật vector và biểu đồ dữ liệu độc lập cho `IMG-001`, `IMG-002`, `IMG-003`, bảo đảm tính toán chính xác 100% số liệu và nhãn tiếng Việt Segoe UI chuẩn xác, không có lỗi phông chữ.

---

## 3. KHỞI TẠO IMG-FEATURED (FEATURED IMAGE)

- **Tên tệp**: `featured-vfd-vs-soft-starter-808x500.webp`
- **Kích thước thực tế**: `808 × 500 px` (Tỷ lệ 16:10).
- **Căn cứ chứng cứ kỹ thuật**: `EVD-001`, `EVD-002`, `EVD-005`, `EVD-015`.
- **Thực thi thiết kế**:
  - Tủ điện điều khiển động cơ MCC sạch sẽ, chuyên nghiệp.
  - Phía trái: Bộ biến tần VFD với màn hình hiển thị tần số và cánh tản nhiệt nhôm.
  - Phía phải: Bộ khởi động mềm bán dẫn nhỏ gọn hơn rõ rệt (phù hợp với `EVD-015`).
  - Trung tâm phía dưới: Động cơ không đồng bộ 3 pha rô-to lồng sóc kết nối cáp công nghiệp gọn gàng trong máng cáp.
  - Bảng màu: Xanh navy Real Group (`#0f2b46`), xanh cyan kỹ thuật (`#0284c7`), xám kỹ thuật (`#f8fafc`).
  - Hoàn toàn không có chữ méo, không có logo giả mạo, không có dây nối nguy hiểm.

---

## 4. KẾT XUẤT ĐỒ HỌA VECTOR CÓ KIỂM SOÁT IMG-001 (CONTENT IMAGE 1)

- **Tên tệp**: `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp`
- **Kích thước thực tế**: `1200 × 675 px` (Tỷ lệ 16:9).
- **Căn cứ chứng cứ kỹ thuật**: `EVD-001`, `EVD-002`, `EVD-005`, `EVD-006`, `EVD-007`.
- **Thực thi kỹ thuật**:
  - Bố cục đối xứng hai bên trên nền trắng xám kỹ thuật (`#f8fafc`).
  - **Khung VFD (Trái)**: Nguồn lưới 3 pha ($50/60\text{ Hz}$) $\rightarrow$ Tầng 1: Khối chuyển đổi AC-sang-DC $\rightarrow$ Tầng 2: Khối trung gian DC $\rightarrow$ Tầng 3: Khối chuyển đổi DC-sang-AC $\rightarrow$ Động cơ 3 pha ($f = 0 - 250\text{ Hz}$).
  - **Khung Soft Starter (Phải)**: Nguồn lưới 3 pha ($50/60\text{ Hz}$) rẽ thành 2 nhánh song song:
    - Nhánh 1 (Khởi động): 3 cặp Thyristor (SCR) phản song song điều khiển góc kích pha tăng dần điện áp hiệu dụng RMS ở tần số cố định $50/60\text{ Hz}$.
    - Nhánh 2 (Xác lập): Nhánh Contactor Bypass (định mức điển hình AC-1) dẫn dòng trong chế độ xác lập giúp thiết bị chạy mát.
  - Cả 2 nhánh hội tụ về Động cơ 3 pha (tần số giữ nguyên $50/60\text{ Hz}$, điện áp RMS tăng dần đến định mức).
  - Không chứa bất kỳ suy diễn linh kiện bán dẫn chi tiết ngoài chứng cứ (không ghi Diode, không ghi IGBT, không ghi dải 0-100%).

---

## 5. KẾT XUẤT BIỂU ĐỒ SỐ LIỆU THỰC NGHIỆM ĐỘC LẬP IMG-002 (CONTENT IMAGE 2)

- **Tên tệp**: `hinh-2-dong-va-mo-men-khoi-dong.webp`
- **Kích thước thực tế**: `1200 × 675 px` (Tỷ lệ 16:9).
- **Căn cứ chứng cứ kỹ thuật**: `EVD-003` (Rockwell Automation White Paper 150-WP007A-EN-P, Table 1, p. 6).
- **Thực thi kỹ thuật**:
  - Biểu đồ cột nhóm so sánh đa trục thể hiện 4 trường hợp khảo sát rời rạc độc lập:
    1. **DOL**: Dòng khởi động $600\%$, Điện áp stato $100\%$, Mô-men $100\%$.
    2. **Khởi động mềm Điểm 1**: Giới hạn dòng $150\%$, Điện áp $25\%$, Mô-men $6\%$.
    3. **Khởi động mềm Điểm 2**: Giới hạn dòng $300\%$, Điện áp $50\%$, Mô-men $25\%$.
    4. **Khởi động mềm Điểm 3**: Giới hạn dòng $450\%$, Điện áp $75\%$, Mô-men $56\%$.
  - Thẻ kỹ thuật bên phải minh họa giải thích quy luật phi tuyến $T \sim U^2$ ($(0.25)^2 \approx 6\%$, $(0.50)^2 = 25\%$, $(0.75)^2 \approx 56\%$).
  - Ghi chú kỹ thuật bắt buộc: Dữ liệu khảo sát rời rạc theo Table 1 Rockwell Automation; tuyệt đối không vẽ đường cong spline liên tục và không bịa đặt số liệu dòng khởi động cho VFD.

---

## 6. KẾT XUẤT LƯU ĐỒ KHUNG QUYẾT ĐỊNH IMG-003 (CONTENT IMAGE 3)

- **Tên tệp**: `hinh-3-khung-lua-chon-vfd-soft-starter.webp`
- **Kích thước thực tế**: `1200 × 675 px` (Tỷ lệ 16:9).
- **Căn cứ chứng cứ kỹ thuật**: `EVD-003`, `EVD-004`, `EVD-005`, `EVD-006`, `EVD-007`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`.
- **Thực thi kỹ thuật**:
  - Lưu đồ 3 bước tuần tự với văn phong có điều kiện:
    - **Bước 1 (Tốc độ)**: Có đòi hỏi điều chỉnh tốc độ liên tục? $\rightarrow$ Có: Cân nhắc chọn VFD (Khởi động mềm không đáp ứng).
    - **Bước 2 (Mô-men)**: Có đòi hỏi đầy đủ mô-men bứt phá tại zero speed ($0\text{ rpm}$)? $\rightarrow$ Có: Cân nhắc chọn VFD (VFD đáp ứng đầy đủ mô-men tại $0\text{ rpm}$; Soft Starter sụt mô-men).
    - **Bước 3 (Đánh giá tổng hợp 4 tiêu chí)**:
      1. *Dòng khởi động & Mô-men*: Đối chiếu yêu cầu mô-men tải & dữ liệu OEM (`EVD-003`, `EVD-004`).
      2. *Không gian tủ & Tỏa nhiệt*: Kích thước nhỏ gọn, contactor bypass AC-1 chạy mát xác lập (`EVD-006`, `EVD-007`, `EVD-015`).
      3. *Sóng hài & IEEE Std 519*: Đánh giá tại điểm đấu nối chung PCC theo $I_{\text{sc}}/I_L$, không bắt buộc mọi VFD phải có bộ lọc riêng (`EVD-009`, `EVD-014`).
      4. *Chi phí đầu tư ban đầu*: Dải thấp tương đương, dải công suất lớn VFD tăng cao hơn (`EVD-010`).
    - **Kết luận**: Đưa ra lựa chọn kỹ thuật tối ưu dựa trên đối chiếu toàn diện giữa yêu cầu công nghệ và bài toán kinh tế tổng thể.

---

## 7. BẢNG KIỂM ĐỊNH KỸ THUẬT & QUY CÁCH (TECHNICAL QA TABLE)

| Mã Tài sản | Tên tệp xuất bản | Kích thước yêu cầu | Kích thước thực tế | Phương pháp thực hiện | Căn cứ Chứng cứ | Kiểm định Ngữ nghĩa | Kiểm định Thị giác | Kết luận QA |
|:---|:---|:---:|:---:|:---|:---|:---:|:---:|:---:|
| **`IMG-FEATURED`** | `featured-vfd-vs-soft-starter-808x500.webp` | `808 × 500 px` | `808 × 500 px` | AI Generative + Resampling | `EVD-001, 002, 005, 015` | PASS | PASS | **PASS** |
| **`IMG-001`** | `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp` | `1200 × 675 px` | `1200 × 675 px` | Vector Block Diagram | `EVD-001, 002, 005, 006, 007` | PASS | PASS | **PASS** |
| **`IMG-002`** | `hinh-2-dong-va-mo-men-khoi-dong.webp` | `1200 × 675 px` | `1200 × 675 px` | Deterministic Data Chart | `EVD-003` | PASS | PASS | **PASS** |
| **`IMG-003`** | `hinh-3-khung-lua-chon-vfd-soft-starter.webp` | `1200 × 675 px` | `1200 × 675 px` | Controlled Vector Flowchart | `EVD-003, 004, 005, 006, 007, 009, 010, 014, 015` | PASS | PASS | **PASS** |

---

## 8. XÁC THỰC TÍNH NGUYÊN VẸN CỦA TỆP (FILE VALIDATION & INTEGRITY)

| Tên tệp | Định dạng | Kích thước (bytes) | Trạng thái tệp | Mã băm SHA-256 |
|:---|:---:|:---:|:---:|:---|
| `featured-vfd-vs-soft-starter-808x500.webp` | `WEBP` | 116,250 | Hợp lệ (Non-zero) | `871dac5b0eeda11b3e7ca284718937efbe2d503c85fa7d0cab0eda3a18473444` |
| `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp` | `WEBP` | 127,364 | Hợp lệ (Non-zero) | `1f32a3daf4fe4d3171080619ace3a46551100788bf3c4ae434301cbb3f2a814e` |
| `hinh-2-dong-va-mo-men-khoi-dong.webp` | `WEBP` | 96,550 | Hợp lệ (Non-zero) | `68191013571424e3ec08258ffd9e915ea2f6b6c78a0d2802f7358465b9a822ca` |
| `hinh-3-khung-lua-chon-vfd-soft-starter.webp` | `WEBP` | 121,754 | Hợp lệ (Non-zero) | `53e0367d9f622d85c54ec59b2dd64eac4fc65daa9ceb33c746200821a5565927` |

---

## 9. BẢO TỒN TÀI NGUYÊN BẤT BIẾN (ARTIFACT INTEGRITY CONFIRMATION)

- `draft_review_package.md`: **UNCHANGED** (nguyên vẹn 100%).
- `claim_source_map.json`: **UNCHANGED** (nguyên vẹn 100%).
- `evidence.json` / `evidence_dossier.md`: **UNCHANGED** (nguyên vẹn 100%).
- `audit.json` / `technical_audit_report.md`: **UNCHANGED** (nguyên vẹn 100%).
- `revision_request.json`: **UNCHANGED** (nguyên vẹn 100%).

---

## 10. QUYẾT ĐỊNH TRẠNG THÁI VÒNG ĐỜI (LIFECYCLE DECISION)

Do cả **04/04 tài sản thị giác đều đạt kết quả PASS**, Visual Agent chính thức phê duyệt nâng cấp trạng thái bài viết:
```text
article_status.status: TECH_APPROVED → VISUAL_READY
```
- Ghi chú: *"Controlled Visual Asset Generation completed. Featured image and all three technical content images generated and QA verified. Visual package ready for Packaging Agent."*

---

## 11. SẴN SÀNG CHUYỂN GIAO CHO PACKAGING AGENT (PACKAGING READINESS)

Visual Package đã hoàn tất trọn vẹn:
- Các tệp ảnh nhị phân `.webp` đã sẵn sàng tại thư mục bài viết.
- Các khung thẻ HTML responsive chuẩn ADR-016 đã sẵn sàng tại Mục 9 của `image_specifications.md`.
- Sẵn sàng kích hoạt: **`BLOG_04 — Packaging Handoff`**.

---
*Báo cáo được lập bởi: Visual Agent — Real Group*  
*Chữ ký số: `visual_agent:blog_04:generation_full_pass`*
