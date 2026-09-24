# QUY CHUẨN VẬN HÀNH, PHÊ DUYỆT VÀ KHÓA BÀI VIẾT (ARTICLE LIFECYCLE & APPROVAL PROTOCOL)
**Mã tài liệu**: `02_AGENT_TEMPLATES/ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md`
**Phiên bản**: 2.0 (Phase 2.5 Architecture Hardening)
**Dự án**: Hệ thống Tự động hóa Đa Agent Sản xuất Nội dung Kỹ thuật (Real Group / TTC)
**Mục đích**: Quy định nền tảng tương tác ra đề bài, máy trạng thái vòng đời bài viết, phân tách 2 cổng kiểm định, cơ chế khóa toàn vẹn mã băm (Content Integrity Hash) và vai trò phát hành thủ công của con người.

---

## 1. NỀN TẢNG VẬN HÀNH ĐỂ RA ĐỀ BÀI (EXECUTION PLATFORMS)

### Nền tảng Chính thức: Trực tiếp trên Google Antigravity (ADR-018)
- **Phương thức**: Người dùng giao tiếp trực tiếp với hệ thống tại khung chat của Antigravity IDE hoặc CLI.
- **Cú pháp ra đề bài chuẩn**:
  ```text
  Tạo bài viết mới dạng [MÃ_CANONICAL_TAXONOMY] về chủ đề: "[TÊN CHỦ ĐỀ]"
  Yêu cầu trọng tâm: [CÁC ĐIỂM KỸ THUẬT CẦN LÀM RÕ]
  ```
  *Lưu ý*: `MÃ_CANONICAL_TAXONOMY` bắt buộc phải là 1 trong 5 mã chuẩn trong `00_SKILL/BLOG_TAXONOMY_CANONICAL_v1.0.md` (`BLOG-T01` đến `BLOG-T05`).
- **Các Slash Commands hỗ trợ tăng tốc**:
  - `/goal`: Tự động vận hành liên tục cho đến khi hoàn tất thẩm định qua các cổng kiểm định.
  - `/boost`: Phân tích sâu các vấn đề tính toán công thức, rà soát logic đa chiều.
  - `/teamwork-preview`: Điều phối và trực quan hóa luồng phối hợp giữa các subagents.

---

## 2. MÁY TRẠNG THÁI VÒNG ĐỜI BÀI VIẾT (STANDARDIZED ARTICLE STATE MACHINE)

Toàn bộ quy trình từ đề bài đến ấn bản chính thức tuân thủ máy trạng thái 10 bước chuẩn mực:

```text
[Khởi tạo đề bài]
       │
       ▼
    1. DRAFT ◄──────────────────────────────────────────────┐
       │ (Research Agent hoàn thành evidence.json)          │
       ▼                                                    │
 2. RESEARCHED                                              │
       │ (Drafting Agent soạn thảo & tạo claim map)         │
       ▼                                                    │
 3. TECH_REVIEW ────────────────────────────────────────────┤
       │ (Technical Review Gate: Claim, Citation, Math)     │
       ▼ PASS                                               │ REVISION_REQUESTED
4. TECH_APPROVED                                            │ (Tối đa 3 vòng lặp)
       │ (Visual Agent hoàn thiện image_specifications.md)  │
       ▼                                                    │
 5. VISUAL_READY                                            │
       │ (Packaging Agent đóng gói HTML sạch & manifest)    │
       ▼                                                    │
 6. PRESENTATION_REVIEW ────────────────────────────────────┘
       │ (Presentation Review Gate: Laptop/Mobile Responsive, CSS Inline)
       ▼ PASS
  7. IN_REVIEW
       │
       ▼ (Kỹ sư trưởng kiểm tra toàn diện & gõ lệnh phê duyệt)
8. APPROVED / LOCKED ────────────── [Chỉ mở khi có lệnh: UNLOCK]
       │
       ▼ (Kỹ sư trưởng tự tay copy mã HTML và xuất bản lên CMS)
 9. PUBLISHED
```

### Chi tiết các trạng thái trong hệ thống:
1. **`DRAFT`**: Trạng thái khởi tạo bài viết, tiếp nhận đề tài từ người dùng.
2. **`RESEARCHED`**: Research Agent đã thẩm định xong nguồn tài liệu, xuất song song `evidence.json` (Stable Source IDs `SRC-xxx`) và `evidence_dossier.md`.
3. **`TECH_REVIEW`**: Bản thảo và bản đồ luận điểm (`claim_source_map.json`) đang được Review Agent thẩm định tại **Cổng 1 (Technical Review Gate)**.
4. **`TECH_APPROVED`**: Cổng 1 đã ký duyệt PASS. Nội dung kỹ thuật, công thức và trích dẫn chuẩn IEEE ở cuối câu đã được khóa cứng.
5. **`VISUAL_READY`**: Visual Agent đã hoàn thiện hồ sơ đặc tả ảnh `image_specifications.md` và các hình ảnh kỹ thuật liên quan.
6. **`PRESENTATION_REVIEW`**: Publisher Agent đã đóng gói xong mã HTML CKEditor và bản kê `article_manifest.json`. Tệp đang được Review Agent thẩm định tại **Cổng 2 (Presentation & Responsive Review Gate)**.
7. **`IN_REVIEW`**: Cả 2 cổng kiểm định đều đã PASS. Toàn bộ hồ sơ bài viết sẵn sàng chờ Kỹ sư trưởng nghiệm thu.
8. **`REVISION_REQUESTED`**: Có phát hiện sai sót tại Cổng 1 hoặc Cổng 2. Review Agent phát hành `revision_request.json` yêu cầu hiệu chỉnh có phạm vi chỉ định (tối đa 3 vòng lặp).
9. **`APPROVED`**: Kỹ sư trưởng đã kiểm duyệt thực tế và phê duyệt chính thức. Kích hoạt cơ chế khóa toàn vẹn 3 lớp.
10. **`PUBLISHED`**: **Chỉ được thiết lập sau khi Kỹ sư trưởng xác nhận bài viết đã được đăng tải thực tế thành công lên website**. Agent tuyệt đối không tự ý gán trạng thái này.

---

## 3. CƠ CHẾ BẢO VỆ TOÀN VẸN 3 LỚP (3-LAYER INTEGRITY PROTECTION)

Nhằm bảo vệ tuyệt đối các bài viết đã được phê duyệt khỏi mọi hành vi sửa đổi ngoài ý muốn:

### Lớp 1: Mã Băm Toàn Vẹn Máy Đọc (Content SHA-256 Integrity Hash)
Trong tệp `article_status.json` của mỗi bài viết, khi chuyển sang trạng thái `APPROVED`, hệ thống bắt buộc ghi nhận các trường bảo chứng:
```json
{
  "article_id": "BLOG_03",
  "title": "Tên bài viết",
  "category": "BLOG-T03",
  "status": "APPROVED",
  "is_locked": true,
  "approved_by": "Kỹ sư trưởng",
  "approved_at": "2026-09-24T15:05:00+07:00",
  "approved_content_sha256": "BF8BF18B11DDA71D3E3FCF31EAC05635113451C8009B83B44C7F635E4F327DC1",
  "approved_commit_sha": "fb92e7b1c4e1ca73caea7508412ac6954596e191",
  "html_file": "bai-viet-chan-doan-qua-dong-bien-tan-ckeditor.html",
  "notes": "Đã phê duyệt và khóa an toàn."
}
```

> [!IMPORTANT]
> **QUY TẮC KIỂM TRA TOÀN VẸN (INTEGRITY CHECK)**:
> Khi bất kỳ Agent nào đọc một bài viết có `status: "APPROVED"` hoặc `is_locked: true`, Agent phải tính toán mã băm SHA-256 của tệp HTML hiện tại và đối chiếu với `approved_content_sha256`.
> Nếu có sự sai lệch: Lập tức phát cảnh báo **`INTEGRITY_WARNING`**, từ chối xử lý và báo cáo ngay cho Kỹ sư trưởng. Git history và commit hash là căn cứ xác thực tối thượng.

### Lớp 2: Kiểm soát bằng Guardrail trong `AGENT_GUIDE.md`
- Trước khi thực hiện bất kỳ thao tác ghi đè hoặc chỉnh sửa nào trong thư mục `03_Articles/[Tên_Bài]`, Agent **BẮT BUỘC PHẢI ĐỌC** `article_status.json`.
- Nếu bài viết đã `APPROVED` hoặc `is_locked: true`: Agent **BẮT BUỘC TỪ CHỐI THỰC HIỆN** chỉnh sửa.

### Lớp 3: Khóa tệp ở tầng Hệ điều hành (OS Read-Only)
- Khi phê duyệt, file HTML CKEditor sẽ được bật cờ Read-Only của hệ điều hành:
  ```powershell
  attrib +r "03_Articles/[Tên_Bài]/bai-viet-*-ckeditor.html"
  ```
  *(Cờ Read-Only là lớp bảo vệ phụ trợ tại local, ngăn các công cụ tự động ghi đè).*

---

## 4. QUY ĐỊNH PHÁT HÀNH THỦ CÔNG (MANUAL CMS PUBLISHING RULE)

Hệ thống AI đa tác tử được định vị là công cụ đóng gói và đảm bảo chất lượng, **không thay thế con người trong quyền xuất bản công khai**:

1. **Agent chỉ đóng gói (Packaging Only)**: Publisher Agent tạo ra tệp HTML hoàn thiện, sạch sẽ và tương thích 100% với CKEditor 3.6.6.2.
2. **Kỹ sư trưởng là người xuất bản duy nhất**: Kỹ sư trưởng kiểm tra giao diện bài viết trên website thực tế, copy mã HTML vào CMS, kiểm tra ảnh đại diện và nhấn nút "Đăng bài".
3. **Cập nhật trạng thái `PUBLISHED`**: Chỉ sau khi bài viết đã có URL hoạt động công khai trên website `real-group.org`, Kỹ sư trưởng mới ra lệnh cập nhật trạng thái `PUBLISHED` trong `article_status.json`.

---

## 5. GIAO THỨC MỞ KHÓA (UNLOCK PROTOCOL)

Khi bài viết đã ở trạng thái `APPROVED / LOCKED`, nếu Kỹ sư trưởng thực sự muốn cập nhật nội dung (ví dụ: bổ sung số liệu tiêu chuẩn mới):
- **Cú pháp bắt buộc từ Kỹ sư trưởng**:
  > *"UNLOCK [MÃ_BÀI_VIẾT]: [LÝ DO MỞ KHÓA VÀ YÊU CẦU SỬA]"*
- **Hành động của Agent**:
  1. Gỡ bỏ thuộc tính Read-Only trên hệ điều hành (`attrib -r`).
  2. Chuyển `is_locked: false` và `status: "DRAFT"` trong `article_status.json`.
  3. Ghi log sự kiện mở khóa vào [WORKLOG.md](file:///d:/Agents_Tools/05_WebsiteTTC/WORKLOG.md).
  4. Tiến hành sửa đổi theo đúng phạm vi đã chỉ định.
