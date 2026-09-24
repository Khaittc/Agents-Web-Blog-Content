# HƯỚNG DẪN DÀNH CHO AI AGENT (AGENT ONBOARDING GUIDE)
**Dự án**: Hệ thống Tự động hóa Đa Agent Sản xuất Nội dung Kỹ thuật (Real Group / TTC)  
**Workspace**: `d:/Agents_Tools/05_WebsiteTTC`

Tài liệu này là **điểm đọc bắt buộc đầu tiên** cho mọi AI Agent (chính hoặc subagent) khi được khởi tạo trong không gian làm việc này.

---

## 1. NGUYÊN TẮC BẤT DI BẤT DỊCH (SAFETY & CONSTRAINTS)

> [!CAUTION]
> **QUY TẮC BẮT BUỘC ƯU TIÊN CAO NHẤT: CÔ LẬP KHÔNG GIAN LÀM VIỆC & LƯU TRỮ TRONG PROJECT (HIGHEST PRIORITY)**:
> 1. **BẮT BUỘC LƯU TRỰC TIẾP TRONG PROJECT**: Mọi tệp tin mới được tạo ra (bao gồm mã nguồn, kế hoạch thực thi, báo cáo nghiệm thu, tệp `walkthrough.md`, tài liệu kỹ năng, ghi chú, prompt ảnh, bản thảo, v.v.) **BẮT BUỘC 100% PHẢI ĐƯỢC TẠO VÀ LƯU TRỰC TIẾP BÊN TRONG THƯ MỤC PROJECT (`d:/Agents_Tools/05_WebsiteTTC/`)**. Đây là quy định có ưu tiên cao nhất, mang tính bắt buộc tuyệt đối.
> 2. **CẤM TUYỆT ĐỐI LƯU RA NGOÀI**: Nghiêm cấm lưu trữ bất kỳ tệp tin dự án nào ra ngoài phạm vi thư mục project (như AppData, thư mục tạm `%TEMP%`, thư mục `brain/` của AI, Desktop, hoặc các folder cha).
> 3. **CƠ CHẾ ĐỒNG BỘ NỘI BỘ BẮT BUỘC**: Nếu bất kỳ công cụ nền tảng nào tự động sinh file ra vùng đệm/brain của AI, Agent **BẮT BUỘC PHẢI SAO CHÉP HOẶC GHI NGAY MỘT BẢN HOÀN CHỈNH VÀO THƯ MỤC PROJECT** (`d:/Agents_Tools/05_WebsiteTTC/`) để Kỹ sư trưởng và hệ thống Git quản lý tập trung toàn diện tài sản dự án.
> 4. Tuyệt đối không xóa các tài liệu chuẩn trong `00_SKILL/` trừ khi có lệnh nâng cấp phiên bản cụ thể từ người dùng (tuân thủ quy trình lưu trữ phiên bản ADR-009).

---

## 2. QUY TRÌNH 3 BƯỚC KHỞI ĐỘNG (STARTUP PROTOCOL)

Khi nhận một nhiệm vụ mới, Agent không cần đọc lại toàn bộ lịch sử hội thoại mà hãy thực hiện đúng 3 bước:

```text
BƯỚC 1: Đọc WORKLOG.md
         └─ Nắm bắt trạng thái hiện tại, các quyết định kiến trúc (ADR) và việc dở dang.
         ↓
BƯỚC 2: Đọc ROADMAP.md
         └─ Định vị nhiệm vụ hiện tại thuộc Phase nào, mục tiêu và tiêu chí đạt là gì.
         ↓
BƯỚC 3: Tra cứu 00_SKILL/ và 02_AGENT_TEMPLATES/
         └─ Áp dụng đúng bộ quy chuẩn tương ứng với vai trò và nội dung bài viết.
```

---

## 3. CƠ CẤU THƯ MỤC VÀ ĐỊA CHỈ TRUY CẬP

```text
05_WebsiteTTC/
├── README.md                  # Giới thiệu tổng quan hệ thống, kiến trúc và ứng dụng trên GitHub
├── AGENT_GUIDE.md             # [BẠN ĐANG ĐỌC] Cẩm nang vận hành dành cho Agent
├── ROADMAP.md                 # Lộ trình 4 giai đoạn và tiến độ các Milestone
├── WORKLOG.md                 # Nhật ký làm việc, các ADR và danh sách việc cần làm
├── walkthrough.md             # Báo cáo tổng kết nghiệm thu & tiến độ phiên làm việc gần nhất
├── 00_SKILL/                  # Bộ quy chuẩn kỹ năng kỹ thuật cốt lõi
│   ├── archive/                                      # Thư mục lưu trữ các phiên bản cũ
│   ├── BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md       # Cấu trúc nội dung 5 loại bài
│   ├── IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md   # Hệ thống trích dẫn IEEE Master Suite v2.0
│   │   ├── IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.1.md # Nguồn & Live URL check 200
│   │   ├── IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md               # Trích dẫn nội văn ở CUỐI CÂU
│   │   ├── IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL_v1.1.md        # Khuôn mẫu đặt tên & Link bấm được CKEditor
│   │   └── IEEE_04_CITATION_AUDIT_PROTOCOL_v1.1.md                          # Kiểm duyệt 6 cửa ải & Vị trí cuối câu
│   ├── LATEX_FORMULA_SKILL_v1.0.md                   # Quy chuẩn công thức toán & SI
│   ├── REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md # Chuẩn giao diện HTML CKEditor
│   ├── SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md         # Quy trình xác minh nguồn Tier 1-3
│   ├── TECHNICAL_REVIEW_AUDIT_PROTOCOL_v1.1.md       # Kiểm duyệt 4 trụ cột & Responsive Laptop/Mobile (ADR-017)
│   └── IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md   # Chuẩn đặc tả ảnh, Prompt AI 5 tầng & khung responsive
├── 01_KNOWLEDGE_BASE/         # Kho tài liệu kỹ thuật, tiêu chuẩn, PDF (liên kết NotebookLM)
├── 02_AGENT_TEMPLATES/        # System prompts & Hợp đồng giao tiếp giữa 5 Subagents
├── 03_Articles/               # Lưu trữ các bài viết (bản thảo, audit report, HTML cuối)
│   ├── BLOG_01_Dong_co_non_tai/                      # Bài viết mẫu Baseline đầu tiên (LOCKED)
│   ├── BLOG_02_He_so_cong_suat_va_Song_hai/          # Bài viết mẫu thứ 2 (LOCKED)
│   └── BLOG_03_Chan_doan_qua_dong_bien_tan/          # Bài viết mẫu thứ 3 (LOCKED)
└── 04_PLANS/                  # Lưu trữ các bản kế hoạch thực thi [yymmdd]_implementation_plan.md
```


---

## 4. QUY TẮC BẢO VỆ BÀI VIẾT ĐÃ PHÊ DUYỆT (ARTICLE LOCKING & PROTECTION)

> [!IMPORTANT]
> **CƠ CHẾ BẢO VỆ TUYỆT ĐỐI**:
> 1. Trước khi thực hiện bất kỳ thao tác chỉnh sửa hoặc ghi đè file nào trong thư mục `03_Articles/[Tên_Bài]/`, Agent **BẮT BUỘC PHẢI ĐỌC** file `article_status.json`.
> 2. Nếu trường `"status": "APPROVED"` hoặc `"is_locked": true`:
>    - Agent **BẮT BUỘC PHẢI TỪ CHỐI THỰC HIỆN** chỉnh sửa.
>    - Thông báo rõ ràng cho người dùng: *"Bài viết này đã được phê duyệt và khóa nội dung. Muốn chỉnh sửa, người dùng cần cung cấp lệnh: UNLOCK [MÃ_BÀI_VIẾT]"*.
> 3. Tuyệt đối không tự ý gỡ bỏ thuộc tính `is_locked` nếu người dùng không ra lệnh rõ ràng bằng cú pháp `UNLOCK`.
> 4. Chi tiết quy chuẩn xem tại: [02_AGENT_TEMPLATES/ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md](file:///d:/Agents_Tools/05_WebsiteTTC/02_AGENT_TEMPLATES/ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md).

---

## 5. QUY TRÌNH ĐÓNG PHIÊN (SHUTDOWN PROTOCOL)

Trước khi kết thúc lượt trả lời hoặc hoàn thành một công việc:
1. **Cập nhật WORKLOG.md**:
   - Ghi lại các việc đã hoàn thành vào mục `NHẬT KÝ CHI TIẾT THEO PHIÊN`.
   - Cập nhật mục `DANH SÁCH HÀNH ĐỘNG TIẾP THEO (NEXT ACTION ITEMS)`.
2. **Cập nhật ROADMAP.md**:
   - Nếu hoàn thành một đầu việc hoặc Milestone, tích chọn `[x]` vào checklist của giai đoạn đó.

