# LIVE RESEARCH PROVIDER & TOOLING ABSTRACTION

**Module**: `03_TOOLING/live_research/`  
**Phase**: Phase 3.0 (Live Research Foundation v1)  
**Mục tiêu**: Cung cấp kiến trúc trừu tượng hóa cho việc khai thác tài liệu kỹ thuật trực tiếp từ Web (Live Web Research), tách biệt giữa nguồn ứng viên (Candidate Source `CAN-xxx`) và nguồn chính thức được chấp nhận (Accepted Source `SRC-xxx`).

---

## 1. TỔNG QUAN KIẾN TRÚC PROVIDER (PROVIDER ARCHITECTURE)

Hệ thống Research được thiết kế dưới dạng **Provider-Agnostic** (Độc lập với nhà cung cấp tìm kiếm). Live Web Research là Provider đầu tiên được chuẩn hóa. Kiến trúc này cho phép tích hợp thêm các Provider tương lai mà không làm thay đổi các hợp đồng cốt lõi (`research_plan.json`, `evidence.json`):

```text
┌────────────────────────────────────────────────────────┐
│              RESEARCH AGENT (ORCHESTRATOR)             │
│        (research_plan.json, RQ-001 .. RQ-xxx)          │
└───────────────────────────┬────────────────────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
┌─────────────────┐┌─────────────────┐┌─────────────────┐
│ LIVE WEB        ││ NOTEBOOKLM      ││ INTERNAL KB     │
│ PROVIDER (v1)   ││ PROVIDER (Ph3.x)││ PROVIDER (Ph3.x)│
│ [HOẠT ĐỘNG]     ││ [DEFERRED]      ││ [PLANNED]       │
└────────┬────────┘└─────────────────┘└─────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────┐
│ Candidate Sources (CAN-001, CAN-002, ...)              │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ SOURCE ACCEPTANCE GATE (Thẩm định 8 tiêu chí khắt khe) │
└───────────────────────────┬────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
    [ACCEPTED SOURCE]             [REJECTED CANDIDATE]
    (SRC-001, SRC-002)            (Ghi nhận lý do từ chối)
              │
              ▼
    Evidence Extraction & Dossier
```

---

## 2. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Phân biệt rạch ròi Candidate Source vs Accepted Source**:
   - `CAN-xxx` (Candidate Source): Nguồn tiềm năng phát hiện từ kết quả tìm kiếm sơ cấp. **Chưa được coi là nguồn chính thức**.
   - `SRC-xxx` (Accepted Source): Nguồn đã vượt qua trọn vẹn 8 tiêu chí của Cửa ải Thẩm định (Source Acceptance Gate). Chỉ các nguồn này mới được trích xuất bằng chứng kỹ thuật và đưa vào `evidence.json`.
2. **Không coi Snippet là Bằng chứng (No Snippet Evidence)**:
   - Nghiêm cấm đặt `claim_verified: true` dựa trên tóm tắt Google Snippet, trích đoạn tìm kiếm hay tên file. Agent bắt buộc phải đọc nội dung thực tế của tài liệu.
3. **Nhật ký Truy vấn Minh bạch (`research_log.json`)**:
   - Mọi câu lệnh truy vấn tìm kiếm đều được ghi nhận có cấu trúc (`query_id`, `rq_id`, `query`, `provider`, `executed_at`, `result_count`) nhằm phục vụ truy nguyên và kiểm toán nghiên cứu.

---

## 3. CƠ CẤU TỆP TIN TRONG THƯ MỤC

```text
03_TOOLING/live_research/
├── README.md                      # [BẠN ĐANG ĐỌC] Tổng quan module Live Research
├── provider_contract.md           # Hợp đồng giao tiếp, đặc tả dữ liệu Input/Output của Provider
└── examples/                      # Các tệp JSON mẫu minh họa định dạng dữ liệu
    ├── candidate_source.example.json
    └── research_query_record.example.json
```
