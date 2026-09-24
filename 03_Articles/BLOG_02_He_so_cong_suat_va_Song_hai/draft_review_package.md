# GÓI THẨM ĐỊNH BÀI VIẾT (DRAFT REVIEW PACKAGE) — BLOG_02

**Loại bài**: `BLOG-T01` — Technical Explanation  
**Mục tiêu**: Giải thích bản chất kỹ thuật của Hệ số công suất trong môi trường có sóng hài, phân biệt \(\cos\varphi\) và True Power Factor, phân tích nguy cơ cộng hưởng tụ bù và đề xuất giải pháp xử lý.

---

## PHẦN 1–6: THÔNG TIN XUẤT BẢN & SEO METADATA

### 1. Tiêu đề bài viết
> **Hệ số công suất cos phi và sóng hài trong nhà máy: Phân biệt bản chất và giải pháp xử lý triệt để**

### 2. Meta Title
> Hệ số công suất cos phi và sóng hài: Bản chất & Giải pháp xử lý | Real Group

### 3. Keyword Tag
- hệ số công suất
- cos phi và sóng hài
- true power factor
- displacement power factor
- nổ tụ bù sóng hài
- cuộn kháng chặn sóng hài 7%
- lọc sóng hài tích cực AHF
- biến dạng dòng điện THDi

### 4. Description Tag
> Phân biệt sự khác nhau giữa cos phi và True Power Factor (PF) trong lưới điện có tải phi tuyến. Hướng dẫn tính toán méo sóng hài THDi, nguy cơ cộng hưởng nổ tụ bù và giải pháp cuộn kháng lọc sóng hài hiệu quả.

### 5. Featured Image Specification
- **Kích thước chuẩn**: `808 × 500 px`
- **Tên file đề xuất**: `he-so-cong-suat-cos-phi-va-song-hai-nha-may-808x500.webp`
- **ALT Text**: Kỹ sư điện đo kiểm hệ số công suất và phân tích sóng hài trên tủ điện phân phối hạ thế bằng thiết bị phân tích chất lượng điện năng
- **Image Prompt (Visual Agent)**:
  > *"Professional industrial photograph of an electrical engineer in high-visibility safety clothing and insulated gloves using a calibrated digital power quality analyzer at an industrial main distribution switchboard (MDB). The analyzer screen clearly shows electrical harmonic waveforms and power factor metrics with cool blue and amber LED indicators. Clean, modern factory electrical substation environment, crisp technical lighting, photorealistic, 8k resolution, authentic industrial photography."*

### 6. Mô tả ngắn (Excerpt)
> Nhiều nhà máy dù trang bị hệ thống tụ bù tự động với đồng hồ đo chỉ số \(\cos\varphi\) đạt trên 0.95 nhưng vẫn bị công ty điện lực phạt tiền điện năng phản kháng hoặc liên tục gặp sự cố nổ tụ bù, máy biến áp phát nóng bất thường. Nguyên nhân cốt lõi bắt nguồn từ sự nhầm lẫn giữa **Displacement Power Factor (\(\cos\varphi\))** và **True Power Factor (PF tổng)** trong môi trường lưới điện bị ô nhiễm sóng hài bởi các tải phi tuyến như biến tần, bộ chỉnh lưu và máy hàn. Bài viết này làm rõ bản chất toán học, cơ chế cộng hưởng nguy hiểm và các phương án xử lý kỹ thuật chuẩn xác.

---

## PHẦN 7: BẢN THẢO NỘI DUNG KỸ THUẬT (TECHNICAL DRAFT)

### MỞ ĐẦU
Trong các hệ thống điện công nghiệp truyền thống trước đây, hầu hết phụ tải là các tải tuyến tính (động cơ không đồng bộ chạy trực tiếp qua lưới, lò điện trở, cuộn cảm biến áp). Khi đó, dạng sóng dòng điện và điện áp đều duy trì hình sin chuẩn 50 Hz, và khái niệm "hệ số công suất" được hiểu đơn giản là \(\cos\varphi\) — tức góc lệch pha giữa điện áp và dòng điện.

Tuy nhiên, với sự phổ cập của công nghệ tự động hóa hiện đại, hơn 60% đến 80% phụ tải trong các nhà máy ngày nay là **tải phi tuyến (Non-linear Loads)**: biến tần điều khiển động cơ (VFD), bộ chỉnh lưu công suất (Rectifier), nguồn tổ ong (SMPS), hệ thống chiếu sáng LED công nghiệp và lò hồ quang hàn. Sự hiện diện của các bộ tử bán dẫn đóng cắt phi tuyến làm xuất hiện các sóng hài dòng điện tần số cao (150 Hz, 250 Hz, 350 Hz...), khiến việc áp dụng quan niệm bù \(\cos\varphi\) truyền thống không còn chính xác, thậm chí biến các dàn tụ bù thành "quả bom nổ chậm" trong trạm biến áp [1, p. 3].

---

### 1. Phân biệt bản chất: Displacement Power Factor (\(\cos\varphi\)) và True Power Factor (PF)

Một trong những sai lầm phổ biến nhất của các kỹ sư vận hành là đánh đồng \(\cos\varphi\) với hệ số công suất thực tế của nhà máy.

Theo tiêu chuẩn Schneider Electric và IEEE, hệ số công suất trong lưới điện công nghiệp được phân tách thành hai khái niệm hoàn toàn độc lập [3, p. M10]:

1. **Displacement Power Factor (\(\text{DPF}\) hay \(\cos\varphi_1\))**:
   - Là hệ số công suất tính riêng cho **thành phần sóng cơ bản tần số 50 Hz**.
   - Đo lường mức độ lệch pha về mặt thời gian giữa sóng điện áp cơ bản và sóng dòng điện cơ bản.
   - Các đồng hồ cơ (kim chỉ) hoặc đồng hồ đo tụ bù truyền thống đa phần chỉ đo lường giá trị \(\cos\varphi_1\) này.

2. **True Power Factor (\(\text{PF}\) tổng / Hệ số công suất thực)**:
   - Là tỷ số giữa tổng công suất tác dụng thực tế tiêu thụ (\(P\)) và tổng công suất biểu kiến toàn phần (\(S\)) chạy trên đường dây, bao gồm cả thành phần sóng cơ bản và mọi bậc sóng hài.
   - Đồng hồ đo điện tử đa năng và công tơ điện tử 3 giá của điện lực luôn ghi nhận giá trị \(\text{PF}\) tổng này để tính toán tiền phạt công suất phản kháng.

Khi lưới điện hoàn toàn không có sóng hài (dòng điện và điện áp sin chuẩn), ta có \(\text{PF} = \cos\varphi_1\). Nhưng khi xuất hiện sóng hài, \(\text{PF}\) luôn nhỏ hơn \(\cos\varphi_1\).

---

### 2. Tải phi tuyến làm méo dòng điện và sinh ra sóng hài như thế nào?

Tải phi tuyến là thiết bị tiêu thụ dòng điện không tỷ lệ thuận với điện áp đặt vào nó. Điển hình nhất trong nhà máy là **bộ chỉnh lưu cầu 6 xung (6-pulse bridge rectifier)** ở đầu vào của các biến tần (VFD) hoặc bộ nguồn UPS:

- Cầu đi-ốt chỉ dẫn điện khi biên độ tức thời của điện áp lưới cao hơn điện áp trên thanh cái một chiều (DC bus).
- Hậu quả là dòng điện lấy từ lưới điện không phải là dạng sóng sin liên tục, mà là những xung nhọn ngắt quãng ngắn (dòng điện biến dạng nặng nề).
- Theo nguyên lý phân tích chuỗi Fourier, bất kỳ dạng sóng tuần hoàn méo mó nào cũng có thể phân rã thành một sóng hình sin cơ bản (50 Hz) cộng với tổng của vô số các sóng hình sin có tần số là bội số nguyên của tần số cơ bản (bậc 3: 150 Hz, bậc 5: 250 Hz, bậc 7: 350 Hz, bậc 11: 550 Hz...) [4, p. 8].

Do tính chất đối xứng của nguồn điện 3 pha, các sóng hài bậc chẵn và sóng hài bội 3 thường bị triệt tiêu trên đường dây 3 pha đối xứng. Các bậc sóng hài chiếm tỷ trọng lớn và gây hại nặng nề nhất cho trạm biến áp nhà máy là **bậc 5 (250 Hz)** và **bậc 7 (350 Hz)** [4, p. 10].

<!-- IMAGE_1: Technical Figure — So sánh dạng sóng dòng điện và phổ sóng hài giữa tải tuyến tính và biến tần 6-pulse. -->
> **[Hình 1: Minh họa kỹ thuật]**: So sánh dạng sóng dòng điện giữa tải tuyến tính (sin chuẩn) và tải phi tuyến biến tần 6-pulse (xung nhọn), kèm phổ phân tích sóng hài bậc 5 (250 Hz) và bậc 7 (350 Hz). *(Xem chi tiết AI Prompt và thông số chèn HTML tại `image_specifications.md`)*.

---

### 3. Mối quan hệ toán học giữa sóng hài và hệ số công suất

Trong môi trường điện áp còn tương đối bằng phẳng (\(\text{THD}_u < 5\%\)), biến dạng dòng điện (\(\text{THD}_i\)) là nguyên nhân chính làm suy giảm hệ số công suất thực.

Hệ số công suất tổng (\(\text{PF}\)) được xác định bằng công thức toán học chặt chẽ theo tiêu chuẩn quốc tế [3, p. M12, eq. (2)]:

\begin{equation}
\text{PF} = \frac{P}{S} = \frac{1}{\sqrt{1 + \text{THD}_i^2}} \cdot \cos\varphi_1
\end{equation}

Trong đó:
- \(\text{PF}\): Hệ số công suất thực tế toàn phần (True Power Factor), không có thứ nguyên (giá trị từ 0 đến 1.0).
- \(\cos\varphi_1\): Hệ số dịch pha sóng cơ bản 50 Hz (Displacement Power Factor).
- \(\text{THD}_i\): Độ méo tổng dòng điện (Total Harmonic Distortion of Current), tính theo hệ số tương đối (ví dụ \(\text{THD}_i = 40\% = 0.40\)).

Đại lượng \(\frac{1}{\sqrt{1 + \text{THD}_i^2}}\) được gọi là **Hệ số biến dạng (Distortion Factor)**.

#### Không gian Công suất Budeanu khi có sóng hài:
Khi có sóng hài, công suất biểu kiến toàn phần \(S\) không còn thỏa mãn định lý Pytago tam giác 2 chiều thông thường (\(S = \sqrt{P^2 + Q^2}\)), mà mở rộng thành hình hộp không gian 3 chiều [4, p. 14]:

\begin{equation}
S = \sqrt{P^2 + Q_1^2 + D^2}
\end{equation}

Trong đó:
- \(P\): Công suất tác dụng hữu ích (\(\text{kW}\)).
- \(Q_1\): Công suất phản kháng dịch pha cơ bản 50 Hz (\(\text{kvar}\)) — *đây là thành phần duy nhất tụ bù thông thường có thể triệt tiêu*.
- \(D\): Công suất biến dạng sóng hài (Distortion Power, đơn vị \(\text{kvar}\) hoặc \(\text{kVA}\)) — *hoàn toàn không thể triệt tiêu bằng tụ điện thông thường*.
- \(S\): Công suất biểu kiến toàn phần cấp bởi máy biến áp (\(\text{kVA}\)).

<!-- IMAGE_2: Technical Figure — Mô hình hình học không gian công suất Budeanu 3D (P-Q-D). -->
> **[Hình 2: Minh họa kỹ thuật]**: Mô hình hình học không gian công suất Budeanu 3D (P-Q-D), giải thích vì sao tụ bù truyền thống chỉ triệt tiêu \(Q_1\) mà không thể giảm công suất biến dạng sóng hài \(D\). *(Xem chi tiết AI Prompt và thông số chèn HTML tại `image_specifications.md`)*.

---

### 4. Ví dụ tính toán thực tế tại trạm biến áp nhà máy

Để hiểu rõ tại sao nhà máy dù có \(\cos\varphi\) rất cao nhưng vẫn bị điện lực phạt, hãy xét một trường hợp đo đạc thực tế:

Một phân xưởng dệt may vận hành nhiều dàn máy may và máy dệt điều khiển bằng biến tần, được cấp nguồn từ máy biến áp 1000 kVA. Các thông số đo được bằng máy phân tích chất lượng điện năng Fluke 435 như sau:

- Công suất tác dụng tiêu thụ: \(P = 500\text{ kW}\)
- Hệ số dịch pha sóng cơ bản: \(\cos\varphi_1 = 0.96\) (hệ thống tụ bù đã đóng hoàn tất)
- Độ méo dòng điện tổng: \(\text{THD}_i = 45\% = 0.45\) (do tải biến tần chưa lắp cuộn kháng chặn)

#### Bước 1: Tính toán True Power Factor (\(\text{PF}\)) thực tế
Áp dụng công thức (1):

\begin{equation}
\begin{aligned}
\text{PF} &= \frac{1}{\sqrt{1 + (0.45)^2}} \cdot 0.96 \\
&= \frac{1}{\sqrt{1 + 0.2025}} \cdot 0.96 \\
&= \frac{1}{\sqrt{1.2025}} \cdot 0.96 \\
&\approx \frac{1}{1.0966} \cdot 0.96 \approx 0.875
\end{aligned}
\end{equation}

#### Bước 2: Diễn giải kết quả kỹ thuật
- Đồng hồ hiển thị tụ bù tại chỗ báo: \(\cos\varphi = 0.96\) \(\rightarrow\) Kỹ sư lầm tưởng hệ thống vận hành tối ưu.
- Tuy nhiên, hệ số công suất thực tế ghi nhận bởi công tơ điện tử điện lực chỉ đạt **\(\text{PF} \approx 0.88\)**.
- Theo quy định ngành điện Việt Nam (Thông tư 15/2014/TT-BCT), bên mua điện có hệ số công suất dưới \(0.90\) **bắt buộc phải trả tiền mua công suất phản kháng**. Nhà máy bị phạt tiền hàng tháng mặc dù dàn tụ bù luôn đóng hết công suất!

---

### 5. Nguy cơ cộng hưởng LC và hiện tượng nổ tụ bù trong nhà máy

Tụ điện công nghiệp có đặc tính trở kháng tỷ lệ nghịch với tần số dòng điện:

\begin{equation}
X_c = \frac{1}{2 \pi f C}
\end{equation}

Ở tần số cơ bản 50 Hz, dung kháng \(X_c\) của tụ rất lớn. Nhưng với sóng hài bậc 5 (250 Hz), \(X_c\) giảm đi 5 lần; với sóng hài bậc 7 (350 Hz), \(X_c\) giảm đi 7 lần. Điều này biến dàn tụ điện thành một "bể hút" dòng điện sóng hài tần số cao từ toàn bộ tải trong nhà máy chạy vào tụ [3, p. M22].

#### Hiện tượng Cộng hưởng Song song (Parallel Resonance):
Nguy hiểm hơn cả dòng quá tải là sự xuất hiện của **tần số cộng hưởng song song** giữa điện cảm của máy biến áp cấp nguồn (\(L_{tr}\)) và điện dung của dàn tụ bù (\(C\)).

Bậc sóng hài cộng hưởng (\(h_r\)) được xác định gần đúng theo công thức [4, p. 28, eq. (6.2)]:

\begin{equation}
h_r = \sqrt{\frac{S_{sc}}{Q_c}}
\end{equation}

Trong đó:
- \(h_r\): Bậc sóng hài xảy ra cộng hưởng (không thứ nguyên).
- \(S_{sc}\): Công suất ngắn mạch tại thanh cái hạ thế (\(\text{kVA}\)).
- \(Q_c\): Công suất danh định của dàn tụ bù đang đóng vào lưới (\(\text{kvar}\)).

Nếu vô tình dung lượng tụ bù \(Q_c\) làm cho \(h_r\) rơi vào gần các bậc sóng hài hiện hữu trong xưởng (đặc biệt là bậc 5: \(h_r \approx 4.8 \div 5.2\)):
- Hiện tượng cộng hưởng song song xảy ra, tổng trở của hệ thống tại tần số 250 Hz tăng vọt lên gấp hàng chục lần.
- Dòng điện sóng hài bậc 5 chạy qua tụ bù bị khuếch đại lên gấp 5 đến 15 lần định mức.
- Điện áp thanh cái bị méo dạng nghiêm trọng, gây nổ bung tụ bù, nổ cầu chì bảo vệ, nổ biến tần lân cận và gây rung giật, quá nhiệt nghiêm trọng cuộn dây máy biến áp [4, p. 29].

---

### 6. Các hiểu nhầm phổ biến trong vận hành công nghiệp

| Quan niệm sai lầm | Thực tế kỹ thuật đã chứng minh |
|---|---|
| *"Hệ thống bị phạt công suất phản kháng thì cứ mua thêm tụ bù lắp vào là xong."* | Tụ bù thường chỉ triệt tiêu \(Q_1\), không bù được công suất méo \(D\). Lắp thêm tụ bù càng làm tăng nguy cơ kéo tần số cộng hưởng rơi trúng bậc sóng hài 5 hoặc 7, làm dòng sóng hài tăng vọt và nổ tụ nhanh hơn. |
| *"Biến tần (VFD) hiện đại có \(\cos\varphi \approx 0.98\) nên không lo về chất lượng điện."* | Biến tần dùng chỉnh lưu đi-ốt có \(\cos\varphi_1\) rất cao (gần như bằng 1), nhưng dòng điện ngõ vào bị méo dạng với \(\text{THD}_i\) từ 35% đến 80%. Tải biến tần không cần bù \(Q\), nhưng tạo ra lượng sóng hài khổng lồ cần được xử lý lọc méo. |
| *"Máy biến áp bị nóng là do quá tải công suất kW."* | Dòng điện sóng hài gây hiệu ứng bề mặt (Skin Effect) và dòng điện xoáy Foucault, làm tăng tổn hao đồng và tổn hao sắt trong lõi thép máy biến áp theo bình phương tần số (\(\Delta P \propto f^2\)), khiến MBA phát nhiệt dữ dội dù chỉ đang chạy ở 70% công suất danh định. |

---

### 7. Các giải pháp kỹ thuật xử lý triệt để

Để vừa đáp ứng hệ số công suất \(\text{PF} \ge 0.95\) theo quy định, vừa triệt tiêu nguy cơ nổ tụ bù và giảm biến dạng điện áp, nhà máy cần áp dụng các giải pháp công nghệ phù hợp với mức độ ô nhiễm sóng hài [3, p. M25], [7]:

#### 7.1. Giải pháp 1: Tủ tụ bù có cuộn kháng chặn sóng hài (Detuned Reactor Capacitor Bank)
- **Cơ chế**: Mắc nối tiếp một cuộn kháng điện cảm (\(L\)) với từng cấp tụ điện (\(C\)).
- **Nguyên lý thiết kế**: Hệ \(LC\) nối tiếp được thiết kế sao cho tần số cộng hưởng riêng của bộ tụ-kháng luôn nằm **thấp hơn bậc sóng hài nhỏ nhất** trong lưới.
  - Phổ biến nhất là cuộn kháng **7% (tuning factor \(p = 7\%\))**, có tần số cộng hưởng rơi vào **189 Hz**.
  - Ở tần số 50 Hz: Hệ đóng vai trò là dung kháng thuần túy \(\rightarrow\) Bù công suất phản kháng bình thường cho hệ thống.
  - Ở tần số 250 Hz (bậc 5) trở lên: Hệ đóng vai trò là một **cuộn cảm** \(\rightarrow\) Chống cộng hưởng và ngăn không cho dòng sóng hài bậc cao xâm nhập vào tụ.
- **Phạm vi áp dụng**: Các nhà máy có tỷ lệ công suất tải phi tuyến chiếm từ 15% đến 50% tổng công suất máy biến áp.

#### 7.2. Giải pháp 2: Lọc sóng hài tích cực (Active Harmonic Filter - AHF)
- **Cơ chế**: Thiết bị điện tử công suất sử dụng vi xử lý DSP và van bán dẫn IGBT tốc độ cao.
- **Nguyên lý hoạt động**: AHF liên tục đo lường dòng điện tải, tính toán tức thời thành phần sóng hài và bơm ngược trở lại lưới một dòng điện có biên độ bằng đúng biên độ sóng hài nhưng **ngược pha 180°** [6, p. 1314].
  - Dòng sóng hài của tải và dòng bù của AHF triệt tiêu lẫn nhau ngay tại điểm đấu nối, dòng điện quay trở lại lưới hoặc máy biến áp là sóng sin chuẩn.
  - AHF có khả năng xử lý đồng thời từ bậc 2 đến bậc 50, kiểm soát \(\text{THD}_i < 3\%\) và tự động bù công suất phản kháng siêu tốc từng mili-giây.
- **Phạm vi áp dụng**: Các nhà máy tự động hóa cao, dây chuyền dập kim loại, máy cán thép, trung tâm dữ liệu (Data Center), bệnh viện hoặc các nhà máy có tỷ lệ tải biến tần > 50%.

#### 7.3. Giải pháp 3: Lắp đặt cuộn kháng DC / AC (Choke Reactor) cho từng biến tần
- Lắp đặt cuộn kháng đầu vào xoay chiều (AC Reactor 3% hoặc 5%) hoặc cuộn kháng một chiều (DC Link Choke) tích hợp bên trong biến tần.
- Giải pháp này làm giảm xung nhọn dòng điện nạp tụ DC, hạ \(\text{THD}_i\) của riêng biến tần từ mức 70%–80% xuống còn khoảng 35%–40%, giảm tải đáng kể cho toàn bộ hệ thống phân phối.

---

### 8. Checklist khảo sát chất lượng điện năng tại trạm biến áp

Trước khi đầu tư hoặc thay thế hệ thống tụ bù, đội ngũ kỹ thuật nhà máy cần thực hiện đo đạc và rà soát theo bảng kiểm sau:

- [ ] **1. Tỷ lệ công suất tải phi tuyến (\(S_h / S_n\))**: Đánh giá tổng công suất của các biến tần, UPS, chỉnh lưu so với dung lượng định mức của MBA. Nếu \(S_h / S_n > 20\%\), tuyệt đối không dùng tụ bù thường không kháng.
- [ ] **2. Đo đạc phổ sóng hài bằng máy phân tích chuyên dụng**: Thu thập phổ biến dạng dòng điện (\(\text{THD}_i\)) và điện áp (\(\text{THD}_u\)) liên tục tối thiểu trong 24–48 giờ hoạt động đầy tải.
- [ ] **3. Đối chiếu tiêu chuẩn IEEE 519**: Đảm bảo điện áp tại điểm đấu nối chung có \(\text{THD}_u \le 5.0\%\) và từng sóng hài bậc lẻ không vượt quá 3.0%.
- [ ] **4. Kiểm tra nhiệt độ và dòng điện qua tụ bù**: Sử dụng camera nhiệt kiểm tra các bình tụ đang vận hành; nếu nhiệt độ bề mặt vượt quá 55°C hoặc dòng điện kẹp vượt quá 1.3 lần dòng định mức bình tụ, phải lập tức ngắt cấp tụ để tránh sự cố cháy nổ.
- [ ] **5. Lựa chọn giải pháp bù kết hợp**: Ưu tiên phương án tủ tụ bù kháng 7% kết hợp bộ lọc tích cực AHF công suất vừa đủ để tối ưu chi phí đầu tư (CapEx) và hiệu quả vận hành (OpEx).

---

### 9. Kết luận

Hệ số công suất trong các nhà máy hiện đại không còn là một bài toán thuần túy về việc "bù thừa hay bù thiếu" công suất phản kháng cơ bản 50 Hz. Sự hiện diện áp đảo của các tải phi tuyến biến tần đòi hỏi kỹ sư vận hành phải phân biệt rõ ràng giữa **\(\cos\varphi\)** và **True Power Factor (PF tổng)**.

Việc lắp đặt tụ bù thông thường vào một hệ thống điện bị ô nhiễm sóng hài nặng là một sai lầm kỹ thuật nguy hiểm, trực tiếp kích hoạt hiện tượng cộng hưởng song song làm phá hủy thiết bị. Giải pháp bền vững nhất là khảo sát toàn diện phổ sóng hài, trang bị cuộn kháng chặn sóng hài (Detuned Reactor) cho hệ thống bù tĩnh và tích hợp bộ lọc sóng hài tích cực (AHF) để bảo vệ an toàn cho máy biến áp, nâng cao độ tin cậy và tối ưu hóa chi phí năng lượng toàn diện cho nhà máy.

---

### 10. Tài liệu tham khảo

- [1] *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022.
- [2] *Electromagnetic Compatibility (EMC) - Part 2-4: Compatibility Levels in Industrial Plants for Low-Frequency Conducted Disturbances*, IEC Standard 61000-2-4, 2002.
- [3] *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, Rueil-Malmaison, France, 2018.
- [4] *Technical Guide No. 6: Guide to Harmonics with AC Drives*, ABB Oy, Helsinki, Finland, Tech. Guide 3BFE64292714, 2011.
- [5] “Improving motor and drive system performance: A sourcebook for industry,” US Department of Energy (DOE), Washington, DC, USA, Rep. DOE/GO-102014-4421, 2014.
- [6] H. Akagi, “New trends in active filters for power conditioning,” *IEEE Trans. Ind. Appl.*, vol. 32, no. 6, pp. 1312–1322, Nov./Dec. 1996, doi: 10.1109/28.556635.
- [7] K. Kaiser, “5 Harmonic mitigation methods that help keep costs down and production running,” *Schneider Electric Blog*, Feb. 21, 2017. Accessed: Mar. 10, 2026. [Online]. Available: https://blog.se.com/industry/machine-and-process-management/2017/02/21/5-harmonic-mitigation-methods-help-keep-costs-production-running/

