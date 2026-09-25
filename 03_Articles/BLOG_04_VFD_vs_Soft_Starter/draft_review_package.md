# VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải

## Tóm tắt Kỹ thuật Dành cho Kỹ sư Vận hành (Executive Technical Summary)

Trong kỹ thuật truyền động điện công nghiệp, Biến tần (Variable Frequency Drive — VFD) và Khởi động mềm (Soft Starter) là hai giải pháp được sử dụng phổ biến trong việc kiểm soát quá trình khởi động của động cơ không đồng bộ ba pha rô-to lồng sóc. Khởi động mềm sử dụng các cặp thyristor điều khiển góc kích pha nhằm thay đổi điện áp hiệu dụng trong khi giữ nguyên tần số lưới $50/60\text{ Hz}$; sau khi kết thúc quá trình khởi động, thiết bị thường được chuyển sang chế độ đóng mạch bypass và động cơ quay cố định theo tần số nguồn lưới [1, pp. 21–22]. Ngược lại, biến tần chuyển đổi điện năng qua cấu trúc AC-DC-AC, cho phép điều khiển tốc độ động cơ thông qua việc thay đổi tần số ngõ ra từ $0\text{ Hz}$ đến $250\text{ Hz}$ [1, p. 16] và cung cấp đầy đủ mô-men định mức tại tốc độ zero speed ($0\text{ rpm}$) cho các tải khởi động nặng [3]. Việc lựa chọn giải pháp phù hợp phụ thuộc vào yêu cầu điều chỉnh tốc độ liên tục của quy trình [1, p. 17], mô-men khởi động tại $0\text{ rpm}$ [3], mức độ phát sinh sóng hài đối chiếu với chuẩn IEEE Std 519 tại Điểm Đấu Nối Chung (PCC) [4, p. 10], [5, p. 12], không gian lắp đặt [2, pp. 15–16] và chi phí đầu tư ban đầu [1, p. 20], [2, p. 15].

---

## 1. VFD và Soft Starter Giải quyết Hai Bài toán Khác nhau Thế nào?

Để lựa chọn giải pháp phù hợp cho hệ thống, kỹ sư cần phân định rõ mục tiêu kỹ thuật của từng thiết bị:

1. **Khởi động mềm (Soft Starter)**: Giải quyết bài toán **khởi động êm và dừng êm (Soft Start / Soft Stop)**. Mục đích là giảm xung kích dòng điện lên lưới phân phối và giảm thiểu các xung lực cơ khí (va đập hộp số, giật đứt dây đai truyền động, hiện tượng búa nước đường ống) trong giai đoạn quá độ. Sau khi kết thúc giai đoạn tăng tốc, vai trò điều khiển của khởi động mềm hoàn tất; động cơ vận hành như một động cơ nối trực tiếp vào lưới điện xoay chiều tiêu chuẩn [1, p. 17].
2. **Biến tần (VFD)**: Giải quyết bài toán **điều khiển quá trình liên tục (Continuous Process Control)** thông qua việc thay đổi tốc độ quay của từ trường stato [1, p. 16]. VFD không chỉ đảm nhiệm khâu khởi động và hãm dừng với khả năng cung cấp mô-men bứt phá, mà còn liên tục điều chỉnh tốc độ động cơ theo yêu cầu vận hành [1, p. 16].

Do đó, biến tần và khởi động mềm giải quyết hai bài toán công nghệ khác nhau: biến tần là hệ thống điều khiển tần số và tốc độ động cơ liên tục, trong khi khởi động mềm là giải pháp chuyên biệt cho các phụ tải chạy tốc độ cố định [1, p. 17].

---

## 2. Khác biệt Cốt lõi về Nguyên lý Biến đổi Điện năng và Cấu trúc Công suất

### 2.1. Biến tần (VFD): Cấu trúc AC-DC-AC và Điều khiển Tần số Ngõ ra

Biến tần hạ thế hoạt động dựa trên nguyên lý chuyển đổi năng lượng gián tiếp qua cấu trúc AC-DC-AC [1, p. 16]:

1. **Khối chỉnh lưu (Rectifier Stage)**: Chuyển đổi điện áp xoay chiều ba pha ($50\text{ Hz}$ hoặc $60\text{ Hz}$) từ nguồn lưới thành điện áp một chiều (DC) [1, p. 16].
2. **Khối trung gian DC (DC Bus Stage)**: San phẳng và tích trữ năng lượng điện áp một chiều [1, p. 16].
3. **Khối nghịch lưu (Inverter Stage)**: Chuyển đổi điện áp một chiều trở lại thành điện áp xoay chiều ba pha với tần số ngõ ra biến thiên liên tục trong dải từ $0\text{ Hz}$ đến $250\text{ Hz}$ [1, p. 16].

Thông qua việc thay đổi và điều khiển tần số ngõ ra, biến tần trực tiếp kiểm soát tốc độ quay của từ trường stato và tốc độ của động cơ [1, p. 16]. Đồng thời, theo tài liệu kỹ thuật của Schneider Electric, biến tần có thể cung cấp đầy đủ $100\%$ mô-men định mức (full torque) ngay tại tốc độ zero speed ($0\text{ rpm}$) cho các ứng dụng đòi hỏi mô-men bứt phá [3].

### 2.2. Khởi động mềm (Soft Starter): Điều khiển Góc Kích pha Thyristor (SCR)

Khác với VFD, khởi động mềm không làm thay đổi tần số của nguồn điện cấp mà chỉ điều khiển điện áp hiệu dụng RMS [1, pp. 21–22]. Cấu trúc mạch công suất của Soft Starter bao gồm 3 cặp thyristor (SCR — Silicon Controlled Rectifier) mắc phản song song (back-to-back / anti-parallel) trên ba pha [1, pp. 21–22].

Trong quá trình khởi động, mạch điều khiển phát tín hiệu kích trễ tại các góc mở pha $\alpha$ nhất định đối với từng nửa chu kỳ của điện áp hình sin [1, pp. 21–22]. Bằng cách cho phép chỉ phần sau của mỗi bán kỳ điện áp đi qua và giảm dần góc kích $\alpha$ theo thời gian dốc cài đặt (ramp time), điện áp hiệu dụng cấp tới các đầu cực động cơ tăng dần từ một giá trị khởi đầu cho đến điện áp lưới định mức $100\%$ [1, pp. 21–22]. Tần số của điện áp vẫn giữ nguyên tần số lưới $50\text{ Hz}$ hoặc $60\text{ Hz}$ trong toàn bộ quá trình khởi động [1, pp. 21–22].

---

## 3. So sánh Định lượng Dòng Khởi động và Quan hệ Mô-men - Điện áp

### 3.1. Đặc tính Dòng Khởi động Cực đại (Inrush Current)

Dòng khởi động cực đại là một chỉ tiêu kỹ thuật quan trọng khi thiết kế trạm biến áp và lựa chọn thiết bị đóng cắt bảo vệ:

- **Khởi động Trực tiếp (DOL)**: Dữ liệu thực nghiệm của Rockwell Automation ghi nhận trường hợp khởi động trực tiếp tương ứng với dòng khởi động khoảng $600\%$ dòng định mức ($6.0 \cdot I_n$) [2, Tab. 1, p. 6].
- **Khởi động Mềm (Soft Starter)**: Bảng 1 của Rockwell Automation đưa ra các điểm khảo sát giới hạn dòng ở mức $150\%$, $300\%$ và $450\%$ dòng định mức ($I_n$) với các mức điện áp và mô-men khởi động tương ứng [2, Tab. 1, p. 6].
- **Biến tần (VFD)**: Biến tần có khả năng kiểm soát gia tốc và quá trình khởi động của động cơ thông qua điều khiển tần số và điện áp ngõ ra [1, p. 16]; tuy nhiên, trong gói hồ sơ bằng chứng hiện tại không xác lập một dải số liệu định lượng cụ thể cho dòng khởi động của VFD.

### 3.2. Quan hệ Phi tuyến Giữa Mô-men Khởi động và Điện áp ($T \propto U^2$)

Trong động cơ không đồng bộ, mô-men quay tỷ lệ với bình phương của điện áp hiệu dụng đặt vào cuộn dây stato [2, Tab. 1, p. 6]:

\begin{equation}
T_{\text{start}} \approx \left(\frac{U_{\text{start}}}{U_n}\right)^2 \cdot T_n
\end{equation}

*Trong đó:*
- $T_{\text{start}}$: Mô-men khởi động do động cơ sinh ra ($\text{N}\cdot\text{m}$).
- $T_n$: Mô-men định mức của động cơ ($\text{N}\cdot\text{m}$).
- $U_{\text{start}}$: Điện áp hiệu dụng do Soft Starter cấp tại thời điểm khởi động ($\text{V}$).
- $U_n$: Điện áp định mức của lưới điện ($\text{V}$).

Bảng số liệu thực nghiệm của Rockwell Automation thể hiện quan hệ giữa mức giới hạn dòng, điện áp và mô-men khởi động [2, Tab. 1, p. 6]:

| Phương thức Khởi động | Mức Giới hạn Dòng (% $I_n$) | Điện áp Tương ứng (% $U_n$) | Mô-men Khởi động (% $T_n$) |
|:---|:---:|:---:|:---:|
| **Khởi động Trực tiếp (DOL)** | $600\%$ | $100\%$ | $100\%$ |
| **Khởi động Mềm (Điểm 1)** | $150\%$ | $25\%$ | **$6\%$** |
| **Khởi động Mềm (Điểm 2)** | $300\%$ | $50\%$ | **$25\%$** |
| **Khởi động Mềm (Điểm 3)** | $450\%$ | $75\%$ | **$56\%$** |

Theo các số liệu trên, khi cài đặt giới hạn dòng khởi động ở mức $150\%$, điện áp stato chỉ đạt $25\%$, khiến mô-men khởi động sụt giảm xuống mức $6\%$ mô-men định mức [2, Tab. 1, p. 6]. Nếu mô-men cản ma sát tĩnh ban đầu của hệ thống cơ khí lớn hơn $6\%$, động cơ sẽ không thể khởi động thành công [2, Tab. 1, p. 6].

### 3.3. Yêu cầu Mô-men Bứt phá tại Tốc độ Zero Speed

Khác biệt bản chất giữa VFD và Soft Starter nằm ở khả năng cung cấp mô-men tại thời điểm tốc độ bằng $0$ ($0\text{ rpm}$):

- Biến tần có khả năng cung cấp đầy đủ $100\%$ mô-men định mức ngay tại tốc độ $0\text{ rpm}$ cho các tải khởi động nặng [3].
- Khởi động mềm không có khả năng đáp ứng yêu cầu cung cấp mô-men đầy đủ tại tốc độ $0\text{ rpm}$ [3]. Do đó, đối với các phụ tải đòi hỏi mô-men bứt phá ma sát tĩnh ban đầu (breakaway torque) cao, VFD là phương án cần được xem xét để đảm bảo khả năng khởi động [2, Tab. 1, p. 6], [3].

---

## 4. Khả năng Điều chỉnh và Duy trì Tốc độ Vận hành Liên tục

Khả năng điều khiển tốc độ là ranh giới phân định rõ ràng về mặt phạm vi ứng dụng giữa hai thiết bị [1, p. 17]:

- **Khởi động Mềm**: Sau khi hoàn tất quá trình tăng tốc, khởi động mềm **không có khả năng điều chỉnh tốc độ liên tục** của động cơ; động cơ vận hành cố định theo tần số của nguồn lưới cấp [1, p. 17].
- **Biến tần (VFD)**: Cung cấp khả năng điều chỉnh tốc độ liên tục cho động cơ thông qua việc thay đổi tần số điện áp ngõ ra trong dải từ $0\text{ Hz}$ đến $250\text{ Hz}$ [1, p. 16]. Khi quy trình công nghệ đòi hỏi điều chỉnh tốc độ liên tục trong quá trình vận hành, biến tần là phương án cần được xem xét [1, p. 16], [1, p. 17].

---

## 5. Hiệu suất Năng lượng và Lợi thế của Contactor Bypass

### 5.1. So sánh Hiệu suất và Nhiệt năng Vận hành

Khi vận hành ở tốc độ định mức đầy tải có tích hợp contactor bypass, dòng điện của khởi động mềm được chuyển nhánh qua contactor [2, p. 7], [3]. Điều này giúp khởi động mềm chạy mát hơn và đạt hiệu suất cao hơn so với biến tần vì không có linh kiện bán dẫn công suất chủ động nào phát sinh nhiệt [3]. Ngược lại, trong biến tần, dòng điện liên tục chạy qua các khối linh kiện bán dẫn trong suốt quá trình động cơ làm việc [1, p. 16].

### 5.2. Định mức AC-1 của Contactor Bypass Tích hợp

Contactor bypass tích hợp bên trong bộ khởi động mềm thông thường chỉ cần chọn theo định mức tiêu chuẩn **AC-1** (không yêu cầu định mức tải cảm động cơ **AC-3**) vì contactor bypass không bao giờ phải đóng hoặc cắt dòng điện trong quá trình vận hành bypass thông thường [2, p. 7]. Nhờ đó, kích thước vật lý của contactor được tối ưu hóa mà vẫn đảm bảo độ bền cơ điện [2, p. 7].

---

## 6. Sóng Hài Dòng điện và Ranh giới Áp dụng Chuẩn IEEE Std 519

### 6.1. Đặc tính Sóng Hài Ngắn hạn của Soft Starter

Mức độ phát sinh sóng hài của khởi động mềm mang tính chất cục bộ và ngắn hạn [1, p. 68], [2, p. 12]:

- Trong giai đoạn tăng tốc hoặc giảm tốc (thường kéo dài từ $5$ đến $30$ giây), các thyristor cắt xén dạng sóng điện áp hình sin, làm phát sinh méo dạng dòng điện [1, pp. 21–22], [2, p. 12]. Tuy nhiên, theo các kết quả đo đạc thực nghiệm của Rockwell Automation, độ méo sóng hài dòng điện ($THD_i$) của Soft Starter trong giai đoạn quá độ này thường nằm dưới ngưỡng $10\%$ [2, p. 12].
- Khi chuyển sang chế độ vận hành xác lập đóng contactor bypass, dòng điện hình sin được nối trực tiếp vào lưới nên bản thân thiết bị **hầu như không phát sinh sóng hài** lên hệ thống phân phối [1, p. 68], [2, p. 12].

### 6.2. Sóng Hài Liên tục của VFD theo Cấu trúc Chỉnh lưu

Ngược lại với khởi động mềm, biến tần hoạt động như một phụ tải phi tuyến liên tục tạo ra dòng điện sóng hài trong suốt thời gian vận hành [4, pp. 13–18]. Dòng nạp phi tuyến vào dàn tụ điện DC qua cầu chỉnh lưu tạo ra các bậc sóng hài đặc trưng theo quy luật $h = 6k \pm 1$ (bậc 5, 7, 11, 13, ...) [4, p. 16].

Tuy nhiên, kỹ sư không nên quy chụp một giá trị méo hài cố định cho toàn bộ các hệ truyền động [4, p. 18]. Mức độ méo dòng sóng hài ($THD_i$) ngõ vào của VFD phụ thuộc rất lớn vào cấu trúc mạch chỉnh lưu và trang bị cuộn kháng, với các số liệu điển hình được công bố trong cẩm nang kỹ thuật của ABB [4, pp. 16–18]:

- **Bộ chỉnh lưu 6 xung tiêu chuẩn có trang bị cuộn kháng AC hoặc DC**: Độ méo dòng $THD_i$ điển hình ở tải danh định vào khoảng **$40\%$** [4, p. 18]. Nếu biến tần không được trang bị bất kỳ cuộn kháng nào, đỉnh dòng nạp tụ rất nhọn làm $THD_i$ tăng cao hơn đáng kể [4, p. 13].
- **Bộ chỉnh lưu 12 xung (sử dụng biến áp cách ly lệch pha $30^\circ$)**: Triệt tiêu phần lớn sóng hài bậc 5 và bậc 7, giúp giảm độ méo dòng $THD_i$ xuống xấp xỉ **$10\%$** [4, p. 18].
- **Biến tần nguồn chủ động (Active Front End — AFE / Low Harmonic Drive)**: Sử dụng khối nguồn chủ động IGBT phía ngõ vào, có khả năng triệt tiêu sóng hài chủ động và đưa độ méo dòng $THD_i$ xuống khoảng **$4\%$** [4, p. 18].

Độ méo sóng hài dòng điện tổng được tính toán theo biểu thức chuẩn hóa [4, p. 7]:

\begin{equation}
THD_i = \frac{\sqrt{\sum_{h=2}^{\infty} I_h^2}}{I_1} \times 100\%
\end{equation}

*Trong đó:*
- $I_1$: Dòng điện hiệu dụng ở tần số cơ bản $50\text{ Hz}$ ($\text{A}$).
- $I_h$: Dòng điện hiệu dụng của thành phần sóng hài bậc $h$ ($\text{A}$).

### 6.3. Ranh giới Áp dụng Chuẩn IEEE Std 519-2022 tại Điểm Đấu Nối Chung (PCC)

Một ngộ nhận kỹ thuật phổ biến trong ngành điện là cho rằng: *"Chuẩn IEEE Std 519 quy định giới hạn sóng hài trực tiếp tại cực của từng chiếc biến tần, và do đó mọi biến tần có $THD_i > 5\%$ đều bắt buộc phải gắn thêm bộ lọc ngoại vi"*.

Cách diễn giải này không đúng với nguyên lý và phạm vi của tiêu chuẩn [4, p. 10], [5, p. 12]:

1. **Ranh giới điểm PCC**: Tiêu chuẩn IEEE Std 519-2022 quy định rõ ràng rằng các giới hạn méo dòng tổng ($TDD$ — Total Demand Distortion) chỉ áp dụng tại **Điểm Đấu Nối Chung (PCC — Point of Common Coupling)** giữa khách hàng tiêu thụ điện và đơn vị điện lực (thường là phía thứ cấp hoặc sơ cấp của máy biến áp phân phối trạm), áp dụng cho tổng phụ tải của toàn bộ cơ sở chứ không áp dụng riêng rẽ cho từng thiết bị đơn lẻ [4, p. 10], [5, p. 12].
2. **Quy luật tỷ số ngắn mạch $I_{sc}/I_L$**: Giới hạn méo dòng cho phép được phân tầng dựa trên tỷ số dòng ngắn mạch khả dụng của hệ thống trên dòng phụ tải tổng cực đại của cơ sở ($I_{sc}/I_L$) [4, p. 10], [5, p. 12]. Theo Bảng 2 của IEEE Std 519-2022, đối với các hệ thống điện hạ thế và trung thế từ $120\text{ V}$ đến $69\text{ kV}$, giới hạn méo dòng tổng $TDD$ được quy định ở mức $5.0\%$ khi $I_{sc}/I_L < 20$, và được nới lỏng dần lên $8.0\%$, $12.0\%$, $15.0\%$ và $20.0\%$ khi độ cứng của lưới điện tăng cao ($I_{sc}/I_L > 1000$) [5, p. 12].
3. **Đánh giá sóng hài là bài toán cấp hệ thống tại điểm PCC**: Tiêu chuẩn IEEE Std 519 không bắt buộc mọi biến tần phải lắp đặt bộ lọc sóng hài riêng lẻ; việc lựa chọn biện pháp giảm sóng hài phải dựa trên đánh giá tổng thể toàn bộ cơ sở tại điểm PCC phụ thuộc vào tỷ số $I_{sc}/I_L$ [4, p. 10], [5, p. 12]. Hồ sơ bằng chứng hiện tại không thiết lập một quy tắc áp đặt việc bắt buộc trang bị bộ lọc cho mọi biến tần [4, p. 10].

---

## 7. Chi phí Đầu tư (CAPEX), Không gian Lắp đặt (Footprint) và Bảo trì Vòng đời

### 7.1. Tương quan Chi phí Ban đầu theo Bối cảnh Lịch sử Công nghệ

Khi đánh giá bài toán kinh tế giữa VFD và Soft Starter, kỹ sư cần tiếp cận dưới góc độ quan hệ cấu trúc thiết bị và bối cảnh chi phí tương đối:

- **Ở dải dòng điện và công suất thấp**: Theo so sánh định tính lịch sử của Rockwell Automation, chi phí ban đầu giữa VFD và Soft Starter có mức tương đương hoặc chênh lệch không quá lớn [2, p. 15].
- **Khi dòng điện và công suất tăng lên**: Chi phí đầu tư của biến tần tăng cao hơn đáng kể so với khởi động mềm [2, p. 15]. Sự chênh lệch chi phí này bắt nguồn từ độ phức tạp cấu trúc phần cứng của biến tần công suất lớn so với cấu trúc bán dẫn đơn giản hơn của khởi động mềm [1, p. 20], [2, p. 15].

Để hình dung tương quan về chi phí cấu trúc lắp đặt, bảng đối chiếu kinh nghiệm của ABB cung cấp một chỉ số tham chiếu tương đối có giá trị lịch sử kỹ thuật [1, p. 20]:

| Phương thức Khởi động | Chỉ số Chi phí Lắp đặt Bình quân Ước tính | Đánh giá Cấu trúc Chi phí |
|:---|:---:|:---|
| **Khởi động Trực tiếp (DOL)** | **1** | Mức chuẩn cơ sở tối thiểu (Contactor + Rơ-le nhiệt) |
| **Khởi động Sao - Tam giác (Star-Delta)** | **3** | Gấp 3 lần chuẩn cơ sở (Yêu cầu 3 contactor và rơ-le thời gian) |
| **Khởi động Mềm (Softstarter)** | **6** | Gấp 6 lần chuẩn cơ sở (Khối SCR công suất + Mạch kích vi điều khiển) |
| **Biến tần (Drives)** | **> 12** | Gấp trên 12 lần chuẩn cơ sở (Khối AC-DC-AC, lọc tụ, vi xử lý PWM) |

> [!NOTE]
> Bảng chỉ số trên là dữ liệu đối chiếu cấu trúc chi phí lắp đặt bình quân định tính trong tài liệu kỹ thuật của ABB [1, p. 20], không phải là bảng giá thương mại hay tỷ lệ cố định cho thị trường năm 2026. Cấu trúc phần cứng phức tạp của biến tần thường đặt ra mức chi phí đầu tư ban đầu cao hơn so với khởi động mềm khi công suất tăng lên [1, p. 20], [2, p. 15].

### 7.2. Thể tích Lắp đặt và Không gian Tủ điện (Panel Footprint)

Về kích thước vật lý, khởi động mềm có thể tích nhỏ hơn đáng kể so với biến tần trên toàn bộ dải công suất [2, pp. 15–16]:

- Soft Starter có kích thước bao ngoài nhỏ hơn, cấu trúc cơ khí gọn gàng và không đòi hỏi không gian tủ quá lớn [2, pp. 15–16].
- Biến tần công suất lớn có thể tích vật lý tăng mạnh do phải bố trí dàn tụ điện DC bus và quạt làm mát lưu lượng cao [2, pp. 15–16]. Ngoài ra, biến tần công suất lớn thường được lắp đặt trong các khoang tủ dạng Trung tâm Điều khiển Động cơ (MCC — Motor Control Center) nhằm tích hợp thêm các thiết bị phụ trợ đồng bộ như thiết bị cách ly, cuộn kháng đường dây ngõ vào/ngõ ra và bộ hạn chế nhiễu EMC [2, p. 15]. Điều này đòi hỏi không gian lắp đặt tủ điện lớn hơn trong phòng điện.

### 7.3. Quy trình Bảo dưỡng Định kỳ và Kiểm soát Lão hóa Linh kiện

Về yêu cầu bảo trì vòng đời, tài liệu của Rockwell Automation cung cấp danh mục kiểm tra bảo dưỡng phòng ngừa chi tiết cho hệ thống truyền động biến tần [6, pp. 1–4]:
1. **Chu kỳ kiểm tra**: Khuyến nghị thực hiện kiểm tra ban đầu trong vòng $3$ đến $4$ tháng sau khi đưa vào vận hành, và lặp lại định kỳ hàng năm trong điều kiện vận hành bình thường [6, p. 1].
2. **Bảo dưỡng hệ thống làm mát cưỡng bức**: Quạt làm mát và quạt thổi khí cưỡng bức cần được kiểm tra định kỳ [2, p. 17], [6, p. 2]. Kỹ sư phải kiểm tra độ rơ trục, hiện tượng nứt/mẻ cánh quạt và thay thế khi quạt không quay trơn tru [2, p. 17], [6, p. 2]. Tấm lọc bụi phải được vệ sinh hoặc thay mới; tài liệu OEM khuyến cáo nghiêm ngặt **tuyệt đối không dùng khí nén xịt trực tiếp** để làm sạch bụi bẩn trên thiết bị [6, p. 2].
3. **Quy trình kích hoạt lại tụ điện (Bus Capacitor Reforming)**: Tụ điện điện phân DC bus bị suy giảm nếu không được cấp điện trong thời gian dài [6, p. 4]. Đối với các biến tần lưu kho dự phòng lâu ngày, trước khi đóng điện vận hành chính thức, kỹ sư cần thực hiện quy trình kích hoạt lại tụ điện (capacitor reforming guidelines) theo khuyến nghị của nhà sản xuất [6, p. 4].

---

## 8. Ma trận Đánh giá và Hướng dẫn Lựa chọn theo Nhóm Phụ tải Công nghiệp

### 8.1. Bơm Ly tâm (Centrifugal Pumps)

Trong ứng dụng máy bơm, tài liệu của ABB ghi nhận việc khởi động động cơ thường không phải là vấn đề lớn về mặt điện học, mà thách thức kỹ thuật chủ yếu là hiện tượng hao mòn do sóng áp suất trong hệ thống đường ống xuất hiện khi động cơ khởi động và đặc biệt là khi dừng quá nhanh [1, p. 29]:

- Nếu mục tiêu chính là giảm thiểu hiện tượng sóng áp suất va đập (búa nước) khi dừng động cơ, khởi động mềm cung cấp giải pháp điều khiển dốc dừng êm (soft stop) để hỗ trợ giảm thiểu hiện tượng này [1, p. 29].
- Nếu quy trình công nghệ đòi hỏi điều chỉnh tốc độ liên tục trong quá trình vận hành, biến tần là phương án cần được xem xét đối chiếu thêm theo nguyên lý điều khiển tần số [1, p. 16], [1, p. 17].

### 8.2. Quạt và Blower (Fans & Blowers)

Hiện tại gói hồ sơ bằng chứng kỹ thuật không thiết lập tài liệu chuyên biệt riêng cho phụ tải quạt và blower; do đó việc đánh giá giải pháp cần bám sát các nguyên lý điều khiển cơ bản:

- Nếu ứng dụng yêu cầu điều chỉnh tốc độ liên tục trong quá trình vận hành, biến tần là phương án cần được xem xét theo nguyên lý điều khiển tần số [1, p. 16], [1, p. 17].
- Nếu ứng dụng chỉ yêu cầu khởi động và dừng mà không cần điều chỉnh tốc độ liên tục, khởi động mềm có thể được đánh giá tùy thuộc vào yêu cầu mô-men của tải [1, p. 17], [2, Tab. 1, p. 6].

### 8.3. Băng tải Công nghiệp (Industrial Conveyors)

Băng tải là dạng phụ tải đòi hỏi mô-men khởi động ổn định [3]:

- **Tiêu chí lựa chọn**:
  - *Xem xét Khởi động mềm*: Phù hợp khi yêu cầu chủ yếu là khởi động và dừng êm mà không đòi hỏi điều chỉnh tốc độ liên tục trong quá trình làm việc, tùy thuộc vào yêu cầu mô-men của tải [1, p. 17], [2, Tab. 1, p. 6].
  - *Cân nhắc Biến tần*: Khi phụ tải yêu cầu đầy đủ mô-men ngay tại tốc độ zero speed ($0\text{ rpm}$), biến tần là phương án cần được xem xét để đảm bảo khả năng khởi động [2, Tab. 1, p. 6], [3].

### 8.4. Máy Nghiền Đá, Máy Xay và Máy Khuấy (Crushers, Mills & Mixers)

Nhóm phụ tải này có đặc tính khởi động khắc nghiệt do mô-men quán tính lớn và lực cản ban đầu cao [1, p. 37]:

- **Nguyên tắc định cỡ Soft Starter**: Đối với các ứng dụng có mô-men quán tính rất lớn như máy nghiền (crushers, mills) hoặc máy khuấy (mixers, stirrers), tài liệu kỹ thuật của ABB cho biết Soft Starter thường được chọn lớn hơn một cấp công suất (oversizing: one size larger) so với công suất động cơ ($kW\text{ size}$) [1, p. 37].
- **Cân nhắc Biến tần**: Khi ứng dụng đòi hỏi mô-men bứt phá ban đầu tại tốc độ $0\text{ rpm}$, biến tần là giải pháp kỹ thuật phù hợp nhờ khả năng cung cấp đầy đủ mô-men ngay tại tốc độ zero speed [3].

---

## 9. Bảng Đối chiếu Tổng hợp Đa chiều Giữa VFD và Soft Starter

| Tiêu chí Đánh giá Kỹ thuật | Khởi động Mềm (Soft Starter) | Biến tần (VFD) | Căn cứ Chứng minh Kỹ thuật |
|:---|:---|:---|:---:|
| **Nguyên lý Biến đổi** | Điều khiển góc kích pha Thyristor (SCR); điện áp RMS thay đổi, tần số lưới giữ nguyên ($50/60\text{ Hz}$). | Chuyển đổi gián tiếp AC-DC-AC; biến đổi liên tục tần số ngõ ra ($0-250\text{ Hz}$) và điện áp. | `EVD-001`, `EVD-002` [1] |
| **Dòng Khởi động Điển hình** | Bảng 1 của Rockwell khảo sát các điểm giới hạn dòng $150\%$, $300\%$, $450\%$ dòng định mức ($I_n$). | Kiểm soát quá trình khởi động qua tần số và điện áp; hồ sơ bằng chứng không xác lập số liệu định lượng dải dòng. | `EVD-001`, `EVD-003` [1], [2] |
| **Mô-men Khởi động tại $0\text{ rpm}$** | Sụt giảm mạnh theo bình phương điện áp ($T \propto U^2$); điểm giới hạn dòng $150\%$ chỉ cho mô-men $6\%$. Không cung cấp được full torque tại $0\text{ rpm}$. | Cung cấp đầy đủ $100\%$ mô-men định mức ngay tại tốc độ $0\text{ rpm}$ trong các ứng dụng yêu cầu. | `EVD-003`, `EVD-004` [2], [3] |
| **Điều khiển Tốc độ Vận hành** | Không hỗ trợ; sau dốc khởi động động cơ quay cố định theo tần số nguồn lưới. | Điều chỉnh dải tốc độ liên tục theo tần số ngõ ra ($0-250\text{ Hz}$). | `EVD-001`, `EVD-005` [1] |
| **Hiệu suất Vận hành Xác lập** | Cao hơn khi đóng Contactor Bypass; thiết bị chạy mát hơn do không có linh kiện bán dẫn công suất phát nhiệt. | Dòng tải liên tục chạy qua linh kiện bán dẫn công suất và phát sinh nhiệt trong quá trình làm việc. | `EVD-001`, `EVD-006` [1], [3] |
| **Định mức Contactor Bypass** | Tích hợp định mức AC-1 do không đóng cắt dòng điện trong vận hành bypass thông thường. | Không áp dụng bypass trong cấu trúc vận hành biến tần tiêu chuẩn. | `EVD-007` [2] |
| **Đặc tính Phát sinh Sóng Hài** | Sóng hài ngắn hạn ($< 10\%$) khi khởi động; ở bypass hầu như không phát sinh sóng hài từ thiết bị. | Phát sinh sóng hài liên tục; $THD_i$ phụ thuộc cấu hình (6-pulse $\approx 40\%$, 12-pulse $\approx 10\%$, AFE $\approx 4\%$). | `EVD-008`, `EVD-013` [1], [2], [4] |
| **Ranh giới Chuẩn IEEE Std 519** | Hầu như không tác động lên ranh giới PCC ở chế độ bypass. | Đánh giá tổng thể tại điểm PCC theo tỷ số $I_{sc}/I_L$; không bắt buộc từng drive phải có lọc riêng. | `EVD-008`, `EVD-009`, `EVD-014` [1], [2], [4], [5] |
| **Kích thước & Tủ điện** | Rất nhỏ gọn; không gian tủ điện hẹp, cấu trúc cơ khí đơn giản. | Cồng kềnh; công suất lớn đòi hỏi tủ kiểu MCC có thiết bị phụ trợ (cách ly, cuộn kháng, EMC). | `EVD-015` [2] |
| **Yêu cầu Bảo trì Vòng đời** | Gói hồ sơ bằng chứng hiện tại không xác lập danh mục kiểm tra bảo trì chi tiết cho khởi động mềm. | Kiểm tra ban đầu sau 3-4 tháng và định kỳ hàng năm; kiểm tra quạt làm mát, reforming tụ DC lưu kho. | `EVD-017` [6] |
| **Tương quan Chi phí (CAPEX)** | Chi phí ban đầu dải thấp có thể tương đương; chỉ số chi phí lắp đặt định tính lịch sử của ABB là 6. | Khi dòng và công suất tăng chi phí VFD tăng cao hơn; chỉ số chi phí lắp đặt định tính lịch sử của ABB là > 12. | `EVD-010`, `EVD-016` [1], [2] |

---

## 10. Tiêu chí Lựa chọn Kỹ thuật Tối ưu (Decision Framework)

Để đưa ra quyết định chọn lựa thiết bị chính xác cho dự án, kỹ sư có thể áp dụng các tiêu chí kỹ thuật tuần tự sau:

1. **Câu hỏi 1: Quy trình công nghệ có đòi hỏi điều chỉnh tốc độ liên tục không?**
   - *Có*: **Cân nhắc chọn VFD** [1, p. 16], [1, p. 17]. Khởi động mềm hoàn toàn không đáp ứng được yêu cầu điều chỉnh tốc độ liên tục [1, p. 17].
   - *Không*: Chuyển sang Câu hỏi 2.
2. **Câu hỏi 2: Phụ tải có đòi hỏi đầy đủ mô-men bứt phá tại tốc độ zero speed ($0\text{ rpm}$) không?**
   - *Có*: **Cân nhắc chọn VFD**. Biến tần có khả năng cung cấp đầy đủ $100\%$ mô-men định mức tại tốc độ $0\text{ rpm}$ [3], trong khi khởi động mềm bị sụt giảm mô-men nghiêm trọng khi giảm điện áp [2, Tab. 1, p. 6] và không đáp ứng được yêu cầu này [3].
   - *Không*: Chuyển sang Câu hỏi 3.
3. **Câu hỏi 3: Có các yêu cầu về dòng khởi động, chi phí ban đầu, không gian lắp đặt hoặc tuân thủ giới hạn sóng hài cần đánh giá không?**
   - *Giới hạn dòng khởi động*: Nếu lưới điện có giới hạn nghiêm ngặt về dòng khởi động, kỹ sư cần đối chiếu yêu cầu dòng/mô-men của tải với khả năng của từng phương án và dữ liệu của nhà sản xuất [1], [2].
   - *Chi phí ban đầu & Không gian lắp đặt*: Ở dải công suất thấp chi phí ban đầu giữa VFD và Soft Starter có thể tương đương; khi dòng điện và công suất tăng lên thì chi phí của biến tần tăng cao hơn [2, p. 15]. Khởi động mềm chiếm không gian nhỏ hơn [2, pp. 15–16] và vận hành mát hơn khi đóng bypass [3].
   - *Tuân thủ chuẩn IEEE Std 519*: Đánh giá tổng thể độ méo dòng TDD tại Điểm Đấu Nối Chung (PCC) của toàn bộ cơ sở dựa trên tỷ số ngắn mạch $I_{sc}/I_L$ [4, p. 10], [5, p. 12].

---

## 11. Kết luận Kỹ thuật

Trong kỹ thuật truyền động điện công nghiệp, việc lựa chọn giữa Biến tần (VFD) và Khởi động mềm (Soft Starter) cần căn cứ chặt chẽ vào yêu cầu công nghệ của phụ tải:

- **Khởi động mềm (Soft Starter)**: Là giải pháp phù hợp khi yêu cầu cốt lõi là kiểm soát quá trình khởi động êm và dừng êm nhằm giảm xung dòng và giảm ứng suất cơ học, đồng thời hệ thống không đòi hỏi điều chỉnh tốc độ liên tục trong quá trình vận hành [1, p. 17].
- **Biến tần (VFD)**: Là giải pháp phù hợp khi hệ thống đòi hỏi khả năng điều chỉnh tốc độ liên tục thông qua thay đổi tần số ngõ ra [1, p. 16] hoặc phụ tải yêu cầu cung cấp đầy đủ mô-men định mức ngay tại tốc độ zero speed ($0\text{ rpm}$) [3].

Việc nắm vững các nguyên lý điều khiển, quan hệ dòng - mô-men và ranh giới đánh giá sóng hài tại điểm PCC theo chuẩn IEEE Std 519 sẽ giúp kỹ sư đưa ra quyết định thiết kế phù hợp với yêu cầu thực tế của từng ứng dụng.

---

## Tài liệu Tham khảo (References)

[1] *Softstarter Handbook*, ABB AB, Cewe-Control, Västerås, Sweden, Doc. 1SFC132060M0201, 2011. [Online]. Available: https://library.e.abb.com/public/6b4e1a3530814df0c12579bb0030e58b/1SFC132060M0201.pdf

[2] “When to use a Soft Starter or an AC Variable Frequency Drive,” Rockwell Automation, Inc., Milwaukee, WI, USA, White Paper 150-WP007A-EN-P, 2014. [Online]. Available: https://literature.rockwellautomation.com/idc/groups/literature/documents/wp/150-wp007_-en-p.pdf

[3] M. Duncan, “Soft starters vs. VFDs: Which one is right for your conveyor motor application?,” *Schneider Electric Blog*, Aug. 3, 2020. Accessed: Sep. 24, 2026. [Online]. Available: https://blog.se.com/industrial-automation/2020/08/03/soft-starters-vs-vfds-which-one-is-right-for-your-conveyor-motor-application/

[4] *Technical Guide No. 6: Guide to Harmonics with AC Drives*, ABB Oy, Drives, Helsinki, Finland, Tech. Guide 3AFE64292714 Rev F, 2017. [Online]. Available: https://library.e.abb.com/public/bc35ffb4386c4c039e3a8ec20cef89c5/Technical_guide_No_6_3AFE64292714_RevF_EN.pdf

[5] *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. [Online]. Available: https://ieeexplore.ieee.org/document/9848440

[6] “Preventive Maintenance Checklist of Industrial Control and Drive System Equipment,” Rockwell Automation, Inc., Milwaukee, WI, USA, Tech. Report DRIVES-TD001C-EN-P, 2019. [Online]. Available: https://literature.rockwellautomation.com/idc/groups/literature/documents/td/drives-td001_-en-p.pdf
