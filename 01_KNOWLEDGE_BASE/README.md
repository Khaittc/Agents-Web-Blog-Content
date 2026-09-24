# KHO TRI THỨC KỸ THUẬT (KNOWLEDGE BASE)

Thư mục này dùng để lưu trữ và quản lý các nguồn tài liệu kỹ thuật, tiêu chuẩn, datasheets và tài liệu tham khảo phục vụ quá trình nghiên cứu của **Research & Evidence Agent**.

---

## 1. Cấu trúc Phân tầng Nguồn (Source Tiering)

Mọi tài liệu lưu trữ tại đây hoặc nạp vào NotebookLM phải được phân loại theo cấp độ tin cậy kỹ thuật:

```text
01_KNOWLEDGE_BASE/
├── Tier1_Standards/           # Tiêu chuẩn quốc tế (IEC, IEEE, ISO, NEMA), tài liệu hãng chính thức (Siemens, ABB, Schneider)
├── Tier2_Manuals_Handbooks/   # Sổ tay kỹ thuật, sách chuyên ngành, báo cáo của cơ quan năng lượng (DOE, VEEA)
└── Tier3_Articles_Papers/     # Bài báo khoa học, whitepapers, bài phân tích chuyên gia đã qua kiểm chứng
```

---

## 2. Quy tắc Lưu trữ & Đặt tên

1. **Định dạng ưu tiên**: PDF, TXT, MD.
2. **Quy tắc đặt tên file**:
   ```text
   [TIER]_[ORGANIZATION/AUTHOR]_[DOCUMENT_TITLE]_[YEAR/VERSION].[ext]
   ```
   *Ví dụ*:
   - `TIER1_IEC_60034-30-1_Motor_Efficiency_Classes_2014.pdf`
   - `TIER1_ABB_Technical_Guide_Motor_Load_2020.pdf`
   - `TIER2_DOE_Continuous_Energy_Improvement_Motor_2017.pdf`

---

## 3. Tích hợp với NotebookLM MCP

Khi sử dụng MCP `notebooklm` để truy vấn kho tri thức:
- Tạo notebook theo từng chủ đề hoặc lĩnh vực (ví dụ: `Motor Systems`, `Power Quality`, `VFD & Inverters`).
- Nạp các tài liệu Tier 1 và Tier 2 vào notebook nguồn.
- Khi truy vấn, yêu cầu NotebookLM trích xuất kèm số trang, số chương hoặc tiêu đề bảng biểu cụ thể để phục vụ việc gắn **Verified Locator** theo chuẩn `IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0.md`.
