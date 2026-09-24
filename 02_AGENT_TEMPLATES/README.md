# HỆ THỐNG MẪU SUBAGENT & HỢP ĐỒNG GIAO TIẾP (AGENT TEMPLATES & PROTOCOLS)
**Mã thư mục**: `02_AGENT_TEMPLATES/`
**Phiên bản**: 2.0 (Phase 2.5 Architecture Hardening)
**Mục đích**: Định nghĩa vai trò chuyên môn (Role Specification), System Prompts, Ranh giới trách nhiệm (Ownership Boundaries) và Hợp đồng giao tiếp máy đọc (Machine-Readable Contracts) cho đội ngũ 5 Subagents.

---

## 1. DANH SÁCH 5 SUBAGENT CHUYÊN TRÁCH

| Subagent | Vai trò chính | Tệp Đặc tả | Chuẩn kỹ năng áp dụng | Giao phẩm Canonical (Deliverables) |
|---|---|---|---|---|
| **1. Research Agent** | Khai thác tài liệu Tier 1/2, cấp Stable Source ID (`SRC-xxx`), tách bạch HTTP 200 vs Content/Claim verification, trích xuất verified locators | [research_agent.md](research_agent.md) | `SOURCE_TIER v1.0`, `IEEE_01 v1.1` | `evidence.json`, `evidence_dossier.md` |
| **2. Drafting Agent** | Soạn thảo theo 5 Canonical Types, công thức LaTeX SI, lập bản đồ luận điểm, gán số IEEE `[n]` theo thứ tự xuất hiện đầu tiên, **100% trích dẫn ở CUỐI CÂU** | [drafting_agent.md](drafting_agent.md) | `BLOG_TAXONOMY_CANONICAL v1.0`, `LATEX_FORMULA v1.0`, `IEEE_02 v1.1`, `IEEE_03 v1.1` | `draft_review_package.md`, `claim_source_map.json` |
| **3. Visual Agent** | Lập đặc tả ảnh & Prompt AI 5 tầng, kích thước chuẩn 808x500 px, khung HTML responsive chống méo ảnh (chỉ hoàn thiện sau Technical Gate PASS) | [visual_agent.md](visual_agent.md) | `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2` | `image_specifications.md`, file ảnh `.png` |
| **4. Review Agent** | Vận hành 2 Cổng Kiểm định độc lập (Technical Gate & Presentation Gate), quản trị vòng lặp hiệu chỉnh có cấu trúc (tối đa 3 vòng lặp) | [review_agent.md](review_agent.md) | `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1`, `IEEE_04 v1.1` | `technical_audit_report.md`, `audit.json`, `revision_request.json` |
| **5. Publisher Agent** | Kỹ sư Đóng gói Ấn phẩm (Packaging Agent), chuyển hóa sang HTML CKEditor 3.6.6.2 sạch 100% Inline CSS, tính mã băm SHA-256, lập bản kê phát hành | [publisher_agent.md](publisher_agent.md) | `MASTER_STYLE v1.0`, `IEEE_03 v1.1`, `ARTICLE_LIFECYCLE_PROTOCOL` | `bai-viet-[slug]-ckeditor.html`, `article_manifest.json`, `article_status.json` |

---

## 2. QUY TRÌNH PHỐI HỢP 2 CỔNG KIỂM ĐỊNH (TWO-GATE PRODUCTION PIPELINE)

```text
               [Đề tài từ Kỹ sư trưởng qua Chat Antigravity]
                                     │
                                     ▼
Stage 1: RESEARCH AGENT ──> [evidence.json] & [evidence_dossier.md]
                                     │ (Stable Source IDs: SRC-xxx, HTTP 200, Locators)
                                     ▼
Stage 2: DRAFTING AGENT ──> [draft_review_package.md] & [claim_source_map.json]
                                     │ (5 Canonical Types, LaTeX SI, 100% Citation Cuối câu)
                                     ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG 1: TECHNICAL REVIEW GATE (Review Agent - Supreme Gatekeeper)       │
│ Thẩm định Claim accuracy, Citation mapping, Locators, Formula, Logic   │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ PASS (TECH_APPROVED)
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
Stage 3: VISUAL AGENT                     Stage 4: PUBLISHER / PACKAGING AGENT
         │ (Finalize prompts & assets)             │ (100% Inline CSS HTML CKEditor)
         ▼                                         │ (Tính Content SHA-256 & Manifest)
   [image_specifications.md]                       ▼
         │                               [bai-viet-[slug]-ckeditor.html]
         └───────────────────────────────────┬─> [article_manifest.json]
                                             │
                                             ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG 2: PRESENTATION & RESPONSIVE REVIEW GATE (Review Agent)           │
│ Thẩm định Hiển thị Song song: Laptop (>=1200px) & Mobile (360-480px)   │
│ Kiểm tra Chống méo ảnh, Cuộn bảng min-width, Bẻ dòng URL, Output Clean │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ PASS
                                     ▼
Stage 5: HUMAN REVIEW & MANUAL CMS PUBLISHING
         ├── Kỹ sư trưởng nghiệm thu toàn diện bài viết
         ├── Kích hoạt cơ chế khóa 3 lớp (article_status.json LOCKED, attrib +r)
         └── Kỹ sư trưởng tự tay copy mã HTML và đăng tải lên CMS website
```

---

## 3. THƯ MỤC HỢP ĐỒNG GIAO TIẾP MÁY ĐỌC (CONTRACTS/)

Chi tiết xem tại [`02_AGENT_TEMPLATES/contracts/README.md`](contracts/README.md):
- [`contracts/article_brief.schema.json`](contracts/article_brief.schema.json)
- [`contracts/evidence.schema.json`](contracts/evidence.schema.json)
- [`contracts/claim_source_map.schema.json`](contracts/claim_source_map.schema.json)
- [`contracts/audit.schema.json`](contracts/audit.schema.json)
- [`contracts/revision_request.schema.json`](contracts/revision_request.schema.json)
- [`contracts/article_manifest.schema.json`](contracts/article_manifest.schema.json)

---

## 4. NGUYÊN TẮC BẤT DI BẤT DỊCH (CORE PRINCIPLES)

1. **Đơn chủ sở hữu (Single Ownership)**: Không có 2 Agent cùng là chủ sở hữu ghi của một tệp giao phẩm.
2. **Không tự ý xuất bản CMS**: Agent chỉ đóng gói giao phẩm hoàn thiện. Quyền xuất bản công khai lên CMS thuộc về Kỹ sư trưởng.
3. **Tiêu chuẩn là Bất biến (Skills are Read-Only)**: Toàn bộ thư mục `00_SKILL/` là chỉ đọc đối với Agent khi thực hiện nhiệm vụ sản xuất bài viết. Chỉ có tác vụ Kiến trúc/Bảo trì mới được cập nhật tiêu chuẩn.
4. **Vòng lặp hiệu chỉnh có cấu trúc**: Phải sử dụng `revision_request.json`, giới hạn đúng phạm vi lỗi, tối đa 3 vòng lặp trước khi chuyển cho con người can thiệp.
