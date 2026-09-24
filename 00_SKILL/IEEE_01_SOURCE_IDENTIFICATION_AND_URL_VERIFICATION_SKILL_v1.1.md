# QUY CHUẨN NHẬN DIỆN NGUỒN TÀI LIỆU & XÁC THỰC URL ĐIỀU HƯỚNG TRỰC TIẾP (IEEE-01: SOURCE IDENTIFICATION & DIRECT LIVE URL VERIFICATION SKILL)
**Version**: 1.1
**Mã tài liệu**: `IEEE_01_SOURCE_IDENTIFICATION_AND_URL_VERIFICATION_SKILL_v1.1`
**Thuộc bộ**: Hệ thống Trích dẫn IEEE Chuẩn hóa (IEEE Modular Citation Suite v2.0)
**Agent áp dụng chính**: **Research Agent** (bắt buộc cho mọi khâu thu thập dữ liệu)
**Trạng thái**: Áp dụng chính thức
**Ngày ban hành**: 24/09/2026
**Lịch sử nâng cấp**: Nâng cấp từ `v1.0` (ADR-015) nhằm giải quyết triệt để lỗi link chỉ mở trang chủ/trang tìm kiếm chung chung hoặc sai lệch bài viết. Bổ sung bắt buộc Cửa ải Điều hướng Trực tiếp (Direct Content Navigation & Deep-Linking Gate) và Cửa ải Khớp Tiêu đề Nội dung (Content Title Verification Gate).

---

## 1. MỤC TIÊU & CÁC NGUYÊN TẮC BẮT BUỘC (CRITICAL GATES)

Tài liệu tham khảo là nền tảng sống còn của bài viết kỹ thuật. Nó chứng minh tính xác thực chuyên môn, tôn trọng bản quyền tác giả và cho phép Kỹ sư trưởng / Người kiểm duyệt / Độc giả có thể nhấp chuột và đọc trực tiếp tài liệu gốc mà không phải tự tìm kiếm lại.

> [!CAUTION]
> ### CỬA ẢI 1: CẤM TUYỆT ĐỐI URL ẢO / LINK CHẾT (ZERO DEAD-LINK GATE)
> - Mọi tài liệu trực tuyến trước khi đưa vào bài viết **BẮT BUỘC phải được kiểm tra thực tế bằng công cụ (`curl`, `read_url_content` hoặc công cụ tìm kiếm)** để xác nhận URL đang hoạt động bình thường (**HTTP Status Code: 200 OK**).
> - **NGHIÊM CẤM TUYỆT ĐỐI**:
>   1. Tự suy đoán cấu trúc đường dẫn (slug) của các hãng.
>   2. Chép lại URL chưa qua kiểm tra trực tiếp.
>   3. Sử dụng link 404, link lỗi redirect hoặc domain giả định.
> - Bất kỳ bài viết nào có dù chỉ **01 link 404 / link ảo** đều bị đánh trượt ngay lập tức (**FAIL**) trong phiên kiểm duyệt kỹ thuật!

> [!IMPORTANT]
> ### CỬA ẢI 2: ĐIỀU HƯỚNG TRỰC TIẾP & KHỚP NỘI DUNG (DIRECT CONTENT NAVIGATION & DEEP-LINKING GATE — ADR-015)
> - **CẤM TRÍCH DẪN TRANG CHỦ (HOMEPAGE/ROOT DOMAIN)**:
>   Tuyệt đối không được dùng trang chủ chung chung của cơ quan hoặc hãng sản xuất (ví dụ `https://www.energy.gov/`, `https://www.yaskawa.com/`) để trích dẫn một tài liệu kỹ thuật cụ thể.
> - **CẤM TRANG TÌM KIẾM/DANH MỤC KHÔNG LỌC (GENERIC SEARCH/DOWNLOAD PORTAL)**:
>   Tuyệt đối không sử dụng trang tìm kiếm chung hoặc thư mục download tổng (ví dụ `https://library.abb.com/`, `https://www.semikron-danfoss.com/service-support/downloads.html`) nếu tài liệu đó có đường dẫn tải trực tiếp hoặc trang chi tiết riêng.
> - **THỨ TỰ ƯU TIÊN ĐỊNH TUYẾN URL (DIRECT LINK HIERARCHY)**:
>   1. **Ưu tiên 1 (Tối ưu nhất)**: Link tải trực tiếp file PDF hoặc link Document Viewer chuyên dụng hiển thị trọn vẹn tài liệu (ví dụ: `https://search.abb.com/library/Download.aspx?DocumentID=...&Action=Launch`, `https://download.se.com/files?p_Doc_Ref=...`, `https://www.energy.gov/sites/prod/files/...`).
>   2. **Ưu tiên 2 (Tiêu chuẩn/Khoa học)**: Link DOI định danh vĩnh viễn (`https://doi.org/10.1109/...`) hoặc link bài báo trên IEEE Xplore (`https://ieeexplore.ieee.org/document/...`).
>   3. **Ưu tiên 3 (Cổng bài viết/Sản phẩm)**: Link trang bài viết cụ thể (Canonical Article Page) hoặc trang sản phẩm chuyên biệt chứa tài liệu hướng dẫn đó.
> - **CỬA ẢI KHỚP TIÊU ĐỀ NỘI DUNG (CONTENT TITLE VERIFICATION GATE)**:
>   Khi kiểm tra URL bằng công cụ mạng, Agent bắt buộc phải đọc thẻ `<title>`, thẻ `<h1>`, hoặc tiêu đề trong `Content-Disposition`. Tiêu đề trang web trả về phải khớp đúng với tên tài liệu/tiêu chuẩn đang trích dẫn. Nếu trang trả về mã 200 nhưng nội dung là tài liệu khác (ví dụ lấy nhầm tiêu chuẩn khác cùng mã số) hoặc trang báo chặn ("Access Denied"), URL đó bị coi là **KHÔNG HỢP LỆ**.

---

## 2. MA TRẬN NHẬN DIỆN LOẠI HÌNH TÀI LIỆU KỸ THUẬT (OPEN SOURCE TAXONOMY)

Trước khi trích dẫn, Research Agent bắt buộc phải xác định chính xác bản chất của nguồn tài liệu, không được quy đồng mọi trang web thành "Website" hay mọi file PDF thành "Report":

| Mã loại hình (Source Type) | Định nghĩa & Bản chất | Dấu hiệu nhận diện đặc trưng | Ví dụ thực tế tiêu biểu |
|:---|:---|:---|:---|
| **`STANDARD`** | Tiêu chuẩn kỹ thuật của các tổ chức quốc tế hoặc quốc gia | Ban hành bởi IEEE, IEC, ISO, TCVN; có số hiệu tiêu chuẩn (Std Number) và năm hiệu lực. | *IEEE Std 519-2022*, *IEEE Std 43-2013* |
| **`MANUAL`** | Sổ tay kỹ thuật, cẩm nang lắp đặt của hãng sản xuất | Tài liệu hướng dẫn thiết kế/vận hành dày từ vài chục đến hàng trăm trang do hãng phát hành. | *ACS880 Firmware Manual* (ABB), *ATV600 Programming Manual* (Schneider) |
| **`JOURNAL_PAPER`** | Bài báo khoa học trên tạp chí chuyên ngành có bình duyệt | Xuất bản định kỳ, có Volume, Issue, dải trang (pp. xx–yy) và mã định danh số DOI. | Bài báo của H. Akagi trên *IEEE Trans. Ind. Appl.*, doi: 10.1109/28.556635 |
| **`CONF_PAPER`** | Báo cáo tại hội nghị khoa học kỹ thuật | Có tên hội nghị in nghiêng (*Proc. of...*), địa điểm tổ chức, ngày diễn ra và DOI. | Bài báo tại hội nghị IEEE PES General Meeting |
| **`TECH_REPORT`** | Báo cáo kỹ thuật của cơ quan nghiên cứu hoặc chính phủ | Có mã số báo cáo (Report Number: Rep. DOE/GO-...), cơ quan ban hành, địa điểm trụ sở. | Báo cáo của Bộ Năng lượng Hoa Kỳ (US DOE), Rep. DOE/GO-102014-4421 |
| **`BLOG_POST`** | Bài viết phân tích kỹ thuật trên Blog chuyên ngành | Nằm trong mục Blog của hãng (ví dụ `blog.se.com`), có tên Tác giả cụ thể, ngày đăng rõ ràng. | Bài phân tích của Karl Kaiser trên *Schneider Electric Blog* |
| **`WEB_ARTICLE`** | Bài viết kỹ thuật trên website thông tin hoặc cổng kiến thức | Trang web kỹ thuật chính thức, không có cấu trúc blog cá nhân, thuộc quyền sở hữu tổ chức. | Bài viết trên Wikipedia kỹ thuật, Electrical Engineering Portal (EEP) |
| **`BOOK`** | Sách giáo trình, sách chuyên khảo kỹ thuật | Có nhà xuất bản (Publisher), nơi xuất bản, năm, tên tác giả, số hiệu ISBN. | Sách *Application Manual Power Semiconductors* (ISLE Verlag, ISBN 978-3-938843-83-3) |
| **`DATASHEET`** | Bảng thông số kỹ thuật sản phẩm của nhà sản xuất | Tài liệu ngắn (1–8 trang) chứa bảng thông số định mức, mã sản phẩm (Part Number), bản vẽ kích thước. | Datasheet tụ bù Enerlux, datasheet biến tần Danfoss VLT |
| **`THESIS`** | Luận văn thạc sĩ hoặc luận án tiến sĩ | Đề tài nghiên cứu học thuật, có tên trường đại học, học vị (M.S. thesis / Ph.D. dissertation), năm. | Ph.D. dissertation, Dept. Elect. Eng., Univ. of Wisconsin |
| **`DATASET` / `PREPRINT` / `PATENT` / `LEGAL` / `VIDEO` / `OTHER_IEEE_SUPPORTED`** | Các nguồn học thuật và định dạng số phụ trợ | Dữ liệu đo kiểm thực nghiệm, bằng sáng chế, quy chuẩn pháp lý hoặc video mô phỏng chính hãng. | US Patent, IEEE Dataport |
| **`SOURCE_TYPE_REVIEW_REQUIRED`** | Nguồn chưa xác định chắc chắn loại hình | Áp dụng khi chưa thể phân loại rạch ròi. **BẮT BUỘC** gán nhãn này để Tech Review Agent rà soát, tuyệt đối không được đoán mò. | Nguồn hỗn hợp, brochure kỹ thuật lai catalogue |

---

## 3. QUY TRÌNH 4 BƯỚC XÁC THỰC BẰNG CHỨNG (VERIFICATION WORKFLOW)

```text
┌──────────────────────┐      ┌─────────────────────────────┐      ┌─────────────────────────────┐
│ 1. Giám định Nguồn   │ ───> │ 2. Live-Check & Deep Link   │ ───> │ 3. Trích xuất & Đối chiếu   │
│ (Xác định 1 trong 10)│      │ (HTTP 200 + Link Trực tiếp) │      │ Tiêu đề (Title Verification)│
└──────────────────────┘      └─────────────────────────────┘      └─────────────────────────────┘
                                                                                 │
                                                                                 ▼
                                                                    ┌─────────────────────────────┐
                                                                    │ 4. Đóng dấu VERIFIED        │
                                                                    │ vào evidence_dossier.md     │
                                                                    └─────────────────────────────┘
```

### Bước 1: Giám định nguồn gốc (Source Identification)
- Xác định tài liệu đang đọc: Tiêu chuẩn chính thức? Cẩm nang kỹ thuật của hãng? Bài báo khoa học? Hay bài phân tích trên Blog?
- Gán nhãn loại hình (ví dụ: `BLOG_POST`, `STANDARD`, `MANUAL`, `BOOK`).

### Bước 2: Kiểm tra URL sống & Định tuyến trực tiếp (Live Deep-Link Verification)
- **Hành động bắt buộc của Agent**:
  1. Lấy URL dự kiến trích dẫn.
  2. Áp dụng quy tắc ADR-015: Đảm bảo URL là đường dẫn sâu (Deep link) hoặc link tải trực tiếp (Launch/Download link), tuyệt đối không dùng domain gốc hoặc trang tìm kiếm chung.
  3. Gọi công cụ mạng (`curl`, `read_url_content`) kiểm tra mã trạng thái HTTP.
  4. Nếu trả về thành công (**HTTP 200** hoặc redirect đến đúng trang đích HTTP 200) $\rightarrow$ Chuyển sang Bước 3.
  5. Nếu công cụ báo lỗi **404 Not Found**, **403 Access Denied** hoặc không thể kết nối: **DỪNG LẠI NGAY LẬP TỨC**. Dùng công cụ tìm kiếm (`search_web`) để tìm link tải trực tiếp chính thức hoặc đổi sang nguồn tài liệu khác đã được kiểm chứng.

### Bước 3: Đối chiếu tiêu đề & Trích xuất siêu dữ liệu thực tế (Title Matching & Metadata Extraction)
- **Kiểm tra tiêu đề**: Kiểm tra tiêu đề hiển thị trong mã HTML/PDF xem có khớp với tên tài liệu trích dẫn hay không. Tránh tuyệt đối trường hợp lấy nhầm mã số sang tài liệu khác (ví dụ: nhầm chuẩn chống sét thay vì chuẩn đo điện trở cách điện).
- **Trích xuất thông tin**:
  - **Tác giả (Author)**: Họ và tên viết tắt của tác giả (ví dụ: `A. Wintrich, U. Nicolai...`). Nếu không có tên cá nhân thì dùng tên tổ chức (ví dụ: `ABB Oy`, `Schneider Electric`).
  - **Tiêu đề gốc (Original Title)**: Sao chép nguyên văn tiêu đề tài liệu.
  - **Mã tài liệu / Số hiệu / ISBN / DOI**: Bắt buộc ghi nhận nếu có (Doc ID, ISBN, DOI).
  - **Năm xuất bản / Phiên bản**: Năm phát hành thực tế.
  - **URL trực tiếp**: URL trực tiếp xem/tải tài liệu.

### Bước 4: Đóng gói vào `evidence_dossier.md`
Chỉ các nguồn đã vượt qua cả Bước 2 và Bước 3 mới được ghi vào bảng đăng ký nguồn (`Source Registry`) và đánh trạng thái `VERIFIED (Live Direct URL 200)` trong `evidence_dossier.md`.

---

## 4. BẢNG MẪU ĐẦU RA BẮT BUỘC TRONG `evidence_dossier.md` VÀ `evidence.json`

> [!IMPORTANT]
> **QUY TẮC STABLE SOURCE ID (PHASE 2.5 ARCHITECTURE HARDENING)**:
> Mọi nguồn tài liệu trong hồ sơ nghiên cứu BẮT BUỘC sử dụng Stable Source ID: `SRC-001`, `SRC-002`, `SRC-003`,...
> **TUYỆT ĐỐI KHÔNG** gán số trích dẫn IEEE `[1]`, `[2]` ở giai đoạn này. Số IEEE sẽ do Drafting Agent gán dựa trên thứ tự xuất hiện đầu tiên trong bài viết.
> **TÁCH BẠCH KIỂM CHỨNG**: `HTTP 200 OK` chỉ chứng minh URL truy cập được (Access Status: OK), không được coi là chứng cứ nội dung claim đã đúng.

Mọi tệp `evidence_dossier.md` do Research Agent bàn giao phải có cấu trúc cột như sau:

```markdown
| Source ID | Phân cấp Tier | Loại hình (Source Type) | Tên tài liệu / Tiêu đề | Cơ quan / Tác giả | Năm / Bản | Mã tài liệu / DOI / ISBN | URL Trực tuyến (Đã test HTTP 200 & Direct Link) | Trạng thái Mạng | Content ID | Claim Verified | Locator Verified |
|:---:|:---|:---:|:---|:---|:---:|:---|:---|:---:|:---:|:---:|:---|
| `SRC-001` | Tier 1 | `STANDARD` | *IEEE Recommended Practice for Testing Insulation Resistance of Electric Machinery* | IEEE Power and Energy Society | 2014 | IEEE Std 43-2013 / DOI: 10.1109/IEEESTD.2014.6754111 | `https://ieeexplore.ieee.org/document/6754111` | HTTP 200 OK | YES | YES | YES (Tab. 4, p. 20) |
| `SRC-002` | Tier 1 | `MANUAL` | *ACS880 Primary Control Program Firmware Manual* | ABB Oy, Helsinki, Finland | 2023 | 3AUA0000085967 Rev. X | `https://search.abb.com/library/Download.aspx?DocumentID=3AUA0000085967&LanguageCode=en&DocumentPartId=1&Action=Launch` | HTTP 200 OK | YES | YES | YES (Fault 2310, p. 504) |
| `SRC-003` | Tier 1 | `MANUAL` | *Altivar Process ATV600 Variable Speed Drives Programming Manual* | Schneider Electric | 2021 | EAV64318 | `https://download.se.com/files?p_Doc_Ref=EAV64318&p_enDocType=User+guide` | HTTP 200 OK | YES | YES | YES (Sec. 5, p. 88) |
```
