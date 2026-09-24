# HỢP ĐỒNG GIAO TIẾP LIVE RESEARCH PROVIDER (PROVIDER CONTRACT)

**Mã tài liệu**: `03_TOOLING/live_research/provider_contract.md`  
**Phiên bản**: 1.0 (Phase 3.0 Live Research Foundation)  
**Vai trò**: Định nghĩa giao diện logic, quy chuẩn đầu vào/đầu ra, và cửa ải thẩm định nguồn ứng viên trước khi cấp phát Stable Source ID (`SRC-xxx`).

---

## 1. GIAO DIỆN LOGIC CỦA RESEARCH PROVIDER (INTERFACE LOGIC)

Mọi Research Provider (bao gồm Live Web Provider hiện tại và NotebookLM / Internal KB Provider trong tương lai) đều phải tuân thủ chuẩn giao diện logic thống nhất:

### 1.1. Dữ liệu Đầu vào (INPUT):
* **`research_question`** (`rq_id`, `question`): Câu hỏi kỹ thuật cần giải đáp cụ thể từ `research_plan.json`.
* **`preferred_source_types`**: Danh mục loại tài liệu ưu tiên (ví dụ: `MANUAL`, `STANDARD`, `DATASHEET`).
* **`preferred_publishers`**: Hãng sản xuất hoặc cơ quan tiêu chuẩn mục tiêu (ví dụ: ABB, Siemens, Schneider Electric, Danfoss, IEEE, IEC).
* **`freshness_required`**: Cờ yêu cầu tài liệu cập nhật mới nhất (true/false).

### 1.2. Dữ liệu Đầu ra (OUTPUT):
* Danh sách các **Nguồn Ứng Viên (Candidate Sources)** có định dạng `CAN-xxx`.

---

## 2. ĐẶC TẢ NGUỒN ỨNG VIÊN (CANDIDATE SOURCE MODEL)

Một Nguồn Ứng Viên (`CAN-xxx`) là một kết quả tìm kiếm sơ bộ, **chưa được coi là nguồn chính thức và chưa được cấp mã `SRC-xxx`**.

```json
{
  "candidate_id": "CAN-001",
  "rq_id": "RQ-001",
  "title": "ABB Drives Technical Guide No. 1: Direct Torque Control",
  "publisher": "ABB",
  "url": "https://library.e.abb.com/public/...",
  "discovered_via": "LIVE_WEB",
  "discovery_query": "ABB direct torque control VFD working principle technical guide pdf",
  "discovered_at": "2026-09-24T21:30:00Z"
}
```

---

## 3. CỬA ẢI THẨM ĐỊNH NGUỒN ỨNG VIÊN (SOURCE ACCEPTANCE GATE)

Trước khi chuyển một `CAN-xxx` thành nguồn chính thức `SRC-xxx` trong `evidence.json`, Agent bắt buộc phải kiểm tra và xác nhận đạt **8 tiêu chí khắt khe**:

1. **Khả năng truy cập mạng (URL access status)**: Kết nối thành công (`OK` hoặc `REDIRECTED_OK` đến URL chính thống).
2. **Khớp danh tính tài liệu (Content identity)**: Tiêu đề trang, tên tài liệu, hãng chế tạo, số hiệu tài liệu khớp với thông tin công bố.
3. **Phân loại loại hình nguồn (Source type)**: Xác định rõ ràng theo open taxonomy (`MANUAL`, `STANDARD`, `TECH_REPORT`,...).
4. **Cấp độ thẩm quyền (Authority / Tier)**: Phù hợp phân tầng Tier 1 (Chuẩn, Manuals chính hãng) hoặc Tier 2 (Giáo trình, Báo cáo viện năng lượng).
5. **Độ tương thích với câu hỏi nghiên cứu (Relevance to RQ)**: Tài liệu trực tiếp trả lời trọng tâm của câu hỏi `rq_id`.
6. **Khả năng đọc nội dung thực tế (Actual content readable)**: Nội dung đầy đủ phải được đọc và phân tích trực tiếp bởi Agent (qua công cụ đọc nội dung hoặc tài liệu tải về); không bị tường lửa, captcha hay trang login chặn (`CONTENT_NOT_READABLE`).
7. **Hỗ trợ luận điểm kỹ thuật (Claim support)**: Các câu văn, số liệu hoặc công thức trong tài liệu thực sự chứng minh luận điểm kỹ thuật đặt ra.
8. **Độ tươi mới (Freshness check)**: Nếu `freshness_required: true`, phải là phiên bản tài liệu/tiêu chuẩn hiện hành, không sử dụng tài liệu đã bị hủy bỏ hoặc thay thế.

### Kết quả Thẩm định (Acceptance Verdicts):
* **`ACCEPTED`**: Thỏa mãn 100% 8 tiêu chí. Cấp phát mã `SRC-xxx`, ghi nhận `accepted_from_candidate_id: "CAN-xxx"` và tiến hành trích xuất bằng chứng (`EVD-xxx`).
* **`REJECTED`**: Không đạt một hoặc nhiều tiêu chí. Lưu hồ sơ kèm mã lý do từ chối.
* **`REVIEW_REQUIRED`**: Chưa đủ căn cứ để kết luận hoặc cần ý kiến của Kỹ sư trưởng (Human Reviewer).

### Danh mục Mã Lý do Từ chối (Rejection Reasons):
* `SEARCH_RESULT_ONLY`: Mới chỉ thấy kết quả trên trang tìm kiếm mà chưa mở được văn bản.
* `HOMEPAGE_ONLY`: Liên kết trỏ về trang chủ hoặc cổng thông tin chung chung, không mở đúng tài liệu (vi phạm ADR-015).
* `CONTENT_NOT_READABLE`: Tệp bị khóa bản quyền, yêu cầu đăng nhập, lỗi mạng hoặc không thể trích xuất văn bản.
* `IDENTITY_MISMATCH`: Tiêu đề hoặc nội dung tài liệu thực tế không khớp với kết quả tìm kiếm.
* `LOW_RELEVANCE`: Tài liệu nói về chủ đề khác hoặc chỉ nhắc qua loa, không trả lời được `rq_id`.
* `DUPLICATE_SOURCE`: Trùng lặp với một tài liệu đã được ghi nhận trước đó (cùng số hiệu, cùng phiên bản).
* `OUTDATED_FOR_CURRENT_CLAIM`: Phiên bản tài liệu đã lỗi thời đối với yêu cầu `freshness_required`.
* `UNVERIFIED_CLAIM`: Nội dung trong tài liệu không thực sự ủng hộ hoặc mâu thuẫn với luận điểm kỹ thuật.

---

## 4. QUY TẮC TUYỆT ĐỐI: KHÔNG DÙNG SEARCH SNIPPET LÀM BẰNG CHỨNG

> [!CAUTION]
> **NO SNIPPET EVIDENCE RULE**:
> Tuyệt đối **CẤM** đặt cờ `claim_verified: true` nếu chỉ dựa vào:
> - Tóm tắt tìm kiếm của Google (Google Search Snippet)
> - Đoạn văn tóm tắt tự động của AI Search Engine
> - Tiêu đề trang (Page title only)
> - Tên tệp tin (Filename only)
>
> Bắt buộc phải sử dụng công cụ đọc tài liệu để đọc toàn bộ đoạn văn bản chứa thông tin, đối chiếu câu chữ, số liệu, đơn vị SI và số trang/mục thực tế trước khi xác nhận claim.

---

## 5. NHẬT KÝ TRUY VẤN TÌM KIẾM (`research_log.json`)

Mọi hành động tìm kiếm trực tiếp trên Live Web đều phải được ghi nhận vào `research_log.json` tại thư mục bài viết:

```json
{
  "article_id": "BLOG_04",
  "queries": [
    {
      "query_id": "Q-001",
      "rq_id": "RQ-001",
      "query": "ABB direct torque control vs soft starter principle pdf",
      "provider": "LIVE_WEB",
      "executed_at": "2026-09-24T21:35:00Z",
      "result_count": 5
    }
  ]
}
```
