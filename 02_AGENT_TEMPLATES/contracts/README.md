# MACHINE-READABLE CONTRACTS (INTER-AGENT SCHEMAS)
**Mã thư mục**: `02_AGENT_TEMPLATES/contracts/`
**Phiên bản**: 1.0 (Phase 2.5 Architecture Hardening)
**Mục đích**: Chuẩn hóa giao diện dữ liệu máy đọc (Machine-Readable Artifacts) trao đổi giữa 5 Subagents, đảm bảo tính chặt chẽ, dễ kiểm định và không phụ thuộc vào văn bản tự do.

---

## DANH MỤC CÁC SCHEMA CHUẨN

| Tệp Schema | Subagent Tạo Lập (Owner) | Subagent Tiêu Thụ (Consumer) | Mục Đích Sử Dụng |
|---|---|---|---|
| [`article_brief.schema.json`](article_brief.schema.json) | Orchestrator / Lead Engineer | Research, Drafting | Khởi tạo đề tài bài viết với `blog_type` chuẩn (1 trong 5 loại canonical: `BLOG-T01`..`T05`). |
| [`evidence.schema.json`](evidence.schema.json) | **Research Agent** | Drafting, Review | Chứa danh mục nguồn thẩm định với **Stable Source ID (`SRC-001`, `SRC-002`, ...)**, trạng thái URL, locator và supported claims. |
| [`claim_source_map.schema.json`](claim_source_map.schema.json) | **Drafting Agent** | Review, Publisher | Liên kết từng luận điểm kỹ thuật (`CLM-001`) với `SRC-xxx`, xác nhận locator và gán số thứ tự trích dẫn IEEE `[n]` theo thứ tự xuất hiện cuối cùng trong bài. |
| [`audit.schema.json`](audit.schema.json) | **Review Agent** | Drafting, Visual, Publisher, Human | Báo cáo kiểm định độc lập cho 2 cửa ải: **Technical Review Gate** và **Presentation & Responsive Review Gate**. |
| [`revision_request.schema.json`](revision_request.schema.json) | **Review Agent** | Assigned Agent (Research/Drafting/Visual/Publisher) | Danh sách yêu cầu hiệu chỉnh có cấu trúc, giới hạn phạm vi sửa đổi (scope-limited, cấm viết lại toàn bài), tối đa 3 vòng lặp tự động trước khi chuyển cho con người. |
| [`article_manifest.schema.json`](article_manifest.schema.json) | **Publisher / Packaging Agent** | Review, Human Approver | Bản kê khai đóng gói phát hành gồm đường dẫn HTML, mã băm toàn vẹn SHA-256, danh mục hình ảnh và hướng dẫn đăng tải thủ công lên CMS. |

---

## NGUYÊN TẮC QUẢN TRỊ CONTRACT

1. **Nguyên tắc Đơn Chủ Sở Hữu (Single Ownership)**: Mỗi artifact machine-readable chỉ có duy nhất 1 Agent được quyền tạo và ghi (Write Owner). Các Agent khác chỉ có quyền đọc (Read-Only).
2. **Song hành Markdown & JSON**:
   - Tệp `.json` (theo schema) dùng cho máy đọc, kiểm toán tự động và chuyển giao trạng thái.
   - Tệp `.md` dùng cho con người (Kỹ sư trưởng) đọc, phê duyệt và phản biện trực quan.
3. **Phân tách Rõ Ràng**:
   - `access_status: "OK"` (HTTP 200) **KHÔNG ĐƯỢC** đồng nhất với việc nội dung claim hay locator đã được kiểm chứng.
   - Bắt buộc kiểm tra `content_identity_verified`, `claim_verified` và `locator_verified`.
