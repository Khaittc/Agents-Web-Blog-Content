# HỒ SƠ CHỨNG CỨ KỸ THUẬT & DANH MỤC NGUỒN XÁC MINH (EVIDENCE DOSSIER) — BLOG_04

**Mã bài viết**: `BLOG_04`<br>
**Chủ đề**: VFD và Soft Starter: Khác nhau về nguyên lý, dòng khởi động, điều khiển tốc độ và phạm vi ứng dụng<br>
**Thể loại Canonical**: `BLOG-T04` (So sánh Kỹ thuật Đa chiều — Comparison)<br>
**Người thực hiện**: Kỹ sư Nghiên cứu Hệ thống (Research Agent)<br>
**Ngày xác thực**: 2026-09-24<br>
**Tổng số nguồn tiếp nhận**: 4 (3 Tier 1, 1 Tier 3 — Tỷ lệ Tier 1+2: 75% >= 70%)<br>
**Ngoại lệ nguồn hẹp (Source Policy Exception)**: `NONE` (Tuân thủ chính sách mặc định 4–7 nguồn, không yêu cầu ngoại lệ)<br>
**Trạng thái Kế hoạch Nghiên cứu**: `REVIEW_REQUIRED` (RQ-005, RQ-006 đạt `PARTIALLY_ANSWERED`, CON-002 trạng thái `REVIEW_REQUIRED`)

---

## 1. BẢNG PHỦ SÓNG CÂU HỎI NGHIÊN CỨU (RESEARCH QUESTIONS COVERAGE TABLE)

| Mã RQ | Mức ưu tiên | Câu hỏi Nghiên cứu Kỹ thuật | Trạng thái | Nguồn chứng minh | Mã bằng chứng trích xuất |
|:---:|:---:|:---|:---:|:---|:---|
| `RQ-001` | **HIGH** | Nguyên lý biến đổi điện áp/tần số và cấu trúc linh kiện công suất giữa VFD (AC-DC-AC, PWM với IGBT) và Soft Starter (điều khiển góc mở pha SCR/Thyristor phản song song)? | `ANSWERED` | `SRC-001`, `SRC-002` | `EVD-001`, `EVD-002` |
| `RQ-002` | **HIGH** | Đặc tính định lượng của dòng khởi động cực đại và khả năng sinh mô-men khởi động (quan hệ $T \propto U^2$) của Soft Starter so với VFD và DOL? | `ANSWERED` | `SRC-001`, `SRC-002`, `SRC-003` | `EVD-003`, `EVD-004` |
| `RQ-003` | **HIGH** | Khả năng điều chỉnh và duy trì tốc độ động cơ liên tục trong quá trình làm việc của VFD so với giới hạn tốc độ cố định của Soft Starter sau khởi động? | `ANSWERED` | `SRC-001`, `SRC-003` | `EVD-005` |
| `RQ-004` | **HIGH** | So sánh tổn hao công suất (Power losses), sinh nhiệt và hiệu suất vận hành giữa VFD (tổn hao IGBT liên tục) và Soft Starter (Bypass contactor triệt tiêu tổn hao)? | `ANSWERED` | `SRC-002`, `SRC-003` | `EVD-006`, `EVD-007` |
| `RQ-005` | **MEDIUM** | Mức độ phát sinh sóng hài (Harmonics) và tác động lên chất lượng điện lưới giữa VFD và Soft Starter trong giai đoạn khởi động và giai đoạn vận hành định mức? | `PARTIALLY_ANSWERED` | `SRC-001`, `SRC-002`, `SRC-004` | `EVD-008`, `EVD-009` |
| `RQ-006` | **MEDIUM** | So sánh chi phí đầu tư ban đầu (CAPEX), kích thước lắp đặt tủ điện (Footprint) và yêu cầu bảo trì vòng đời giữa VFD và Soft Starter theo các dải công suất? | `PARTIALLY_ANSWERED` | `SRC-002` | `EVD-010` |
| `RQ-007` | **HIGH** | Ma trận hướng dẫn và tiêu chí lựa chọn kỹ thuật giữa VFD và Soft Starter cho các nhóm phụ tải công nghiệp điển hình (Bơm, Quạt, Băng tải, Máy nghiền)? | `ANSWERED` | `SRC-001`, `SRC-002`, `SRC-003` | `EVD-011`, `EVD-012` |

---

## 2. BẢNG ĐĂNG KÝ NGUỒN ỔN ĐỊNH (STABLE SOURCE REGISTRY TABLE)

| Source ID | Tên tài liệu / Tiêu chuẩn / Tác giả | Loại hình | Tier | Canonical URL | Retrieval URL | Trạng thái Mạng | Content ID | Claim Ver. | Locator Status | Bộ định vị kiểm chứng (Locators) |
|:---:|:---|:---|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|
| `SRC-001` | *Softstarter Handbook* (ABB AB, Cewe-Control, Doc ID: 1SFC132060M0201) | `MANUAL` | Tier 1 | [ABB Library](https://library.abb.com/d/1SFC132060M0201) | [Direct PDF](https://library.e.abb.com/public/6b4e1a3530814df0c12579bb0030e58b/1SFC132060M0201.pdf) | `OK` | `true` | `true` | `LOCATOR_VERIFIED` | Ch. Different starting methods, pp. 12-20; Ch. Applications, pp. 26-38; Ch. Harmonics, p. 68 |
| `SRC-002` | *When to use a Soft Starter or an AC Variable Frequency Drive* (Rockwell Automation, Pub. 150-WP007A-EN-P) | `TECH_REPORT` | Tier 1 | [Rockwell Literature](https://rok.auto/literature) | [Direct PDF](https://literature.rockwellautomation.com/idc/groups/literature/documents/wp/150-wp007_-en-p.pdf) | `OK` | `true` | `true` | `LOCATOR_VERIFIED` | Table 1, p. 6; Bypass, p. 7; Harmonics, p. 12; Initial Cost & Size, pp. 15-16; Maintenance, p. 17 |
| `SRC-003` | *Soft starters vs. VFDs: Which one is right for your conveyor motor application?* (Mark Duncan, Schneider Electric) | `WEB_ARTICLE` | Tier 3 | [Schneider Blog](https://blog.se.com/industry/machine-and-process-management/2020/08/03/soft-starters-vs-vfds-which-one-is-right-for-your-conveyor-motor-application/) | [Schneider Article](https://blog.se.com/industrial-automation/2020/08/03/soft-starters-vs-vfds-which-one-is-right-for-your-conveyor-motor-application/) | `REDIRECTED_OK` | `true` | `true` | `LOCATOR_VERIFIED` | Sections: Benefits, Efficiency comparisons, Harmonics, Application FAQ |
| `SRC-004` | *IEEE Standard for Harmonic Control in Electric Power Systems* (IEEE Std 519-2022) | `STANDARD` | Tier 1 | [IEEE Standards](https://standards.ieee.org/ieee/519/10540/) | [IEEE Xplore](https://ieeexplore.ieee.org/document/9848440) | `OK` | `true` | `true` | `LOCATOR_VERIFIED` | Table 1: Voltage Distortion Limits; Table 2: Current Distortion Limits, p. 12 |

---

## 3. DANH MỤC BẰNG CHỨNG HẠT NHÂN TRÍCH XUẤT (EXTRACTED GRANULAR EVIDENCES)

### `EVD-001`: Cấu trúc và nguyên lý biến đổi tần số của biến tần (VFD)
- **Câu hỏi giải quyết**: `RQ-001`
- **Nguồn chứng minh**: `SRC-001` (*Softstarter Handbook*, ABB)
- **Vị trí định vị**: Chương "Different starting methods", Trang in: 16, Trang PDF: 22 (`document_page: 16`, `pdf_page_index: 22`)
- **Trích dẫn gốc**:  
  > *"The drive consists primarily of two parts, one which converts AC (50 or 60 Hz) to DC and a second part which converts the DC back to AC, but now with a variable frequency of 0-250 Hz. By controlling the frequency, the drive can control the speed of the motor."*
- **Ý nghĩa kỹ thuật**: Biến tần thực hiện chuyển đổi năng lượng hai tầng gián tiếp (AC $\rightarrow$ DC $\rightarrow$ AC). Tốc độ từ trường quay của stato được điều khiển vô cấp thông qua biến thiên tần số cấp $f$ theo hệ thức $n = \frac{60f}{p}$, cho phép điều chỉnh tốc độ từ 0 rpm đến vượt tốc độ định mức.

### `EVD-002`: Cấu trúc van bán dẫn và điều khiển góc kích của Khởi động mềm (Soft Starter)
- **Câu hỏi giải quyết**: `RQ-001`
- **Nguồn chứng minh**: `SRC-001` (*Softstarter Handbook*, ABB)
- **Vị trí định vị**: Chương "General about softstarters", Trang in: 21-22, Trang PDF: 27-28 (`document_page: 22`, `pdf_page_index: 28`)
- **Trích dẫn gốc**:  
  > *"A softstarter consists of a number of anti-parallel thyristors; two in each phase. When performing a soft start, a firing signal is sent to the thyristors so that only the last part of each half period of the voltage sinus curve passes through. Then during the start, the firing signal is send earlier and earlier allowing a bigger and bigger part of the voltage to pass through the thyristors."*
- **Ý nghĩa kỹ thuật**: Khởi động mềm sử dụng 6 van thyristor (3 cặp đấu song song ngược) điều khiển góc kích mở $\alpha$. Tần số dòng điện cấp vào động cơ luôn giữ cố định ở tần số lưới ($50\text{ Hz}$ hoặc $60\text{ Hz}$); chỉ có trị số điện áp hiệu dụng RMS được điều chỉnh tăng dần từ giá trị ban đầu lên điện áp định mức.

### `EVD-003`: Định lượng quan hệ dòng khởi động và mô-men khởi động ($T \propto U^2$)
- **Câu hỏi giải quyết**: `RQ-002`
- **Nguồn chứng minh**: `SRC-002` (*When to use a Soft Starter or an AC VFD*, Rockwell Automation)
- **Vị trí định vị**: Bảng 1: *Type of Start, Voltage, Torque, and Current*, Trang in: 6, Trang PDF: 6 (`document_page: 6`, `pdf_page_index: 6`)
- **Số liệu kỹ thuật gốc**:  
  - **Khởi động trực tiếp (DOL)**: $100\%$ Điện áp $\rightarrow 100\%$ Mô-men khởi động định mức $\rightarrow 600\%$ Dòng định mức ($6.0\,I_n$).
  - **Khởi động mềm (Giới hạn dòng 150%)**: $25\%$ Điện áp $\rightarrow 6\%$ Mô-men khởi động.
  - **Khởi động mềm (Giới hạn dòng 300%)**: $50\%$ Điện áp $\rightarrow 25\%$ Mô-men khởi động.
  - **Khởi động mềm (Giới hạn dòng 450%)**: $75\%$ Điện áp $\rightarrow 56\%$ Mô-men khởi động.
- **Ý nghĩa kỹ thuật**: Khẳng định quy luật mô-men động cơ không đồng bộ tỉ lệ với bình phương điện áp: $M \approx \left(\frac{U}{U_n}\right)^2 \cdot M_{kd}$. Việc ép dòng khởi động xuống thấp ở Soft Starter làm suy giảm nghiêm trọng khả năng sinh công bứt phá ban đầu.

### `EVD-004`: Khả năng sinh mô-men ở tốc độ không (Zero Speed Torque)
- **Câu hỏi giải quyết**: `RQ-002`, `RQ-007`
- **Nguồn chứng minh**: `SRC-003` (*Soft starters vs. VFDs*, Schneider Electric, Tier 3)
- **Vị trí định vị**: Section: *Frequently asked questions: application considerations*
- **Trích dẫn gốc**:  
  > *"Question: Does the application need full torque at zero speed? Answer: An AC Drive can provide full torque at zero speed where a soft starter cannot."*
- **Ý nghĩa kỹ thuật**: Biến tần (AC Drive) có khả năng cung cấp đầy đủ mô-men (full torque) ở tốc độ zero speed trong các ứng dụng công nghiệp đòi hỏi mô-men bứt phá tải tại chỗ, trong khi khởi động mềm (Soft Starter) chỉ điều khiển giảm áp điện áp xoay chiều nên không thể duy trì full torque tại zero speed. (Lưu ý: Không suy diễn vượt nguồn về các tỷ lệ phần trăm cụ thể).

### `EVD-005`: Giới hạn điều khiển tốc độ ổn định của Khởi động mềm
- **Câu hỏi giải quyết**: `RQ-003`
- **Nguồn chứng minh**: `SRC-001` (*Softstarter Handbook*, ABB, Tier 1)
- **Vị trí định vị**: Chương "Different starting methods", Trang in: 17, Trang PDF: 23 (`document_page: 17`, `pdf_page_index: 23`)
- **Trích dẫn gốc**:  
  > *"In many applications it is required to continuously regulate the speed of the motor, and a drive is then a very good solution. However, in many applications a drive is used only for starting and stopping the motor, even though there is no need for continuous speed regulation. This will create an unnecessarily expensive solution if comparing with, for instance a softstarter."*
- **Ý nghĩa kỹ thuật**: Khởi động mềm chỉ kiểm soát giai đoạn quá độ khởi động và dừng. Sau khi tăng tốc xong, động cơ làm việc ở tốc độ cố định đồng bộ/trượt với tần số lưới điện. Nếu quy trình công nghệ đòi hỏi liên tục thay đổi tốc độ thì biến tần là giải pháp kỹ thuật phù hợp.

### `EVD-006`: Hiệu suất vận hành và tổn hao nhiệt qua Bypass Contactor
- **Câu hỏi giải quyết**: `RQ-004`
- **Nguồn chứng minh**: `SRC-003` (*Soft starters vs. VFDs*, Schneider Electric, Tier 3)
- **Vị trí định vị**: Section: *Energy efficiency comparisons of soft starters vs. VFDs*
- **Trích dẫn gốc**:  
  > *"When operating at full speed and adequately loaded, soft starters are more efficient than VFDs. With an integrated bypass, current in the soft starter is carried across the contactor, so it runs cooler, as no active solid-state components are generating heat. VFDs: Active components such as insulated-gate bipolar transistors (IGBTs) stay on during run and stop functions... inherently are hotter during operation."*
- **Ý nghĩa kỹ thuật**: Khi vận hành ở tốc độ định mức đầy tải có tích hợp bypass contactor, dòng điện chạy qua tiếp điểm tiếp xúc thay vì van bán dẫn, giúp Soft Starter đạt hiệu suất cao hơn và chạy mát hơn VFD vì không có linh kiện bán dẫn công suất chủ động sinh nhiệt liên tục.

### `EVD-007`: Cấu hình tiếp điểm Bypass AC-1 bên trong Soft Starter
- **Câu hỏi giải quyết**: `RQ-004`
- **Nguồn chứng minh**: `SRC-002` (*When to use a Soft Starter or an AC VFD*, Rockwell Automation, Tier 1)
- **Vị trí định vị**: Section: *Bypass Configuration*, Trang in: 7, Trang PDF: 7 (`document_page: 7`, `pdf_page_index: 7`)
- **Trích dẫn gốc**:  
  > *"The internal bypass is typically rated AC-1, not AC-3, because the bypass contactor never makes or breaks current. If an external bypass is used for emergency run... an AC-3 utilization rating is needed."*
- **Ý nghĩa kỹ thuật**: Contactor bypass tích hợp trong Soft Starter chỉ cần định mức AC-1 vì nó không bao giờ phải đóng hoặc cắt dòng hồ quang tải cảm ứng, giúp tối ưu hóa kích thước và chi phí linh kiện so với contactor ngoài dùng cho chạy khẩn cấp (đòi hỏi AC-3).

### `EVD-008`: Đặc tính sóng hài của Soft Starter trong chu kỳ vận hành
- **Câu hỏi giải quyết**: `RQ-005`
- **Nguồn chứng minh**: `SRC-002` (*When to use a Soft Starter or an AC VFD*, Rockwell Automation, Tier 1)
- **Vị trí định vị**: Section: *Harmonics, Wiring Methods and Installation Considerations*, Trang in: 12, Trang PDF: 12 (`document_page: 12`, `pdf_page_index: 12`)
- **Trích dẫn gốc**:  
  > *"Soft starter harmonics are typically less than 10% in starting or stopping modes when SCRs are turned on and provide partial voltage amplitudes, producing partial sine waves. With the motor at full speed, the SCRs are fully conducting, there are virtually no harmonics. In bypass condition, there are almost no harmonics generated."*
- **Ý nghĩa kỹ thuật**: Sóng hài của Soft Starter thường dưới 10% trong chế độ khởi động hoặc dừng khi SCR dẫn; ở trạng thái bypass, hầu như không có sóng hài nào phát sinh (almost no harmonics generated). Không khẳng định tuyệt đối THD = 0% để bảo đảm độ chính xác học thuật.

### `EVD-009`: Chuẩn mực giới hạn méo dòng sóng hài theo IEEE Std 519-2022
- **Câu hỏi giải quyết**: `RQ-005`
- **Nguồn chứng minh**: `SRC-004` (*IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE, Tier 1)
- **Vị trí định vị**: Table 2: *Current Distortion Limits for Systems Rated 120 V Through 69 kV*, Trang in: 12, Trang PDF: 16
- **Số liệu kỹ thuật gốc**:  
  > *"Maximum harmonic current distortion in percent of IL for Isc/IL < 20 is TDD 5.0% for systems rated 120 V through 69 kV."*
- **Ý nghĩa kỹ thuật**: Theo IEEE Std 519-2022 (Bảng 2), giới hạn méo dòng tổng TDD tại điểm đấu nối chung (PCC) là 5.0% đối với tỷ số ngắn mạch $I_{sc}/I_L < 20$ cho các hệ thống điện có điện áp từ 120 V đến 69 kV. Tiêu chuẩn đánh giá tại điểm đấu nối chung PCC của toàn trạm chứ không phải tại cực của từng thiết bị riêng lẻ; nhu cầu lắp đặt bộ lọc hài (thụ động hoặc tích cực) phụ thuộc vào độ ngắn mạch của trạm và mức độ phụ tải phi tuyến tổng thể.

### `EVD-010`: So sánh chi phí đầu tư (CAPEX), kích thước tủ điện và bảo dưỡng
- **Câu hỏi giải quyết**: `RQ-006`
- **Nguồn chứng minh**: `SRC-002` (*When to use a Soft Starter or an AC VFD*, Rockwell Automation, Tier 1)
- **Vị trí định vị**: Section: *Initial Cost & Maintenance*, Trang in: 15-17, Trang PDF: 15-17
- **Trích dẫn gốc**:  
  > *"At lower amperage, the drive and the soft starter have similar costs, but as the amperage and power go up, so does the cost of a drive... on a drive operating 24 hours per day, in year 3, you should replace cooling fans and inspect DC bus capacitors."*
- **Ý nghĩa kỹ thuật**: Ở dải dòng và công suất thấp, chi phí ban đầu giữa VFD và Soft Starter là tương đương, nhưng khi dòng điện và công suất tăng lên thì chi phí của VFD tăng cao hơn đáng kể so với Soft Starter. Ngoài ra, VFD yêu cầu quy trình bảo trì định kỳ nghiêm ngặt hơn như thay quạt làm mát ở năm thứ 3 và kiểm tra tụ DC bus.

### `EVD-011`: Triệt tiêu hiện tượng búa nước trong ứng dụng bơm ly tâm
- **Câu hỏi giải quyết**: `RQ-007`
- **Nguồn chứng minh**: `SRC-001` (*Softstarter Handbook*, ABB, Tier 1)
- **Vị trí định vị**: Chương "Different applications - Centrifugal pump", Trang in: 29, Trang PDF: 35 (`document_page: 29`, `pdf_page_index: 35`)
- **Trích dẫn gốc**:  
  > *"Starting up a pump is normally not a big problem electrically. The problem is the wear and tear caused by pressure waves in the pipe system created when the motor starts but especially when it stops too quickly."*
- **Ý nghĩa kỹ thuật**: Trong ứng dụng máy bơm, hiện tượng hao mòn cơ khí và áp lực đường ống chủ yếu do sóng áp suất (búa nước) khi động cơ khởi động và đặc biệt là khi dừng quá nhanh; Soft Starter cung cấp giải pháp giảm áp lực đường ống thông qua tính năng điều khiển dốc dừng êm.

### `EVD-012`: Nguyên tắc định cỡ thiết bị cho tải nặng, quán tính lớn (Crusher/Mill)
- **Câu hỏi giải quyết**: `RQ-007`
- **Nguồn chứng minh**: `SRC-001` (*Softstarter Handbook*, ABB, Tier 1)
- **Vị trí định vị**: Chương "Different applications - Crusher and Mill", Trang in: 37, Trang PDF: 43 (`document_page: 37`, `pdf_page_index: 43`)
- **Trích dẫn gốc**:  
  > *"Crushers and mills usually have constant load curves. These applications can have a very big flywheel and can be a very heavy duty start... Crushers, mixers, mills and stirrers usually have a very big moment of inertia so the softstarter is selected one size larger than the motor kW size."*
- **Ý nghĩa kỹ thuật**: Đối với các ứng dụng có mô-men quán tính rất lớn như máy nghiền (crushers, mills) hoặc máy khuấy (mixers, stirrers), Soft Starter thường được chọn lớn hơn một cấp công suất (one size larger) so với công suất kW của động cơ để đáp ứng điều kiện khởi động nặng.

---

## 4. PHÂN TÍCH BẤT ĐỒNG & SẮC THÁI KỸ THUẬT (TECHNICAL NUANCE & CONFLICT ANALYSIS)

### `CON-001`: Giới hạn dòng khởi động tối thiểu của Soft Starter và nguy cơ kẹt Rotor
* **Trạng thái**: `RESOLVED`
* **Các bên liên quan**: Rockwell Automation (`SRC-002`, Table 1, p. 6) đối chiếu với ABB (`SRC-001`, p. 20 & p. 37).
* **Nội dung bất đồng/sắc thái**:
  - Rockwell Automation công bố số liệu thực nghiệm: khi giảm giới hạn dòng khởi động của Soft Starter xuống $150\%$, mô-men khởi động sụt giảm xuống chỉ còn $6\%$ mô-men định mức.
  - ABB khuyến cáo đối với các tải nặng có quán tính lớn (băng tải tải nặng, máy nghiền, máy khuấy), việc cài đặt dòng khởi động quá thấp sẽ khiến động cơ không thể sinh đủ mô-men bứt phá ma sát tĩnh ban đầu ($T_{breakaway}$), có thể gây kẹt rotor và phát nóng.
* **Định hướng xử lý cho Drafting Agent**:
  - Không được đưa ra nhận định chung chung rằng "Khởi động mềm luôn có thể giảm dòng khởi động xuống mức rất thấp mà vẫn khởi động êm mọi loại tải".
  - Nhấn mạnh mối quan hệ phi tuyến $T \approx \left(\frac{U}{U_n}\right)^2 \cdot T_n$. Với tải nặng hoặc tải quán tính lớn, cần đánh giá chọn Soft Starter lớn hơn một cấp công suất (oversizing) hoặc chuyển sang đánh giá VFD / phương pháp truyền động khác nếu tải đòi hỏi mô-men bứt phá cao ngay tại tốc độ $0\text{ rpm}$.

### `CON-002`: Đánh giá mức độ phát sinh sóng hài và sự cần thiết của bộ lọc hài
* **Trạng thái**: `REVIEW_REQUIRED`
* **Các bên liên quan**: ABB (`SRC-001`, p. 68), Rockwell Automation (`SRC-002`, p. 12), và IEEE Std 519-2022 (`SRC-004`, Table 2).
* **Nội dung bất đồng/sắc thái**:
  - Rockwell chỉ ra rằng ở chế độ bypass Soft Starter hầu như không phát sinh sóng hài, và ABB nhận định sóng hài ít liên quan đối với softstarter trong đa số ứng dụng. Trong khi đó, VFD tạo sóng hài liên tục trong suốt quá trình hoạt động.
  - Tuy nhiên, chuẩn IEEE Std 519-2022 đánh giá giới hạn biến dạng dòng điện (TDD) tại điểm đấu nối chung (PCC) của toàn hệ thống/nhà máy, chứ không áp đặt trực tiếp lên từng thiết bị riêng lẻ. Do đó, sự cần thiết và loại bộ lọc sóng hài (cuộn kháng, lọc thụ động, lọc tích cực) phụ thuộc vào tỷ số ngắn mạch của trạm $I_{sc}/I_L$ và tổng phụ tải phi tuyến, không thể khẳng định mọi VFD đều vi phạm hoặc bắt buộc phải gắn lọc ngoại vi.
* **Định hướng xử lý cho Drafting Agent**:
  - Phân tách 2 trạng thái của Soft Starter: giai đoạn tăng tốc có sóng hài ngắn hạn ($< 10\%$), giai đoạn bypass hầu như không phát sinh sóng hài.
  - Trình bày IEEE Std 519-2022 như chuẩn mực đánh giá tại PCC. Không khẳng định số liệu suy diễn chưa kiểm chứng (như 35%-45% THD-I hay THD = 0%). Chờ Technical Review Gate thẩm định thêm trước khi kết luận về yêu cầu bộ lọc.

---

## 5. NHẬT KÝ SÀNG LỌC ỨNG VIÊN NGUỒN (CANDIDATE SOURCE EVALUATION LOG)

Thực thi theo quy chuẩn Cổng tiếp nhận ứng viên nguồn (Source Acceptance Gate — 8 tiêu chí cốt lõi):

| Mã ứng viên | Nhà xuất bản / Tiêu đề | URL truy xuất | Kết quả Thẩm định | Mã lý do loại bỏ (nếu rớt) | Ghi chú kỹ thuật |
|:---:|:---|:---|:---:|:---:|:---|
| `CAN-001` | ABB — *Softstarter Handbook* | Direct PDF (library.e.abb.com) | **ACCEPTED** $\rightarrow$ `SRC-001` | - | Nguồn sơ cấp Tier 1 OEM Manual, đối chiếu trực tiếp từ file PDF chính thức của ABB. |
| `CAN-002` | Rockwell Automation — *When to use Soft Starter vs VFD* | Direct PDF (literature.rockwellautomation.com) | **ACCEPTED** $\rightarrow$ `SRC-002` | - | Báo cáo kỹ thuật Tier 1 OEM White Paper chuẩn mực, có bảng số liệu thực nghiệm dòng - mô-men định lượng. |
| `CAN-003` | Schneider Electric — *Soft starters vs. VFDs Conveyor Guide* | Direct URL (blog.se.com) | **ACCEPTED** $\rightarrow$ `SRC-003` | - | Bài viết chuyên gia Tier 3 OEM Blog, phân tích tổn hao bypass và zero speed torque (đạt điều kiện nguồn bổ trợ thực hành). |
| `CAN-004` | IEEE — *IEEE Std 519-2022 Harmonic Control* | Canonical / IEEE Xplore | **ACCEPTED** $\rightarrow$ `SRC-004` | - | Tiêu chuẩn quốc tế Tier 1 về giới hạn méo dòng sóng hài tại PCC. |
| `CAN-005` | Siemens — *SIRIUS 3RW44 Soft Starters Manual* | SIOS Portal Entry 21772518 | **REJECTED** | `REJECTED_PAYWALL_OR_BOT_BLOCK` | Máy chủ Siemens kích hoạt tường lửa chống bot (WAF) trả về HTTP 403 Forbidden trên crawler tự động. |
| `CAN-006` | Danfoss — *VLT / MCD Design Guide* | files.danfoss.com/MG90N502.pdf | **REJECTED** | `REJECTED_DEAD_LINK` | Đường dẫn máy chủ cũ trả về HTTP 404 Not Found (link chết), vi phạm ADR-015. |
| `CAN-007` | Chint Global — *VFD vs Soft Starter Guide* | chintglobal.com blog | **REJECTED** | `REJECTED_TIER3_UNQUALIFIED` | Bài viết tổng hợp thương mại cấp 3 (Tier 3), không có số liệu kỹ thuật hoặc công thức gốc kiểm chứng. |

---

## 6. TỔNG KẾT TRẠNG THÁI NGHIÊN CỨU & CÁC HẠNG MỤC CHỜ THẨM ĐỊNH (RESEARCH SUMMARY & OUTSTANDING ITEMS)

Thu thập chứng cứ nghiên cứu kỹ thuật đã hoàn thành cho tập nguồn tài liệu hiện tại (`SRC-001` đến `SRC-004`).

### Các hạng mục kỹ thuật chờ xử lý chuyên đề (Outstanding Review Items):
1. **`RQ-006`** — Khảo sát dữ liệu tươi mới về chi phí đầu tư ban đầu (CAPEX), kích thước lắp đặt tủ điện (Footprint) và yêu cầu bảo trì vòng đời (`freshness_required: true`, hiện ở trạng thái `PARTIALLY_ANSWERED`).
2. **`CON-002`** — Thẩm định ranh giới kỹ thuật về phát sinh sóng hài giữa Soft Starter và VFD đối chiếu với chuẩn IEEE Std 519-2022 tại điểm đấu nối chung PCC (`status: REVIEW_REQUIRED`).

### Cam kết tuân thủ quy chuẩn nghiên cứu & kiểm soát tiến trình:
- [x] Sử dụng $100\%$ Stable Source ID (`SRC-001` đến `SRC-004`), tuyệt đối không cấp phát số trích dẫn IEEE `[n]` ở giai đoạn này.
- [x] Tách biệt độc lập giữa kiểm tra mạng (`HTTP 200` / `REDIRECTED_OK`) và kiểm tra xác thực nội dung (`claim_verified: true`, `content_identity_verified: true`).
- [x] Áp dụng nghiêm ngặt nguyên tắc **"No Snippet Evidence Rule"**: $100\%$ bằng chứng kỹ thuật được đọc và trích xuất trực tiếp từ văn bản gốc đã tải về (PDF ABB, PDF Rockwell, IEEE 519-2022, bài phân tích Schneider Electric).
- [x] Tỷ lệ nguồn Tier 1 + Tier 2 đạt $75\%$ (3/4 nguồn Tier 1, 1/4 nguồn Tier 3), thỏa mãn mục tiêu $\ge 70\%$.
- [x] Đã xuất bản song song và đồng bộ 4 tệp cốt lõi: `article_status.json`, `research_plan.json`, `research_log.json`, `evidence.json`, và `evidence_dossier.md`.
- [x] **DRAFTING READINESS: NOT READY** — Chưa đủ điều kiện handoff sang khâu Drafting do còn 2 task chuyên đề `RQ-006` và `CON-002` cần xử lý. Dừng kiểm soát tại cửa ải nghiên cứu: tuyệt đối không tự ý viết bản thảo (`draft_review_package.md`), không tạo bảng đặc tả ảnh và không sinh mã HTML cho đến khi có lệnh điều phối tiếp theo.
