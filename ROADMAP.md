# LỘ TRÌNH PHÁT TRIỂN HỆ THỐNG (ROADMAP)
**Dự án**: Hệ thống Tự động hóa Đa Agent Sản xuất Nội dung Kỹ thuật (Real Group / TTC)  
**Mục tiêu**: Tự động hóa khép kín từ nghiên cứu tài liệu, thẩm định kỹ thuật, tạo hình ảnh đến xuất bản bài viết lên website `real-group.org` (CKEditor 3.6.6.2).

---

## 1. Tổng quan Trạng thái Hiện tại (Current Status)

| Giai đoạn | Tên Giai đoạn | Trạng thái | Mốc hoàn thành dự kiến |
|---|---|---|---|
| **Phase 1** | Baseline & Standards Foundation | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 2** | Stress-test & Standards Expansion | ✅ **HOÀN THÀNH** | 09/2026 |
| **Phase 3** | Multi-Agent Specification & Tooling | 🟡 **ĐANG THỰC HIỆN** | Q4/2026 |
| **Phase 4** | Autonomous Pipeline & Publishing | ⚪ **DỰ KIẾN** | Q1/2027 |

> [!IMPORTANT]
> **Vị trí hiện tại của dự án**: Đang ở bước chuyển giao từ **Phase 2** sang **Phase 3**. 
> - Toàn bộ 3 bài viết kiểm nghiệm mẫu (`BLOG_01`, `BLOG_02`, `BLOG_03`) đại diện cho 3 thể loại bài viết kỹ thuật cốt lõi đã được Kỹ sư trưởng chính thức nghiệm thu và kích hoạt cơ chế khóa an toàn (`APPROVED / LOCKED`, Read-Only flag).
> - Bộ quy chuẩn kỹ năng đã hoàn thiện toàn diện với các quyết định kiến trúc: **ADR-012** (IEEE Modular Suite v2.0), **ADR-013** (Trích dẫn bắt buộc ở cuối câu), **ADR-014** (Lưu trữ 100% tệp trong project), **ADR-015** (Link trực tiếp Deep-link / Direct PDF), **ADR-016** (Tiêu chuẩn Responsive Laptop & Mobile), và **ADR-017** (Cửa ải kiểm định hiển thị song song Laptop & Mobile).
> - Nhiệm vụ trọng tâm hiện tại: **Định nghĩa chuyên biệt 5 Subagents trong `02_AGENT_TEMPLATES/`** để chuẩn bị tự động hóa hoàn toàn quy trình sản xuất bài viết.

---

## 2. Chi tiết Các Giai đoạn Phát triển

### Giai đoạn 1: Thiết lập Nền tảng Chuẩn hóa & Khóa Baseline (Phase 1)
*Trạng thái*: ✅ **ĐÃ HOÀN THÀNH** (Tháng 09/2026)
*Mục tiêu*: Xây dựng bộ quy chuẩn cốt lõi và kiểm nghiệm bằng một bài viết thực tế.
- [x] Xây dựng [BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md) phân định 5 loại bài (`BLOG-T01` đến `BLOG-T05`), logic luồng kỹ thuật và bắt buộc tối thiểu 1 hình content.
- [x] Xây dựng [IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md) (Bộ 4 Sub-Skills: IEEE-01 Nhận diện & URL check 200, IEEE-02 Trích dẫn nội văn, IEEE-03 Đặt tên & Link bấm được CKEditor, IEEE-04 Biên bản kiểm duyệt 6 cửa ải).
- [x] Xây dựng [LATEX_FORMULA_SKILL_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/LATEX_FORMULA_SKILL_v1.0.md) chuẩn hóa công thức toán học và đơn vị SI.
- [x] Xây dựng [REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md) chuẩn hóa HTML CKEditor inline, semantic callouts và khoảng trắng.
- [x] Tạo bài viết kiểm nghiệm thực tế đầu tiên làm baseline: [Cách phát hiện động cơ điện đang chạy non tải trong nhà máy](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_01_Dong_co_non_tai/bai-viet-dong-co-chay-non-tai-ckeditor.html) (✅ **APPROVED / LOCKED**).
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

### Giai đoạn 3: Định nghĩa Chuyên biệt Subagent & Tích hợp Công cụ (Phase 3)
*Trạng thái*: 🟡 **ĐANG THỰC HIỆN** (Khởi động Tháng 09/2026)
*Mục tiêu*: Chuyển đổi các quy chuẩn lý thuyết thành các Prompt và Hợp đồng giao tiếp tự động của 5 Subagents.

- [x] **Định nghĩa 5 Subagents chuyên trách (trong `02_AGENT_TEMPLATES/`) — ĐÃ HOÀN THÀNH**:
  - [x] `research_agent.md`: System prompt, công cụ tìm kiếm, Live URL Check 200, trích xuất locator theo `IEEE-01 v1.1` & `SOURCE_TIER v1.0`.
  - [x] `drafting_agent.md`: System prompt, cấu trúc `BLOG-T01`..`T05`, công thức LaTeX SI, trích dẫn bắt buộc ở cuối câu theo `IEEE-02 v1.1`.
  - [x] `visual_agent.md`: System prompt, Prompt AI 5 tầng, kích thước 808x500 px, HTML placeholder chống méo dọc theo `IMAGE_SPEC v1.2`.
  - [x] `review_agent.md`: System prompt, 4 trụ cột kiểm duyệt độc lập, Gate 5 vị trí cuối câu, kiểm tra responsive song song Laptop & Mobile theo `REVIEW_PROTOCOL v1.1` (ADR-017).
  - [x] `publisher_agent.md`: System prompt, đóng gói HTML CKEditor sạch, link `<a>` có `word-break: break-all;`, bảng `min-width`, quản lý `article_status.json` theo `ADR-005` và `ADR-016`.
- [ ] **Tích hợp Công cụ Ngoài (Tooling Integration)**:
  - [ ] Kết nối `notebooklm` MCP vào `01_KNOWLEDGE_BASE/` để truy xuất nguồn Tier 1/2 với locator tự động.
  - [ ] Tích hợp công cụ `generate_image` với quy chuẩn 808x500 px tự động.
  - [ ] Tạo template kiểm tra tự động mã HTML CKEditor không để lọt thẻ sai quy cách.

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
