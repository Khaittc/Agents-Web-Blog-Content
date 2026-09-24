# BIÊN BẢN & CỬA ẢI KIỂM DUYỆT TRÍCH DẪN IEEE (IEEE-04: CITATION AUDIT PROTOCOL)
**Version**: 1.1  
**Mã tài liệu**: `IEEE_04_CITATION_AUDIT_PROTOCOL_v1.1`  
**Thuộc bộ**: Hệ thống Trích dẫn IEEE Chuẩn hóa (IEEE Modular Citation Suite v2.0)  
**Agent áp dụng chính**: **Tech Review Agent** (Trụ cột 1 trong `TECHNICAL_REVIEW_AUDIT_PROTOCOL`)  
**Trạng thái**: Áp dụng chính thức  
**Ngày ban hành**: 23/09/2026  
**Thay thế**: `IEEE_04_CITATION_AUDIT_PROTOCOL_v1.0.md` (Đã lưu trữ trong `00_SKILL/archive/`)  

---

## 1. MỤC ĐÍCH & TRÁCH NHIỆM CỦA TECH REVIEW AGENT

Tech Review Agent đóng vai trò là "người gác cổng" (Quality Gatekeeper) cuối cùng trước khi một bài viết được chuyển sang xuất bản. Mọi sai sót về link ảo, tác giả giả mạo, trích dẫn lệch sự thật, sai cấu trúc IEEE hoặc đặt sai vị trí trích dẫn trong câu đều phải bị chặn lại ở bước này.

---

## 2. MA TRẬN 6 CỬA ẢI NGHIỆM THU TRÍCH DẪN (6-GATE CITATION AUDIT)

Tech Review Agent bắt buộc phải thực hiện kiểm duyệt tuần tự qua cả 6 cửa ải dưới đây. Chỉ khi **100% tiêu chí đạt chuẩn** thì Trụ cột 1 mới được cấp kết quả **PASS**:

```text
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ Gate 1: Live URL 200 │ ───> │ Gate 2: Tác giả thật │ ───> │ Gate 3: Fact-Check   │
│ (Không có link 404)  │      │ (Tác giả/Bài có thật)│      │ (Khớp nội dung gốc)  │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                       │
                                                                       ▼
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ Gate 6: Locator Đủ   │ <─── │ Gate 5: Cú pháp [] & │ <─── │ Gate 4: Khuôn mẫu    │
│ (Trang, Bảng, Eq.)   │      │ VỊ TRÍ CUỐI CÂU      │      │ Đặt tên chuẩn IEEE   │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
```

| Cửa ải (Gate) | Nội dung kiểm tra | Phương pháp thực hiện của Reviewer | Tiêu chí ĐẠT (PASS) | Hành động khi KHÔNG ĐẠT (FAIL) |
|:---|:---|:---|:---|:---|
| **Gate 1: Live URL Testing** | Xác minh mọi đường dẫn trực tuyến đều đang hoạt động | Dùng công cụ `read_url_content` truy cập trực tiếp từng URL trong danh mục tham khảo. | Tất cả URL trả về **HTTP 200 OK**, nội dung tải về hoàn chỉnh. | Đánh trượt ngay (**FAIL**). Yêu cầu Research Agent thay bằng link thật. |
| **Gate 2: Tác giả & Nguồn thật** | Kiểm tra bài viết và tác giả có tồn tại trên thực tế hay do AI tự nghĩ | Đối chiếu tên tác giả và tiêu đề bài viết với nội dung HTML/Metadata vừa tải về ở Gate 1. | Tên tác giả (ví dụ K. Kaiser), tiêu đề bài viết và tên blog/website khớp 100% với trang gốc. | Đánh trượt (**FAIL**). Trừ điểm vi phạm đạo đức học thuật/bản quyền. |
| **Gate 3: Fact-Check nội dung** | Kiểm tra lập luận trong bài có đúng với ý của tài liệu gốc hay bị xuyên tạc | Đọc lướt đoạn văn bản trong bài gốc tương ứng với locator. | Số liệu, khuyến nghị kỹ thuật (ví dụ: cuộn kháng 7%, AHF) hoàn toàn phản ánh đúng quan điểm bài gốc. | Yêu cầu Drafting Agent viết lại lập luận cho trung thực. |
| **Gate 4: Cấu trúc Đặt tên IEEE** | Kiểm tra thứ tự và kiểu chữ (in nghiêng vs ngoặc kép) theo chuẩn IEEE | So khớp với mẫu chuẩn tại `IEEE_03_REFERENCE_NAMING_AND_CKEDITOR_STYLE_SKILL`. | Standards/Manuals in nghiêng đầu; Reports/Blogs/Papers trong ngoặc kép; đầy đủ ngày truy cập và URL clickable. | Sửa lại đúng cấu trúc IEEE tương ứng của loại hình đó. |
| **Gate 5: Cú pháp Ngoặc & Vị trí Cuối câu** | Kiểm tra định dạng ngoặc vuông và **vị trí xuất hiện trong câu** (tuân thủ `IEEE-02 v1.1`) | Quét toàn bộ bài viết tìm các chuỗi `[` và `]`. | 1. Đánh số tuyến tính tăng dần `[1]` đến `[n]`.<br>2. Liệt kê rời `[1], [2]`, cấm gạch nối `[1]–[3]`.<br>3. **100% trích dẫn nằm ở CUỐI CÂU** (trước dấu `.` hoặc `:`). Tuyệt đối không có trích dẫn nào nằm ở đầu câu, giữa câu, hoặc dùng làm chủ ngữ. | Đánh trượt (**FAIL**). Yêu cầu Drafting Agent tách ngoặc và dồn vị trí trích dẫn về cuối câu. |
| **Gate 6: Bộ định vị (Locators)** | Kiểm tra số trang, số công thức, bảng biểu | Kiểm tra các công thức toán học và ngưỡng kỹ thuật quan trọng trong bài. | Các công thức và ngưỡng quan trọng đều có locator rõ ràng (ví dụ: `[3, p. M12, eq. (2)]`, `[1, Tab. 1, p. 21]`). | Yêu cầu bổ sung số trang/mục chính xác. |

---

## 3. CHECKLIST KIỂM ĐỊNH MẪU ĐƯA VÀO `technical_audit_report.md`

Khi lập báo cáo `technical_audit_report.md`, Tech Review Agent phải điền đầy đủ bảng nghiệm thu này vào Trụ cột 1:

```markdown
### Trụ cột 1: Citation & Reference Audit (Tuân thủ IEEE Suite v2.0)
- [x] **Gate 1 - Live URL Check**: Đã kiểm tra 100% URL bằng công cụ `read_url_content`, tất cả đều trả về HTTP 200 OK (0 link chết/404).
- [x] **Gate 2 - Tác giả & Bản quyền**: Tác giả cá nhân (K. Kaiser) và tổ chức ban hành đã được xác minh danh tính thực tế.
- [x] **Gate 3 - Fact-Checking**: Toàn bộ số liệu và công thức đều khớp với tài liệu gốc tại các vị trí locator.
- [x] **Gate 4 - Đặt tên chuẩn IEEE**: Đã phân loại đúng 100% loại hình (Standard, Manual, Report, Paper, Blog) và áp dụng đúng cấu trúc đặt tên IEEE tương ứng.
- [x] **Gate 5 - Cú pháp Ngoặc vuông & Vị trí Cuối câu**: 100% trích dẫn dùng cặp ngoặc riêng biệt `[1], [2], [3]`, không có gạch nối `[1]–[3]`. Đánh số tuyến tính từ [1] đến [7]. **100% vị trí đặt trích dẫn nằm ở CUỐI CÂU** (trước dấu `.` hoặc `:`), không làm đứt đoạn mạch văn.
- [x] **Gate 6 - Clickable Hyperlinks & Locators**: Mọi tài liệu trực tuyến trong file HTML đều đã bọc thẻ `<a>` có link bấm trực tiếp `target="_blank"`. Các công thức toán và ngưỡng kỹ thuật có locator trang/công thức rõ ràng.
- **KẾT QUẢ TRỤ CỘT 1**: ✅ **PASS (7/7 NGUỒN ĐẠT CHUẨN KỸ THUẬT TOÀN DIỆN)**
```
