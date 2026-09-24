# HỆ THỐNG MẪU AGENT (AGENT TEMPLATES & PROTOCOLS)

Thư mục này lưu trữ các bản định nghĩa vai trò (Role Specification), System Prompts và Hợp đồng giao tiếp (Interface Contracts) của đội ngũ 5 AI Agent chuyên trách sản xuất bài viết kỹ thuật.

---

## 1. Danh sách 5 Role Agent Chuyên trách

| Agent | Vai trò chính | Tệp Đặc tả Template | Chuẩn kỹ năng áp dụng | Đầu ra chuẩn hóa (Deliverable) |
|---|---|---|---|---|
| **1. Research Agent** | Khai thác tài liệu, phân cấp Tier, bắt buộc kiểm tra URL sống (HTTP 200), trích xuất verified locator, Deep-link trực tiếp (ADR-015) | [research_agent.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/research_agent.md) | `IEEE_01 v1.1`, `SOURCE_TIER v1.0` | `evidence_dossier.md` |
| **2. Drafting Agent** | Thiết kế logic bài 5 Archetypes, công thức toán LaTeX SI, **100% trích dẫn ở CUỐI CÂU (ADR-013)** | [drafting_agent.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/drafting_agent.md) | `BLOG_CONTENT_STRUCTURE v1.3`, `LATEX_FORMULA v1.0`, `IEEE_02 v1.1`, `IEEE_03 v1.1` | `draft_review_package.md` |
| **3. Visual Agent** | Thiết kế Prompt AI 5 tầng, ảnh đại diện 808x500, khung HTML placeholder chống méo dọc mobile (ADR-010, ADR-016) | [visual_agent.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/visual_agent.md) | `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2` | `image_specifications.md` |
| **4. Review Agent** | Phản biện 4 trụ cột độc lập, Gate 5 trích dẫn cuối câu, **Cửa ải Responsive Song song Laptop & Mobile (ADR-017)** | [review_agent.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/review_agent.md) | `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1`, `IEEE_04 v1.1` | `technical_audit_report.md` |
| **5. Publisher Agent** | Đóng gói 100% Inline CSS cho CKEditor 3.6.6.2, link `<a>` ngắt dòng `word-break: break-all;`, bảng `min-width`, quản lý khóa bài 3 lớp (ADR-005, ADR-016) | [publisher_agent.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/publisher_agent.md) | `MASTER_STYLE v1.0`, `IEEE_03 v1.1`, `ARTICLE_LIFECYCLE_PROTOCOL` | `bai-viet-[slug]-ckeditor.html` & `article_status.json` |

---

## 2. Quy trình Phối hợp 5 Agent (5-Stage Autonomous Pipeline)

```text
[Đề tài từ Kỹ sư trưởng]
       │
       ▼
1. RESEARCH AGENT ──> [evidence_dossier.md] (HTTP 200, Deep Links, Verified Locators)
       │
       ▼
2. DRAFTING AGENT ──> [draft_review_package.md] (5 Archetypes, LaTeX SI, 100% Citation Cuối câu)
       │
       ├─────────────────────────────────┐
       ▼                                 ▼
3. VISUAL AGENT                   4. REVIEW AGENT (Supreme Gatekeeper)
       │ (Prompt AI 5 tầng, 808x500)     │ (4 Trụ cột + Cửa ải Responsive Laptop & Mobile ADR-017)
       ▼                                 ▼
   [image_specifications.md] ──> [technical_audit_report.md]
                                         │
                                         ▼ (Chỉ khi có chữ ký PASS)
                                  5. PUBLISHER AGENT
                                         │ (100% Inline CSS CKEditor, Khóa an toàn ADR-005)
                                         ▼
                             [bai-viet-[slug]-ckeditor.html]
                             [article_status.json (APPROVED/LOCKED)]
```

---

## 3. Nguyên tắc Giao tiếp giữa các Agent (Agent Interface Contracts)

1. **Giao tiếp qua File Artifacts**: Các Agent trao đổi thông tin bằng các file trung gian chuẩn hóa trong thư mục bài viết tương ứng (tại `03_Articles/[Tên_Bài]/`), không truyền miệng hoặc tóm tắt thiếu sót.
2. **Quy định Nhận diện Loại Nguồn (Source Classification Contract)**: Research Agent bắt buộc phải xác định chính xác bản chất loại tài liệu (`STANDARD`, `MANUAL`, `JOURNAL_PAPER`, `CONF_PAPER`, `BLOG_POST`, `WEB_ARTICLE`, `TECH_REPORT`, `BOOK`, `DATASHEET`) trong `evidence_dossier.md`. Drafting Agent và Publisher Agent chỉ được áp dụng đúng khuôn mẫu IEEE tương ứng cho loại đó.
3. **Không vượt cấp**: Drafting Agent không tự bịa nguồn khi chưa có `evidence_dossier.md` từ Research Agent. Publisher Agent không xuất HTML nếu chưa có chữ ký duyệt (*PASS*) trong `technical_audit_report.md` của Review Agent.
4. **Giữ sạch mã nguồn công khai**: Mọi thông tin trao đổi, audit checklist, prompt ảnh phải nằm trong file review nội bộ, tuyệt đối không xuất vào file HTML công khai dùng cho website.
5. **Nền tảng vận hành chính thức**: Toàn bộ luồng phối hợp được ra lệnh và kiểm soát trực tiếp tại khung chat của Google Antigravity theo [ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md).

