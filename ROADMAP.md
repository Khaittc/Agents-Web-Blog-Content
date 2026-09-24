# LỘ TRÌNH PHÁT TRIỂN HỆ THỐNG (ROADMAP)
**Dự án**: Hệ thống Tự động hóa Đa Agent Sản xuất Nội dung Kỹ thuật (Real Group / TTC)
**Mục tiêu**: Tự động hóa khép kín từ nghiên cứu tài liệu, thẩm định kỹ thuật, tạo hình ảnh đến xuất bản bài viết lên website `real-group.org` (CKEditor 3.6.6.2).

---

## 1. Tổng quan Trạng thái Hiện tại (Current Status)

| Giai đoạn | Tên Giai đoạn | Trạng thái | Mốc hoàn thành dự kiến |
|---|---|---|---|
| **Phase 1** | Baseline & Standards Foundation | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 2** | Stress-test & Standards Expansion | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 2.5** | Multi-Agent Architecture Hardening | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 2.5.1** | Final Architecture Validation & CI Hardening | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 3** | Tooling Integration (MCP & Visual) | 🟡 **SẴN SÀNG KHỞI ĐỘNG** | Q4/2026 |
| **Phase 4** | Autonomous Pipeline & Human Publishing | ⚪ **DỰ KIẾN** | Q1/2027 |

> [!IMPORTANT]
> **Vị trí hiện tại của dự án**: Đã hoàn tất xuất sắc **Phase 2.5 & Phase 2.5.1 (Final Architecture Validation & CI Hardening)**.
> - Toàn bộ 5 Subagents đã được tái cấu trúc ranh giới trách nhiệm (Ownership Boundaries), thiết lập thư mục hợp đồng máy đọc `02_AGENT_TEMPLATES/contracts/`, phân tách 2 Cổng Kiểm định độc lập (Technical Review Gate & Presentation Gate), ban hành nguồn chuẩn duy nhất `BLOG_TAXONOMY_CANONICAL_v1.0.md`, quy chuẩn Stable Source ID (`SRC-xxx`), và cơ chế bảo vệ mã băm toàn vẹn SHA-256 (`approved_content_sha256`).
> - Thiết lập hệ thống CI tự động hóa (`.github/workflows/architecture-validation.yml`, `scripts/validate_architecture.py`, `scripts/verify_locked_articles.py`) khóa chặt cấu trúc, schemas và tính toàn vẹn của các bài viết đã duyệt.
> - Chuẩn hóa chính sách nguồn: Khuyến nghị 4–7 nguồn mặc định, mở ngoại lệ 1–3 nguồn thẩm quyền cao cho chủ đề hẹp (ADR-024) và tách bạch hoàn toàn ngữ nghĩa kiểm chứng URL (`canonical_url`, `retrieval_url`, `access_status`) (ADR-025).
> - Khẳng định nguyên tắc bất biến: **Subagents chỉ đóng gói giao phẩm xuất bản sẵn sàng (Packaging); Con người (Kỹ sư trưởng) là người phê duyệt và tự tay đăng tải lên CMS**.
> - **Phase 2.5 chính thức KHÓA ĐÓNG HOÀN TOÀN (FULLY CLOSED)**. Hệ thống sẵn sàng tuyệt đối để bước vào **Phase 3 (Tooling Integration)**.

---

## 2. Chi tiết Các Giai đoạn Phát triển

### Giai đoạn 1: Thiết lập Nền tảng Chuẩn hóa & Khóa Baseline (Phase 1)
*Trạng thái*: ✅ **ĐÃ HOÀN THÀNH** (Tháng 09/2026)
*Mục tiêu*: Xây dựng bộ quy chuẩn cốt lõi và kiểm nghiệm bằng một bài viết thực tế.
- [x] Xây dựng [BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md) phân định 5 loại bài (`BLOG-T01` đến `BLOG-T05`), logic luồng kỹ thuật và bắt buộc tối thiểu 1 hình content.
- [x] Xây dựng [IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md) (Bộ 4 Sub-Skills: IEEE-01 Nhận diện & URL check 200, IEEE-02 Trích dẫn nội văn, IEEE-03 Đặt tên & Link bấm được CKEditor, IEEE-04 Biên bản kiểm duyệt 6 cửa ải).
- [x] Xây dựng [LATEX_FORMULA_SKILL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/LATEX_FORMULA_SKILL_v1.0.md) chuẩn hóa công thức toán học và đơn vị SI.
- [x] Xây dựng [REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md) chuẩn hóa HTML CKEditor inline, semantic callouts và khoảng trắng.
- [x] Tạo bài viết kiểm nghiệm thực tế đầu tiên làm baseline: [Cách phát hiện động cơ điện đang chạy non tải trong nhà máy](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_01_Dong_co_non_tai/bai-viet-dong-co-chay-non-tai-ckeditor.html) — dạng `BLOG-T02` (✅ **APPROVED / LOCKED**).
- [x] Tái cấu trúc không gian làm việc (`00_SKILL`, `01_KNOWLEDGE_BASE`, `02_AGENT_TEMPLATES`, `03_Articles`).

---

### Giai đoạn 2: Thử nghiệm Chéo & Hoàn thiện Quy chuẩn Còn thiếu (Phase 2)
*Trạng thái*: ✅ **ĐÃ HOÀN THÀNH** (Tháng 09/2026)
*Mục tiêu*: Bổ sung các văn bản quy chuẩn phụ trợ và viết thêm 2 bài mẫu để kiểm tra tính linh hoạt của hệ thống.

- [x] **Bổ sung các Standard phụ trợ (trong `00_SKILL/`) — ĐÃ HOÀN THÀNH**:
  - [x] [SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md): Phân cấp mức độ tin cậy của tài liệu (Tier 1: Standards, Tier 2: Handbooks, Tier 3: Articles) và giải quyết xung đột dữ liệu.
  - [x] [TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md): Bộ tiêu chí và ma trận chấm điểm kiểm duyệt kỹ thuật (Citation Audit, Formula Audit, Semantic Check, và Dual-Viewport Responsive Audit Laptop & Mobile theo ADR-017).
  - [x] [IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md): Chuẩn đặc tả ảnh `image_specifications.md`, prompt AI 5 tầng, thư viện archetype và khung placeholder HTML chống méo ảnh trên mobile (ADR-010, ADR-016).
- [x] **Thực hiện 2 bài viết Stress-test (trong `03_Articles/`) — ĐÃ HOÀN THÀNH**:
  - [x] [BLOG_02_He_so_cong_suat_va_Song_hai](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_02_He_so_cong_suat_va_Song_hai/): Dạng `BLOG-T01` (Technical Explanation) — *Hệ số công suất cos phi và sóng hài bậc cao trong nhà máy* (✅ **ĐÃ NGHIỆM THU & KHÓA BÀI VIẾT: APPROVED / LOCKED**).
  - [x] [BLOG_03_Chan_doan_qua_dong_bien_tan](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/): Dạng `BLOG-T03` (Troubleshooting) — *Quy trình 4 bước chẩn đoán và khắc phục lỗi quá dòng (Overcurrent) trên biến tần công nghiệp* (✅ **ĐÃ NGHIỆM THU & KHÓA BÀI VIẾT: APPROVED / LOCKED**).
- [x] **Nâng cấp tài liệu `00_SKILL`**: Hoàn tất nâng cấp toàn bộ hệ thống kỹ năng lên phiên bản chuẩn hóa ổn định:
  - `IEEE Modular Suite v2.0` (`IEEE_01 v1.1`, `IEEE_02 v1.1`, `IEEE_03 v1.1`, `IEEE_04 v1.1`).
  - `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2`.
  - `TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1`.

---

### Giai đoạn 2.5: Củng Cố Kiến Trúc & Hợp Đồng Đa Agent (Phase 2.5 — Architecture Hardening)
*Trạng thái*: ✅ **ĐÃ HOÀN THÀNH** (Tháng 09/2026)
*Mục tiêu*: Khóa chặt các lỗ hổng kiến trúc, chuẩn hóa giao diện máy đọc (JSON schemas), tách bạch 2 cổng kiểm định và xác lập ranh giới trách nhiệm đơn quyền trước khi tích hợp công cụ ngoài.

- [x] **Canonical BLOG Taxonomy thống nhất**: Ban hành [BLOG_TAXONOMY_CANONICAL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/BLOG_TAXONOMY_CANONICAL_v1.0.md) làm nguồn chuẩn duy nhất cho 5 thể loại (`BLOG-T01` đến `BLOG-T05`); sửa mọi mapping sai lệch trong tài liệu.
- [x] **Stable Source IDs**: Research Agent chuyển đổi 100% sang mã định danh ổn định `SRC-001`, `SRC-002`,... Tuyệt đối không cấp số IEEE `[n]` ở khâu nghiên cứu.
- [x] **Machine-readable Contracts**: Thiết lập thư mục `02_AGENT_TEMPLATES/contracts/` với 6 JSON Schemas: `article_brief`, `evidence`, `claim_source_map`, `audit`, `revision_request`, `article_manifest`.
- [x] **Claim-Source Mapping**: Drafting Agent xuất tệp canonical `claim_source_map.json` mapping từng claim với `SRC-xxx` và gán số IEEE theo thứ tự xuất hiện đầu tiên.
- [x] **Structured Revision Loop**: Review Agent phát hành `revision_request.json` giới hạn đúng phạm vi lỗi, tối đa 3 vòng lặp tự động trước khi chuyển cho con người.
- [x] **Technical Review Gate (Cổng 1)**: Tách bạch cổng kiểm định chuyên môn kỹ thuật, toán học và trích dẫn cuối câu (chạy ngay sau Drafting).
- [x] **Presentation & Responsive Review Gate (Cổng 2)**: Tách bạch cổng kiểm định hiển thị song song Laptop & Mobile (chạy sau khi Packaging Agent đóng gói HTML).
- [x] **Human-only Final Publishing**: Định vị Publisher Agent là Packaging Agent (chỉ đóng gói tệp); quyền phê duyệt và đăng bài lên CMS thuộc về Kỹ sư trưởng.
- [x] **Integrity Hash**: Bổ sung `approved_content_sha256` và `approved_commit_sha` vào `article_status.json` để kiểm tra toàn vẹn tự động (`INTEGRITY_WARNING` nếu sai lệch).
- [x] **Agent Ownership Boundaries**: Cập nhật trọn bộ 5 Agent Templates với các mục INPUT, OUTPUT, READ-ONLY, WRITABLE, FAIL CONDITIONS, HANDOFF CONDITIONS rõ ràng.
- [x] **Documentation Consistency Pass**: Rà soát và cập nhật đồng bộ toàn bộ tài liệu dự án, bảo vệ nguyên vẹn các bài viết đã duyệt.

---

### Giai đoạn 2.5.1: Kiểm Tra Toàn Diện & Tự Động Hóa CI Kiến Trúc (Phase 2.5.1 — Final Architecture Validation & CI Hardening)
*Trạng thái*: ✅ **ĐÃ HOÀN THÀNH** (Tháng 09/2026)
*Mục tiêu*: Thiết lập hệ thống GitHub Actions CI kiểm tra tự động kiến trúc, kiểm tra toàn vẹn bài viết đã khóa bằng SHA-256, chuẩn hóa chính sách ngoại lệ nguồn thẩm quyền cao và ngữ nghĩa kiểm chứng URL trước khi mở Phase 3.

- [x] **Architecture CI Workflow**: Thiết lập `.github/workflows/architecture-validation.yml` chạy trên push và PR vào nhánh `main`.
- [x] **Architecture Validation Script**: `scripts/validate_architecture.py` kiểm định JSON Schemas, Canonical Taxonomy, Stable Source IDs, Hợp đồng bắt buộc, Human-only Publishing và Two-Gate Pipeline.
- [x] **Locked Content Integrity Script**: `scripts/verify_locked_articles.py` kiểm chứng toàn vẹn SHA-256 của toàn bộ bài viết đã phê duyệt (`BLOG_01`, `BLOG_02`, `BLOG_03`).
- [x] **Source Policy & Authoritative Exception (ADR-024)**: Mặc định 4–7 nguồn ($\ge 70\%$ Tier 1+2); cho phép ngoại lệ 1–3 nguồn thẩm quyền cao cho chủ đề hẹp với cờ máy đọc `source_policy_exception` và cửa ải phê duyệt của Review Agent.
- [x] **URL Verification Semantics (ADR-025)**: Chuẩn hóa `access_status` (7 trạng thái), phân tách `canonical_url` và `retrieval_url`, chính sách PDF trực tiếp, và tách bạch 4 cấp độ kiểm chứng độc lập.
- [x] **Two-Gate Pipeline & Human-Only Publishing Consistency**: Đồng bộ hóa tuyệt đối tài liệu hoạt động, đảm bảo pipeline 2 cổng độc lập và nguyên tắc chỉ con người đăng bài lên CMS.

> [!NOTE]
> **Kết luận**: Toàn bộ tiêu chí nghiệm thu của Phase 2.5 và Phase 2.5.1 đã đạt 100% PASS. Phase 2.5 chính thức KHÓA ĐÓNG HOÀN TOÀN (FULLY CLOSED). Hệ thống sẵn sàng tuyệt đối để bước vào **Phase 3 (Tooling Integration)**.

---

### Giai đoạn 3: Định nghĩa Chuyên biệt Subagent & Tích hợp Công cụ (Phase 3)
*Trạng thái*: 🟡 **ĐANG THỰC HIỆN** (Khởi động Tháng 09/2026)
*Mục tiêu*: Chuyển đổi các quy chuẩn lý thuyết thành các Prompt và Hợp đồng giao tiếp tự động của 5 Subagents, tích hợp công cụ nghiên cứu thực địa (Live Research), tiến tới tự động hóa quy trình sản xuất nội dung kỹ thuật.

- [x] **Định nghĩa 5 Subagents chuyên trách (trong `02_AGENT_TEMPLATES/`) — ĐÃ HOÀN THÀNH**:
  - [x] `research_agent.md` v3.0: System prompt, kế hoạch nghiên cứu `research_plan.json`, công cụ truy vấn Live Web, sàng lọc ứng viên `CAN-xxx`, Cổng tiếp nhận nguồn, trích xuất bằng chứng hạt nhân `EVD-xxx` và phân tích bất đồng kỹ thuật `CON-xxx`.
  - [x] `drafting_agent.md`: System prompt, cấu trúc `BLOG-T01`..`T05`, công thức LaTeX SI, trích dẫn bắt buộc ở cuối câu theo `IEEE-02 v1.1`.
  - [x] `visual_agent.md`: System prompt, Prompt AI 5 tầng, kích thước 808x500 px, HTML placeholder chống méo dọc theo `IMAGE_SPEC v1.2`.
  - [x] `review_agent.md`: System prompt, 4 trụ cột kiểm duyệt độc lập, Gate 5 vị trí cuối câu, kiểm tra responsive song song Laptop & Mobile theo `REVIEW_PROTOCOL v1.1` (ADR-017).
  - [x] `publisher_agent.md`: System prompt, đóng gói HTML CKEditor sạch, link `<a>` có `word-break: break-all;`, bảng `min-width`, quản lý `article_status.json` theo `ADR-005` và `ADR-016`.

- [x] **Phase 3.0 — Live Research Foundation v1 (Checkpoint: `live-research-foundation-v1`) — ĐÃ HOÀN THÀNH**:
  - [x] **Hợp đồng Kế hoạch Nghiên cứu (`research_plan.schema.json`)**: Chuẩn hóa cấu trúc câu hỏi nghiên cứu `RQ-xxx` (ưu tiên `HIGH`/`MEDIUM`/`LOW`, trạng thái phân giải `OPEN`, `SEARCHING`, `PARTIALLY_ANSWERED`, `ANSWERED`, `BLOCKED`). Toàn bộ câu hỏi `HIGH` bắt buộc giải quyết trước khi hoàn tất kế hoạch.
  - [x] **Mô hình Ứng viên Nguồn & Cổng Tiếp nhận (`03_TOOLING/live_research/`)**: Đặc tả hợp đồng nhà cung cấp (`provider_contract.md`), quy trình đánh mã `CAN-xxx`, 8 tiêu chí Acceptance Gate loại trừ nguồn rác/link chết/paywall/quảng cáo, và nguyên tắc bất di bất dịch **No Snippet Evidence Rule**.
  - [x] **Hợp đồng Bằng chứng Hạt nhân & Phân tích Bất đồng (`evidence.schema.json`)**: Hỗ trợ đồng bộ `accepted_from_candidate_id`, `research_question_ids`, mảng bằng chứng `evidences` (`EVD-xxx`), và mảng bất đồng kỹ thuật `conflicts` (`CON-xxx`) giải quyết sự khác biệt thông số giữa các nhà sản xuất OEM.
  - [x] **Thử nghiệm Thực địa Thẩm định Nghiên cứu (Pilot `BLOG_04_VFD_vs_Soft_Starter`)**:
    - Thực thi nghiên cứu trực tiếp cho chủ đề: *"VFD và Soft Starter: Khác nhau về nguyên lý, dòng khởi động, điều khiển tốc độ và phạm vi ứng dụng"* (Thể loại `BLOG-T04`).
    - Lập `article_brief.json`, `research_plan.json` (7 RQs, 5 HIGH RQs đều đạt `ANSWERED`), `research_log.json` (ghi nhận 7 truy vấn và 7 ứng viên).
    - Tiếp nhận 4 nguồn kỹ thuật chuẩn mực (1 Tier 1, 3 Tier 2): ABB Softstarter Handbook (`SRC-001`), Rockwell Automation White Paper (`SRC-002`), Schneider Electric Guide (`SRC-003`), IEEE Std 519-2022 (`SRC-004`).
    - Trích xuất 12 bằng chứng hạt nhân định lượng (`EVD-001` đến `EVD-012`) và giải quyết 2 bất đồng kỹ thuật (`CON-001`, `CON-002`).
    - Xuất bản hồ sơ máy đọc `evidence.json` (100% hợp lệ schema) và báo cáo kỹ thuật `evidence_dossier.md`.
    - **Dừng kiểm soát tại Cửa ải Nghiên cứu**: Không viết bản thảo, không sinh ảnh, không tạo HTML, giữ nguyên tính toàn vẹn tuyệt đối của các bài viết đã khóa (`BLOG_01`, `BLOG_02`, `BLOG_03`).

- [ ] **Kế hoạch Tích hợp Công cụ Tiếp theo (Phase 3.1+)**:
  - [ ] **Tích hợp NotebookLM MCP** (*Trạng thái*: `DEFERRED` — Tạm hoãn đến khi nền tảng Live Research và Drafting Agent đồng bộ hoàn toàn).
  - [ ] **Tích hợp Image Generation Tool** (*Trạng thái*: `DEFERRED` — Tạm hoãn đến khi mở cổng Visual Agent).
  - [ ] **Tạo template tự động hóa kiểm tra HTML CKEditor**.


---

### Giai đoạn 4: Vận hành Tự động hóa Khép kín & Quản trị Vòng đời (End-to-End Pipeline) (Phase 4)
*Trạng thái*: ⚪ **DỰ KIẾN**
*Mục tiêu*: Thiết lập pipeline một chạm từ Chủ đề bài viết tới Giao phẩm hoàn chỉnh, tích hợp nền tảng ra đề bài và cơ chế phê duyệt/khóa bài viết.

- [ ] **Nền tảng Ra đề bài & Vận hành (Execution Platforms)**:
  - [ ] Vận hành trực tiếp trên Google Antigravity: Chuẩn hóa bộ lệnh prompt và slash commands (`/goal`, `/boost`).
  - [ ] Mở rộng giao diện Web Dashboard (tùy chọn): Sử dụng Google Antigravity Python SDK xây dựng UI nội bộ để nhập đề bài, preview HTML và bấm nút duyệt.
- [ ] **Quản trị Vòng đời & Phê duyệt (Approval & State Machine)**:
  - [ ] Chuẩn hóa quy trình 4 trạng thái: `DRAFT` → `IN_REVIEW` → `APPROVED / LOCKED` → `PUBLISHED`.
  - [ ] Tích hợp file `article_status.json` tự động cập nhật hash và timestamp phê duyệt.
- [ ] **Cơ chế Khóa 3 Lớp (3-Layer Protection)**:
  - [ ] Khóa trạng thái máy đọc (`is_locked: true`).
  - [ ] Guardrail trong Prompt Agent (từ chối sửa bài APPROVED trừ khi có lệnh `UNLOCK`).
  - [ ] Khóa file ở tầng hệ điều hành (OS Read-Only flag).
- [ ] **Orchestration Workflow**: Phối hợp luồng làm việc tự động giữa các agent thông qua subagent invocation.
- [ ] **Đóng gói xuất bản đa kênh**: Xuất bản đồng thời HTML cho CKEditor, bản lưu trữ PDF/DOCX có định dạng chuyên nghiệp.
- [ ] **Tối ưu SEO tự động**: Kiểm tra mật độ từ khóa kỹ thuật, thẻ meta description và readability score.

---


## 3. Tiêu chí Đánh giá Thành công (Success Metrics)
1. **Độ chính xác kỹ thuật 100%**: Mọi thông số, công thức toán và trích dẫn đều có nguồn gốc truy nguyên rõ ràng (No hallucinations).
2. **Độ sạch của HTML**: Mã xuất bản tương thích 100% với CKEditor 3.6.6.2, không rác styling, không chứa ghi chú Agent nội bộ.
3. **Tính nhất quán hình ảnh**: Mọi bài viết đều có kích thước Featured Image 808x500 px và biểu đồ kỹ thuật cùng phong cách nhận diện Real Group.
4. **Tiết kiệm thời gian kỹ sư**: Giảm 80% thời gian biên soạn và định dạng thủ công của kỹ sư chuyên môn.
