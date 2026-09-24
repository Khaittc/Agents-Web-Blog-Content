# QUY CHUẨN TRÍCH DẪN NỘI VĂN & BỘ ĐỊNH VỊ CHÍNH XÁC (IEEE-02: IN-TEXT CITATION & EXACT LOCATOR SKILL)
**Version**: 1.0  
**Mã tài liệu**: `IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0`  
**Thuộc bộ**: Hệ thống Trích dẫn IEEE Chuẩn hóa (IEEE Modular Citation Suite v2.0)  
**Agent áp dụng chính**: **Drafting Agent** (soạn thảo bản thảo kỹ thuật)  
**Trạng thái**: Áp dụng chính thức  
**Ngày ban hành**: 23/09/2026  

---

## 1. NGUYÊN TẮC ĐÁNH SỐ TRÍCH DẪN TUYẾN TÍNH (SEQUENTIAL NUMBERING)

Theo tiêu chuẩn IEEE, các tài liệu tham khảo được đánh số theo thứ tự xuất hiện lần đầu tiên trong văn bản:

1. **Thứ tự số nguyên tăng dần liên tục**: Tài liệu xuất hiện đầu tiên trong bài là `[1]`, tài liệu tiếp theo là `[2]`, tiếp tục đến `[n]`. Tuyệt đối không được bỏ sót số hoặc nhảy cóc (ví dụ: đang `[2]` nhảy sang `[5]`).
2. **Tái sử dụng số hiệu**: Khi một tài liệu đã được đánh số ở phần trước (ví dụ `[3]`) được tham chiếu lại ở các mục sau, **bắt buộc dùng lại đúng số `[3]`** kèm theo số trang hoặc mục tương ứng của lần trích dẫn đó. Tuyệt đối không cấp số mới cho tài liệu đã xuất hiện.

---

## 2. QUY TẮC CÚ PHÁP NGOẶC VUÔNG (BRACKET SYNTAX RULES)

> [!IMPORTANT]
> **QUY TẮC BẮT BUỘC KHI TRÍCH DẪN NHIỀU NGUỒN LIÊN TIẾP**:
> - Khi trích dẫn từ 2 nguồn trở lên cùng một chỗ, **BẮT BUỘC PHẢI LIỆT KÊ TỪNG CẶP NGOẶC VUÔNG RIÊNG BIỆT**, phân tách bằng dấu phẩy và khoảng trắng:
>   - **ĐÚNG CHUẨN IEEE**: `[1], [2]` hoặc `[1], [2], [3]` hoặc `[3], [7]`
>   - **SAI — NGHIÊM CẤM**:
>     - `[1-3]` hoặc `[1–3]` (dùng dấu gạch nối hoặc gạch ngang)
>     - `[1, 2, 3]` (gom nhiều số vào một cặp ngoặc)
>     - `[1]-[3]` (nối hai cặp ngoặc bằng gạch ngang)

---

## 3. CÚ PHÁP BỘ ĐỊNH VỊ CHÍNH XÁC (EXACT LOCATORS)

Để người kiểm duyệt và độc giả có thể lật đúng trang hoặc vị trí trong tài liệu gốc để kiểm chứng số liệu, Drafting Agent bắt buộc phải gắn các bộ định vị cụ thể (Locators) vào sau số trích dẫn:

### 3.1. Các dạng Locator tiêu chuẩn:

| Mục tiêu định vị | Cú pháp IEEE chuẩn | Ví dụ mẫu | Ý nghĩa kiểm chứng |
|:---|:---|:---|:---|
| **Một trang cụ thể** | `[n, p. X]` | `[1, p. 21]` | Xem trang 21 của tài liệu số [1] |
| **Dải nhiều trang** | `[n, pp. X–Y]` | `[3, pp. M10–M12]` | Xem từ trang M10 đến M12 của tài liệu [3] |
| **Công thức toán học** | `[n, p. X, eq. (Y)]` | `[3, p. M12, eq. (2)]` | Xem công thức số (2) tại trang M12 |
| **Bảng dữ liệu kỹ thuật** | `[n, Tab. X, p. Y]` | `[1, Tab. 1, p. 21]` | Đối chiếu bảng Table 1 tại trang 21 |
| **Mục hoặc điều khoản** | `[n, Sec. X.Y]` | `[4, Sec. 4.1]` | Xem mục 4.1 của tài liệu số [4] |
| **Mục bài viết trực tuyến** | `[n, Mục_hoặc_Heading]` | `[7, Solution 1-4]` | Đối chiếu mục giải pháp 1-4 trong bài blog |

### 3.2. Khi nào bắt buộc phải có Locator?
- Mọi **công thức toán học** lấy từ tiêu chuẩn/sổ tay bắt buộc phải có locator đến đúng công thức hoặc trang chứa công thức đó.
- Mọi **ngưỡng giá trị kỹ thuật bắt buộc** (ví dụ: \(\text{THD}_u \le 5.0\%\), cuộn kháng 7%) phải có locator đến đúng bảng hoặc điều khoản tiêu chuẩn.
- Các định nghĩa hoặc khái niệm chung của cả tài liệu có thể chỉ ghi `[n]`.

---

## 4. VỊ TRÍ ĐẶT DẤU TRÍCH DẪN TRONG CÂU

1. **Đặt trong dấu chấm câu**: Dấu trích dẫn đặt trước dấu chấm câu hoặc dấu phẩy:
   - *Đúng*: `...theo khuyến cáo của các chuyên gia Schneider Electric [3, p. M25], [7].`
   - *Sai*: `...theo khuyến cáo của các chuyên gia Schneider Electric. [3, p. M25], [7]`
2. **Đóng vai trò chủ ngữ trong câu**: Có thể dùng `[n]` như một danh từ thay thế cho tên tác giả:
   - *Đúng*: `Như đã được chứng minh bởi Akagi trong [6, p. 1314], bộ lọc tích cực AHF...`
   - *Đúng*: `Theo [1, p. 21], giới hạn méo điện áp tổng là 5.0%.`
