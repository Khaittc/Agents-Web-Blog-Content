# BLOG CONTENT STRUCTURE STANDARD v1.2

## 1. Mục đích

Tài liệu này quy định **cấu trúc nội dung cho các bài Blog kỹ thuật** đăng trên website.

Tài liệu này **không quy định Research Architecture** và không thay thế các Skill chuyên biệt về citation hoặc công thức.

Các Skill được tham chiếu bởi Standard này:

```text
IEEE_CITATION_REFERENCE_SKILL_v1.3.md
LATEX_FORMULA_SKILL_v1.0.md
```

Blog Standard kiểm soát **cấu trúc, vai trò và cách trình bày nội dung**. IEEE Skill kiểm soát citation/reference. LaTeX Formula Skill kiểm soát cú pháp, biến, đơn vị và kiểm tra công thức.

Mục tiêu:

- Giữ các bài Blog có logic kỹ thuật rõ ràng.
- Không ép mọi chủ đề phải dùng cùng một bộ Heading.
- Cho phép Chat/Agent chọn cấu trúc phù hợp với loại bài.
- Tạo bài dễ đọc, dễ kiểm duyệt và dễ chuyển sang CKEditor.
- Hỗ trợ công thức, bảng kỹ thuật và tối đa 3 hình ảnh trong phần nội dung.
- Phân biệt rõ Blog kỹ thuật với bài Giải pháp.

---

# 2. Cấu trúc tổng thể của một bài Blog

Mỗi bài Blog gồm 7 thành phần chính.

## Phần cố định

1. **Tiêu đề**
2. **Meta Title**
3. **Keyword Tag**
4. **Description Tag**
5. **Featured Image**
6. **Mô tả**

## Phần động

7. **Nội dung Blog**

Phần 1–6 sử dụng cùng một nguyên tắc cho mọi bài Blog.

Phần 7 thay đổi theo chủ đề và loại bài Blog.

---

# 3. Thành phần 1–6

## 3.1. Tiêu đề

Tiêu đề dùng để hiển thị trên website.

Yêu cầu:

- Diễn đạt rõ vấn đề hoặc giá trị bài viết.
- Không giật tít.
- Không dùng từ ngữ tuyệt đối nếu nội dung kỹ thuật không chứng minh được.
- Ưu tiên ngôn ngữ mà kỹ sư hoặc người vận hành thực tế có thể tìm kiếm.

Ví dụ:

> Cách phát hiện động cơ điện đang chạy non tải trong nhà máy

---

## 3.2. Meta Title

Meta Title phục vụ SEO.

Yêu cầu:

- Phản ánh đúng nội dung chính.
- Có keyword trọng tâm.
- Không tạo nội dung khác với tiêu đề bài viết.
- Không nhồi nhét từ khóa.

---

## 3.3. Keyword Tag

Keyword Tag gồm:

- Primary keyword.
- Secondary keywords.
- Technical terms liên quan trực tiếp.

Không thêm keyword không được xử lý trong bài.

Ví dụ:

- động cơ chạy non tải
- motor load factor
- hiệu suất động cơ
- động cơ quá cỡ
- đo tải động cơ
- tiết kiệm năng lượng động cơ

---

## 3.4. Description Tag

Meta Description dùng cho công cụ tìm kiếm.

Yêu cầu:

- Tóm tắt đúng nội dung.
- Nêu được vấn đề và giá trị bài viết.
- Không dùng thông tin hoặc con số không xuất hiện trong bài.
- Không dùng câu quảng cáo chung chung.

---

## 3.5. Featured Image

Kích thước chuẩn:

```text
808 × 500 px
```

Featured Image là hình đại diện của bài.

Yêu cầu:

- Có liên quan trực tiếp đến chủ đề.
- Không cần chứa quá nhiều chữ.
- Không được thể hiện sai kỹ thuật.
- Nếu là hình minh họa AI, không dùng hình để truyền đạt sơ đồ đấu dây, công thức hoặc thông số chính xác.

Nên chuẩn bị:

- Filename.
- ALT text.
- Image Prompt.
- Mục đích hình.

---

## 3.6. Mô tả

Mô tả là phần giới thiệu ngắn hiển thị trên website.

Khác với Description Tag.

Mô tả nên:

- Giải thích bài viết giúp người đọc giải quyết vấn đề gì.
- Dài hơn Meta Description nếu cần.
- Không lặp nguyên văn đoạn mở đầu của bài.

---

# 4. Nguyên tắc cấu trúc phần 7 — Nội dung Blog

Không sử dụng một bộ Heading cố định cho tất cả Blog.

Thay vào đó, mọi bài Blog phải tuân theo **logic nội dung cốt lõi**:

```text
CONTEXT / INTRO
      ↓
PROBLEM / QUESTION
      ↓
TECHNICAL EXPLANATION
      ↓
PRACTICAL APPLICATION
      ↓
DECISION / ACTION
      ↓
CONCLUSION
```

Đây là **logic**, không phải tên Heading bắt buộc.

Tên H2/H3 phải được viết riêng theo chủ đề.

---

# 5. Phân loại Blog kỹ thuật

Blog được chia thành 5 loại chính.

```text
BLOG-T01 — Technical Explanation
BLOG-T02 — How-to / Measurement
BLOG-T03 — Troubleshooting
BLOG-T04 — Comparison
BLOG-T05 — Best Practice / Engineering Guide
```

Một bài có thể có đặc điểm của nhiều loại, nhưng phải chọn **một loại chính** để điều khiển cấu trúc.

---

# 6. BLOG-T01 — Technical Explanation

## Mục đích

Dùng khi bài viết chủ yếu giải thích:

- Khái niệm.
- Nguyên lý.
- Thuật ngữ.
- Công thức.
- Hiện tượng kỹ thuật.

## Ví dụ

- Hệ số công suất là gì?
- Harmonic là gì?
- Motor Service Factor là gì?
- Vì sao dòng khởi động động cơ cao?

## Cấu trúc đề xuất

```text
Introduction

1. Khái niệm / Định nghĩa

2. Nguyên lý hoặc cơ chế

3. Các thông số liên quan

4. Công thức hoặc cách tính
   → Formula nếu cần

5. Ví dụ kỹ thuật
   → Table / Worked Example nếu cần

6. Ý nghĩa trong vận hành thực tế

7. Các hiểu nhầm thường gặp

8. Lưu ý kỹ thuật / giới hạn áp dụng

9. Kết luận

10. Tài liệu tham khảo
```

Không bắt buộc dùng đầy đủ mọi mục.

---

# 7. BLOG-T02 — How-to / Measurement

## Mục đích

Dùng khi bài viết hướng dẫn:

- Cách kiểm tra.
- Cách đo.
- Cách đánh giá.
- Cách xác định tình trạng thiết bị.
- Cách đưa ra quyết định từ dữ liệu đo.

## Ví dụ

- Cách phát hiện động cơ điện đang chạy non tải.
- Cách kiểm tra mất cân bằng điện áp.
- Cách đo điện năng tiêu thụ của một máy.
- Cách đánh giá hệ số tải của máy biến áp.

## Cấu trúc đề xuất

```text
Introduction

1. Vấn đề cần phát hiện / kiểm tra

2. Vì sao cần kiểm tra

3. Những thông số cần thu thập

4. Phương pháp đo hoặc xác định
   → IMAGE_1 nếu giúp hiểu quy trình đo

5. Công thức / cách tính
   → Formula

6. Ví dụ tính toán hoặc ví dụ đo thực tế
   → Table / Worked Example

7. Cách diễn giải kết quả

8. Ngưỡng / điều kiện cần chú ý
   → Chỉ nêu khi có nguồn hoặc điều kiện áp dụng rõ ràng

9. Các nguyên nhân có thể dẫn đến tình trạng đó
   → IMAGE_2 nếu thực sự có giá trị

10. Các phương án xử lý

11. Khi nào không nên áp dụng phương án xử lý

12. Checklist kiểm tra thực tế
    → IMAGE_3 nếu cần

13. Kết luận

14. Tài liệu tham khảo
```

Đây là loại ưu tiên cho bài **động cơ chạy non tải**.

---

# 8. BLOG-T03 — Troubleshooting

## Mục đích

Dùng khi bài viết xử lý lỗi, cảnh báo hoặc hiện tượng bất thường.

## Ví dụ

- Tại sao biến tần báo Overcurrent?
- PLC mất kết nối Modbus TCP.
- Motor bị nóng bất thường.
- Contactor thường xuyên cháy tiếp điểm.

## Cấu trúc đề xuất

```text
Introduction

1. Hiện tượng / triệu chứng

2. Điều kiện xuất hiện lỗi

3. Các nguyên nhân có thể

4. Trình tự kiểm tra
   → Nên trình bày theo logic từ đơn giản đến phức tạp

5. Các phép đo cần thực hiện

6. Cách phân biệt từng nguyên nhân

7. Biện pháp xử lý tương ứng

8. Cảnh báo / giới hạn an toàn

9. Các lỗi thường gặp khi troubleshooting

10. Checklist

11. Kết luận

12. Tài liệu tham khảo
```

Không viết theo kiểu liệt kê nguyên nhân mà không có trình tự kiểm tra.

---

# 9. BLOG-T04 — Comparison

## Mục đích

Dùng để so sánh:

- Công nghệ.
- Thiết bị.
- Kiến trúc.
- Phương pháp kỹ thuật.
- Phương án triển khai.

## Ví dụ

- VFD và Soft Starter khác nhau như thế nào?
- Modbus TCP và Profinet.
- Motor IE3 và IE4.
- PLC và Remote I/O.

## Cấu trúc đề xuất

```text
Introduction

1. Hai hoặc nhiều phương án là gì?

2. Nguyên lý của từng phương án

3. Tiêu chí so sánh

4. Bảng so sánh kỹ thuật
   → Table

5. Phân tích theo từng tiêu chí

6. Ưu điểm và giới hạn của từng phương án

7. Điều kiện ứng dụng phù hợp

8. Các yếu tố cần xem xét trước khi lựa chọn

9. Ví dụ ứng dụng

10. Kết luận

11. Tài liệu tham khảo
```

Không được tự kết luận một công nghệ "tốt hơn" trong mọi trường hợp nếu không có điều kiện áp dụng.

---

# 10. BLOG-T05 — Best Practice / Engineering Guide

## Mục đích

Dùng cho các bài:

- Hướng dẫn thiết kế.
- Checklist kỹ thuật.
- Best practice.
- Kinh nghiệm triển khai.
- Các lỗi cần tránh.

## Ví dụ

- Các điểm cần kiểm tra khi thiết kế tủ PLC.
- Best practice khi bố trí máng cáp.
- Các lưu ý khi lắp đặt biến tần.
- Checklist nghiệm thu tủ điện.

## Cấu trúc đề xuất

```text
Introduction

1. Phạm vi áp dụng

2. Các yêu cầu hoặc tiêu chí thiết kế

3. Best practices chính

4. Giải thích kỹ thuật cho từng best practice

5. Ví dụ / sơ đồ minh họa nếu cần

6. Các lỗi phổ biến

7. Các trường hợp ngoại lệ

8. Checklist kiểm tra

9. Kết luận

10. Tài liệu tham khảo
```

---

# 11. Content Modules

Ngoài cấu trúc theo loại Blog, Chat/Agent có thể sử dụng các Content Module sau.

Chỉ sử dụng module khi nó làm bài viết rõ hơn.

## Definition

Dùng để định nghĩa khái niệm.

## Principle

Dùng để giải thích nguyên lý.

## Measurement

Dùng cho phép đo hoặc phương pháp kiểm tra.

## Formula

Dùng khi có công thức kỹ thuật.

## Worked Example

Dùng khi cần ví dụ tính toán.

## Comparison

Dùng để đối chiếu các phương án.

## Causes

Dùng để phân tích nguyên nhân.

## Troubleshooting

Dùng cho trình tự chẩn đoán.

## Checklist

Dùng cho khảo sát hoặc kiểm tra thực tế.

## Best Practice

Dùng cho hướng dẫn triển khai.

## Technical Note

Dùng cho thông tin quan trọng nhưng không phải cảnh báo an toàn.

## Warning

Dùng khi có nguy cơ:

- mất an toàn;
- hỏng thiết bị;
- sai phép đo;
- sai kết luận kỹ thuật.

## Table

Dùng khi dữ liệu so sánh tốt hơn trình bày bằng văn bản.

## Case Example

Dùng cho tình huống minh họa.

---

# 11A. Visual Hierarchy cho nội dung kỹ thuật

Không phải mọi nội dung kỹ thuật đều được đặt trong box/card. Agent phải dùng visual treatment theo semantic role.

| Thành phần | Fill/Background | Border | Ghi chú |
|---|---|---|---|
| Paragraph | Không | Không | Nội dung chính |
| Formula | **Không** | **Không** | Nền trắng/transparent |
| Variable definitions | Không | Không | List đơn giản |
| Worked calculation | Không mặc định | Không | Formula + prose/table |
| Technical Note | Có thể dùng nhẹ | Border-left | Chỉ thông tin bổ sung quan trọng |
| Warning / Safety | Có | Border-left | Dùng có chủ đích |
| Table header | Có thể dùng fill nhẹ | Có grid nhẹ | Tăng khả năng đọc |
| Figure caption | Không | Không | Text nhỏ hơn body |
| Key Takeaway | Có thể | Border-left | Dùng tiết chế |

Nguyên tắc:

```text
Semantic importance ≠ More boxes
```

Nếu mọi công thức, dữ liệu và note đều có fill/border, bài sẽ bị chia vụn thành nhiều card và mất nhịp đọc.

Ưu tiên:

```text
Whitespace
Typography
Heading hierarchy
Tables khi có dữ liệu dạng bảng
Callout chỉ khi có semantic reason
```

---

# 12. Quy tắc sử dụng và trình bày công thức

## 12.1. Skill bắt buộc

Khi bài có công thức, Agent phải sử dụng:

```text
LATEX_FORMULA_SKILL_v1.0.md
```

Nếu công thức hoặc quan hệ kỹ thuật được lấy/adapt từ nguồn, citation phải tuân theo:

```text
IEEE_CITATION_REFERENCE_SKILL_v1.3.md
```

Blog Standard không tự định nghĩa lại cú pháp LaTeX hoặc format citation.

---

## 12.2. Cấu trúc nội dung quanh công thức

Mỗi công thức quan trọng nên đi theo flow:

```text
Mục đích / giải thích trước công thức
      ↓
Citation nguồn nếu cần
      ↓
Công thức LaTeX
      ↓
Định nghĩa biến
      ↓
Đơn vị
      ↓
Điều kiện / giả thiết áp dụng
      ↓
Worked Example nếu cần
      ↓
Diễn giải kết quả
```

Không đặt công thức đơn độc giữa hai Heading mà không có giải thích.

---

## 12.3. Visual Rule — Công thức không phải Callout/Card

Công thức toán học là một phần của luồng đọc chính. Vì vậy **mặc định không đặt công thức trong ô có màu nền, border hoặc card-style container**.

### Mặc định phải dùng

```text
Background: transparent / white
Border: none
Box shadow: none
Fill color: none
Text alignment: center hoặc theo renderer LaTeX
Vertical spacing: rõ ràng phía trên và dưới
Horizontal overflow: auto khi thật sự cần trên mobile
```

Công thức không được trình bày giống:

- code block;
- Technical Note;
- Warning;
- information card;
- table cell.

### Không dùng mặc định

```html
<div style="background:#eef5fa;border:1px solid #c9dae6;...">
    [LATEX]
</div>
```

hoặc bất kỳ wrapper nào có:

```text
background fill
border
border-left callout
box-shadow
monospace code-card styling
```

chỉ nhằm chứa công thức.

### Wrapper HTML khuyến nghị cho CKEditor

Nếu cần wrapper để kiểm soát spacing/mobile:

```html
<div style="margin:18px 0;text-align:center;overflow-x:auto;">
    [LATEX FORMULA]
</div>
```

Wrapper chỉ làm nhiệm vụ bố cục, **không tạo card trực quan quanh công thức**.

---

## 12.4. Khi nào được dùng nền màu?

Nền màu chỉ dành cho nội dung có semantic role rõ ràng:

```text
Technical Note
Warning / Safety
Important Limitation
Key Takeaway
```

Không dùng nền màu chỉ vì nội dung là công thức.

Nếu cần nhấn mạnh một kết quả sau phép tính, hãy nhấn mạnh **kết luận hoặc con số kết quả trong prose**, không tô cả vùng công thức.

---

## 12.5. Worked Example

Ví dụ tính toán không được render như source code.

Không ưu tiên:

```text
monospace gray box
code block
preformatted calculation card
```

Ưu tiên:

```text
Dữ liệu đầu vào → bảng nhỏ hoặc bullet
Công thức → LaTeX nền trắng
Thay số → LaTeX nền trắng
Kết quả → câu diễn giải rõ ràng
```

Nếu chỉ có 2–4 giá trị đầu vào, có thể dùng bullet list. Nếu nhiều giá trị hoặc nhiều pha, dùng table.

---

## 12.6. Equation Numbering không phải nội dung dành cho người đọc

Các quy tắc như:

```text
article equation number
source equation locator
LOCATOR_VERIFIED
```

là quy tắc cho Agent/reviewer, **không nên xuất thành một callout giải thích trong bài public** trừ khi người đọc thực sự cần hiểu điều đó.

Không tạo box kiểu:

```text
Lưu ý về số công thức:
Số công thức của bài và equation number của nguồn là hai hệ thống khác nhau...
```

Thông tin này phải nằm trong Skill hoặc review artifact, không làm gián đoạn bài Blog.

---

## 12.7. Công thức, citation và reviewer

Citation đặt trong prose ngay trước/sau công thức theo IEEE Skill.

Ví dụ:

```text
DOE sử dụng quan hệ sau để ước tính ... [1, eq. (3)].

[FORMULA LATEX]
```

Không chèn citation vào bên trong LaTeX environment.

Nếu locator chưa được xác minh, dùng `[1]` theo IEEE Skill v1.2.

---

## 12.8. Formula Acceptance Checklist

- [ ] Formula được tạo bằng LaTeX Skill.
- [ ] Formula có mục đích rõ ràng trong flow bài.
- [ ] Formula không nằm trong colored card/box mặc định.
- [ ] Formula không có border hoặc box-shadow chỉ để trang trí.
- [ ] Formula không được trình bày như code block.
- [ ] Variable definitions nằm ngay sau hoặc gần formula.
- [ ] Units rõ ràng.
- [ ] Assumption/condition được nêu khi cần.
- [ ] Citation nằm ngoài LaTeX.
- [ ] Worked example phân biệt source data / real data / illustrative assumption.
- [ ] Kết quả được diễn giải bằng prose.

---

# 13. Quy tắc sử dụng bảng

Nên sử dụng bảng khi:

- So sánh nhiều thông số.
- Có nhiều giá trị đo.
- Có tiêu chí đánh giá.
- Có checklist dạng ma trận.
- Có nhiều phương án xử lý.

Không dùng bảng cho một nội dung chỉ có 1–2 ý.

Bảng phải có:

- Tiêu đề cột rõ ràng.
- Đơn vị nếu có.
- Nội dung ngắn.
- Không nhồi cả đoạn văn dài vào ô.

---

# 14. Quy tắc sử dụng hình ảnh trong nội dung

## Featured Image

Bắt buộc:

```text
1 hình — 808 × 500 px
```

## Content Images

Cho phép:

```text
0 đến tối đa 3 hình
```

Không bắt buộc phải đủ 3 hình.

Mỗi hình phải có mục đích rõ ràng.

### IMAGE_1

Ưu tiên:

- Giải thích nguyên lý.
- Vị trí đo.
- Sơ đồ khái niệm.
- Quy trình.

### IMAGE_2

Ưu tiên:

- So sánh.
- Phân tích dữ liệu.
- Biểu đồ.
- Sơ đồ nguyên nhân.

### IMAGE_3

Ưu tiên:

- Checklist.
- Workflow.
- Ứng dụng.
- Tổng hợp phương án.

Nếu một bài chỉ cần 1 hình để giải thích tốt thì chỉ dùng 1 hình.

Không tạo hình chỉ để trang trí.

---

# 15. Hình minh họa và hình kỹ thuật

Phân biệt hai nhóm.

## Illustrative Image

Có thể dùng AI Image Generation.

Phù hợp cho:

- Featured Image.
- Bối cảnh nhà máy.
- Hình minh họa motor.
- Automation.
- Energy monitoring.

Không dùng để truyền đạt:

- sơ đồ đấu dây chính xác;
- thông số;
- formula;
- chart có số liệu;
- terminal connection.

## Technical Figure

Ưu tiên tạo từ dữ liệu hoặc sơ đồ có kiểm soát.

Ví dụ:

- biểu đồ;
- flowchart;
- sơ đồ logic;
- sơ đồ vị trí đo;
- energy flow;
- calculation diagram.

Hình kỹ thuật phải ưu tiên **độ chính xác hơn tính thẩm mỹ**.

---

# 16. Trích dẫn và Tài liệu tham khảo

Mọi Blog kỹ thuật sử dụng nguồn ngoài phải tuân theo:

```text
IEEE_CITATION_REFERENCE_SKILL_v1.3.md
```

Bài public nên có section:

```text
Tài liệu tham khảo
```

Blog Standard chỉ quy định vị trí và vai trò của section này. Toàn bộ logic về:

- `[n]`;
- verified locator;
- source classification;
- IEEE reference format;
- citation audit;
- reference numbering;

thuộc IEEE Skill.

Không đưa nguồn vào References nếu nguồn đó không thực sự được sử dụng trong bài.

---

# 17. Nguyên tắc viết

## Phải làm

- Viết cho kỹ sư và người vận hành có nền tảng kỹ thuật.
- Giải thích thuật ngữ khi cần.
- Giữ đơn vị nhất quán.
- Phân biệt rated value, measured value và estimated value.
- Phân biệt dữ liệu đo với suy luận.
- Nêu điều kiện áp dụng khi sử dụng ngưỡng.
- Nêu giới hạn của phương pháp đo.
- Dùng ví dụ có giá trị thực tế.

## Không làm

- Viết theo kiểu quảng cáo.
- Dùng từ "luôn luôn", "chắc chắn", "bắt buộc" khi không có cơ sở.
- Tự tạo số liệu.
- Tự tạo threshold.
- Dùng một ví dụ để kết luận cho mọi trường hợp.
- Lặp keyword để SEO.
- Viết dài chỉ để tăng số lượng từ.
- Sử dụng hình ảnh chỉ để lấp chỗ trống.

---

# 18. Cấu trúc đề xuất riêng cho bài động cơ chạy non tải

## Blog Type

```text
BLOG-T02 — How-to / Measurement
```

## Chủ đề

```text
Cách phát hiện động cơ điện đang chạy non tải trong nhà máy
```

## Trọng tâm

```text
- Cách xác định hệ số tải.
- Nhận diện động cơ vận hành dưới tải.
- Phân tích trường hợp dưới khoảng 50% tải khi có cơ sở kỹ thuật phù hợp.
- Đánh giá nguyên nhân motor bị oversize.
- Phương án xử lý: giữ nguyên, cấu hình lại, VFD, thay đổi truyền động hoặc thay motor.
```

## Outline đề xuất

```text
MỞ ĐẦU
- Motor non tải thường khó nhận biết chỉ bằng quan sát.
- Không nên kết luận chỉ dựa trên dòng điện.
- Bài viết tập trung vào cách đo, tính và đánh giá.

H2 — 1. Động cơ chạy non tải là gì?

H2 — 2. Vì sao cần phát hiện động cơ vận hành non tải?

H2 — 3. Những dữ liệu cần thu thập trước khi đánh giá
- Nameplate.
- Công suất định mức.
- Điện áp.
- Dòng điện.
- Công suất thực.
- Power factor.
- Thời gian vận hành.
- Duty profile.
- Điều kiện tải.

H2 — 4. Các phương pháp xác định hệ số tải

H3 — 4.1. Đánh giá bằng công suất điện đo được

H3 — 4.2. Ước tính từ dòng điện
- Phải nêu hạn chế.
- Không coi current ratio là load ratio trong mọi trường hợp.

H3 — 4.3. Đánh giá từ công suất cơ hoặc dữ liệu quá trình nếu có

[IMAGE_1 — Vị trí đo / phương pháp thu thập dữ liệu]

H2 — 5. Công thức và cách tính hệ số tải
- Công thức.
- Định nghĩa biến.
- Đơn vị.
- Điều kiện áp dụng.

H2 — 6. Ví dụ tính toán
- Nameplate.
- Dữ liệu đo.
- Calculation.
- Interpretation.

H2 — 7. Làm thế nào nhận diện motor thường xuyên vận hành dưới tải?
- Không dùng một snapshot.
- Xem operating profile.
- Xem thời gian ở từng mức tải.
- Phân biệt low-load tạm thời và oversizing thực sự.

H2 — 8. Trường hợp động cơ vận hành dưới khoảng 50% tải nên được đánh giá như thế nào?
- Không mặc định 50% là ngưỡng thay motor.
- Chỉ sử dụng threshold nếu nguồn kỹ thuật hỗ trợ.
- Xem hiệu suất.
- Power factor.
- Duty cycle.
- Load variability.
- Starting requirements.
- Future expansion.
- Reliability.

[IMAGE_2 — Load profile / efficiency concept nếu cần]

H2 — 9. Vì sao động cơ bị chọn quá lớn?
- Design margin.
- Thay đổi process.
- Dự phòng mở rộng.
- Equipment modification.
- Sai assumptions ban đầu.

H2 — 10. Các phương án xử lý

H3 — 10.1. Giữ nguyên động cơ

H3 — 10.2. Điều chỉnh chế độ vận hành

H3 — 10.3. Sử dụng VFD khi phù hợp với loại tải

H3 — 10.4. Điều chỉnh tỷ số truyền hoặc cơ cấu truyền động

H3 — 10.5. Thay motor công suất phù hợp hơn

H2 — 11. Khi nào không nên thay motor chỉ vì tải thấp?
- Load variation.
- High starting torque.
- Intermittent peak.
- Process criticality.
- Future requirements.
- Replacement economics.

H2 — 12. Checklist khảo sát motor tại nhà máy
- Nameplate.
- Electrical measurement.
- Load profile.
- Operating hours.
- Process demand.
- Mechanical transmission.
- Maintenance condition.
- Candidate action.

[IMAGE_3 — Checklist / decision workflow nếu có giá trị]

H2 — 13. Kết luận

H2 — 14. Tài liệu tham khảo
```

---

# 19. Yêu cầu khi dùng file này để cập nhật bài hiện có

Khi Chat/Agent nhận một bài Blog đã viết trước đó:

1. **Không viết lại toàn bộ bài ngay lập tức.**
2. Xác định Blog Type.
3. So sánh cấu trúc hiện tại với Standard.
4. Giữ lại các nội dung kỹ thuật còn phù hợp.
5. Di chuyển nội dung về đúng section nếu cần.
6. Bổ sung section còn thiếu chỉ khi có đủ thông tin hoặc nguồn.
7. Không tự tạo claim để lấp section thiếu.
8. Loại các đoạn lặp.
9. Đánh dấu các claim cần kiểm chứng.
10. Sau khi cấu trúc nội dung ổn định mới chuyển sang format CKEditor.

---

# 20. Output mong muốn khi yêu cầu Chat cập nhật bài

Chat nên trả lại:

```text
A. BLOG TYPE
B. ĐÁNH GIÁ CẤU TRÚC HIỆN TẠI
C. CẤU TRÚC MỚI ĐỀ XUẤT
D. NHỮNG PHẦN GIỮ LẠI
E. NHỮNG PHẦN CẦN BỔ SUNG / KIỂM CHỨNG
F. VISUAL/PRESENTATION REVIEW
G. BÀI VIẾT ĐÃ TÁI CẤU TRÚC
H. CITATION AUDIT theo IEEE Skill nếu có nguồn
I. FORMULA AUDIT theo LaTeX Skill nếu có công thức
```

Nếu người dùng đã yêu cầu trực tiếp HTML CKEditor, phần F có thể được xuất theo chuẩn HTML tương ứng sau khi hoàn tất review nội dung.

---

# 21. Acceptance Checklist

Trước khi coi một bài Blog đạt cấu trúc:

- [ ] Đã xác định Blog Type.
- [ ] Tiêu đề phản ánh đúng nội dung.
- [ ] Meta Title phù hợp.
- [ ] Keyword chỉ gồm nội dung bài thực sự xử lý.
- [ ] Description Tag không chứa claim ngoài bài.
- [ ] Featured Image có mục đích rõ.
- [ ] Mô tả khác Meta Description.
- [ ] Introduction nêu đúng vấn đề.
- [ ] Flow từ vấn đề → giải thích → thực tế → hành động rõ ràng.
- [ ] Heading phù hợp chủ đề, không máy móc.
- [ ] Công thức có định nghĩa biến và đơn vị.
- [ ] Công thức không bị đặt trong colored box/card nếu không có semantic reason.
- [ ] Công thức không dùng border/fill chỉ để trang trí.
- [ ] Worked example không bị trình bày như code block nếu không phải source code.
- [ ] Technical Note/Warning dùng callout có chủ đích, không lạm dụng.
- [ ] Nội dung public không chứa implementation note dành riêng cho Agent/reviewer.
- [ ] Có nêu giới hạn phương pháp khi cần.
- [ ] Không dùng threshold thiếu căn cứ.
- [ ] Bảng chỉ được dùng khi cần.
- [ ] Content Image không vượt quá 3.
- [ ] Mỗi Content Image có mục đích kỹ thuật.
- [ ] Có phần kết luận.
- [ ] Có tài liệu tham khảo.
- [ ] Không có claim kỹ thuật không thể truy nguyên.
- [ ] Không biến Blog thành bài quảng cáo bán hàng.

---

# 22. Phạm vi của Standard v1.2

Standard này quy định:

```text
BLOG CONTENT STRUCTURE
+
ARTICLE PRESENTATION HIERARCHY
+
FORMULA PLACEMENT / VISUAL RULES
```

Chưa quy định:

```text
- Research Architecture
- Source Tier / Evidence workflow
- Antigravity workflow
- Gemini Notebook integration
- Live Research process
- Technical Review Agent
- SEO automation
- Image generation workflow
- DOCX / PDF packaging
- Full CKEditor HTML/CSS component library
```

Các phần trên sẽ được xây dựng thành tài liệu riêng sau khi cấu trúc Blog được kiểm chứng bằng các bài thực tế.


---

# 23. Change Log — v1.2

Bản v1.2 được cập nhật sau khi review bài test **“Cách phát hiện động cơ điện đang chạy non tải trong nhà máy”** sử dụng IEEE Skill và LaTeX Formula Skill.

Các thay đổi chính:

1. Tách Citation và Formula logic sang Skill độc lập.
2. Thêm Visual Hierarchy cho Paragraph / Formula / Table / Note / Warning.
3. Quy định formula mặc định nền trắng/transparent, không border/fill/card.
4. Không trình bày worked calculation như code block.
5. Implementation note dành cho Agent/reviewer không được đưa vào public article.
6. Bổ sung Presentation Review, Citation Audit và Formula Audit vào output contract.
7. Bổ sung acceptance checks cho formula presentation và callout usage.
