# QUY CHUẨN TRÍCH DẪN NỘI VĂN & BỘ ĐỊNH VỊ CHÍNH XÁC (IEEE-02: IN-TEXT CITATION & EXACT LOCATOR SKILL)
**Version**: 1.1  
**Mã tài liệu**: `IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1`  
**Thuộc bộ**: Hệ thống Trích dẫn IEEE Chuẩn hóa (IEEE Modular Citation Suite v2.0)  
**Agent áp dụng chính**: **Drafting Agent** (soạn thảo bản thảo kỹ thuật)  
**Trạng thái**: Áp dụng chính thức  
**Ngày ban hành**: 23/09/2026  
**Thay thế**: `IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.0.md` (Đã lưu trữ trong `00_SKILL/archive/`)  

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

## 4. QUY TẮC BẮT BUỘC: VỊ TRÍ ĐẶT TRÍCH DẪN PHẢI LUÔN LUÔN Ở CUỐI CÂU (END-OF-SENTENCE ENFORCEMENT)

> [!CAUTION]
> **RÀNG BUỘC KIẾN TRÚC NGHIÊM NGẶT**:
> Trong toàn bộ các bài viết kỹ thuật xuất bản trên website Real Group / TTC, **100% các ký hiệu trích dẫn nội văn `[n]` BẮT BUỘC PHẢI ĐẶT Ở CUỐI CÂU**, ngay trước dấu kết thúc câu (dấu chấm câu `.` hoặc dấu hai chấm `:` khi dẫn nhập công thức/bảng/danh sách).
>
> **Mục tiêu**: Đảm bảo mạch đọc văn phong kỹ thuật của kỹ sư được liền mạch, không bị đứt đoạn bởi các khối số ngoặc vuông nằm rải rác giữa chừng.

### 4.1. Quy tắc Vị trí Chi tiết:

1. **Trước dấu chấm câu kết thúc (`.`):**
   - Ký hiệu trích dẫn nằm liền sau từ cuối cùng của câu và **đứng ngay trước dấu chấm câu**: `... [n].`
   - *Ví dụ ĐÚNG*: `...thậm chí biến các dàn tụ bù thành "quả bom nổ chậm" trong trạm biến áp [1, p. 3].`
   - *Ví dụ SAI*: `...trong trạm biến áp. [1, p. 3]` (Đặt sau dấu chấm câu).

2. **Trước dấu hai chấm dẫn nhập (`:`):**
   - Khi câu kết thúc bằng dấu hai chấm để mở ra một khối công thức toán học, bảng biểu hoặc danh sách gạch đầu dòng: `... [n]:`
   - *Ví dụ ĐÚNG*: `Mối quan hệ giữa True Power Factor và méo sóng hài được biểu diễn bằng công thức [3, p. M12, eq. (2)]:`
   - *Ví dụ SAI*: `Theo công thức [3, p. M12, eq. (2)], mối quan hệ giữa True Power Factor và sóng hài là:` (Đặt ở đầu/giữa câu).

3. **CẤM TUYỆT ĐỐI đặt trích dẫn ở đầu câu hoặc dùng làm chủ ngữ:**
   - Trong văn phong chuẩn của Real Group, **không bao giờ biến con số `[n]` thành danh từ/chủ ngữ**. Phải gọi tên thực thể kỹ thuật (tên tiêu chuẩn, tên tác giả, tên tổ chức) và đẩy `[n]` về cuối câu.
   - *Ví dụ SAI*: `Theo [1, p. 21], giới hạn độ méo điện áp tổng là 5.0%.`
   - *Ví dụ ĐÚNG*: `Theo tiêu chuẩn IEEE 519-2022, giới hạn độ méo điện áp tổng trên lưới hạ thế là 5.0% [1, p. 21].`
   - *Ví dụ SAI*: `Như đã được chứng minh bởi Akagi trong [6, p. 1314], bộ lọc tích cực...`
   - *Ví dụ ĐÚNG*: `Như nghiên cứu của Hirofumi Akagi đã chứng minh, bộ lọc sóng hài tích cực AHF có khả năng bù dòng tức thời [6, p. 1314].`

4. **CẤM TUYỆT ĐỐI đặt trích dẫn ở giữa câu làm ngắt quãng mạch văn:**
   - *Ví dụ SAI*: `Hệ thống tụ bù [3, p. M10] nếu không có cuộn kháng sẽ gây cộng hưởng.`
   - *Ví dụ ĐÚNG*: `Hệ thống tụ bù nếu không trang bị cuộn kháng chặn sẽ đối mặt với nguy cơ quá nhiệt và nổ tụ do hiện tượng cộng hưởng sóng hài [3, p. M10].`

---

## 5. BẢNG ĐỐI CHIẾU NHANH: ĐÚNG VS SAI VỀ VỊ TRÍ TRÍCH DẪN

| Ngữ cảnh trích dẫn | CÁCH VIẾT SAI (BỊ CHẶN BỞI TECH REVIEW) | CÁCH VIẾT ĐÚNG CHUẨN REAL GROUP (PASS) |
|:---|:---|:---|
| **Dẫn chứng tiêu chuẩn** | `Theo [1], độ méo THDu không được vượt quá 5%.` | `Theo tiêu chuẩn IEEE 519-2022, độ méo điện áp tổng không được vượt quá 5.0% [1, p. 21].` |
| **Dẫn chứng công thức** | `Công thức [3, eq. (2)] xác định hệ số công suất thực.` | `Hệ số công suất thực True Power Factor được xác định chính xác theo công thức của Schneider Electric [3, p. M12, eq. (2)]:` |
| **Dẫn chứng tác giả** | `Akagi [6] đề xuất cấu trúc topo nghịch lưu song song.` | `Cấu trúc topo biến đổi nghịch lưu song song đã được giáo sư Hirofumi Akagi đề xuất và thử nghiệm thành công [6, p. 1314].` |
| **Dẫn nhiều nguồn** | `Nhiều tài liệu [3], [7] khuyến cáo dùng cuộn kháng 7%.` | `Để tránh cộng hưởng bậc 5, các chuyên gia khuyến cáo lắp đặt cuộn kháng chặn sóng hài 7% [3, p. M25], [7].` |
| **Vị trí dấu chấm** | `Nhà máy vẫn có thể bị phạt tiền điện lực. [3]` | `Nhà máy vẫn có thể bị phạt tiền điện lực dù cos phi hiển thị mức cao [3, p. M12].` |
