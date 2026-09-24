# IEEE CITATION & REFERENCE SKILL FOR TECHNICAL CONTENT AGENTS
Version: 1.3
Status: Canonical standard — synchronized with official IEEE Reference Guide V 3.28.2025
Authority: IEEE Publication Operations (445 Hoes Lane, Piscataway, NJ 08854 USA)
Primary reference: https://docs.google.com/document/d/1j1L96U2NagwWI9MEVDNVKt9pXxRzTH7h3krI3Mb6wZE/edit?tab=t.0#heading=h.b2e0set9htjw
Primary use: Technical blog / solution / engineering content
Citation system: IEEE numeric reference style

---

# 1. PURPOSE

This Skill defines how an Agent must:

1. identify the type of a source actually used in technical content;
2. collect the metadata required for that source type;
3. insert IEEE-style in-text citations;
4. create the corresponding IEEE-style reference entry;
5. keep citation numbering consistent across the article;
6. audit citations and references before final delivery.

This Skill does **not** restrict which source types may be used.

Possible sources include, but are not limited to:

- official websites;
- technical blogs;
- manufacturer web pages;
- product documentation;
- manuals;
- handbooks;
- datasheets;
- application notes;
- white papers;
- technical reports;
- standards;
- journal papers;
- magazine articles;
- conference papers;
- books;
- book chapters;
- theses and dissertations;
- preprints;
- datasets;
- patents;
- online videos;
- lectures;
- government documents;
- legal documents;
- other technical publications.

The Agent must apply the IEEE reference format that corresponds to the **actual source type used**.

---

# 2. SCOPE BOUNDARY

## 2.1. Citation formatting is not source-quality evaluation

This Skill answers:

> How must this source be cited?

It does not answer:

> Is this source sufficiently authoritative to support the claim?

Source credibility, freshness, conflict resolution, and evidence quality belong to the Research / Evidence workflow.

A low-quality blog can still be formatted correctly as an IEEE website reference.

Correct citation formatting does **not** make a weak source authoritative.

---

## 2.2. Never change the source type to make formatting easier

Examples:

- A manufacturer PDF titled "Installation Manual" must not be converted into a generic website reference merely because it was downloaded from a website.
- A peer-reviewed paper found through Google Scholar must be cited as the journal/conference paper, not as a Google Scholar webpage.
- An IEC standard landing page must not replace the actual standard identity if the article uses requirements from the standard.
- A blog post must normally be treated as a website/web article unless it is part of a periodical that has formal volume/issue metadata.

---

# 2A. CRITICAL IEEE REFERENCE PATTERNS & ANTI-PATTERNS (QUY TẮC ĐẶT TÊN BẮT BUỘC)

> [!CAUTION]
> **CÁC LỖI PHỔ BIẾN NHẤT AGENT THƯỜNG MẮC PHẢI VÀ BẮT BUỘC PHẢI TRÁNH**:

### 1. TIÊU CHUẨN (Standards)
- **LỖI SAI**: Đưa tên tổ chức lên đầu, ví dụ:
  `[x] IEEE Power and Energy Society, *IEEE Standard for Harmonic Control...*`
  `[x] International Electrotechnical Commission, *Electromagnetic compatibility...*`
- **ĐÚNG THEO CHUẨN IEEE (Mục P)**: Tiêu chuẩn **BẮT BUỘC BẮT ĐẦU BẰNG TIÊU ĐỀ IN NGHIÊNG**, theo sau là số hiệu tiêu chuẩn và năm:
  `[v] *Title of Standard*, Standard number, Corporate author, location, date.`
  `[v] *Title of Standard*, Standard number, date.`
  *Ví dụ*:
  `[1] *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022.`
  `[2] *Electromagnetic Compatibility (EMC) - Part 2-4: Compatibility Levels in Industrial Plants for Low-Frequency Conducted Disturbances*, IEC Standard 61000-2-4, 2002.`

### 2. SỔ TAY KỸ THUẬT / CATALOGUE HÃNG (Manuals & Handbooks)
- **LỖI SAI**: Đưa tên công ty/nhà sản xuất lên trước tiêu đề sổ tay:
  `[x] Schneider Electric, *Electrical Installation Guide...*`
  `[x] ABB Drives, *Technical Guide No. 6...*`
- **ĐÚNG THEO CHUẨN IEEE (Mục I)**: Bắt đầu bằng **TÊN SỔ TAY/TÀI LIỆU IN NGHIÊNG**, sau đó mới đến tên công ty và địa điểm:
  `[v] *Name of Manual/Handbook*, x ed., Abbrev. Name of Co., City of Co., Abbrev. State, Country, year.`
  *Ví dụ*:
  `[3] *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, Rueil-Malmaison, France, 2018.`
  `[4] *Technical Guide No. 6: Guide to Harmonics with AC Drives*, ABB Oy, Helsinki, Finland, Tech. Guide 3BFE64292714, 2011.`

### 3. BÁO CÁO KỸ THUẬT / SÁCH TRẮNG (Technical Reports & White Papers)
- **LỖI SAI**: In nghiêng tiêu đề báo cáo kỹ thuật.
- **ĐÚNG THEO CHUẨN IEEE (Mục N)**: Tiêu đề báo cáo kỹ thuật **BẮT BUỘC ĐẶT TRONG DẤU NGOẶC KÉP `“...”`**, KHÔNG in nghiêng. Tên tác giả hoặc cơ quan ban hành đứng đầu (hoặc sau), kèm mã số báo cáo `Rep. xxx`:
  `[v] J. K. Author or Corporate Author, “Title of report,” Organization/Company, Location, Rep. no. xxx, year.`
  *Ví dụ*:
  `[5] “Improving motor and drive system performance: A sourcebook for industry,” US Department of Energy (DOE), Washington, DC, USA, Rep. DOE/GO-102014-4421, 2014.`

### 4. BÀI BÁO TẠP CHÍ / KHOA HỌC (Periodicals)
- **ĐÚNG (Mục M)**: Tên bài báo trong ngoặc kép, tên tạp chí in nghiêng viết tắt chính thức:
  `[v] J. K. Author, “Title of paper,” *Abbrev. Title of Periodical*, vol. x, no. x, pp. xxx–xxx, Abbrev. Month, year, doi: xxx.`

### 5. SÁCH CHUYÊN KHẢO (Books)
- **ĐÚNG (Mục B)**: Tên sách in nghiêng, tên tác giả viết tắt chữ cái đầu + họ:
  `[v] J. K. Author, *Title of Book*, xth ed. City of Publisher, Country: Abbrev. Publisher, year.`

### 6. TRANG WEB / BLOG (Websites)
- **ĐÚNG (Mục T)**: Tên tác giả. “Tiêu đề trang.” Tên Website. Ngày truy cập. [Online]. Available: URL.
  `[v] J. Smith. “Page title.” CNN.com. Accessed: Feb. 1, 2009. [Online]. Available: http://www.url.com`

### 7. TÊN TÁC GIẢ & THỜI GIAN
- Viết tắt chữ cái đầu: `J. K. Author` (không viết `Author, J. K.` trừ bảng tra cứu đặc biệt).
- Không dùng dấu phẩy cho hậu tố: `Michael Smith Jr.`, `Lucas Molignaro III`.
- Tối đa 6 tác giả liệt kê đầy đủ; trên 6 tác giả dùng: `First Author et al.`
- Không có ngày tháng: ghi `(n.d.)`.
- Dải trích dẫn trong văn bản: Viết rõ từng số `[1], [2], [3]`, KHÔNG dùng gạch nối `[1]–[3]`.

---

# 2B. MA TRẬN NHẬN DIỆN LOẠI TÀI LIỆU & CẤU TRÚC ĐẶT TÊN CHUẨN IEEE (SOURCE CLASSIFICATION & NAMING MASTER MATRIX)

> [!IMPORTANT]
> **NGUYÊN TẮC BẮT BUỘC DÀNH CHO AGENT**:
> 1. Chuẩn trích dẫn IEEE **phụ thuộc 100% vào loại hình tài liệu (Document Type)**. Một bài blog kỹ thuật không thể định dạng như một bài báo khoa học; một tiêu chuẩn quốc tế không thể định dạng như một báo cáo kỹ thuật.
> 2. Trước khi trích dẫn, Agent **BẮT BUỘC PHẢI NHẬN DIỆN VÀ PHÂN LOẠI** tài liệu mình đang sử dụng thuộc nhóm nào trong 10 nhóm dưới đây.
> 3. Tuyệt đối không quy đồng tất cả tài liệu có link mạng thành "Website", và không biến tất cả tài liệu dạng PDF thành "Report" hay "Paper".

### 1. BẢNG MA TRẬN NHẬN DIỆN 10 LOẠI TÀI LIỆU KỸ THUẬT (CLASSIFICATION MASTER MATRIX)

| Mã loại (Type Key) | Loại hình tài liệu | Dấu hiệu nhận diện đặc trưng (Identification Signatures) | Quy tắc kiểu chữ (Typography) | Cấu trúc đặt tên chuẩn IEEE (Naming Syntax) |
|---|---|---|---|---|
| `BLOG_POST` | **Bài viết Blog Kỹ thuật** | Đăng trên trang blog kỹ thuật (hãng, tổ chức, chuyên gia), có tiêu đề bài, tên blog, ngày đăng cụ thể, URL bài viết. Không có vol/no/issue. | - Tên bài: trong ngoặc kép `"..."`<br>- Tên blog: in nghiêng `*...*` | `[n] F. M. Lastname, “Title of post,” *Name of Blog*, Month Day, Year. Accessed: Month Day, Year. [Online]. Available: URL`<br>*(Nếu tác giả là công ty/tổ chức: thay F. M. Lastname bằng Company Name)* |
| `WEB_ARTICLE` | **Bài viết Trang Web / Cổng thông tin** | Trang thông tin, bài giải thích, tin tức kỹ thuật trên website chính thức của tổ chức/hãng; không thuộc chuyên mục blog; có URL. | - Tên bài: trong ngoặc kép `"..."`<br>- Tên website: in nghiêng `*...*` | `[n] Organization Name, “Title of webpage,” *Website Title*, Month Day, Year (nếu có). Accessed: Month Day, Year. [Online]. Available: URL` |
| `JOURNAL_PAPER` | **Bài báo Tạp chí Khoa học (Periodicals)** | Đăng trong tạp chí khoa học chuyên ngành có bình duyệt (IEEE Trans, Elsevier...); có số tập (vol.), số kỳ (no.), trang (pp.), mã DOI. | - Tên bài: trong ngoặc kép `"..."`<br>- Tên tạp chí: in nghiêng viết tắt `*...*` | `[n] F. M. Lastname, “Title of paper,” *Abbrev. Title of Periodical*, vol. x, no. x, pp. xxx–xxx, Abbrev. Month, Year, doi: 10.xxxx/xxxxx.` |
| `CONF_PAPER` | **Bài báo Hội nghị Khoa học (Proceedings)** | Xuất bản trong kỷ yếu hội thảo / hội nghị khoa học; có cụm từ "Proceedings", "Conference", địa điểm tổ chức (Thành phố, Quốc gia). | - Tên bài: trong ngoặc kép `"..."`<br>- Tên kỷ yếu hội nghị: in nghiêng `in *Proc. ...*` | `[n] F. M. Lastname, “Title of paper,” in *Proc. Abbrev. Conf. Title*, City, State/Country, Year, pp. xxx–xxx, doi: xx.xxxx/xxxxx.` |
| `STANDARD` | **Tiêu chuẩn Kỹ thuật (IEEE, IEC, ISO, TCVN)** | Tài liệu chuẩn hóa chính thức do các tổ chức tiêu chuẩn ban hành; có mã chuẩn rõ ràng (IEEE Std, IEC Standard, ISO, TCVN). | - **Tên tiêu chuẩn: BẮT BUỘC in nghiêng `*...*` đứng đầu!**<br>- Không đưa tên tổ chức lên trước tiêu đề. | `[n] *Title of Standard*, Standard number, Year.`<br>*(Bản online: thêm Accessed date & Available: URL)* |
| `MANUAL` | **Sổ tay Kỹ thuật & Cẩm nang Hãng (Manuals/Guides)** | Sách hướng dẫn lắp đặt, vận hành, cẩm nang ứng dụng của hãng (Schneider, ABB, Siemens...); có từ Manual, Guide, Handbook, Doc ID. | - **Tên sổ tay: BẮT BUỘC in nghiêng `*...*` đứng đầu!**<br>- Không đưa tên hãng lên trước tiêu đề. | `[n] *Name of Manual/Handbook*, Edition/Revision (nếu có), Abbrev. Company Name, City, Country, Year, Mã tài liệu (nếu có).` |
| `TECH_REPORT` | **Báo cáo Kỹ thuật & Sách trắng (Reports/White Papers)** | Báo cáo của cơ quan nhà nước, viện nghiên cứu (US DOE, NREL, EPRI) hoặc White Paper của hãng; thường có mã số báo cáo `Rep. xxx`. | - **Tên báo cáo: BẮT BUỘC đặt trong ngoặc kép `"..."`**, KHÔNG in nghiêng. | `[n] F. M. Lastname hoặc Corporate Author, “Title of report in double quotes,” Organization Name, City, State/Country, Rep. [Report Number], Year.` |
| `BOOK` | **Sách Chuyên khảo & Giáo trình (Books/Monographs)** | Sách in hoặc giáo trình hoàn chỉnh của nhà xuất bản uy tín (McGraw-Hill, Wiley, Springer); có số tái bản (ed.), nơi xuất bản, nhà xuất bản. | - **Tên sách: BẮT BUỘC in nghiêng `*...*`**<br>- Tên tác giả đứng đầu. | `[n] F. M. Lastname, *Title of Book*, xth ed. City of Publisher, Country: Publisher Name, Year.` |
| `DATASHEET` | **Bảng Thông số Kỹ thuật (Datasheets/Specifications)** | Tài liệu tóm tắt thông số kỹ thuật, bảng giá trị định mức của thiết bị hoặc linh kiện cụ thể (2-10 trang). | - Tên linh kiện/thiết bị: trong ngoặc kép `"..."` | `[n] Company Name, “Product Name: Datasheet,” Document ID / Cat. No., Month Year. Accessed: Month Day, Year. [Online]. Available: URL` |
| `THESIS` | **Luận văn & Luận án (Theses/Dissertations)** | Luận văn thạc sĩ (M.S. thesis) hoặc luận án tiến sĩ (Ph.D. dissertation) bảo vệ tại trường đại học. | - Tên luận văn: trong ngoặc kép `"..."` | `[n] F. M. Lastname, “Title of thesis,” Degree type, Dept. Name, Univ. Name, City, State/Country, Year.` |

---

### 2. VÍ DỤ THỰC TẾ CHI TIẾT CHO TỪNG LOẠI TÀI LIỆU

#### 2.1. Loại `BLOG_POST` (Bài viết Blog kỹ thuật)
- **Tác giả cá nhân**:  
  `[1] J. Smith, “Understanding total harmonic distortion in industrial power,” *Schneider Electric Blog*, Oct. 15, 2023. Accessed: Mar. 10, 2026. [Online]. Available: https://blog.se.com/energy-management/understanding-thd/`
- **Tác giả doanh nghiệp/tổ chức**:  
  `[2] ABB Drives, “How variable speed drives improve motor efficiency,” *ABB Conversations*, Jan. 20, 2024. Accessed: Feb. 15, 2026. [Online]. Available: https://conversations.abb.com/vfd-efficiency/`

#### 2.2. Loại `WEB_ARTICLE` (Bài viết Trang web chính thức)
- `[3] U.S. Department of Energy, “Advanced manufacturing: Motor systems,” *Energy.gov*, Nov. 2021. Accessed: Jan. 12, 2026. [Online]. Available: https://www.energy.gov/eere/amo/motor-systems`

#### 2.3. Loại `JOURNAL_PAPER` (Bài báo Tạp chí Khoa học)
- `[4] H. Akagi, “Active harmonic filters for power conditioning,” *IEEE Trans. Ind. Appl.*, vol. 32, no. 6, pp. 1312–1322, Nov./Dec. 1996, doi: 10.1109/28.556635.`

#### 2.4. Loại `CONF_PAPER` (Bài báo Kỷ yếu Hội nghị)
- `[5] M. Barnes and K. Wong, “Field evaluation of harmonic resonance in industrial facilities,” in *Proc. IEEE Ind. Appl. Soc. Annu. Meeting*, Seattle, WA, USA, 2017, pp. 120–126.`

#### 2.5. Loại `STANDARD` (Tiêu chuẩn Kỹ thuật)
- `[6] *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022.`
- `[7] *Electromagnetic Compatibility (EMC) - Part 2-4: Compatibility Levels in Industrial Plants for Low-Frequency Conducted Disturbances*, IEC Standard 61000-2-4, 2002.`

#### 2.6. Loại `MANUAL` (Sổ tay Kỹ thuật & Cẩm nang Hãng)
- `[8] *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, Rueil-Malmaison, France, 2018.`
- `[9] *Technical Guide No. 6: Guide to Harmonics with AC Drives*, ABB Oy, Helsinki, Finland, Tech. Guide 3BFE64292714, 2011.`

#### 2.7. Loại `TECH_REPORT` (Báo cáo Kỹ thuật & Sách trắng)
- `[10] “Improving motor and drive system performance: A sourcebook for industry,” US Department of Energy (DOE), Washington, DC, USA, Rep. DOE/GO-102014-4421, 2014.`
- `[11] Schneider Electric, “Power factor correction and harmonic filtering in low voltage installations,” Schneider Electric, Grenoble, France, White Paper 998-2018-05, 2018.`

#### 2.8. Loại `BOOK` (Sách Chuyên khảo)
- `[12] R. C. Dugan, M. F. McGranaghan, and H. W. Beaty, *Electrical Power Systems Quality*, 3rd ed. New York, NY, USA: McGraw-Hill, 2012.`

#### 2.9. Loại `DATASHEET` (Bảng Thông số Sản phẩm)
- `[13] ABB, “ACS880 single drives: Technical catalog,” Doc. 3AUA0000098111 Rev. H, May 2021. Accessed: Jan. 15, 2026. [Online]. Available: https://library.e.abb.com/...`

#### 2.10. Loại `THESIS` (Luận án / Luận văn)
- `[14] T. V. Nguyen, “Harmonic mitigation techniques in variable frequency drive systems,” Ph.D. dissertation, Dept. Elect. Eng., Hanoi Univ. Sci. Technol., Hanoi, Vietnam, 2020.`

---

### 3. QUY TRÌNH 4 BƯỚC NHẬN DIỆN VÀ ĐẶT TÊN DÀNH CHO AGENT (AGENT ACTION WORKFLOW)

```text
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 1: GIÁM ĐỊNH NGUỒN GỐC (Source Inspection)             │
│ - Đọc trang bìa (Title page), Header/Footer, URL, Metadata  │
│ - Trả lời: Có số chuẩn Std? Có Vol/No/DOI? Là Blog hay PDF? │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 2: GÁN NHÃN LOẠI TÀI LIỆU (Classification Tagging)     │
│ - Ghi rõ nhãn: `STANDARD`, `MANUAL`, `JOURNAL_PAPER`,       │
│   `BLOG_POST`, `TECH_REPORT`, `BOOK`, `DATASHEET`           │
│ - Lưu vào cột `Loại tài liệu` trong `evidence_dossier.md`   │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 3: ÁP DỤNG KHUÔN MẪU IEEE TƯƠNG ỨNG (Apply Template)   │
│ - Lấy mẫu cấu trúc chuẩn của đúng loại hình đã gán nhãn     │
│ - Tuyệt đối tuân thủ quy tắc in nghiêng vs đặt trong ngoặc  │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 4: THẨM ĐỊNH CHÉO ĐỘC LẬP (Tech Review Audit)          │
│ - Tech Review Agent kiểm tra: Có gán sai bản chất tài liệu? │
│ - Nếu sai cấu trúc IEEE của loại đó -> REJECT (Từ chối duyệt)│
└─────────────────────────────────────────────────────────────┘
```

---

# 3. IEEE IN-TEXT CITATION RULES

## 3.1. Citation form

Use square-bracket numeric citations:

```text
[1]
[2]
[3]
```

Example:

```text
The motor current does not necessarily vary linearly with shaft load over the complete operating range [1].
```

---

## 3.2. Citation position

Place the citation **inside the punctuation**.

Correct:

```text
... operating range [1].
```

Incorrect:

```text
... operating range. [1]
```

---

## 3.3. Multiple citations

Write every reference number explicitly.

Correct:

```text
[1], [2], [3], [4]
```

Do not use a reference range:

```text
[1]–[4]
```

---

## 3.4. Citation with author or organization in the sentence

Allowed:

```text
Smith [4] reported that ...
```

```text
According to the U.S. Department of Energy [5], ...
```

For three or more author names in an in-text attribution:

```text
Wood et al. [7] ...
```

Do not repeatedly name the publisher when a neutral citation is clearer.

Default style for technical web content:

```text
Technical claim [n].
```

Use explicit attribution when the identity of the organization or author is materially relevant.

---

## 3.5. VERIFIED LOCATOR ONLY — LOCKED POLICY

The Agent may use a detailed IEEE source locator **only when that locator has been directly verified from the referenced source**.

Allowed source-level citation:

```text
[1]
[2]
[1], [2]
```

Allowed detailed citation **only when verified**:

```text
[1, p. 8]
[2, pp. 3–4]
[3, eq. (1)]
[4, Sec. 4.5]
[5, Fig. 2]
[1, p. 8], [2, p. 3]
```

The Agent must never infer, estimate, reconstruct, approximate, or fabricate a locator.

If the source supports a claim but the exact location has not been verified, the Agent must cite only:

```text
[n]
```

Required decision rule:

```text
Source supports claim?
        │
        ├── NO
        │    ↓
        │  Do not use this source for the claim
        │
        └── YES
             ↓
       Locator verified?
             │
        ┌────┴────┐
        │         │
       YES        NO
        │         │
        ↓         ↓
[n, locator]     [n]
```

The Agent is not required to add a locator. A correct source-level citation `[n]` is preferred over an unverified detailed citation.

Detailed source location may be recorded internally even when it is not published.


# 4. NUMBERING RULES

## 4.1. First appearance controls the number

The first source cited in the article becomes:

```text
[1]
```

The next new source becomes:

```text
[2]
```

and so on.

---

## 4.2. Reuse the same number

If the same source appears again later, reuse its existing number.

Example:

```text
First claim from Source A [1].

Claim from Source B [2].

Another claim from Source A [1].
```

Do not create a new number for the same source.

---

## 4.3. One reference number = one source

Never combine several sources under one reference number.

Incorrect:

```text
[5] ABB manual; Siemens manual; DOE report.
```

Correct:

```text
[5] ABB manual...
[6] Siemens manual...
[7] DOE report...
```

---

## 4.4. Do not use ibid. or op. cit.

Reuse the previous numeric reference number.

Correct:

```text
Earlier claim from Source A [3].

Later claim from the same Source A [3].
```

If a verified locator is useful:

```text
Earlier claim from Source A [3, p. 8].

Later claim from the same Source A [3, p. 12].
```

Do not use:

```text
ibid.
op. cit.
```

Never create a locator merely because the same source was cited previously.


# 5. WHEN CITATION IS REQUIRED

The Agent must cite the original source when the article uses or paraphrases:

- ideas;
- processes;
- arguments;
- conclusions;
- technical methods;
- formulas from a source;
- measured data;
- research results;
- numerical values;
- threshold values;
- limits;
- standard requirements;
- manufacturer recommendations;
- specifications;
- graphics;
- tables;
- datasets;
- technical interpretations substantially derived from another source.

Citation is also required for direct quotation.

For technical web content, direct quotation should normally be minimized and paraphrase should be preferred unless exact wording is materially necessary.

---

# 6. SOURCE REGISTRY

Before writing final references, the Agent must create an internal Source Registry.

Minimum structure:

```yaml
source_id: SRC-001
source_type: WEBSITE
title: ""
authors: []
corporate_author: ""
website_or_publication: ""
publisher: ""
publication_date: ""
edition: ""
version: ""
revision: ""
document_number: ""
standard_number: ""
volume: ""
issue: ""
pages: ""
article_number: ""
conference_name: ""
location: ""
report_number: ""
doi: ""
url: ""
accessed_date: ""
locator_type: ""
locator_value: ""
document_page: ""
pdf_page_index: ""
locator_verification_status: LOCATOR_VERIFIED | LOCATOR_UNAVAILABLE | LOCATOR_NOT_CHECKED | LOCATOR_CONFLICT
verification_status: VERIFIED | PARTIAL | UNVERIFIED
notes: ""
```

Only fields applicable to the source type are required.

Do not invent missing metadata.

If a required element cannot be verified, preserve the known metadata and flag the missing item.

---

# 7. SOURCE-TYPE CLASSIFICATION

The Agent must classify each source before creating its IEEE entry.

Use the following decision logic.

---

## 7.1. JOURNAL / PERIODICAL ARTICLE

Use when the source is an article published in:

- journal;
- transaction;
- letters;
- formal magazine/periodical;
- peer-reviewed periodical.

Typical metadata:

```text
Author(s)
Paper title
Periodical title
Volume
Issue
Pages or article number
Month/year
DOI
```

Do not cite Google Scholar, ResearchGate, PubMed, or a search engine as the source if the original paper can be identified.

---

## 7.2. CONFERENCE PAPER / PROCEEDINGS

Use when the work was presented or published in a conference/proceedings.

Typical metadata:

```text
Author(s)
Paper title
Conference title
Location if applicable
Year
Pages
DOI
URL if online
```

---

## 7.3. WEBSITE / WEB ARTICLE / BLOG POST

Use when the source is principally a webpage.

This includes:

- official organization webpage;
- manufacturer webpage;
- engineering blog article;
- company blog post;
- technical web article;
- news webpage;
- institutional webpage.

A Blog is normally classified as:

```text
WEBSITE
```

unless it has formal periodical metadata making another IEEE source category more appropriate.

Typical metadata:

```text
Author(s) or corporate author
Page/article title
Website title
Accessed date
URL
```

---

## 7.4. MANUAL / HANDBOOK / PRODUCT DOCUMENTATION

Use when the source is:

- user manual;
- installation manual;
- programming manual;
- technical manual;
- handbook;
- operating instruction;
- engineering guide clearly issued as documentation.

Preserve technical identity when available:

```text
Edition
Version
Revision
Document number
Firmware/software applicability
Publication year
```

Do not reduce a technical manual to a generic WEBSITE reference merely because the manual is hosted online.

---

## 7.5. DATASHEET / APPLICATION NOTE / TECHNICAL NOTE

IEEE does not require the Agent to pretend every technical PDF is a journal paper.

Classify based on the actual publication identity.

Recommended mapping:

```text
Datasheet / application note / technical note
        ↓
MANUAL / REPORT style, depending on how the publisher identifies the document
```

Preserve:

```text
Company
Document title
Document number
Revision/version
Date
Accessed date
URL
```

Do not invent a report number.

---

## 7.6. TECHNICAL REPORT / WHITE PAPER

Use when the source is formally issued as:

- technical report;
- research report;
- white paper;
- government report;
- organization report.

Typical metadata:

```text
Author(s) / corporate author
Report title
Organization/company
Location if available
Report number if available
Date/year
URL for online version
Accessed date where applicable
```

---

## 7.7. STANDARD

Use when citing a formal technical standard.

Typical metadata:

```text
Full title of standard
Standard number
Corporate author / standards organization when applicable
Location if applicable
Edition/year/date
```

Examples of source families:

```text
IEC
IEEE
ISO
ANSI
NFPA
NEMA
EN
BS
TCVN
```

The Agent must identify the exact standard part/version used.

Do not cite only a family such as:

```text
IEC 60034
```

if the claim comes from a specific part such as:

```text
IEC 60034-xx
```

Preserve edition/year when verified.

---

## 7.8. BOOK / MONOGRAPH

Use when citing a published book.

Typical metadata:

```text
Author(s)
Book title
Edition
Volume if applicable
Publisher location
Publisher
Year
Pages when relevant
```

---

## 7.9. BOOK CHAPTER

Use when citing a specific chapter in an edited/published book.

Typical metadata:

```text
Chapter author
Chapter title
Book title
Edition
Editor(s)
Publisher
Year
Chapter/section/pages
```

---

## 7.10. DATASET

Use when a dataset itself supports the claim, graph, table, or calculation.

Prefer:

```text
DOI
```

when the dataset has one.

Otherwise use the repository/website URL with the appropriate online metadata.

Do not cite only the paper describing the dataset when the article actually uses data from the separate dataset and the dataset has its own citation identity.

---

## 7.11. THESIS / DISSERTATION

Use when the source is a:

```text
M.S. thesis
Ph.D. dissertation
```

Typical metadata:

```text
Author
Title
Degree type
Department
University
City/state/country
Year
URL if online
```

---

## 7.12. PREPRINT / arXiv

Use when the article relies on a preprint that does not yet have a final publication of record.

Typical metadata:

```text
Author(s)
Title
Year
arXiv identifier
```

If the final peer-reviewed version of record exists and supports the same claim, prefer citing the final publication rather than the preprint.

---

## 7.13. PATENT

Use Patent format.

Preserve:

```text
Inventor(s)
Patent title
Country
Patent number
Issued date
```

If online, include the online locator according to IEEE online patent style.

---

## 7.14. ONLINE VIDEO

Use when information is taken from a video source.

Typical metadata:

```text
Video owner/creator
Location if available
Video title
Release date
Accessed date
URL
```

Use a video only when the relevant claim is genuinely sourced from the video.

---

## 7.15. COURSE / LECTURE / LECTURE NOTES

Use the IEEE Course/Lecture/Lecture Notes category when applicable.

Do not convert formal lecture notes into WEBSITE solely because they are downloadable online.

---

## 7.16. LEGAL / GOVERNMENT DOCUMENT

Use the IEEE legal citation category when the source is legislation, regulation, court material, or another legal authority.

Do not force legal documents into ordinary WEBSITE style if IEEE defines a legal reference form for the source.

---

## 7.17. UNKNOWN / AMBIGUOUS SOURCE TYPE

If the Agent cannot confidently classify the source:

```text
DO NOT GUESS
```

Required action:

1. inspect the source title page / metadata / publisher page;
2. determine how the publisher identifies the document;
3. choose the closest IEEE-documented source category;
4. record uncertainty in the Source Registry;
5. do not invent missing bibliographic metadata.

---

# 8. IEEE REFERENCE TEMPLATES

The following templates are normalized operational templates for Agents.

Agents should fill only verified fields.

---

## 8.1. Website / Blog / Web Article

```text
[n] F. M. Lastname. “Page title.” Website Title. Accessed: Mon. day, year. [Online]. Available: URL
```

Corporate author:

```text
[n] Organization Name. “Page title.” Website Title. Accessed: Mon. day, year. [Online]. Available: URL
```

If no individual author is provided, do not invent one.

---

## 8.2. Manual / Handbook

### Manual (Print)
```text
[n] Name of Manual/Handbook, x ed., Abbrev. Name of Co., City of Co., Abbrev. State, Country, year, pp. xxx–xxx.
```

### Manual (Online)
```text
[n] Name of Manual/Handbook, x ed., Abbrev. Name of Co., City of Co., Abbrev. State, Country, year. Accessed: Mon. day, year. [Online]. Available: URL
```
Or when authored by an individual:
```text
[n] J. K. Author. Name of Manual/Handbook, x ed. (year). Accessed: Mon. day, year. [Online]. Available: URL
```

For engineering use, preserve verified:

```text
Document no.
Revision
Edition
Version
Applicable firmware/software version
```

when they materially identify the source.


---

## 8.3. Journal / Periodical With DOI

```text
[n] F. M. Lastname, “Title of paper,” Abbrev. Title of Periodical, vol. x, no. x, pp. xxx–xxx, Mon. year, doi: xx.xxxx/xxxxx.
```

With article number:

```text
[n] F. M. Lastname, “Title of paper,” Abbrev. Title of Periodical, vol. x, no. x, Mon. year, Art. no. xxxxxxx, doi: xx.xxxx/xxxxx.
```

Do not invent an IEEE abbreviation for a journal.

Use the official abbreviation when verified.

---

## 8.4. Conference Paper

Published proceedings:

```text
[n] F. M. Lastname, “Title of paper,” in Abbrev. Name of Conf., City, State/Country if applicable, year, pp. xxx–xxx.
```

If DOI exists, append the verified DOI in the appropriate IEEE form.

For online conference material, include online metadata when the source is used as an online publication.

---

## 8.5. Technical Report

```text
[n] F. M. Lastname or Corporate Author, “Title of report,” Organization/Company, City, State/Country if available, Rep. no. xxx if available, year.
```

Online report:

```text
[n] F. M. Lastname or Corporate Author, “Title of report,” Organization/Company, report number if available, date/year. Accessed: Mon. day, year. [Online]. Available: URL
```

---

## 8.6. Standard

Basic IEEE forms (Tiêu đề in nghiêng BẮT BUỘC đứng đầu, KHÔNG bắt đầu bằng tên tổ chức):

```text
[n] Title of Standard, Standard number, date.
```

or:

```text
[n] Title of Standard, Standard number, Corporate author, location, date.
```

Online standard:

```text
[n] Title of Standard, Standard number, date. [Online]. Available: URL
```

Examples:
- `[1] IEEE Criteria for Class IE Electric Systems, IEEE Standard 308, 1969.`
- `[2] IEEE Standard for Harmonic Control in Electric Power Systems, IEEE Std 519-2022, 2022.`
- `[3] Electromagnetic Compatibility (EMC) - Part 2-4: Compatibility Levels in Industrial Plants for Low-Frequency Conducted Disturbances, IEC Standard 61000-2-4, 2002.`

For an online official landing page, retain the verified standard identity first; add the online locator only when appropriate.

Never replace the standard identity with a generic webpage title.


---

## 8.7. Book

```text
[n] F. M. Lastname, Book Title, xth ed. City, State/Country: Publisher, year.
```

Add volume/pages when relevant.

---

## 8.8. Book Chapter

```text
[n] F. M. Lastname, “Chapter title,” in Book Title, xth ed., Editor information if applicable. City, State/Country: Publisher, year, pp. xxx–xxx.
```

---

## 8.9. Thesis / Dissertation

M.S.:

```text
[n] F. M. Lastname, “Title of thesis,” M.S. thesis, Dept., Univ., City, State/Country, year.
```

Ph.D.:

```text
[n] F. M. Lastname, “Title of dissertation,” Ph.D. dissertation, Dept., Univ., City, State/Country, year.
```

---

## 8.10. Preprint / arXiv

```text
[n] F. M. Lastname, “Title of paper,” year, arXiv:identifier.
```

---

## 8.11. Patent

```text
[n] F. M. Lastname, “Title of patent,” Country Patent number, Mon. day, year.
```

Use the issued date when several patent dates are shown.

---

## 8.12. Online Video

```text
[n] Owner/Creator, Location if available. Title of Video. (Release date). Accessed: Mon. day, year. [Online Video]. Available: URL
```

---

## 8.13. Dataset

Use the IEEE Dataset category.

Operational priority:

```text
Dataset citation supplied by repository
        ↓
Verify metadata
        ↓
Format to IEEE
```

Prefer DOI when available.

Do not substitute the dataset repository homepage for the dataset record.

---

# 9. AUTHOR-NAME RULES

## 9.1. Reference list

Use initials before family name:

```text
J. K. Author
```

Do not write:

```text
Author, John K.
```

unless a specific IEEE source category explicitly requires otherwise.

---

## 9.2. Number of authors

For IEEE publications:

```text
Up to 6 authors:
list all authors.

More than 6 authors:
first author + et al.
```

For non-IEEE publications, use verified author information; do not create missing names.

---

## 9.3. Corporate author

Use the official organization name when the source is authored by an organization.

Examples of valid concept:

```text
International Electrotechnical Commission
U.S. Department of Energy
Siemens AG
ABB
```

Do not invent a person as the author of a corporate document.

---

# 10. TITLE AND PUBLICATION RULES

## 10.1. Preserve the actual source title

Do not rewrite a source title for SEO or readability.

Reference metadata must reflect the source.

---

## 10.2. Journal abbreviation

Use the official periodical abbreviation where IEEE requires it.

Do not create an abbreviation from memory.

---

## 10.3. DOI

If a journal/conference paper has a DOI:

```text
use the DOI
```

Do not cite:

```text
Google search URL
Google Scholar search URL
ResearchGate search page
```

in place of the DOI/original publication.

---

# 11. ONLINE-SOURCE RULES

For online sources, capture:

```text
Original URL
Accessed date
```

when required by the IEEE source format.

The Agent must cite the actual page/document used.

Do not cite:

- search result pages;
- AI-generated summaries;
- URL shorteners;
- tracking redirects;
- cached snippets;

when the original source is available.

---

# 12. SPECIAL RULES FOR TECHNICAL DOCUMENTATION

Technical content frequently uses manufacturer documentation.

For these sources, the Agent must preserve all verified identifiers that materially affect applicability:

```text
Document number
Edition
Revision
Version
Publication date
Firmware version
Software version
Product family
```

Example logic:

```text
Same title
+
different revision
=
potentially different source
```

Do not silently merge two revisions into one reference.

---

# 13. STANDARD-SPECIFIC RULES

When using a standard:

1. identify the exact standard number;
2. identify the part/subpart;
3. identify edition/year if verified;
4. identify the standards organization;
5. use the exact standard title;
6. if a clause/section is directly verified from the standard and helps review, the Agent may publish a detailed locator such as `[n, Sec. x]`;
7. if the clause/section is not verified, cite only `[n]`;
8. never infer or fabricate a clause/section locator;
9. do not infer requirements from a third-party blog when the article claims that the requirement comes from the standard.

If the Agent has only a secondary source describing the standard, cite that secondary source unless the actual standard has been verified.

---

# 14. BLOG-SOURCE RULE

A technical Blog is allowed as a source.

Citation behavior:

```text
Blog post
    ↓
Classify as WEBSITE
    ↓
Author or corporate author
    ↓
Post title
    ↓
Website/blog title
    ↓
Accessed date
    ↓
URL
```

However:

```text
Correct IEEE formatting
≠
technical authority
```

Whether the blog is sufficiently reliable for the claim is handled by the Research / Evidence workflow.

---

# 15. FIGURES, TABLES, AND DATA

If content:

- copies;
- adapts;
- redraws;
- summarizes;
- recalculates

a figure/table/dataset from another source, citation is required.

Examples:

If the exact source figure is verified:

```text
Adapted from [4, Fig. 6].
```

If only the source itself is verified:

```text
Adapted from [4].
```

For source data:

```text
Source data: [5].
```

For multiple verified sources:

```text
Compiled from [2], [3], [7].
```

Never add a figure/table/page locator unless it has been directly verified from the source.

Citation does not automatically grant copyright permission.

Copyright/reuse permission must be evaluated separately.

---

# 16. FORMULA CITATION

## 16.1. Formula directly taken from a source

Cite it.

Example:

```text
The load factor is calculated using the method described in [3]:
...
```

If the referenced source explicitly labels the formula and the equation number has been verified, a locator such as `[3, eq. (2)]` is allowed.

If the equation number has not been verified, cite only `[3]`.

The Agent must never assign its own equation number to the source.

---

## 16.2. Formula adapted or transformed from a source

Cite the supporting source and explain the transformation when relevant.

---

## 16.3. Formula derived entirely within the article

No fake citation is required for the algebraic derivation itself.

However, any externally sourced assumptions, coefficients, limits, or input data still require citations.

---

# 17. THRESHOLD / LIMIT CITATION

All externally sourced engineering thresholds must be cited.

Examples:

```text
< 50%
> 5%
±10%
80 °C
PF < 0.8
```

When used as:

- evaluation criterion;
- limit;
- recommended threshold;
- alarm condition;
- replacement criterion;
- design rule;

the Agent must capture:

```text
value
+
context
+
source
+
applicability
```

Do not convert a context-specific recommendation into a universal rule.

---

# 18. AGENT WORKFLOW

## STEP 1 — COLLECT SOURCES

Research may use any source type permitted by the task.

Do not format references yet.

---

## STEP 2 — REGISTER SOURCES

Create a Source Registry entry for every source actually considered for use.

---

## STEP 3 — CLASSIFY SOURCE TYPE

Assign the closest IEEE source category.

Examples:

```text
manufacturer web article → WEBSITE
engineering blog → WEBSITE
manufacturer programming manual → MANUAL
application note → MANUAL or REPORT based on publisher identity
IEEE journal paper → PERIODICAL
conference paper → CONFERENCE
IEC standard → STANDARD
DOE technical report → REPORT
arXiv manuscript → PREPRINT
dataset record → DATASET
```

---

## STEP 4 — VERIFY METADATA

Verify fields needed by the selected source type.

Do not hallucinate missing metadata.

---

## STEP 5 — WRITE WITH TEMPORARY SOURCE IDs

During drafting, the Agent may internally use:

```text
[SRC-001]
[SRC-002]
```

This prevents citation-number corruption while content is still moving.

These temporary IDs must not appear in the final article.

---

## STEP 6 — ATTACH CITATION TO THE CLAIM

Every claim requiring evidence must map to one or more Source IDs.

Default published citation:

```text
[n]
```

If a locator has been directly verified and improves review:

```text
[n, p. x]
[n, pp. x–y]
[n, eq. (x)]
[n, Sec. x]
[n, Fig. x]
```

Before publishing a locator, the Agent must pass the Locator Verification Gate.


## STEP 7 — FINALIZE ARTICLE STRUCTURE

Only after the article structure is stable should citation numbering be finalized.

---

## STEP 8 — NUMBER BY FIRST APPEARANCE

Convert:

```text
SRC-004 → [1]
SRC-002 → [2]
SRC-009 → [3]
```

based on the first occurrence in the final article.

---

## STEP 9 — RENDER REFERENCE LIST

Generate one IEEE-formatted reference entry per cited source.

---

## STEP 10 — RUN CITATION AUDIT

The Agent must not mark the article as citation-complete until the audit passes.

---

# 19. CITATION AUDIT

Check all of the following.

## 19.1. Orphan citation

Citation exists in text but no reference entry exists.

```text
FAIL
```

---

## 19.2. Unused reference

Reference exists but is never cited.

```text
FAIL
```

---

## 19.3. Duplicate source numbers

Same source has multiple reference numbers.

```text
FAIL
```

---

## 19.4. Duplicate number

Different sources use the same number.

```text
FAIL
```

---

## 19.5. Numbering gap

Example:

```text
[1], [2], [4]
```

without `[3]`.

```text
FAIL
```

---

## 19.6. Wrong first-appearance order

Example:

```text
[4]
```

appears before the first occurrence of `[2]`.

```text
FAIL
```

unless previous numbers genuinely appeared earlier in the final content.

---


## 19.7. Unverified locator in in-text citation

A detailed locator is valid only when its location has been directly verified from the referenced source.

Examples:

```text
[1, p. 8]
[1, pp. 8–10]
[1, eq. (1)]
[1, Sec. 4.5]
[1, Fig. 2]
[1, Table 3]
```

Audit rule:

```text
Locator verified from source → PASS
Locator not verified → FAIL
Locator inferred / estimated / reconstructed → FAIL
```

If locator verification fails, downgrade the citation to:

```text
[1]
```

and keep any uncertain location information out of the published article.


## 19.8. Range citation

Example:

```text
[1]–[5]
```

```text
FAIL
```

Convert to:

```text
[1], [2], [3], [4], [5]
```

---

## 19.9. Citation outside punctuation

```text
Claim. [1]
```

```text
FAIL
```

Correct:

```text
Claim [1].
```

---

## 19.10. Combined references

More than one source under one reference number.

```text
FAIL
```

---

## 19.11. Search-engine citation

Reference points to Google Search / Google Scholar / a search snippet instead of the original source.

```text
FAIL
```

when the original source is identifiable.

---

## 19.12. Invented metadata

DOI, author, document number, date, version, page, or URL was guessed.

```text
FAIL
```

---

## 19.13. Wrong source-type template

Example:

```text
manual formatted as generic website
```

when the document is clearly a manual and its manual metadata is available.

```text
FAIL
```

---

# 20. OUTPUT CONTRACT FOR AGENTS

When the user requests the final article package, the citation system should produce:

```text
ARTICLE BODY
- in-text citations [n]

REFERENCES
- IEEE-formatted list

OPTIONAL INTERNAL REVIEW OUTPUT
- source registry
- claim-to-source map
- missing metadata warnings
- citation audit result
```

Internal research metadata must not be mixed into the public article unless requested.

---

# 21. FAILURE HANDLING

If metadata is missing:

Do not invent it.

Use:

```text
REFERENCE_METADATA_INCOMPLETE
```

and identify the missing fields.

If source type is unclear:

Use:

```text
SOURCE_TYPE_REVIEW_REQUIRED
```

If a claim has no supporting source:

Use:

```text
CITATION_REQUIRED_SOURCE_NOT_VERIFIED
```

These markers are permitted in review drafts only.

They must not appear in the published article.

---

# 22. SKILL INVOCATION RULE

Any Agent creating or revising technical content must invoke this Skill when:

- introducing sourced technical facts;
- adding citations;
- creating a reference list;
- renumbering references;
- changing article structure after citations already exist;
- replacing a source;
- adding/removing a source;
- using figures/tables/data from another source;
- citing standards/manuals/reports/blogs/papers or other external material.

---

# 23. SKILL SEPARATION

Recommended Agent architecture:

```text
Research / Live Research
        ↓
Evidence Validation
        ↓
IEEE Citation & Reference Skill
        ↓
Writing / Revision
        ↓
Citation Audit
        ↓
Article Packaging
```

The Citation Skill does not choose which source is "best."

It ensures that **whatever verified source is actually used is cited correctly according to its IEEE source category**.

---

# 24. AUTHORITATIVE BASIS

This Skill is based on the current IEEE Author Center:

- IEEE Reference Guide.
- IEEE Editorial Style Manual for Authors.
- IEEE Author Center guidance on proper citation practices.

Key IEEE rules incorporated in this Skill include:

- references in text use square-bracket numbers;
- citations are placed inside punctuation;
- multiple reference numbers are written out individually rather than as ranges;
- three or more author names cited in text may use "et al.";
- one reference number contains only one source;
- author initials precede family names in the reference list;
- IEEE publications list up to six authors, with first author + "et al." when more than six;
- the Reference Guide defines source-specific formats for books, conferences, datasets, handbooks, legal sources, manuals, online video, patents, periodicals, reports, standards, theses/dissertations, unpublished work, preprints, and websites;
- paraphrased/summarized ideas, data, results, graphics, and tables from another source require citation.

---

# 24A. LOCATOR VERIFICATION GATE

The Agent must pass this gate before publishing any citation more detailed than `[n]`.

```text
Source identity verified?
        ↓
Version/revision verified?
        ↓
Claim supported by this source?
        ↓
Exact locator directly observed?
        ↓
Locator belongs to this exact version?
        ↓
PASS → detailed citation allowed
FAIL / UNKNOWN → use [n]
```

Examples:

```text
Source PDF explicitly shows printed page 8.
Claim is supported on that page.
→ [1, p. 8]
```

```text
Search snippet suggests the claim is somewhere in the PDF.
Exact page has not been opened and checked.
→ [1]
```

```text
Source explicitly labels the formula as equation (6).
→ [2, eq. (6)]
```

```text
Source contains an unlabeled formula.
Agent calls it "equation (1)" for convenience.
→ NOT ALLOWED
→ use [2]
```

---

# 25. AGENT FINAL CHECKLIST

Before returning a citation-complete technical article:

- [ ] Every source has a classified source type.
- [ ] Reference format matches that source type.
- [ ] No source metadata was invented.
- [ ] In-text citation uses `[n]`.
- [ ] Every detailed locator in an in-text citation has been directly verified from the referenced source.
- [ ] Document page numbers are not confused with PDF viewer page indexes.
- [ ] Locator verification is invalidated after a source version/revision change until rechecked.
- [ ] Unpaginated web pages do not receive invented page numbers.
- [ ] Equation/section/figure identifiers come from the source itself, not from the Agent.
- [ ] Citation is inside punctuation.
- [ ] Multiple citations are written individually.
- [ ] Same source always uses the same number.
- [ ] Every reference number contains one source only.
- [ ] Numbers follow first appearance.
- [ ] Technical claims requiring attribution are cited.
- [ ] Numerical thresholds/limits are cited.
- [ ] Standards are identified to the correct part/edition when verified.
- [ ] Manufacturer documentation preserves relevant revision/version/document number.
- [ ] Papers use original publication metadata and DOI when available.
- [ ] Websites/blogs use the actual page URL, not a search result.
- [ ] Figures/tables/data adapted from sources are cited.
- [ ] No orphan citations.
- [ ] No unused references.
- [ ] No citation ranges.
- [ ] No duplicate numbers.
- [ ] No invented DOI/URL/date/author/version.
- [ ] All review-only markers are resolved before publication.

---

# 26. IMPORTANT IMPLEMENTATION NOTE

Do not hard-code one universal Reference template into the writing Agent.

Correct implementation:

```text
SOURCE
  ↓
CLASSIFY TYPE
  ↓
EXTRACT TYPE-SPECIFIC METADATA
  ↓
SELECT IEEE TEMPLATE
  ↓
RENDER REFERENCE
  ↓
ASSIGN / REUSE [n]
```

Incorrect implementation:

```text
SOURCE
  ↓
Convert everything into "Website"
  ↓
Reference list
```

The source type determines the IEEE reference format.

---

# 27. PROJECT-LEVEL VERIFIED LOCATOR POLICY

This project uses IEEE numeric citations with a **Verified Locator Only** policy.

## 27.1. Allowed citation forms

Source-level citations:

```text
[1]
[2]
[1], [2]
[1], [2], [3]
```

Verified detailed citations:

```text
[1, p. 8]
[2, pp. 3–4]
[3, eq. (1)]
[4, Sec. 4.5]
[5, Fig. 2]
[1, p. 8], [2, p. 3]
```

## 27.2. Verification requirement

A locator may be published only if the Agent has directly verified it from the referenced source.

The Agent must not guess, infer, estimate, reconstruct, approximate, or fabricate a page, page range, section, equation, figure, table, clause, chapter, appendix, algorithm, or other locator.

If the source supports the claim but locator verification is incomplete:

```text
use [n]
```

## 27.3. Locator verification statuses

Use one of:

```text
LOCATOR_VERIFIED
LOCATOR_UNAVAILABLE
LOCATOR_NOT_CHECKED
LOCATOR_CONFLICT
```

Only `LOCATOR_VERIFIED` allows a detailed locator in the published article. All other statuses require `[n]`.

## 27.4. PDF page number versus document page number

The Agent must distinguish the PDF viewer page index from the document printed page number.

Example:

```text
PDF viewer: 12 / 64
Document footer: Page 8
```

Published citation:

```text
[1, p. 8]
```

Internal metadata may keep:

```text
document_page: 8
pdf_page_index: 12
```

The Agent must not cite the PDF viewer index as the document page number unless the document itself uses the same numbering.

## 27.5. Unpaginated web pages

If a webpage or blog has no official page number, do not invent one.

Use:

```text
[n]
```

Do not create:

```text
[n, p. 1]
```

## 27.6. Section / equation / figure verification

A locator is allowed only when that identifier appears in the source itself.

Allowed when verified:

```text
[n, Sec. 4.5]
[n, eq. (6)]
[n, Fig. 3]
```

Forbidden behavior:

```text
Agent assigns its own section/equation/figure number to the source
```

If the source has an unlabeled formula, use `[n]`, not `[n, eq. (1)]`.

## 27.7. Version change invalidates locator verification

```text
Old source revision
      ↓
Verified locator
      ↓
New source revision detected
      ↓
Locator status becomes LOCATOR_NOT_CHECKED
      ↓
Reverify before publishing detailed locator
```

Until reverified, use `[n]`.

Do not carry page/section/equation locations from one version into another version automatically.

## 27.8. Internal evidence record

When a detailed locator is published, the Agent should retain an internal record:

```yaml
claim_id: C-001
source_id: SRC-001
citation_number: 1
locator_type: page
locator_value: 8
document_page: 8
pdf_page_index: 12
locator_verification_status: LOCATOR_VERIFIED
claim_supported: true
evidence_note: ""
```

This internal record is for review and audit. It is not part of the public article unless requested.

## 27.9. Reference List metadata remains independent

Bibliographic page ranges that identify a publication remain valid in the Reference List.

Example:

```text
[4] A. Author, “Paper title,” Journal Name, vol. 10, no. 2, pp. 100–110, 2025.
```

This does not prove that a particular article claim occurs on page 108.

A claim may use `[4]` unless page 108 has separately passed locator verification.

## 27.10. Locator Verification Gate

Before outputting `[n, locator]`, verify:

```text
1. Correct source identity?
2. Correct source version/revision?
3. Claim actually supported?
4. Locator exists in source?
5. Locator matches the exact source being cited?
6. Locator value directly verified?
```

If every answer is YES, `[n, locator]` is allowed.

If any answer is NO or UNKNOWN, use `[n]`.

This gate is mandatory.

---

# 28. CHANGE LOG — v1.3

Bản v1.3 được nâng cấp đồng bộ toàn diện với **IEEE Reference Guide (V 3.28.2025)** do IEEE Publication Operations ban hành (tham chiếu: `https://docs.google.com/document/d/1j1L96U2NagwWI9MEVDNVKt9pXxRzTH7h3krI3Mb6wZE/edit?tab=t.0#heading=h.b2e0set9htjw`).

Các điểm nâng cấp cốt lõi:
1. **Thiết lập Section 2A (Critical Patterns & Anti-Patterns)**: Cảnh báo nghiêm cấm đưa tên tổ chức/hãng sản xuất lên trước tiêu đề của Tiêu chuẩn (Standard) và Sổ tay kỹ thuật (Manual).
2. **Quy chuẩn Tiêu chuẩn (Standards)**: Bắt buộc tiêu đề in nghiêng đứng đầu: `*Title of Standard*, Standard number, date.`
3. **Quy chuẩn Sổ tay kỹ thuật (Manuals)**: Bắt buộc tên sổ tay in nghiêng đứng đầu: `*Name of Manual/Handbook*, x ed., Company, City, State, Country, year.`
4. **Quy chuẩn Báo cáo kỹ thuật (Technical Reports)**: Tiêu đề báo cáo đặt trong dấu ngoặc kép `“Title of report,”`, tên cơ quan và số hiệu `Rep. xxx` đứng sau.
5. **Quy chuẩn Tên tác giả & Thời gian**: Initials + Last name (`J. K. Author`), không dùng phẩy cho hậu tố (`Michael Smith Jr.`). Dùng `(n.d.)` nếu thiếu ngày tháng. Viết rời dải trích dẫn `[1], [2], [3]`.


