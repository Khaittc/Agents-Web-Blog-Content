# BỘ QUY CÁCH HÌNH ẢNH & PROMPT TẠO ẢNH AI (IMAGE SPECIFICATIONS & PROMPT DOSSIER) — BLOG_02

**Mã bài viết**: `BLOG_02`  
**Tiêu đề bài viết**: Hệ số công suất cos phi và sóng hài trong nhà máy: Phân biệt bản chất và giải pháp xử lý triệt để  
**Visual & Asset Unit**: Antigravity Technical Visual Agent  
**Ngày cập nhật**: 23/09/2026  
**Chuẩn áp dụng**: `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md` & `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` (Mục 14: 1 ≤ n ≤ 3)  
**Nguyên tắc vận hành (ADR-010)**: Không render hình ảnh từ mã code thô (SVG) trong HTML bài viết. Cung cấp Prompt chi tiết để Kỹ sư trưởng / Người dùng tạo ảnh qua AI (Midjourney / DALL-E 3 / Leonardo / Imagen) và chèn URL vào đúng vị trí thẻ `<img>` đã bố trí sẵn trong mã HTML CKEditor.

---

## MỤC LỤC
1. [Hướng dẫn Quy trình Tạo ảnh & Nhúng vào CKEditor](#huong-dan-quy-trinh)
2. [Featured Image: Ảnh Đại diện Bài viết (808 × 500 px)](#1-featured-image)
3. [Hình 1 (Content Image 1): So sánh Dạng sóng Dòng điện & Phổ Sóng hài](#2-hinh-1-content-image-1)
4. [Hình 2 (Content Image 2): Mô hình Không gian Công suất Budeanu 3D](#3-hinh-2-content-image-2)
5. [Bảng Tổng hợp Khung HTML Snippets cho CKEditor](#4-bang-tong-hop-html)

---

<a name="huong-dan-quy-trinh"></a>
## 1. HƯỚNG DẪN QUY TRÌNH TẠO ẢNH & NHÚNG VÀO CKEDITOR

```text
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ 1. Sao chép AI Prompt  │ ───> │ 2. Tạo ảnh qua AI Tool │ ───> │ 3. Tối ưu & Tải lên    │
│ (Mục 2, Mục 3 hoặc 4)  │      │ (Midjourney/DALL-E 3)  │      │ (WebP < 200KB, lấy URL)│
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
                                                                             │
                                                                             ▼
                                ┌────────────────────────┐      ┌────────────────────────┐
                                │ 5. Xuất bản bài viết   │ <─── │ 4. Thay [URL_HINH_ANH] │
                                │ (Hoàn thiện CKEditor)  │      │ vào khung mã HTML      │
                                └────────────────────────┘      └────────────────────────┘
```

- **Bước 1**: Chọn hình cần tạo, sao chép đoạn **Copy-Paste AI Prompt** bên dưới.
- **Bước 2**: Dán prompt vào công cụ AI yêu thích (Midjourney v6, ChatGPT DALL-E 3, Leonardo.Ai, Google Imagen 3).
- **Bước 3**: Tải ảnh về, nén nhẹ định dạng `.webp` hoặc `.jpg` dung lượng < 200 KB, tải lên thư viện media của website để lấy đường dẫn URL (ví dụ: `https://real-group.org/wp-content/uploads/2026/09/hinh-1-dang-song-va-pho-song-hai.webp`).
- **Bước 4**: Mở file HTML [bai-viet-he-so-cong-suat-va-song-hai-ckeditor.html](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_02_He_so_cong_suat_va_Song_hai/bai-viet-he-so-cong-suat-va-song-hai-ckeditor.html) (hoặc giao diện Source của CKEditor), tìm kiếm chuỗi `[URL_HINH_ANH_1]` hoặc `[URL_HINH_ANH_2]` và thay thế bằng URL ảnh thực tế.

---

<a name="1-featured-image"></a>
## 2. FEATURED IMAGE (ẢNH ĐẠI DIỆN BÀI VIẾT)

- **Vị trí**: Ảnh đại diện chính thức ở đầu bài viết trên website và thumbnail chia sẻ mạng xã hội (OpenGraph / Zalo / LinkedIn).
- **Kích thước chuẩn**: `808 × 500 px` (Tỷ lệ xấp xỉ 16:10 / 1.618).
- **Tên file đề xuất khi lưu**: `he-so-cong-suat-cos-phi-va-song-hai-nha-may-808x500.webp`
- **Thẻ Alt**: `Kỹ sư điện đo kiểm hệ số công suất và phân tích sóng hài trên tủ điện phân phối hạ thế bằng thiết bị phân tích chất lượng điện năng`

### Copy-Paste AI Prompt:
```text
Professional wide-angle industrial documentary photograph of a clean, modern electrical substation and motor control center (MCC) in a high-tech manufacturing plant. In the foreground, an experienced Vietnamese certified electrical engineer wearing a safety hardhat, high-visibility vest, and safety glasses operates a calibrated digital power quality analyzer connected with color-coded test leads to a low-voltage distribution cabinet. The analyzer screen shows glowing technical waveforms, power factor readings, and harmonic spectrum charts with cool blue and amber LED status lights. In the background, neatly organized industrial capacitor bank cubicles with detuned reactors and active harmonic filter racks. Crisp technical lighting, authentic industrial color grading with clean navy blue (#0f2b46) and metallic steel tones, highly realistic textures, photorealistic 8k, no cartoon, no distorted cables, no surreal artifacts --ar 16:10 --v 6.1
```

### Negative Prompt (Điều cấm khi tạo):
```text
blurry, distorted wires, floating equipment, cartoonish, caricature, hazardous open sparking, messy chaotic floor, low resolution, watermark, deformed hands, illegible typography
```

### Ý nghĩa & Bố cục:
Thể hiện bối cảnh trạm biến áp công nghiệp thực tế với tác phong chuyên nghiệp, khẳng định chất lượng chuyên gia của Real Group trong lĩnh vực đo kiểm và xử lý chất lượng điện năng.

---

<a name="2-hinh-1-content-image-1"></a>
## 3. HÌNH 1 (CONTENT IMAGE 1): SO SÁNH DẠNG SÓNG DÒNG ĐIỆN & PHỔ SÓNG HÀI

- **Vị trí đề xuất trong bài viết**: Ngay sau **Mục 2** (*Cơ chế sinh ra sóng hài từ tải phi tuyến trong công nghiệp*).
- **Mục tiêu kỹ thuật**: Trực quan hóa sự khác biệt giữa dòng điện hình sin chuẩn 50 Hz của tải tuyến tính với dòng điện xung nhọn méo mó của biến tần 6-pulse, đồng thời chỉ rõ sự xuất hiện của hai đỉnh sóng hài bậc 5 (250 Hz) và bậc 7 (350 Hz).
- **Kích thước đề xuất**: `1200 × 675 px` hoặc `1000 × 562 px` (Tỷ lệ 16:9).
- **Tên file đề xuất khi lưu**: `hinh-1-so-sanh-dang-song-dong-dien-va-pho-song-hai-bien-tan.webp`
- **Thẻ Alt**: `So sánh dạng sóng dòng điện tải tuyến tính và tải biến tần 6-pulse kèm phổ sóng hài bậc 5 bậc 7`
- **Chú thích (Caption)**:  
  `Hình 1: So sánh dạng sóng dòng điện giữa tải tuyến tính (sin chuẩn) và tải phi tuyến biến tần 6-pulse (xung nhọn), kèm phổ phân tích sóng hài bậc 5 (250 Hz) và bậc 7 (350 Hz).`

### Copy-Paste AI Prompt (Midjourney / DALL-E 3 / Leonardo):
```text
Clean professional engineering infographic diagram on an ultra-clean white background, split into two side-by-side technical panels. Left panel titled "Current Waveform i(t)": an oscilloscope-style graph displaying two alternating current waveforms over two electrical cycles; one waveform is a smooth green dashed line representing a pure 50Hz sinusoidal linear load current; the second waveform is an intense bold red solid curve showing a distorted non-linear 6-pulse VFD rectifier current with characteristic double sharp peaks and steep slopes. Right panel titled "Harmonic Current Spectrum (%)": a clean vertical bar chart with sharp gridlines; first tall blue bar labeled "h1 (50Hz)" at 100%; prominent amber-orange bar labeled "h5 (250Hz)" at 35%; secondary amber-orange bar labeled "h7 (350Hz)" at 18%; small gray bar labeled "h11 (550Hz)" at 9%. Minimalist industrial technical aesthetics, sharp vector look, high legibility, precision engineering textbook quality, crisp typography, no clutter, no 3D cartoon, no dark background --ar 16:9 --v 6.1
```

### Negative Prompt:
```text
handwritten scribbles, dark moody background, chaotic noisy lines, cartoon, low resolution, blurry text, illegible symbols, 3D artistic rendering
```

### Đoạn mã HTML chèn vào CKEditor:
```html
<!-- IMAGE_1: Technical Figure — So sánh dạng sóng dòng điện và phổ sóng hài -->
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_1]" alt="So sánh dạng sóng dòng điện tải tuyến tính và tải biến tần 6-pulse kèm phổ sóng hài bậc 5 bậc 7" style="max-width:100%;height:auto;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 1:</strong> So sánh dạng sóng dòng điện giữa tải tuyến tính (sin chuẩn) và tải phi tuyến biến tần 6-pulse (xung nhọn), kèm phổ phân tích sóng hài bậc 5 (250 Hz) và bậc 7 (350 Hz).
    </p>
</div>
```

---

<a name="3-hinh-2-content-image-2"></a>
## 4. HÌNH 2 (CONTENT IMAGE 2): MÔ HÌNH KHÔNG GIAN CÔNG SUẤT BUDEANU 3D (P-Q-D)

- **Vị trí đề xuất trong bài viết**: Ngay sau **Mục 3** (*Không gian Công suất Budeanu khi xuất hiện sóng hài*).
- **Mục tiêu kỹ thuật**: Minh họa hình học không gian 3 chiều của công suất Budeanu: giải thích rõ ràng vì sao tụ điện truyền thống chỉ kéo công suất phản kháng cơ bản \(Q_1 \rightarrow 0\), nhưng không thể giảm công suất biến dạng \(D\), dẫn đến \(\text{PF} < 1.0\) và doanh nghiệp vẫn bị phạt tiền.
- **Kích thước đề xuất**: `1200 × 675 px` hoặc `1000 × 562 px` (Tỷ lệ 16:9).
- **Tên file đề xuất khi lưu**: `hinh-2-mo-hinh-hinh-hoc-khong-gian-cong-suat-3d-budeanu.webp`
- **Thẻ Alt**: `Mô hình hình học không gian công suất Budeanu 3D gồm công suất tác dụng P, công suất phản kháng Q1 và công suất biến dạng D`
- **Chú thích (Caption)**:  
  `Hình 2: Mô hình hình học không gian công suất Budeanu 3D (P-Q-D), giải thích vì sao tụ bù truyền thống chỉ triệt tiêu Q1 mà không thể giảm công suất biến dạng sóng hài D.`

### Copy-Paste AI Prompt (Midjourney / DALL-E 3 / Leonardo):
```text
High-precision 3D isometric technical diagram of the Budeanu Power Box model on a crisp clean off-white background (#f8fafc). An orthogonal 3D coordinate system originating from point (0,0,0): horizontal X-axis labeled "Active Power P (kW)" in deep navy blue (#0f2b46); vertical Y-axis labeled "Fundamental Reactive Power Q1 (kvar, 50Hz)" in bright technical cyan (#0284c7); depth Z-axis receding diagonally labeled "Harmonic Distortion Power D (kvar)" in vivid engineering red (#dc2626). The three axes define a translucent 3D rectangular box with clean dashed projection lines. A bold glowing purple vector spans from the origin diagonally to the opposite far top corner of the box, labeled with mathematical formula "Total Apparent Power S = √(P² + Q1² + D²) (kVA)". A technical callout arrow indicates: capacitor banks only cancel Q1 to zero, leaving distortion power D intact. Sleek architectural geometry, high-end technical publication rendering, crisp sharp vectors, no artistic clutter, no dark shadows --ar 16:9 --v 6.1
```

### Negative Prompt:
```text
dark background, messy scribble lines, cartoon rendering, low resolution, distorted geometry, blurred text, confusing perspective, chaotic colors
```

### Đoạn mã HTML chèn vào CKEditor:
```html
<!-- IMAGE_2: Technical Figure — Mô hình không gian 3D Budeanu -->
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_2]" alt="Mô hình hình học không gian công suất Budeanu 3D gồm công suất tác dụng P, công suất phản kháng Q1 và công suất biến dạng D" style="max-width:100%;height:auto;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 2:</strong> Mô hình hình học không gian công suất Budeanu 3D (P-Q-D), giải thích vì sao tụ bù truyền thống chỉ triệt tiêu Q1 mà không thể giảm công suất biến dạng sóng hài D.
    </p>
</div>
```

---

<a name="4-bang-tong-hop-html"></a>
## 5. BẢNG TỔNG HỢP VỊ TRÍ & MÃ PLACEHOLDER TRONG FILE HTML

| Ký hiệu | Tên gọi & Nội dung | Vị trí chèn trong bài | Tỷ lệ / Kích thước | Placeholder URL trong mã HTML |
| :--- | :--- | :--- | :--- | :--- |
| **Featured** | Kỹ sư đo kiểm chất lượng điện năng trạm biến áp | Đầu bài viết / Meta tag | `16:10` (808×500 px) | Cấu hình trong phần quản trị CMS |
| **IMAGE_1** | So sánh dạng sóng dòng điện & phổ sóng hài | Ngay sau **Mục 2** | `16:9` (1200×675 px) | `[URL_HINH_ANH_1]` |
| **IMAGE_2** | Mô hình hình học không gian công suất Budeanu 3D | Ngay sau **Mục 3** | `16:9` (1200×675 px) | `[URL_HINH_ANH_2]` |

---

## 6. CHECKLIST NGHIỆM THU THEO STANDARD v1.3 & ADR-010

- [x] Không còn mã SVG hay mã code render trực tiếp trong tệp HTML CKEditor.
- [x] Vị trí hình ảnh được bố trí bằng thẻ `<img>` chuẩn responsive kèm caption và thẻ `alt` chi tiết.
- [x] Cung cấp đầy đủ 3 bộ Prompt AI chất lượng cao (Featured Image, Hình 1, Hình 2) kèm thông số tỷ lệ, negative prompt và hướng dẫn chi tiết.
- [x] Đạt chuẩn số lượng hình ảnh nội dung: 2 hình (nằm trong ngưỡng quy định 1 ≤ n ≤ 3 của `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3`).
- [x] Sẵn sàng để Kỹ sư trưởng sao chép prompt, tạo ảnh và đưa vào bài đăng thực tế.
