# THƯ MỤC LƯU TRỮ CÁC PHIÊN BẢN CŨ CỦA BỘ KỸ NĂNG (SKILL ARCHIVE)

Thư mục này lưu trữ các phiên bản tiền nhiệm của các bộ quy chuẩn kỹ năng (Skills & Standards) trong thư mục `00_SKILL/`.

## 1. NGUYÊN TẮC QUẢN LÝ PHIÊN BẢN (VERSIONING & ARCHIVING PROTOCOL)

1. **Không lưu đè**: Khi một bộ kỹ năng được nâng cấp lên phiên bản mới (ví dụ từ `v1.2` lên `v1.3`), phiên bản cũ **bắt buộc phải được di chuyển vào thư mục này (`00_SKILL/archive/`)**, không được xóa bỏ và không được ghi đè.
2. **Phiên bản hiện hành (Active)**: Chỉ phiên bản mới nhất, chính thức có hiệu lực mới được nằm ở thư mục gốc `00_SKILL/`.
3. **Bảo toàn lịch sử quyết định**: Giúp các Agent và Kỹ sư trưởng có thể tra cứu lại các quy định cũ khi kiểm tra các bài viết được sản xuất ở các giai đoạn trước đó mà không gây xung đột quy chuẩn.

## 2. DANH SÁCH CÁC PHIÊN BẢN LƯU TRỮ

| Tên tệp lưu trữ | Phiên bản | Ngày lưu trữ | Lý do thay thế / Nâng cấp |
|---|---|---|---|
| `BLOG_CONTENT_STRUCTURE_STANDARD_v1.2.md` | v1.2 | 23/09/2026 | Nâng cấp lên v1.3: Sửa Mục 14 bắt buộc tối thiểu 1 hình ảnh nội dung (Content Image: 1 ≤ n ≤ 3) thay vì 0 đến 3 hình. |
| `IMAGE_PROMPT_STYLE_GUIDE_v1.0.md` | v1.0 | 23/09/2026 | Nâng cấp lên `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md`: Chuẩn hóa cấu trúc tệp bàn giao `image_specifications.md`, cơ chế Prompt AI 5 tầng, thư viện archetype kỹ thuật, chuyển sang khung placeholder HTML (ADR-010). |
| `IEEE_CITATION_REFERENCE_SKILL_v1.3.md` | v1.3 | 23/09/2026 | Tách nguyên khối 2.204 dòng thành Bộ 4 Sub-Skills chuyên biệt (`IEEE_01` đến `IEEE_04` và Master Suite v2.0): Bổ sung cửa ải bắt buộc xác thực URL sống (HTTP 200), quy chuẩn link bấm được trong CKEditor, loại bỏ 100% nguy cơ link ảo (ADR-012). |
| `IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0.md` | v1.0 | 23/09/2026 | Nâng cấp lên v1.1: Bổ sung ràng buộc bắt buộc 100% vị trí đặt trích dẫn nội văn (in-text citation) phải luôn luôn nằm ở CUỐI CÂU (ngay trước dấu chấm hoặc dấu hai chấm kết thúc câu), cấm đặt ở giữa câu hoặc làm chủ ngữ/tân ngữ. |
| `IEEE_04_CITATION_AUDIT_PROTOCOL_v1.0.md` | v1.0 | 23/09/2026 | Nâng cấp lên v1.1: Bổ sung tiêu chí kiểm duyệt Gate 5 bắt buộc kiểm tra vị trí đặt trích dẫn nội văn luôn luôn ở cuối câu, đánh trượt (FAIL) nếu phát hiện trích dẫn ở giữa câu. |
| `IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.0.md` | v1.0 | 24/09/2026 | Nâng cấp lên v1.1 (ADR-015): Bổ sung Cửa ải Điều hướng Trực tiếp (Direct Content Navigation & Deep-Linking Gate) và Cửa ải Khớp Tiêu đề Nội dung, cấm trích dẫn URL trang chủ (homepage) hoặc trang tìm kiếm chung chung không mở đúng tài liệu tham khảo. |
| `IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL_v1.0.md` | v1.0 | 24/09/2026 | Nâng cấp lên v1.1 (ADR-016): Bổ sung chuẩn Responsive đa thiết bị (Laptop & Mobile), bắt buộc `word-break: break-word; overflow-wrap: anywhere;` cho đoạn tham khảo và `word-break: break-all;` cho thẻ `<a>` chống vỡ khung màn hình mobile. |
| `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.1.md` | v1.1 | 24/09/2026 | Nâng cấp lên v1.2 (ADR-016): Bổ sung tiêu chuẩn responsive chống méo tỷ lệ ảnh trên mobile khi CKEditor 3.6 tự động chèn thuộc tính cố định (`height: auto !important;`, `display: block; margin: 0 auto;`). |
| `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.0.md` | v1.0 | 24/09/2026 | Nâng cấp lên v1.1 (ADR-017): Bổ sung Cửa ải Kiểm định Responsive Song song Bắt buộc trên Laptop và Mobile (Dual-Viewport Responsive Audit Gate), kiểm soát 4 checkpoint: chống méo ảnh, bảng cuộn ngang min-width, link ngắt dòng break-word và phân cấp heading. |




