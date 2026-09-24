# QUY CHUẨN NHẬN DIỆN NGUỒN TÀI LIỆU & XÁC THỰC URL SỐNG (IEEE-01: SOURCE IDENTIFICATION & LIVE URL VERIFICATION SKILL)
**Version**: 1.0  
**Mã tài liệu**: `IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.0`  
**Thuộc bộ**: Hệ thống Trích dẫn IEEE Chuẩn hóa (IEEE Modular Citation Suite v2.0)  
**Agent áp dụng chính**: **Research Agent** (bắt buộc cho mọi khâu thu thập dữ liệu)  
**Trạng thái**: Áp dụng chính thức  
**Ngày ban hành**: 23/09/2026  

---

## 1. MỤC TIÊU & CÁC NGUYÊN TẮC BẮT BUỘC (CRITICAL GATES)

Tài liệu tham khảo là nền tảng sống còn của bài viết kỹ thuật. Nó chứng minh tính xác thực chuyên môn, tôn trọng bản quyền tác giả và cho phép Kỹ sư trưởng / Người kiểm duyệt có thể đối chiếu trực tiếp với bài gốc.

> [!CAUTION]
> **CỬA ẢI BẮT BUỘC: CẤM TUYỆT ĐỐI URL ẢO / LINK CHẾT (ZERO DEAD-LINK GATE)**
> - Mọi tài liệu trực tuyến (Blog Post, Web Article, Online Report/PDF) trước khi đưa vào bài viết **BẮT BUỘC phải được kiểm tra thực tế bằng công cụ (`read_url_content` hoặc công cụ tìm kiếm)** để xác nhận URL đang hoạt động bình thường (**HTTP Status Code: 200 OK**).
> - **NGHIÊM CẤM TUYỆT ĐỐI**:
>   1. Tự suy đoán cấu trúc đường dẫn (slug) của các hãng.
>   2. Chép lại URL chưa qua kiểm tra trực tiếp.
>   3. Sử dụng link 404, link lỗi redirect hoặc domain giả định.
> - Bất kỳ bài viết nào có dù chỉ **01 link 404 / link ảo** đều bị đánh trượt ngay lập tức (**FAIL**) trong phiên kiểm duyệt kỹ thuật!

---

## 2. MA TRẬN NHẬN DIỆN 10 LOẠI HÌNH TÀI LIỆU KỸ THUẬT

Trước khi trích dẫn, Research Agent bắt buộc phải xác định chính xác bản chất của nguồn tài liệu, không được quy đồng mọi trang web thành "Website" hay mọi file PDF thành "Report":

| Mã loại hình (Source Type) | Định nghĩa & Bản chất | Dấu hiệu nhận diện đặc trưng | Ví dụ thực tế tiêu biểu |
|:---|:---|:---|:---|
| **`STANDARD`** | Tiêu chuẩn kỹ thuật của các tổ chức quốc tế hoặc quốc gia | Ban hành bởi IEEE, IEC, ISO, TCVN; có số hiệu tiêu chuẩn (Std Number) và năm hiệu lực. | *IEEE Std 519-2022*, *IEC 61000-2-4* |
| **`MANUAL`** | Sổ tay kỹ thuật, cẩm nang lắp đặt của hãng sản xuất | Tài liệu hướng dẫn thiết kế/vận hành dày từ vài chục đến hàng trăm trang do hãng phát hành. | *Electrical Installation Guide* (Schneider), *Technical Guide No. 6* (ABB) |
| **`JOURNAL_PAPER`** | Bài báo khoa học trên tạp chí chuyên ngành có bình duyệt | Xuất bản định kỳ, có Volume, Issue, dải trang (pp. xx–yy) và mã định danh số DOI. | Bài báo của H. Akagi trên *IEEE Trans. Ind. Appl.*, doi: 10.1109/28.556635 |
| **`CONF_PAPER`** | Báo cáo tại hội nghị khoa học kỹ thuật | Có tên hội nghị in nghiêng (*Proc. of...*), địa điểm tổ chức, ngày diễn ra và DOI. | Bài báo tại hội nghị IEEE PES General Meeting |
| **`TECH_REPORT`** | Báo cáo kỹ thuật của cơ quan nghiên cứu hoặc chính phủ | Có mã số báo cáo (Report Number: Rep. DOE/GO-...), cơ quan ban hành, địa điểm trụ sở. | Báo cáo của Bộ Năng lượng Hoa Kỳ (US DOE), Rep. DOE/GO-102014-4421 |
| **`BLOG_POST`** | Bài viết phân tích kỹ thuật trên Blog chuyên ngành | Nằm trong mục Blog của hãng (ví dụ `blog.se.com`), có tên Tác giả cụ thể, ngày đăng rõ ràng. | Bài phân tích của Karl Kaiser trên *Schneider Electric Blog* |
| **`WEB_ARTICLE`** | Bài viết kỹ thuật trên website thông tin hoặc cổng kiến thức | Trang web kỹ thuật chính thức, không có cấu trúc blog cá nhân, thuộc quyền sở hữu tổ chức. | Bài viết trên Wikipedia kỹ thuật, Electrical Engineering Portal (EEP) |
| **`BOOK`** | Sách giáo trình, sách chuyên khảo kỹ thuật | Có nhà xuất bản (Publisher), nơi xuất bản, năm, tên tác giả, số hiệu chương/trang. | Sách *Power System Harmonics* của J. Arrillaga |
| **`DATASHEET`** | Bảng thông số kỹ thuật sản phẩm của nhà sản xuất | Tài liệu ngắn (1–8 trang) chứa bảng thông số định mức, mã sản phẩm (Part Number), bản vẽ kích thước. | Datasheet tụ bù Enerlux, datasheet biến tần Danfoss VLT |
| **`THESIS`** | Luận văn thạc sĩ hoặc luận án tiến sĩ | Đề tài nghiên cứu học thuật, có tên trường đại học, học vị (M.S. thesis / Ph.D. dissertation), năm. | Ph.D. dissertation, Dept. Elect. Eng., Univ. of Wisconsin |

---

## 3. QUY TRÌNH 4 BƯỚC XÁC THỰC BẰNG CHỨNG (VERIFICATION WORKFLOW)

```text
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ 1. Giám định Nguồn   │ ───> │ 2. Live-Check URL    │ ───> │ 3. Trích xuất Siêu dữ│
│ (Xác định 1 trong 10)│      │ (Bắt buộc tool HTTP) │      │ liệu (Tác giả, Ngày) │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                       │
                                                                       ▼
                                                            ┌──────────────────────┐
                                                            │ 4. Đóng dấu VERIFIED │
                                                            │ vào evidence_dossier │
                                                            └──────────────────────┘
```

### Bước 1: Giám định nguồn gốc (Source Identification)
- Kiểm tra tài liệu đang đọc là gì: Tiêu chuẩn chính thức? Cẩm nang kỹ thuật của hãng? Bài báo khoa học? Hay bài phân tích trên Blog?
- Gán nhãn loại hình (ví dụ: `BLOG_POST`, `STANDARD`, `MANUAL`).

### Bước 2: Kiểm tra URL sống bằng công cụ (Live URL Verification)
- **Hành động bắt buộc của Agent**:
  1. Lấy URL dự kiến trích dẫn.
  2. Gọi công cụ `read_url_content` để nạp nội dung từ URL đó.
  3. Nếu công cụ trả về nội dung thành công (**HTTP 200**): URL hợp lệ -> Chuyển sang Bước 3.
  4. Nếu công cụ báo lỗi **404 Not Found** hoặc không thể kết nối: **DỪNG LẠI NGAY LẬP TỨC**. Tuyệt đối không được dùng link này. Dùng công cụ tìm kiếm (`search_web`) để tìm link bài viết chính thức hoặc đổi sang nguồn tài liệu khác đã được kiểm chứng.

### Bước 3: Trích xuất siêu dữ liệu thực tế (Metadata Extraction)
Không tự sáng tạo metadata, phải lấy đúng 100% từ trang web vừa nạp:
- **Tác giả (Author)**: Lấy họ và tên viết tắt của tác giả bài viết (ví dụ: tác giả `Karl Kaiser` -> `K. Kaiser`). Nếu bài không đề tên tác giả cá nhân thì dùng tên tổ chức (ví dụ: `Schneider Electric`).
- **Tiêu đề gốc (Original Title)**: Sao chép nguyên văn tiêu đề bài viết từ thẻ `<title>` hoặc thẻ `<h1>` của trang.
- **Tên Blog / Website**: Tên chính thức (ví dụ: *Schneider Electric Blog*).
- **Ngày xuất bản (Publication Date)**: Ngày tháng năm đăng bài thực tế (ví dụ: Feb. 21, 2017).
- **Ngày truy cập (Accessed Date)**: Ngày Agent hoặc người dùng thực hiện truy cập kiểm tra (ví dụ: Mar. 10, 2026).
- **URL gốc**: URL canonical chính xác của bài viết.

### Bước 4: Đóng gói vào `evidence_dossier.md`
Chỉ các nguồn đã vượt qua Bước 2 mới được ghi vào bảng đăng ký nguồn (`Source Registry`) và đánh trạng thái `VERIFIED (Live URL 200)` trong `evidence_dossier.md`.

---

## 4. BẢNG MẪU ĐẦU RA BẮT BUỘC TRONG `evidence_dossier.md`

Mọi tệp `evidence_dossier.md` do Research Agent bàn giao phải có cấu trúc cột như sau:

```markdown
| Mã Ref | Phân cấp Tier | Loại hình (Source Type) | Trích dẫn IEEE dự kiến | Năm | Trạng thái URL | Verified Locator |
|---|---|---|---|---|---|---|
| **[1]** | Tier 1 | `STANDARD` | *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. | 2022 | N/A (Standard) | Tab. 1, p. 21 |
| **[7]** | Tier 3 | `BLOG_POST` | K. Kaiser, “5 Harmonic mitigation methods that help keep costs down and production running,” *Schneider Electric Blog*, Feb. 21, 2017. Accessed: Mar. 10, 2026. [Online]. Available: https://blog.se.com/industry/machine-and-process-management/2017/02/21/5-harmonic-mitigation-methods-help-keep-costs-production-running/ | 2017 | **HTTP 200 (Verified)** | Sec. 1–4 |
```
