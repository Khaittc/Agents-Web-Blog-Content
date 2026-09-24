# BÁO CÁO ĐIỀU CHỈNH VÒNG ĐỜI BÀI VIẾT (ARTICLE LIFECYCLE STATE PATCH REPORT)
## BLOG_04 — ARTICLE LIFECYCLE STATE PATCH & CI INVARIANT HARDENING
**Thời điểm thực hiện**: 2026-09-24T23:35:00+07:00  
**Tác nhân thực hiện**: Antigravity Quality & Architecture Agent  
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`  
**Chủ đề**: VFD và Soft Starter: So sánh Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Phạm vi Ứng dụng  
**Mã phân loại chuẩn**: `BLOG-T04` (Comparison)  
**Commit Baseline**: `2c1ae9d — chore: approve BLOG_04 research handoff`  

---

## 1. VẤN ĐỀ (PROBLEM STATEMENT)

Sau khi hoàn tất đợt thẩm định Final Research Gate, bài viết `BLOG_04` đã bị chuyển trạng thái sớm trong `article_status.json`:
```text
status: RESEARCHED → TECH_REVIEW
```
trong khi Drafting Agent chưa được kích hoạt và hai thành phẩm bản thảo bắt buộc chưa được khởi tạo:
- `draft_review_package.md`: Chưa tồn tại
- `claim_source_map.json`: Chưa tồn tại

Theo quy chuẩn vòng đời bài viết (`02_AGENT_TEMPLATES/ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md` và `drafting_agent.md`):
- `RESEARCHED`: Giai đoạn nghiên cứu hoàn tất, hồ sơ chứng cứ và hợp đồng bàn giao sẵn sàng chuyển sang cho Drafting Agent.
- `TECH_REVIEW`: Bản thảo kỹ thuật (`draft_review_package.md`) và bản đồ luận điểm (`claim_source_map.json`) đã được soạn thảo xong và đang nằm tại Cổng kiểm duyệt 1 (Technical Review Gate) để Review Agent kiểm định.
Việc gán `TECH_REVIEW` khi chưa có bản thảo là bước chuyển trạng thái sớm (premature lifecycle transition).

---

## 2. NGUYÊN NHÂN GỐC RỄ (ROOT CAUSE)

Trước bản vá này, kiểm tra tự động Gate 8 (`validate_canonical_article_statuses`) trong CI `scripts/validate_architecture.py` chỉ kiểm tra giá trị của trường `status` có thuộc tập hợp `CANONICAL_ARTICLE_STATUSES` hay không (enum membership check), mà chưa kiểm tra các điều kiện tiên quyết về sự hiện diện của các tệp thành phẩm tương ứng với từng trạng thái (artifact prerequisites).

---

## 3. GIẢI PHÁP ĐIỀU CHỈNH (FIX)

1. **Hiệu chỉnh trạng thái `BLOG_04/article_status.json`**:
   - `status`: Chuyển từ `"TECH_REVIEW"` về `"RESEARCHED"`.
   - `notes`: Cập nhật phản ánh đúng:
     > *"Research Phase đã hoàn thành. Final Research Gate PASS. research_handoff.json đã được tạo và handoff_ready = true. BLOG_04 hiện sẵn sàng cho Drafting Agent. Chưa có draft_review_package.md hoặc claim_source_map.json, vì vậy chưa được chuyển sang TECH_REVIEW."*
2. **Bảo toàn các thành phẩm nghiên cứu**:
   - `research_plan.json`: Giữ nguyên `status = COMPLETE`.
   - `research_handoff.json`: Giữ nguyên `research_status = PASS`, `research_plan_status = COMPLETE`, `handoff_ready = true`.
   - Toàn bộ 17 bằng chứng kỹ thuật, 6 nguồn tài liệu và 2 xung đột kỹ thuật đã giải quyết không thay đổi.

---

## 4. TĂNG CƯỜNG RÀO CHẮN CI (CI INVARIANT HARDENING)

Đã bổ sung cổng kiểm định mới **Gate 10: Lifecycle Artifact Preconditions** trong `scripts/validate_architecture.py`:
- **Quy tắc TECH_REVIEW & TECH_APPROVED**:
  - Nếu `status == "TECH_REVIEW"` hoặc `status == "TECH_APPROVED"`, bắt buộc thư mục bài viết phải có:
    - `draft_review_package.md` (nếu thiếu: báo lỗi `{article_id} is {status} but draft_review_package.md is missing`)
    - `claim_source_map.json` (nếu thiếu: báo lỗi `{article_id} is {status} but claim_source_map.json is missing`)
- **Quy tắc RESEARCHED**:
  - Không bắt buộc sự tồn tại của `draft_review_package.md` và `claim_source_map.json`.
  - Trạng thái `RESEARCHED` hoàn toàn hợp lệ khi `research_handoff.json` có `handoff_ready: true`.
- **Quy tắc Tính Nhất Quán Handoff (Research Handoff Consistency)**:
  - Nếu `research_handoff.json` tồn tại và `handoff_ready: true`, bắt buộc `research_status == "PASS"` và `research_plan_status == "COMPLETE"`.

---

## 5. KẾT QUẢ KIỂM THỬ (VERIFICATION RESULTS)

1. **Negative Case Testing**:
   - Đã kiểm tra trường hợp bài viết có `status = "TECH_REVIEW"` khi chưa có `draft_review_package.md` và `claim_source_map.json` $\rightarrow$ CI phát hiện và chặn thành công với 2 lỗi `[FAIL]`.
   - Đã kiểm tra trường hợp `handoff_ready: true` nhưng `research_status: "FAIL"` $\rightarrow$ CI chặn thành công.
2. **Positive Testing**:
   - `python scripts/validate_architecture.py` $\rightarrow$ **PASS** (10/10 gates xanh).
   - `python scripts/verify_locked_articles.py` $\rightarrow$ **PASS** (100% 3 bài khóa `BLOG_01`, `BLOG_02`, `BLOG_03` toàn vẹn).
   - `git diff --check` $\rightarrow$ **PASS** (Không có lỗi khoảng trắng hay định dạng).

---

## 6. KẾT LUẬN HIỆN TRẠNG (CURRENT STATUS)

- **`BLOG_04` Article Status**: **`RESEARCHED`**
- **Drafting Readiness**: **`READY`** (Đủ điều kiện để kích hoạt Drafting Agent)
- **Technical Review Readiness**: **`NOT YET`** (Chờ Drafting Agent tạo `draft_review_package.md` và `claim_source_map.json` trước khi chuyển sang `TECH_REVIEW`)
