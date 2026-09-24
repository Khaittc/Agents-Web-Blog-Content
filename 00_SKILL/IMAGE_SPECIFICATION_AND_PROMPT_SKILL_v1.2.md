# BỘ QUY CHUẨN ĐẶC TẢ HÌNH ẢNH & KỸ NGHỆ PROMPT KỸ THUẬT (IMAGE SPECIFICATION & PROMPT ENGINEERING SKILL)
**Version**: 1.2  
**Mã tài liệu**: `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2`  
**Trạng thái**: Áp dụng chính thức cho toàn bộ Visual Agent, Drafting Agent và Tech Review Agent  
**Ngày ban hành**: 24/09/2026  
**Thay thế**: `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md` (Đã lưu trữ tại `00_SKILL/archive/`)  
**Căn cứ pháp lý & kỹ thuật**: 
- `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` (Mục 14: 1 ≤ n ≤ 3)
- `REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md` (Hiển thị CKEditor)
- `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md` (Trụ cột 4 Presentation & Visual Audit)
- **ADR-010**: Cơ chế phân tách Prompt AI & Khung placeholder HTML, không render mã code thô trong bài viết.
- **ADR-016**: Tiêu chuẩn Responsive đa thiết bị (Laptop & Mobile), triệt tiêu méo kéo giãn dọc ảnh bằng `height: auto !important;` và `margin: 0 auto;`.

---

## MỤC LỤC
1. [Mục đích & Các Nguyên tắc Cốt lõi](#1-muc-dich)
2. [Cấu trúc Chuẩn của Tệp Bàn giao image_specifications.md](#2-cau-truc-tep-ban-giao)
3. [Khung Kỹ nghệ Prompt AI 5 Tầng (5-Tier Prompt Framework)](#3-khung-ky-nghe-prompt)
4. [Thư viện Khuôn mẫu Tạo Prompt Kỹ thuật (Technical Archetypes)](#4-thu-vien-archetypes)
5. [Quy chuẩn Khung HTML Placeholder cho CKEditor 3.6.6.2](#5-quy-chuan-khung-html)
6. [Cơ chế Mở rộng & Quy trình Nâng cấp Skill (Upgrading Protocol)](#6-co-che-nang-cap)
7. [Checklist Nghiệm thu của Tech Review Agent](#7-checklist-nghiem-thu)

---

<a name="1-muc-dich"></a>
## 1. MỤC ĐÍCH & CÁC NGUYÊN TẮC CỐT LÕI

Mục tiêu của bộ kỹ năng này là xác lập tiêu chuẩn công nghiệp cho toàn bộ hình ảnh minh họa trong các bài viết kỹ thuật của Real Group. Đảm bảo hình ảnh vừa trực quan, giàu tính chuyên môn, vừa đồng nhất về thẩm mỹ kỹ thuật và tương thích 100% với CMS/CKEditor.

### 4 Nguyên tắc Bắt buộc (Non-negotiable Rules):

1. **Nguyên tắc Tách biệt Trách nhiệm (ADR-010 - Separation of Concerns)**:
   - **TUYỆT ĐỐI KHÔNG** chèn mã code vẽ hình trực tiếp (như `<svg>`, canvas, thẻ script) vào tệp mã nguồn HTML của bài viết. Mã code vẽ trực tiếp gây phình dung lượng file, dễ vỡ bố cục khi qua CKEditor 3.6.6.2 và không tận dụng được CDN/caching hình ảnh.
   - **BẮT BUỘC**: Mã HTML chỉ chứa các khung thẻ `<img>` responsive tiêu chuẩn với đường dẫn placeholder `[URL_HINH_ANH_n]`.
   - **TỆP ĐẶC TẢ ĐỘC LẬP**: Mọi thông số thiết kế, câu lệnh Prompt AI hoàn chỉnh và quy cách kích thước phải được lưu trữ trong tệp `image_specifications.md` tại thư mục bài viết.

2. **Nguyên tắc Số lượng Hình ảnh (Standard v1.3 - Mục 14)**:
   - Mỗi bài viết kỹ thuật bắt buộc phải có:
     - **01 Featured Image** (Ảnh đại diện đầu bài / OpenGraph): Kích thước chính xác `808 × 500 px` (Tỷ lệ xấp xỉ 16:10 / 1.618).
     - **1 đến 3 Content Images** (`1 ≤ n ≤ 3`) trong phần thân bài viết để trực quan hóa nguyên lý, phân tích dạng sóng hoặc lưu đồ giải pháp. Nghiêm cấm xuất bản bài viết mà không có hình ảnh nội dung.

3. **Nguyên tắc Chống Ảo giác Kỹ thuật (Anti-Hallucination Guardrails)**:
   - Các công cụ AI tạo ảnh (Midjourney, DALL-E 3, Flux) rất dễ sinh ra các linh kiện điện tử giả, dây nối lộn xộn nguy hiểm hoặc ký tự chữ/số méo mó.
   - Visual Agent khi tạo prompt bắt buộc phải đưa vào các từ khóa khống chế phong cách (`minimalist`, `sharp vector`, `clean wiring`, `crisp gridlines`) và bộ **Negative Prompts** nghiêm ngặt.

4. **Nguyên tắc Tương thích Xuất bản (Ready-to-Publish Workflow)**:
   - Cung cấp sẵn các prompt tiếng Anh chuẩn hóa để Kỹ sư trưởng hoặc người quản trị chỉ cần thực hiện thao tác **Copy -> Paste -> Generate**, không cần tự suy nghĩ cấu trúc prompt phức tạp.

---

<a name="2-cau-truc-tep-ban-giao"></a>
## 2. CẤU TRÚC CHUẨN CỦA TỆP BÀN GIAO `image_specifications.md`

Mỗi bài viết kỹ thuật khi được Visual Agent xử lý bắt buộc phải tạo tệp `image_specifications.md` đặt tại thư mục bài viết (ví dụ: `03_Articles/BLOG_xx_.../image_specifications.md`) theo đúng cấu trúc chuẩn sau:

```markdown
# BỘ QUY CÁCH HÌNH ẢNH & PROMPT TẠO ẢNH AI (IMAGE SPECIFICATIONS & PROMPT DOSSIER) — [MÃ_BÀI]

**Mã bài viết**: `[MÃ_BÀI]`  
**Tiêu đề bài viết**: [Tiêu đề đầy đủ của bài viết]  
**Visual & Asset Unit**: Antigravity Technical Visual Agent  
**Ngày cập nhật**: [dd/mm/yyyy]  
**Chuẩn áp dụng**: `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md` & `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` (Mục 14: 1 ≤ n ≤ 3)  
**Nguyên tắc vận hành**: ADR-010 (Cung cấp Prompt AI + Khung HTML Placeholder)

---

## 1. HƯỚNG DẪN QUY TRÌNH TẠO ẢNH & NHÚNG VÀO CKEDITOR
(Sơ đồ 5 bước và hướng dẫn thao tác chi tiết cho Kỹ sư trưởng)

---

## 2. FEATURED IMAGE (ẢNH ĐẠI DIỆN BÀI VIẾT)
- Vị trí: Đầu bài viết & Thumbnail OpenGraph
- Kích thước chuẩn: `808 × 500 px` (Tỷ lệ 16:10)
- Tên file đề xuất: `[slug-tieu-de]-808x500.webp`
- Thẻ Alt: [Mô tả chi tiết giàu từ khóa kỹ thuật]
- Copy-Paste AI Prompt: [Đoạn prompt tiếng Anh hoàn chỉnh]
- Negative Prompt: [Bộ từ khóa loại trừ]
- Ý nghĩa & Bối cảnh: [Giải thích giá trị truyền tải]

---

## 3. HÌNH 1 (CONTENT IMAGE 1): [TÊN_HÌNH_1]
- Vị trí đề xuất trong bài viết: [Ngay sau Mục X]
- Mục tiêu kỹ thuật: [Giải thích hiện tượng/nguyên lý nào]
- Kích thước & Tỷ lệ đề xuất: `1200 × 675 px` (Tỷ lệ 16:9)
- Tên file đề xuất: `[slug-ten-hinh-1].webp`
- Thẻ Alt: [Mô tả kỹ thuật]
- Chú thích (Caption): `Hình 1: [Lời bình chuyên sâu]`
- Copy-Paste AI Prompt: [Đoạn prompt tiếng Anh chuyên sâu]
- Negative Prompt: [Bộ từ khóa loại trừ]
- Đoạn mã HTML chèn vào CKEditor: [Khung HTML hoàn chỉnh với src="[URL_HINH_ANH_1]"]

---

## 4. HÌNH 2 (CONTENT IMAGE 2): [TÊN_HÌNH_2] (Nếu có)
(Cấu trúc tương tự Hình 1, sử dụng src="[URL_HINH_ANH_2]")

---

## 5. BẢNG TỔNG HỢP VỊ TRÍ & MÃ PLACEHOLDER TRONG FILE HTML
(Bảng ma trận đối chiếu Hình -> Vị trí -> Kích thước -> Placeholder)

---

## 6. CHECKLIST NGHIỆM THU THEO STANDARD v1.3 & ADR-010
(Checklist kiểm tra hoàn tất)
```

---

<a name="3-khung-ky-nghe-prompt"></a>
## 3. KHUNG KỸ NGHỆ PROMPT AI 5 TẦNG (5-TIER PROMPT FRAMEWORK)

Mọi câu lệnh Prompt do Visual Agent xây dựng phải tuân thủ kiến trúc ghép nối 5 tầng để đạt chất lượng hình ảnh đồng nhất và chuyên nghiệp:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: TARGET ENGINE FLAGS & ADAPTERS                                  │
│ (--ar 16:9, --v 6.1, --style raw, photorealistic render flags)          │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 2: BỐI CẢNH & CHỦ THỂ KỸ THUẬT (SCENE & SUBJECT)                   │
│ (Substation, MCC panel, 3-phase induction motor, Fluke analyzer)       │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 3: HÌNH THỨC THỂ HIỆN (VISUAL MEDIUM & ART ARCHETYPE)             │
│ (Industrial photography, engineering infographic, 3D isometric diagram)│
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 4: BẢNG MÀU THƯƠNG HIỆU & ÁNH SÁNG (PALETTE & LIGHTING)           │
│ (Navy blue #0f2b46, Cyan #0284c7, Amber #d97706, Crisp technical light)│
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 5: ĐIỀU KIỆN CHỐNG ẢO GIÁC (NEGATIVE CONSTRAINTS)                 │
│ (No messy wires, no distorted curves, no cartoon, no blurry text)      │
└────────────────────────────────────────────────────────────────────────┘
```

### Chi tiết các Tầng:

- **Tầng 1 (Engine Flags)**:
  - Midjourney: `--ar 16:10` (cho Featured) hoặc `--ar 16:9` (cho Content), `--v 6.1`, `--style raw`.
  - DALL-E 3: `style: natural` hoặc `style: vivid`, kèm chỉ thị `wide format`.
  - Leonardo / Flux: Khóa aspect ratio tương ứng `1.6:1` hoặc `1.77:1`.
- **Tầng 2 (Scene & Subject)**: Xác định rõ thiết bị công nghiệp cụ thể (ví dụ: *variable frequency drive VFD cabinet*, *active harmonic filter rack*, *capacitor bank with detuned iron-core reactors*), tránh dùng từ chung chung như *machine* hay *device*.
- **Tầng 3 (Visual Medium)**:
  - *Industrial Photography*: Chụp tài liệu công nghiệp chân thực.
  - *Engineering Infographic*: Sơ đồ đồ họa phẳng, vạch chia sắc nét, độ tương phản cao.
  - *3D Isometric Diagram*: Khối không gian 3 chiều phối cảnh trục đo kỹ thuật.
- **Tầng 4 (Corporate Palette)**:
  - Màu nền: Nền trắng sáng (`#ffffff`) hoặc xám kỹ thuật (`#f8fafc`).
  - Màu nhấn chính: Xanh hải quân Real Group (`#0f2b46`), xanh kỹ thuật (`#0284c7`).
  - Màu trạng thái: Cảnh báo (`#d97706`), nguy hiểm (`#dc2626`), an toàn (`#16a34a`).
- **Tầng 5 (Negative Constraints)**:
  `blurry, distorted wires, floating components, cartoonish, caricature, chaotic wiring, messy floor, hazardous electrical sparks, low resolution, deformed anatomy, illegible handwriting`.

---

<a name="4-thu-vien-archetypes"></a>
## 4. THƯ VIỆN KHUÔN MẪU TẠO PROMPT KỸ THUẬT (TECHNICAL ARCHETYPES)

Visual Agent căn cứ vào chủ đề bài viết để chọn 1 trong 5 Archetype tiêu chuẩn dưới đây:

### Archetype 1: Ảnh Chụp Bối cảnh Công nghiệp (Industrial Documentary Photography)
- **Ứng dụng**: Featured Image đầu bài, Case Study nhà máy thực tế.
- **Cấu trúc Prompt mẫu**:
  > *"Professional wide-angle industrial documentary photograph of a clean, state-of-the-art [BỐI_CẢNH_CÔNG_NGHIỆP] in a modern manufacturing plant. In the foreground, an experienced Vietnamese certified electrical engineer wearing a safety hardhat, high-visibility vest, and safety glasses operates a calibrated [TÊN_THIẾT_BỊ_ĐO] connected with color-coded test leads to a [TỦ_ĐIỆN_CHỦ_THỂ]. The analyzer screen shows glowing technical metrics and waveforms with cool blue and amber LED indicators. In the background, neatly organized industrial equipment. Crisp technical lighting, authentic industrial color grading with clean navy blue (#0f2b46) and metallic steel tones, highly realistic textures, photorealistic 8k, no cartoon, no distorted cables, no surreal artifacts --ar 16:10 --v 6.1"*

### Archetype 2: Đồ thị Dạng sóng & Phổ Sóng hài (Waveform & Spectrum Infographic)
- **Ứng dụng**: Phân tích chất lượng điện năng, biến tần, sóng hài, lọc tích cực AHF.
- **Cấu trúc Prompt mẫu**:
  > *"Clean professional engineering infographic diagram on an ultra-clean white background, split into two side-by-side technical panels. Left panel titled '[TIÊU_ĐỀ_ĐỒ_THỊ_SÓNG]': an oscilloscope-style graph displaying two alternating current waveforms over two electrical cycles; one waveform is a smooth green dashed line representing a pure 50Hz sinusoidal linear load current; the second waveform is an intense bold red solid curve showing a distorted non-linear waveform with characteristic sharp peaks. Right panel titled '[TIÊU_ĐỀ_PHỔ_TẦN_SỐ]': a clean vertical bar chart with sharp gridlines showing fundamental bar h1 (100% blue) and harmonic bars h5, h7, h11 in amber-orange. Minimalist industrial technical aesthetics, sharp vector look, high legibility, precision engineering textbook quality, crisp typography, no clutter, no 3D cartoon, no dark background --ar 16:9 --v 6.1"*

### Archetype 3: Mô hình Hình học Không gian 3D (3D Isometric Geometric Diagram)
- **Ứng dụng**: Không gian công suất Budeanu (P-Q-D), tam giác công suất, không gian vector dòng/áp, cấu trúc phân lớp.
- **Cấu trúc Prompt mẫu**:
  > *"High-precision 3D isometric technical diagram of the [TÊN_MÔ_HÌNH_3D] on a crisp clean off-white background (#f8fafc). An orthogonal 3D coordinate system originating from point (0,0,0): horizontal X-axis labeled '[TRỤC_X]' in deep navy blue (#0f2b46); vertical Y-axis labeled '[TRỤC_Y]' in bright technical cyan (#0284c7); depth Z-axis receding diagonally labeled '[TRỤC_Z]' in vivid engineering red (#dc2626). The three axes define a translucent 3D rectangular box with clean dashed projection lines. A bold glowing purple vector spans from the origin diagonally to the opposite far top corner of the box, labeled '[VECTOR_TỔNG]'. A technical callout arrow indicates key engineering insight. Sleek architectural geometry, high-end technical publication rendering, crisp sharp vectors, no artistic clutter, no dark shadows --ar 16:9 --v 6.1"*

### Archetype 4: Bố trí Đo kiểm & Vị trí Đấu nối Cảm biến (Sensor Measurement Setup)
- **Ứng dụng**: Kiểm toán năng lượng, phát hiện động cơ non tải, đo kiểm bảo trì dự đoán.
- **Cấu trúc Prompt mẫu**:
  > *"Clear technical engineering illustration showing the correct sensor measurement attachment points on an industrial [THIẾT_BỊ_CHỦ_THỂ]. Clean cutaway view of the motor terminal box and main feed cables. Three color-coded Rogowski current coils (CT) clamped around phases L1, L2, L3 and voltage probes attached to terminal studs. Clear callout arrows with clean labels pointing to measurement points. High-clarity vector technical diagram, engineering manual illustration style, clean white background, professional electrical schematic aesthetic, no clutter, no cartoon --ar 16:9 --v 6.1"*

### Archetype 5: Lưu đồ Chẩn đoán & Xử lý Sự cố (Troubleshooting Decision Flowchart)
- **Ứng dụng**: Các bài viết dạng `BLOG-T03` (Troubleshooting - Quy trình chẩn đoán lỗi biến tần, nổ tụ, trip relay).
- **Cấu trúc Prompt mẫu**:
  > *"Modern engineering decision tree flowchart for troubleshooting [MÃ_LỖI_HOẶC_SỰ_CỐ] in industrial facilities. Clean minimalist flowchart with rounded decision diamonds and rectangular action boxes connected by crisp directional arrows. Clear color coding: blue for normal check steps, amber for cautionary inspections, green for resolution actions, and red for trip/alarm conditions. Ultra-clean light gray background (#f8fafc), crisp readable typography, high-contrast engineering technical presentation, no chaotic lines, no decorative 3D effects --ar 16:9 --v 6.1"*

---

<a name="5-quy-chuan-khung-html"></a>
## 5. QUY CHUẨN KHUNG HTML PLACEHOLDER CHO CKEDITOR 3.6.6.2

Theo tiêu chuẩn [REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md), hình ảnh xuất ra CKEditor phải sử dụng 100% inline CSS, đảm bảo tính responsive tự co giãn trên thiết bị di động và có chú thích in nghiêng thanh lịch.

### Mẫu khung HTML tiêu chuẩn:

```html
<!-- IMAGE_[STT]: [TÊN_LOẠI_HÌNH] — [MÔ_TẢ_NGẮN] -->
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_[STT]]" alt="[MÔ_TẢ_ALT_CHUẨN_KỸ_THUẬT_SEO]" style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình [STT]:</strong> [Nội dung giải thích chuyên môn của hình ảnh, liên kết trực tiếp với lập luận trong bài viết].
    </p>
</div>
```

### Quy tắc Chống Biến dạng & Méo tỷ lệ trên Mobile (ADR-016):
> [!IMPORTANT]
> 1. **Khống chế cơ chế ép kích thước của CKEditor**: Khi tải ảnh lên qua hộp thoại Image của CKEditor 3.6, trình soạn thảo sẽ tự động đọc chiều rộng/chiều cao gốc (ví dụ: `width: 1200px; height: 675px;`) và chèn cứng vào `style`.
> 2. **Hậu quả vỡ layout**: Trên Mobile (màn hình hẹp 360px–480px), `max-width: 100%` ép chiều rộng ảnh về 360px nhưng thuộc tính `height: 675px` vẫn giữ nguyên khiến ảnh bị kéo giãn dọc dị dạng (tỷ lệ 16:9 bị bóp méo thành hình dọc 1:1.87).
> 3. **Giải pháp bắt buộc**:
>    - Thuộc tính `style` của thẻ `<img>` **BẮT BUỘC** phải có `display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;`. Cờ `!important` bảo đảm chiều cao tự động co theo tỷ lệ dù CKEditor có chèn thêm style.
>    - Khi người dùng thao tác qua hộp thoại CKEditor: Trong tab **Image Properties**, hãy **XÓA TRỐNG Ô HEIGHT** (để rỗng) hoặc chuyển sang chế độ Xem mã nguồn (Source) dán trực tiếp đoạn mã chuẩn.

### Quy tắc đặt Tên thẻ Alt & Chú thích (Caption):
- **Thẻ `alt`**: Bắt buộc chứa đầy đủ chủ thể kỹ thuật và ngữ cảnh (Ví dụ: `alt="So sánh dạng sóng dòng điện tải tuyến tính và tải biến tần 6-pulse kèm phổ sóng hài bậc 5 bậc 7"`). Tuyệt đối không để `alt="image"` hoặc nhồi nhét từ khóa SEO vô nghĩa.
- **Đánh số Chú thích (`Hình n`)**: Đánh số theo thứ tự xuất hiện tuyến tính từ trên xuống dưới trong bài viết (`Hình 1`, `Hình 2`, `Hình 3`). Đảm bảo số thứ tự trong file HTML, `image_specifications.md` và `draft_review_package.md` khớp nhau 100%.

---

<a name="6-co-che-nang-cap"></a>
## 6. CƠ CHẾ MỞ RỘNG & QUY TRÌNH NÂNG CẤP SKILL (UPGRADING PROTOCOL)

Khi dự án mở rộng sang các lĩnh vực kỹ thuật mới (IoT, SCADA, Solar, BESS...) hoặc khi các công nghệ AI tạo ảnh có bước nhảy vọt (Midjourney v7, DALL-E 4, Flux thế hệ mới), quy trình nâng cấp bộ kỹ năng này được thực hiện như sau:

```text
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ 1. Đề xuất Nhu cầu   │ ───> │ 2. Thử nghiệm Prompt │ ───> │ 3. Lưu trữ Bản cũ    │
│ (Archetype mới/Model)│      │ (Test tính ổn định)  │      │ (archive/ kèm lý do) │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                       │
                                                                       ▼
                              ┌──────────────────────┐      ┌──────────────────────┐
                              │ 5. Đồng bộ Hệ thống  │ <─── │ 4. Ban hành Bản mới  │
                              │ (Cập nhật liên kết)  │      │ (v1.2 / v2.0)        │
                              └──────────────────────┘      └──────────────────────┘
```

### 1. Bổ sung Archetype Kỹ thuật Mới:
- Khi xuất hiện dạng bài viết mới (ví dụ: *Bài viết Giải pháp Hệ thống Lưu trữ Năng lượng BESS*), Visual Agent sẽ đề xuất bổ sung Archetype mới (ví dụ: `Archetype 6: Container BESS Subsystem Architecture`) vào Mục 4 của Skill.
- Số hiệu phiên bản sẽ tăng theo chuẩn **Minor** (từ `v1.1` lên `v1.2`).

### 2. Thích ứng với Engine AI Mới:
- Khi xuất hiện engine AI mới có cú pháp tham số khác biệt, Visual Agent sẽ cập nhật bảng ánh xạ cờ tham số (Flags Adapter) ở Tầng 1 (Mục 3) mà không làm thay đổi cấu trúc cốt lõi của các Archetype.

### 3. Quy tắc Lưu trữ Khi Nâng cấp (Tuân thủ ADR-009):
- Khi ban hành phiên bản `v1.2` (hoặc cao hơn), phiên bản hiện tại `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md` **bắt buộc phải được di chuyển vào thư mục `00_SKILL/archive/`**.
- Cập nhật bảng kê phiên bản trong `00_SKILL/archive/README.md`.
- Tuyệt đối không xóa bỏ và không ghi đè lên phiên bản cũ.

---

<a name="7-checklist-nghiem-thu"></a>
## 7. CHECKLIST NGHIỆM THU CỦA TECH REVIEW AGENT (AUDIT CHECKLIST)

Khi thực hiện kiểm duyệt theo [TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md) (Trụ cột 4 - Presentation & Visual Audit), Tech Review Agent phải xác minh đủ 6 tiêu chí:

- [ ] **1. Tệp đặc tả độc lập**: Có tồn tại tệp `image_specifications.md` đúng cấu trúc chuẩn tại thư mục bài viết.
- [ ] **2. Không render code trực tiếp**: Trong mã nguồn HTML không còn bất kỳ thẻ `<svg>`, canvas hoặc script code vẽ hình nào (Tuân thủ ADR-010).
- [ ] **3. Số lượng hình đạt chuẩn**: Đúng 1 Featured Image (808x500 px) và từ 1 đến 3 hình nội dung (1 ≤ n ≤ 3) theo Standard v1.3.
- [ ] **4. Prompt AI đạt chuẩn 5 tầng**: Các prompt tiếng Anh có đầy đủ bối cảnh, chủ thể kỹ thuật rõ ràng, tỷ lệ khung hình và negative prompt chống ảo giác.
- [ ] **5. Khung HTML & Placeholder chuẩn xác**: Mỗi hình trong bài đều có khung thẻ `<img>` responsive với placeholder `[URL_HINH_ANH_n]`, viền đổ bóng và caption in nghiêng `Hình n:`.
- [ ] **6. Đồng nhất số thứ tự**: Thứ tự `Hình 1`, `Hình 2` khớp nhau 100% giữa `image_specifications.md`, `draft_review_package.md` và mã HTML CKEditor.
