# ⚡ Autonomous Multi-Agent Technical Blog Production System
### Hệ Thống AI Đa Tác Tử Sản Xuất Nội Dung Kỹ Thuật Công Nghiệp Chuẩn Quốc Tế (IEEE & Real Group)

[![Platform: Google Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4?logo=google&logoColor=white)](https://github.com/Khaittc/Agents-Web-Blog-Content)
[![CI: Architecture Validated](https://img.shields.io/badge/CI-Architecture%20Validated-brightgreen?logo=githubactions&logoColor=white)](.github/workflows/architecture-validation.yml)
[![Citation: IEEE Suite v2.0](https://img.shields.io/badge/Citation-IEEE%20Suite%20v2.0-00629B?logo=ieee&logoColor=white)](00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md)
[![Responsive: Laptop & Mobile](https://img.shields.io/badge/Responsive-Laptop%20%26%20Mobile%20Verified-brightgreen)](00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md)
[![CMS: CKEditor 3.6.6.2 Ready](https://img.shields.io/badge/CMS-CKEditor%203.6.6.2%20Ready-orange)](00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md)
[![Phase: 3 Ready](https://img.shields.io/badge/Roadmap-Phase%203%20Ready-blue)](ROADMAP.md)
[![License: Proprietary Real Group](https://img.shields.io/badge/License-Real%20Group%20TTC-red)](https://www.real-group.org)

---

## 📌 1. TỔNG QUAN DỰ ÁN (PROJECT OVERVIEW)

**Agents-Web-Blog-Content** là hệ thống AI đa tác tử (Multi-Agent System) tự động hóa toàn diện quy trình sản xuất nội dung bài viết kỹ thuật chuyên sâu trong lĩnh vực **Tự động hóa công nghiệp (Industrial Automation)** và **Kỹ thuật Điện tử - Điện công nghiệp (Electrical & Drive Systems)**.

Hệ thống được phát triển dành riêng cho website kỹ thuật công nghiệp [real-group.org](https://www.real-group.org), tích hợp bộ tiêu chuẩn học thuật quốc tế **IEEE Reference Citation**, hệ thống phân cấp nguồn tin cậy **Source-Tier Hierarchy** và cơ chế tương thích hiển thị đa thiết bị **Dual-Viewport Responsive (Laptop & Mobile)**.

### Mục Tiêu Cốt Lõi:
1. **Triệt tiêu hoàn toàn ảo giác (Zero Hallucination)**: 100% dữ liệu kỹ thuật, bảng tra, công thức toán và quy trình xử lý lỗi đều được xác thực từ tài liệu chuẩn quốc tế (IEC, IEEE, ISO) và tài liệu kỹ thuật gốc từ nhà sản xuất (ABB, Siemens, Schneider Electric, Danfoss, Mitsubishi).
2. **Chuẩn hóa Học thuật Khắt khe**: Tự động tra cứu số trang (`p.`, `pp.`), số bảng (`Table`), số mục (`Section`) và kiểm tra tính sống động của URL (`HTTP 200 OK`, Deep-link / Direct PDF).
3. **Trải nghiệm Đa thiết bị Tối ưu**: Đảm bảo toàn bộ bảng kỹ thuật, hình ảnh minh họa, công thức LaTeX và liên kết tham khảo hiển thị hoàn hảo, không tràn màn hình, không méo tỷ lệ ảnh trên cả Laptop (1366px - 1920px) và Điện thoại di động (375px - 430px).
4. **Tương thích Tuyệt đối với CMS CKEditor 3.6.6.2**: Xuất bản mã nguồn HTML sạch, sử dụng inline styling an toàn, không chứa class lạ hoặc style xung đột với theme website.

---

## 🏗️ 2. KIẾN TRÚC 5 SUBAGENT VỚI 2 CỔNG KIỂM ĐỊNH (TWO-GATE MULTI-AGENT PIPELINE)

Hệ thống vận hành theo quy trình phân quyền chuyên biệt với 2 cổng kiểm định độc lập (Technical Gate & Presentation Gate) nhằm đảm bảo cả chiều sâu kỹ thuật lẫn trải nghiệm hiển thị trước khi chuyển giao cho con người nghiệm thu:

```mermaid
flowchart TD
    User([Kỹ sư trưởng / Đề bài kỹ thuật]) --> Research[1. Research Agent<br>Kỹ sư Nghiên cứu Chuyên sâu]

    Research -->|evidence.json & dossier<br>Stable Source IDs: SRC-xxx, Verified Locators| Drafting[2. Drafting Agent<br>Kỹ sư Soạn thảo Chuyên môn]

    Drafting -->|draft_review_package.md<br>claim_source_map.json, Trích dẫn cuối câu| TechGate{CỔNG 1: TECHNICAL REVIEW GATE<br>Review Agent}

    TechGate -- REVISION_REQUIRED<br>(revision_request.json) --> Drafting
    TechGate -- PASS (TECH_APPROVED) --> Visual[3. Visual Agent<br>Kỹ sư Đồ họa & AI Prompt]

    Visual -->|image_specifications.md<br>Prompt AI 5 tầng, 808x500px, Assets| Publisher[4. Packaging Agent (Publisher)<br>Kỹ sư Đóng gói Ấn phẩm]

    Publisher -->|bai-viet-ckeditor.html<br>article_manifest.json (SHA-256)| PresGate{CỔNG 2: PRESENTATION GATE<br>Review Agent}

    PresGate -- REVISION_REQUIRED --> Publisher
    PresGate -- PASS (IN_REVIEW) --> HumanReview([5. Kỹ sư trưởng Nghiệm thu<br>Khóa 3 lớp: article_status.json LOCKED])

    HumanReview --> ManualPublish([Đăng tải Thủ công lên CMS<br>real-group.org])
```

### Chi Tiết Nhiệm Vụ 5 Subagents ([02_AGENT_TEMPLATES/](02_AGENT_TEMPLATES/)):
* 🔬 [**Research Agent**](02_AGENT_TEMPLATES/research_agent.md): Thu thập tài liệu Tier 1/2, gán Stable Source ID (`SRC-xxx`), tách bạch `HTTP 200` và xác thực nội dung, xuất song song `evidence.json` và `evidence_dossier.md`.
* ✍️ [**Drafting Agent**](02_AGENT_TEMPLATES/drafting_agent.md): Biên soạn nội dung theo [Canonical Taxonomy](00_SKILL/BLOG_TAXONOMY_CANONICAL_v1.0.md), tích hợp công thức LaTeX SI, lập `claim_source_map.json`, gán số IEEE `[n]` theo thứ tự xuất hiện đầu tiên và tuân thủ nguyên tắc: **100% trích dẫn IEEE đặt ở CUỐI CÂU** (`IEEE_02 v1.1`).
* 🎨 [**Visual Agent**](02_AGENT_TEMPLATES/visual_agent.md): Thiết kế sơ đồ khối, lưu đồ thuật toán và sinh Prompt AI 5 tầng theo tỷ lệ chuẩn `808x500 px` (`IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md`). Chỉ hoàn thiện giao phẩm khi bản thảo đã đạt Cổng Kỹ thuật (TECH_APPROVED).
* 🛡️ [**Review Agent**](02_AGENT_TEMPLATES/review_agent.md): Vận hành **2 Cổng Kiểm định Tách bạch**: Cổng 1 (Kiểm định chuyên môn toán học, trích dẫn, fact-check) và Cổng 2 (Kiểm định hiển thị song song Laptop & Mobile theo ADR-017). Quản trị vòng lặp hiệu chỉnh có cấu trúc qua `revision_request.json` (tối đa 3 vòng lặp).
* 📦 [**Publisher Agent (Packaging Agent)**](02_AGENT_TEMPLATES/publisher_agent.md): Kỹ sư đóng gói mã HTML sạch 100% Inline CSS cho CKEditor 3.6.6.2, tính toán mã băm SHA-256 toàn vẹn, lập bản kê `article_manifest.json`. **Không tự ý xuất bản lên CMS** — con người là người duyệt và đăng tải thủ công cuối cùng.

---

## 🌟 3. CÁC QUY CHUẨN KỸ NĂNG CỐT LÕI (CORE SKILLS & STANDARDS)

Hệ thống được xây dựng trên nền tảng các tiêu chuẩn kỹ thuật nghiêm ngặt lưu trữ tại thư mục [00_SKILL/](00_SKILL/):

| Mã Quy Chuẩn | Phiên Bản | Tên Quy Chuẩn & Mô Tả | Điểm Nhấn Đột Phá |
|---|---|---|---|
| **BLOG_TAXONOMY** | `v1.0` | [BLOG_TAXONOMY_CANONICAL](00_SKILL/BLOG_TAXONOMY_CANONICAL_v1.0.md) | Nguồn chuẩn duy nhất (Single Source of Truth) chốt 5 thể loại bài viết (`BLOG-T01` đến `BLOG-T05`). |
| **BLOG_CONTENT** | `v1.3` | [BLOG_CONTENT_STRUCTURE_STANDARD](00_SKILL/BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md) | Cấu trúc chi tiết từng dạng bài kỹ thuật, bắt buộc tối thiểu 1 hình content kỹ thuật chuyên sâu. |
| **IEEE_SUITE** | `v2.0` | [IEEE_CITATION_REFERENCE_MASTER_SUITE](00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md) | Bộ tứ kỹ năng trích dẫn: `IEEE_01` (Nguồn & URL check 200), `IEEE_02` (Trích dẫn cuối câu), `IEEE_03` (Format link CKEditor), `IEEE_04` (6 Cửa ải Audit). |
| **SOURCE_TIER** | `v1.0` | [SOURCE_TIER_EVIDENCE_WORKFLOW](00_SKILL/SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md) | Phân tầng nguồn: Tier 1 (IEC, IEEE, OEM Manuals) > Tier 2 (Giáo trình) > Tier 3 (Cổng tin uy tín). Stable Source ID (`SRC-xxx`). |
| **IMAGE_SPEC** | `v1.2` | [IMAGE_SPECIFICATION_AND_PROMPT_SKILL](00_SKILL/IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md) | Cấu trúc Prompt AI 5 tầng, chuẩn kích thước Featured Image 808x500 px, HTML placeholder chống méo dọc mobile. |
| **LATEX_MATH** | `v1.0` | [LATEX_FORMULA_SKILL](00_SKILL/LATEX_FORMULA_SKILL_v1.0.md) | Chuẩn hóa công thức vật lý, toán điện tử, hệ đơn vị đo lường quốc tế SI và bảng biến số. |
| **MASTER_STYLE** | `v1.0` | [REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE](00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md) | Thiết kế giao diện HTML CKEditor 3.6.6.2, semantic callouts (Lưu ý, Cảnh báo), Typography công nghiệp. |
| **TECH_REVIEW** | `v1.1` | [TECHNICAL_REVIEW_AUDIT_PROTOCOL](00_SKILL/TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md) | Biên bản kiểm duyệt 2 cổng độc lập, tích hợp Cửa ải kiểm định hiển thị song song Laptop & Mobile (ADR-017). |

---

## 📱 4. TIÊU CHUẨN HIỂN THỊ ĐA THIẾT BỊ (DUAL-VIEWPORT RESPONSIVE)

Để phục vụ độc giả là kỹ sư, sinh viên và chuyên gia vận hành tra cứu trên cả máy tính xách tay và điện thoại thông minh tại nhà máy, hệ thống áp dụng tiêu chuẩn hiển thị khắt khe:

* 🖼️ **Hình ảnh & Sơ đồ**: Áp dụng container tỷ lệ vàng `max-width: 808px; width: 100%; aspect-ratio: 808 / 500; object-fit: contain;` đảm bảo ảnh hiển thị sắc nét, không bị co kéo, méo hình theo chiều dọc trên điện thoại.
* 📊 **Bảng Thông Số Kỹ Thuật**: Đóng gói trong thẻ bọc chống tràn `overflow-x: auto; -webkit-overflow-scrolling: touch;` với thuộc tính bảng `min-width: 600px;` giúp xem trọn vẹn dữ liệu nhiều cột trên mobile bằng thao tác vuốt ngang mượt mà.
* 🔗 **Đường Dẫn Tài Liệu Tham Khảo (URLs)**: Toàn bộ liên kết dài được cấu hình thuộc tính `word-break: break-all; overflow-wrap: anywhere;` ngăn chặn hoàn toàn lỗi vỡ layout hoặc phình ngang màn hình giao diện.

---

## 📚 5. CÁC BÀI VIẾT MẪU ĐÃ NGHIỆM THU (SHOWCASE ARTICLES)

Toàn bộ các bài viết dưới đây đã được Kỹ sư trưởng nghiệm thu thực tế, đăng tải thành công lên website và kích hoạt cơ chế khóa an toàn bất biến (`APPROVED / LOCKED`):

| Mã Bài | Chủ Đề Bài Viết | Dạng Bài Canonical | Quy Chuẩn Tiêu Biểu | Trạng Thái |
|---|---|---|---|---|
| [**BLOG_01**](03_Articles/BLOG_01_Dong_co_non_tai/) | **Cách phát hiện động cơ điện đang chạy non tải trong nhà máy** | `BLOG-T02` (How-to / Measurement) | Baseline, Bảng tính tải trọng, HTML CKEditor chuẩn | 🔒 `APPROVED / LOCKED` |
| [**BLOG_02**](03_Articles/BLOG_02_He_so_cong_suat_va_Song_hai/) | **Hệ số công suất cos phi và sóng hài bậc cao trong nhà máy** | `BLOG-T01` (Technical Explanation) | Công thức LaTeX biến dạng Fourier, Bảng chuẩn IEEE 519-2022 | 🔒 `APPROVED / LOCKED` |
| [**BLOG_03**](03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan/) | **Quy trình 4 bước chẩn đoán và khắc phục lỗi quá dòng (Overcurrent) trên biến tần công nghiệp** | `BLOG-T03` (Troubleshooting) | Cây quyết định, Quy trình đo 6 van IGBT đồng hồ vạn năng, Chuẩn Responsive Mobile & Laptop | 🔒 `APPROVED / LOCKED` |

---

## 📂 6. CƠ CẤU THƯ MỤC DỰ ÁN (PROJECT STRUCTURE)

```text
Agents-Web-Blog-Content/
├── README.md                      # [BẠN ĐANG ĐỌC] Giới thiệu tổng quan hệ thống & Kiến trúc
├── AGENT_GUIDE.md                 # Cẩm nang vận hành bắt buộc dành cho các AI Agent
├── ROADMAP.md                     # Lộ trình phát triển hệ thống & các Milestones
├── WORKLOG.md                     # Nhật ký làm việc chi tiết, lịch sử phiên & danh mục ADR
├── walkthrough.md                 # Báo cáo tổng kết tiến độ và nghiệm thu kỹ thuật
├── 00_SKILL/                      # Kho lưu trữ các bộ quy chuẩn kỹ năng kỹ thuật cốt lõi
│   ├── archive/                   # Lưu trữ lịch sử các phiên bản cũ
│   ├── BLOG_TAXONOMY_CANONICAL_v1.0.md # Nguồn chuẩn duy nhất phân loại bài viết
│   ├── BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md
│   ├── IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.1.md
│   ├── IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md
│   ├── IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL_v1.1.md
│   ├── IEEE_04_CITATION_AUDIT_PROTOCOL_v1.1.md
│   ├── IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md
│   ├── IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md
│   ├── LATEX_FORMULA_SKILL_v1.0.md
│   ├── REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md
│   ├── SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md
│   └── TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md
├── 01_KNOWLEDGE_BASE/             # Kho tài liệu kỹ thuật, tiêu chuẩn gốc, tích hợp NotebookLM
├── 02_AGENT_TEMPLATES/            # Đặc tả System Prompts & Hợp đồng tương tác 5 Subagents
│   ├── contracts/                 # Các JSON Schemas máy đọc chuẩn mực giữa các Subagent
│   │   ├── article_brief.schema.json
│   │   ├── evidence.schema.json
│   │   ├── claim_source_map.schema.json
│   │   ├── audit.schema.json
│   │   ├── revision_request.schema.json
│   │   └── article_manifest.schema.json
│   ├── ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md # Vòng đời bài viết & cơ chế khóa an toàn
│   ├── research_agent.md          # Đặc tả Subagent Nghiên cứu Nguồn
│   ├── drafting_agent.md          # Đặc tả Subagent Biên soạn Kỹ thuật
│   ├── visual_agent.md            # Đặc tả Subagent Đồ họa & Prompt AI
│   ├── review_agent.md            # Đặc tả Subagent Phản biện & Kiểm toán 2 Cổng
│   └── publisher_agent.md         # Đặc tả Subagent Đóng gói Ấn phẩm (Packaging Agent)
├── 03_Articles/                   # Các gói bài viết độc lập (dossier, draft, image, audit, html)
│   ├── BLOG_01_Dong_co_non_tai/   # BLOG-T02 (LOCKED)
│   ├── BLOG_02_He_so_cong_suat_va_Song_hai/ # BLOG-T01 (LOCKED)
│   └── BLOG_03_Chan_doan_qua_dong_bien_tan/ # BLOG-T03 (LOCKED)
├── 04_PLANS/                      # Kế hoạch thực thi chi tiết theo từng phiên làm việc
├── .github/workflows/             # GitHub Actions CI Workflows
│   └── architecture-validation.yml # Tự động kiểm định kiến trúc & toàn vẹn SHA-256
└── scripts/                       # Bộ công cụ kiểm định tự động hóa độc lập
    ├── validate_architecture.py   # Script kiểm tra JSON schemas, taxonomy, contracts
    └── verify_locked_articles.py  # Script kiểm tra mã băm SHA-256 bài viết đã khóa
```


---

## 🔒 7. CƠ CHẾ BẢO VỆ BÀI VIẾT 3 LỚP (3-LAYER PROTECTION PROTOCOL)

Nhằm đảm bảo an toàn tuyệt đối cho tài sản nội dung sau khi được Kỹ sư trưởng phê duyệt ([ADR-005](WORKLOG.md#quyet-dinh-kien-truc-adr)), hệ thống áp dụng cơ chế khóa 3 lớp:

1. **Lớp Trạng Thái Máy Đọc (Machine State)**: File `article_status.json` trong mỗi thư mục bài viết được gắn `"status": "APPROVED"` và `"is_locked": true`.
2. **Lớp Prompt Guardrail (AI Enforcement)**: Toàn bộ AI Agent khi nhận lệnh chỉnh sửa bài viết đã khóa đều **bắt buộc phải từ chối**, chỉ thực hiện khi Kỹ sư trưởng cấp mã lệnh rõ ràng: `UNLOCK [MÃ_BÀI_VIẾT]`.
3. **Lớp Hệ Điều Hành (OS Read-Only Flag)**: File mã nguồn HTML chính thức được kích hoạt thuộc tính Read-Only của hệ điều hành (`attrib +r`), ngăn chặn mọi hành vi ghi đè hoặc xóa vô tình.

---

## 🚦 8. TIẾN ĐỘ LỘ TRÌNH (ROADMAP PROGRESS)

* ✅ **Phase 1: Baseline & Standards Foundation** (Hoàn thành 09/2026) — Thiết lập bộ quy chuẩn nền tảng, hoàn thành bài viết mẫu `BLOG_01`.
* ✅ **Phase 2: Stress-test & Standards Expansion** (Hoàn thành 09/2026) — Hoàn thành `BLOG_02`, `BLOG_03`, nâng cấp toàn bộ bộ kỹ năng lên `v1.1` - `v2.0`, ban hành tiêu chuẩn Responsive Laptop & Mobile.
* ✅ **Phase 2.5: Multi-Agent Architecture Hardening** (Hoàn thành 09/2026) — Chuẩn hóa Canonical Taxonomy, Stable Source ID (`SRC-xxx`), 6 JSON Schemas, Two-Gate Pipeline, cơ chế bảo vệ mã băm SHA-256.
* ✅ **Phase 2.5.1: Final Architecture Validation & CI Hardening** (Hoàn thành 09/2026) — Tự động hóa GitHub Actions CI (`validate_architecture.py`, `verify_locked_articles.py`), hoàn thiện chính sách ngoại lệ nguồn thẩm quyền cao và ngữ nghĩa kiểm chứng URL.
* 🟡 **Phase 3: Tooling Integration (MCP & Visual)** (Sẵn sàng khởi động Q4/2026) — Khảo sát và tích hợp MCP Tooling (`notebooklm`), image generator và điều phối tự động 5 subagents.
* ⚪ **Phase 4: Autonomous Pipeline & Manual CMS Publishing** (Dự kiến Q1/2027) — Vận hành pipeline một chạm tự động hóa khép kín và quy trình Kỹ sư trưởng nghiệm thu đăng tải thủ công lên CMS.

---

## 👥 9. BẢN QUYỀN & LIÊN HỆ

* **Đơn vị chủ quản**: [Real Group](https://www.real-group.org) / Technical Training Center (TTC)
* **Kỹ sư trưởng & Quản trị dự án**: [Khai TTC](https://github.com/Khaittc)
* **Nền tảng phát triển**: Google Antigravity Agentic AI Framework
