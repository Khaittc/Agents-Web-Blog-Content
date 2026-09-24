# HỒ SƠ QUY CÁCH HÌNH ẢNH & PROMPT AI (IMAGE SPECIFICATIONS) — BLOG_03

**Chủ đề bài viết**: Quy trình 4 bước chẩn đoán và khắc phục lỗi quá dòng (Overcurrent) trên biến tần công nghiệp  
**Mã bài viết**: `BLOG_03`  
**Ngày lập**: 24/09/2026  
**Agent phụ trách**: **Visual Agent**  
**Quy chuẩn tuân thủ**: `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1`, `ADR-010`, `ADR-011`  

---

## 1. TỔNG QUAN & HƯỚNG DẪN QUY TRÌNH 5 BƯỚC

Theo quyết định kiến trúc **ADR-010**, bài viết không nhúng mã vẽ hình thô (SVG) trực tiếp vào file HTML, mà Visual Agent có trách nhiệm cung cấp toàn bộ đặc tả kỹ thuật và câu lệnh Prompt AI hoàn chỉnh để Kỹ sư trưởng / Người dùng chủ động tạo ảnh và xuất bản:

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Bước 1:         │     │ Bước 2:         │     │ Bước 3:         │
│ Copy Prompt AI  │ ──> │ Sinh ảnh bằng   │ ──> │ Lưu ảnh định    │
│ tại Mục 2, 3, 4 │     │ Midjourney v6 / │     │ dạng WebP,      │
│ bên dưới        │     │ DALL-E 3 / Leo  │     │ nén < 200 KB    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                         │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Bước 5:         │     │ Bước 4:         │     │ Bước 4 (tiếp):  │
│ Thay placeholder│ <── │ Lấy link URL    │ <── │ Tải ảnh lên CMS │
│ [URL_HINH_ANH_n]│     │ công khai của   │     │ hoặc CDN của    │
│ trong file HTML │     │ từng hình ảnh   │     │ real-group.org  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 2. ĐẶC TẢ FEATURED IMAGE (ẢNH ĐẠI DIỆN BÀI VIẾT)

- **Vị trí hiển thị**: Ảnh đại diện bài viết trên website `real-group.org`, hiển thị trong danh mục Blog và thẻ OpenGraph khi chia sẻ lên mạng xã hội.
- **Kích thước chuẩn**: `808 × 500 px` (Tỷ lệ ~ 1.618 : 1).
- **Định dạng file**: WebP (hoặc JPG chất lượng cao), dung lượng tối ưu `< 150 KB`.
- **Tên file đề xuất**: `quy-trinh-chan-doan-khac-phuc-loi-qua-dong-bien-tan-808x500.webp`
- **Thẻ ALT Text chuẩn SEO**: *Kỹ sư bảo trì điện sử dụng đồng hồ đo cách điện Megger và đồng hồ vạn năng kiểm tra lỗi quá dòng biến tần trong tủ điện điều khiển MCC*
- **Archetype**: *Archetype 1 — Industrial Context & Electrical Engineer*.

### Copy-Paste AI Prompt (Khung 5 tầng chuẩn Skill v1.1):
```text
Professional industrial photograph of an experienced electrical automation engineer wearing high-visibility flame-retardant PPE, protective safety glasses, and insulated high-voltage electrical gloves, diagnosing a modern high-power variable frequency drive (VFD) inside a clean industrial motor control center (MCC) cabinet. The engineer holds a calibrated digital insulation multimeter, testing control wiring with precision. The inverter digital operator panel is clearly visible displaying technical metrics. Modern manufacturing factory background with soft depth of field, crisp technical studio lighting, corporate deep navy blue (#0f2b46) and technical cyan (#005a9c) accents with amber LED indicators, authentic engineering atmosphere, ultra-realistic, photorealistic, 8k resolution, shot on 50mm f/2.8 lens --ar 16:10 --style raw --v 6.0
```

- **Negative Prompt**:
```text
cartoon, 3d render, anime, blurry, distorted hands, extra fingers, text errors, misspelled labels, messy cables, hazardous unsafe work conditions, dark gloomy lighting, low resolution, watermark
```

---

## 3. ĐẶC TẢ HÌNH ẢNH NỘI DUNG 1 (HÌNH 1 — LƯU ĐỒ CÂY QUYẾT ĐỊNH CHẨN ĐOÁN LỖI OC)

- **Vị trí trong bài**: Đặt sau **Mục 2** (Bảng đối chiếu mã lỗi của các hãng biến tần).
- **Tỷ lệ hiển thị**: `16:9` (Độ phân giải khuyến nghị: `1200 × 675 px` hoặc `1920 × 1080 px`).
- **Tên file đề xuất**: `hinh-1-luu-do-cay-quyet-dinh-chan-doan-loi-qua-dong-bien-tan.webp`
- **Thẻ ALT Text**: *Lưu đồ cây quyết định 4 bước chẩn đoán và cô lập lỗi quá dòng biến tần công nghiệp từ cơ khí đến mạch IGBT*
- **Chú thích hình ảnh (Caption)**:
  *Hình 1: Lưu đồ cây quyết định 4 bước cô lập và xử lý sự cố lỗi quá dòng biến tần (Troubleshooting Decision Tree) từ tải cơ khí đến linh kiện bán dẫn công suất IGBT.*
- **Archetype**: *Archetype 5 — Troubleshooting & Decision Flowchart*.

### Copy-Paste AI Prompt:
```text
Clean technical flowchart diagram illustrating a 4-step troubleshooting decision tree for Variable Frequency Drive (VFD) Overcurrent fault diagnosis. The infographic is organized into 4 logical vertical stages on an off-white technical blueprint grid: Step 1 Mechanical Load Isolation (rotating shaft, decoupled motor), Step 2 Cable & Motor Winding Testing (phase resistance balance Delta-R <= 2% and Megger insulation resistance testing > 5 Megohms per IEEE 43), Step 3 Parameter Tuning (acceleration ramp time increase, torque boost reduction), Step 4 Power Stage IGBT Inverter Bridge Testing (multimeter diode check). Modern industrial infographic style, crisp vector lines, professional typography, technical cyan (#0284c7), deep navy blue (#0f2b46), warning amber (#d97706), and pass green (#16a34a) accents, clean white background, high contrast, engineering publication aesthetic, 8k resolution --ar 16:9 --v 6.0
```

- **Đoạn mã HTML Placeholder sẵn sàng xuất bản**:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_1]" alt="Lưu đồ cây quyết định 4 bước chẩn đoán và cô lập lỗi quá dòng biến tần công nghiệp từ cơ khí đến mạch IGBT" style="max-width:100%;height:auto;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 1:</strong> Lưu đồ cây quyết định 4 bước cô lập và xử lý sự cố lỗi quá dòng biến tần (Troubleshooting Decision Tree) từ tải cơ khí đến linh kiện bán dẫn công suất IGBT.
    </p>
</div>
```

---

## 4. ĐẶC TẢ HÌNH ẢNH NỘI DUNG 2 (HÌNH 2 — SƠ ĐỒ ĐO KIỂM 6 VAN IGBT BẰNG ĐỒNG HỒ VOM)

- **Vị trí trong bài**: Đặt tại **Mục 3 (Bước 4: Kiểm tra Khối Công suất Biến tần)**.
- **Tỷ lệ hiển thị**: `16:9` (Độ phân giải khuyến nghị: `1200 × 675 px` hoặc `1920 × 1080 px`).
- **Tên file đề xuất**: `hinh-2-so-do-do-kiem-tra-6-van-igbt-bien-tan-dong-ho-vom.webp`
- **Thẻ ALT Text**: *Sơ đồ nguyên lý đo kiểm tra 6 van bán dẫn IGBT biến tần bằng thang đo Diode của đồng hồ vạn năng kỹ thuật số*
- **Chú thích hình ảnh (Caption)**:
  *Hình 2: Phương pháp đo kiểm tra phân cực thuận và phân cực nghịch của 6 van IGBT nghịch lưu thông qua đi-ốt xả ngược (Freewheeling Diode) bằng thang đo Diode của đồng hồ VOM.*
- **Archetype**: *Archetype 4 — Measurement Setup & Sensor Placement (Electrical Testing Schematic)*.

### Copy-Paste AI Prompt:
```text
Professional technical electrical schematic and diagnostic diagram showing how to test a 3-phase inverter power stage (6-pack IGBT bridge) using a digital multimeter in diode test mode. The diagram clearly depicts the DC Bus positive terminal (DC+) and negative terminal (DC-), and the three motor output phase terminals (U, V, W). Six IGBT switches with anti-parallel freewheeling diodes are shown in an H-bridge configuration. Red (+) and black (-) multimeter test probes are illustrated testing the forward bias (0.3V - 0.7V drop) and reverse bias (OL open loop). Clean electrical engineering CAD layout style, technical labels, blue and red probe leads, crisp vector lines on clean subtle gray background, high clarity, industrial training manual illustration quality, 8k resolution --ar 16:9 --v 6.0
```

- **Đoạn mã HTML Placeholder sẵn sàng xuất bản**:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_2]" alt="Sơ đồ nguyên lý đo kiểm tra 6 van bán dẫn IGBT biến tần bằng thang đo Diode của đồng hồ vạn năng kỹ thuật số" style="max-width:100%;height:auto;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 2:</strong> Phương pháp đo kiểm tra phân cực thuận và phân cực nghịch của 6 van IGBT nghịch lưu thông qua đi-ốt xả ngược (Freewheeling Diode) bằng thang đo Diode của đồng hồ VOM.
    </p>
</div>
```

---

## 5. BẢNG TỔNG HỢP VỊ TRÍ & MÃ PLACEHOLDER CKEDITOR

| Định danh ảnh | Vai trò trong bài | Tỷ lệ & Kích thước | Chuỗi Placeholder HTML | Tên tệp đề xuất khi tải lên |
|:---|:---|:---:|:---|:---|
| **Featured Image** | Ảnh đại diện bài viết / OpenGraph | 16:10 (`808 × 500 px`) | Đặt tại khung Featured Image trên CMS | `quy-trinh-chan-doan-khac-phuc-loi-qua-dong-bien-tan-808x500.webp` |
| **Hình 1** | Sau Mục 2 (Lưu đồ cây quyết định OC) | 16:9 (`1200 × 675 px`) | `src="[URL_HINH_ANH_1]"` | `hinh-1-luu-do-cay-quyet-dinh-chan-doan-loi-qua-dong-bien-tan.webp` |
| **Hình 2** | Sau Mục 3 (Sơ đồ đo 6 van IGBT) | 16:9 (`1200 × 675 px`) | `src="[URL_HINH_ANH_2]"` | `hinh-2-so-do-do-kiem-tra-6-van-igbt-bien-tan-dong-ho-vom.webp` |

---

## 6. CHECKLIST KIỂM ĐỊNH KỸ THUẬT (DÀNH CHO TECH REVIEW AGENT)

Tech Review Agent đối chiếu các tiêu chí sau khi nghiệm thu Trụ cột 4 (Presentation & Visual Audit):
- [x] Có đầy đủ 1 Featured Image (808x500 px) và 2 hình ảnh nội dung kỹ thuật (1 ≤ n ≤ 3 theo Standard v1.3).
- [x] File HTML không chứa bất kỳ thẻ vẽ mã thô `<svg>` hoặc `<canvas>` nào (tuân thủ ADR-010).
- [x] 100% hình ảnh nội dung sử dụng khung thẻ `<img>` responsive với class/style bóng đổ nhẹ, bo góc 4px và viền xám tinh tế `#e2e8f0`.
- [x] Đoạn chú thích hình ảnh in nghiêng (`Hình 1:`, `Hình 2:`) đồng nhất ngữ nghĩa với nội dung bài viết.
- [x] Chuỗi placeholder `[URL_HINH_ANH_1]` và `[URL_HINH_ANH_2]` rõ ràng, sẵn sàng cho việc tìm-thay thế đường dẫn URL khi đăng bài.
- [x] Mỗi hình ảnh đều có bộ câu lệnh Prompt AI 5 tầng chuyên sâu, khả thi và sẵn sàng sao chép sử dụng trên các nền tảng AI tạo hình ảnh.
