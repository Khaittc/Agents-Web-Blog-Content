# HƯỚNG DẪN TẠO HÌNH ẢNH VÀ PROMPT PHONG CÁCH KỸ THUẬT (IMAGE PROMPT & STYLE GUIDE)
Version: 1.0  
Trạng thái: Áp dụng chính thức cho Visual & Asset Agent  
Mục tiêu: Đảm bảo hình ảnh minh họa trên website `real-group.org` đồng nhất về kích thước, đúng chuẩn kỹ thuật công nghiệp và không gây hiểu nhầm chuyên môn.

---

## 1. MỤC ĐÍCH & NGUYÊN TẮC CỐT LÕI

Hình ảnh trong bài viết kỹ thuật phục vụ mục đích **giải thích trực quan** chứ không đơn thuần để "trang trí".

### 3 Nguyên tắc bắt buộc:
1. **Đúng tỷ lệ chuẩn**: Mọi Featured Image (ảnh đại diện) bắt buộc phải theo tỷ lệ và kích thước chính xác:
   ```text
   808 × 500 px (tỷ lệ xấp xỉ 16:10 / 1.618)
   ```
2. **Không dùng AI vẽ sơ đồ chính xác**: Tuyệt đối không dùng mô hình AI tạo ảnh (DALL-E, Imagen...) để vẽ sơ đồ đấu dây điện, sơ đồ chân vi điều khiển hoặc công thức toán học (vì AI dễ tạo ra các linh kiện giả, dây nối lung tung, ký hiệu sai lệch).
3. **Phân định rõ 2 loại hình ảnh**:
   - **Ảnh Minh họa Bối cảnh (Illustrative Image)**: Dùng AI tạo bối cảnh nhà máy, kỹ sư làm việc, tủ điện tổng quan, động cơ trong dây chuyền.
   - **Biểu đồ Kỹ thuật (Technical Figure)**: Dùng sơ đồ khối vector, đồ thị số liệu có kiểm soát hoặc ảnh chụp thiết bị đo thực tế.

---

## 2. QUY CHUẨN FEATURED IMAGE (ẢNH ĐẠI DIỆN BÀI VIẾT)

### 2.1. Cấu trúc Prompt Chuẩn (Prompt Template)
Khi dùng công cụ tạo ảnh AI (`generate_image`), Visual Agent phải xây dựng prompt theo công thức 5 phần:

```text
[Bối cảnh Công nghiệp thực tế] + [Chủ thể Kỹ thuật trọng tâm] + [Chi tiết / Hành động Kỹ thuật] + [Ánh sáng & Phong cách chụp chuyên nghiệp] + [Negative Constraints]
```

### 2.2. Từ khóa Định hình Phong cách Real Group (Style Keywords)
- **Thiết lập bối cảnh**: `Modern industrial plant`, `clean automation facility`, `electrical substation control room`, `motor control center (MCC)`.
- **Chủ thể**: `Three-phase induction motor with drive shaft`, `variable frequency drive (VFD) cabinet with clean cable management`, `certified electrical engineer using calibrated power quality analyzer`.
- **Ánh sáng & Thẩm mỹ**: `Crisp technical photography`, `cinematic industrial lighting`, `cool neutral color palette (#0284c7 accents)`, `high dynamic range`, `shallow depth of field highlighting the measurement interface`.
- **Negative Prompts (Điều cấm)**: `blurry, distorted wires, surreal floating components, low resolution, cartoon, 3D render caricature, chaotic wiring, dangerous electrical hazards`.

### 2.3. Ví dụ Prompt Hoàn chỉnh

#### Bài toán Động cơ non tải (BLOG-T02):
> **Prompt**: *"Professional high-angle industrial photograph of a clean, modern manufacturing factory floor. In the foreground, an electrical engineer in safety gear uses a calibrated portable power quality analyzer attached to a heavy-duty three-phase electric induction motor. Crisp technical lighting, authentic industrial color grading with clean blue and metallic gray tones, realistic machinery details, 8k resolution, photorealistic."*  
> **Kích thước / Tỷ lệ**: `Aspect Ratio: 16:10` hoặc crop về `808x500 px`.

---

## 3. QUY CHUẨN HÌNH ẢNH TRONG NỘI DUNG (CONTENT IMAGES)

Mỗi bài viết kỹ thuật bắt buộc phải có từ **1 đến tối đa 3 hình ảnh** trong phần thân bài (`IMAGE_1`, `IMAGE_2`, `IMAGE_3`). Tuyệt đối không xuất bản bài viết mà không có hình ảnh nội dung.

```text
┌─────────────────────────────────────────────────────────────┐
│ IMAGE_1: Nguyên lý / Vị trí đo lường                        │
│ (Vị trí kẹp cảm biến CT, điểm đấu nối đo lường thực tế)     │
├─────────────────────────────────────────────────────────────┤
│ IMAGE_2: So sánh kỹ thuật / Đồ thị phân tích                │
│ (Đồ thị suy giảm hiệu suất, so sánh dạng sóng hài)          │
├─────────────────────────────────────────────────────────────┤
│ IMAGE_3: Lưu đồ quyết định / Checklist hành động            │
│ (Flowchart quy trình troubleshooting, bảng ma trận chọn mẫu)│
└─────────────────────────────────────────────────────────────┘
```

---

## 4. QUY CÁCH CHÈN HTML VÀO CKEDITOR 3.6.6.2

Theo chuẩn [REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md), hình ảnh xuất ra CKEditor phải có wrapper căn giữa, responsive và chú thích ảnh (*Caption*) rõ ràng:

```html
<div style="margin:24px 0;text-align:center;">
    <img src="[URL_HINH_ANH]" alt="[Mô tả chính xác cho SEO và kỹ thuật]" style="max-width:100%;height:auto;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
    <p style="font-size:14px;color:#64748b;margin-top:8px;font-style:italic;">
        <strong>Hình 1:</strong> [Chú thích ngắn gọn, giải thích rõ đối tượng trong hình]
    </p>
</div>
```

---

## 5. CHECKLIST NGHIỆM THU HÌNH ẢNH (ASSET ACCEPTANCE CHECKLIST)

- [ ] Featured Image đúng kích thước chuẩn `808 × 500 px`.
- [ ] Ảnh đại diện có liên quan trực tiếp đến tiêu đề và chủ đề kỹ thuật.
- [ ] Không có chữ bị méo mó, biến dạng hoặc lỗi font do AI sinh ra.
- [ ] Số lượng ảnh nội dung trong bài: tối thiểu 1 hình, tối đa 3 hình (1 ≤ n ≤ 3).
- [ ] Mỗi ảnh đều có thẻ `alt` chuẩn kỹ thuật (không nhồi nhét từ khóa SEO vô nghĩa).
- [ ] Có đầy đủ phần chú thích nguồn hoặc chú thích chi tiết (`Hình n: ...`).
- [ ] File hình ảnh được tối ưu dung lượng (định dạng WebP hoặc JPG chất lượng cao < 200 KB) để tối ưu tốc độ tải trang (LCP).
