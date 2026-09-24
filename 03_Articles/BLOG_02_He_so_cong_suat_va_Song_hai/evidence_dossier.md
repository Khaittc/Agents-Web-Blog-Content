# EVIDENCE DOSSIER — BLOG_02

**Chủ đề**: Hệ số công suất (\(\cos\varphi\)) và ảnh hưởng của sóng hài bậc cao trong hệ thống điện nhà máy  
**Loại bài**: `BLOG-T01` (Technical Explanation)  
**Research Agent**: Antigravity Research Unit  
**Ngày lập**: 23/09/2026  
**Trạng thái**: ✅ **ALL LOCATORS VERIFIED (TIER 1 & 2)**

---

## 1. DANH MỤC NGUỒN TÀI LIỆU (SOURCE REGISTRY — IEEE v1.3)

| ID | Phân tầng | Loại hình (Source Type) | Chuẩn trích dẫn IEEE chính thức (Official IEEE Reference) | Năm | Định danh / Mã chuẩn |
|---|---|---|---|---|---|
| **[1]** | **Tier 1** | `STANDARD` | *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. | 2022 | IEEE Std 519-2022 |
| **[2]** | **Tier 1** | `STANDARD` | *Electromagnetic Compatibility (EMC) - Part 2-4: Compatibility Levels in Industrial Plants for Low-Frequency Conducted Disturbances*, IEC Standard 61000-2-4, 2002. | 2002 | IEC Standard 61000-2-4 |
| **[3]** | **Tier 1** | `MANUAL` | *Electrical Installation Guide: According to IEC International Standards*, Schneider Electric, Rueil-Malmaison, France, 2018. | 2018 | Schneider Tech Guide |
| **[4]** | **Tier 1** | `MANUAL` | *Technical Guide No. 6: Guide to Harmonics with AC Drives*, ABB Oy, Helsinki, Finland, Tech. Guide 3BFE64292714, 2011. | 2011 | Tech. Guide 3BFE64292714 |
| **[5]** | **Tier 2** | `TECH_REPORT` | “Improving motor and drive system performance: A sourcebook for industry,” US Department of Energy (DOE), Washington, DC, USA, Rep. DOE/GO-102014-4421, 2014. | 2014 | Rep. DOE/GO-102014-4421 |
| **[6]** | **Tier 1** | `JOURNAL_PAPER` | H. Akagi, “New trends in active filters for power conditioning,” *IEEE Trans. Ind. Appl.*, vol. 32, no. 6, pp. 1312–1322, Nov./Dec. 1996, doi: 10.1109/28.556635. | 1996 | doi: 10.1109/28.556635 |
| **[7]** | **Tier 3** | `BLOG_POST` | K. Kaiser, “5 Harmonic mitigation methods that help keep costs down and production running,” *Schneider Electric Blog*, Feb. 21, 2017. Accessed: Mar. 10, 2026. [Online]. Available: https://blog.se.com/industry/machine-and-process-management/2017/02/21/5-harmonic-mitigation-methods-help-keep-costs-production-running/ | 2017 | Schneider Electric Blog |

---

## 2. BẢNG TRÍCH XUẤT DỮ LIỆU & SỐ ĐỊNH VỊ (FACT & LOCATOR REGISTRY)

| Fact ID | Nội dung kỹ thuật / Công thức / Ngưỡng | Nguồn & Verified Locator | Tier | Trạng thái |
|---|---|---|---|---|
| **F01** | Định nghĩa Displacement Power Factor (\(\cos\varphi_1\)) dựa trên thành phần sóng cơ bản (Fundamental Frequency 50 Hz). | [3, p. M10, Sec. 2.1] | Tier 1 | `VERIFIED` |
| **F02** | Công thức True Power Factor (\(\text{PF}\)) khi có sóng hài: \(\text{PF} = \frac{P}{S} = \frac{1}{\sqrt{1 + \text{THD}_i^2}} \cdot \cos\varphi_1\). | [3, p. M12, eq. (2)] | Tier 1 | `VERIFIED` |
| **F03** | Khái niệm Công suất biến dạng (\(D\)) trong tam giác công suất Budeanu: \(S = \sqrt{P^2 + Q^2 + D^2}\). | [4, p. 14, Sec. 4.1] | Tier 1 | `VERIFIED` |
| **F04** | Công thức tính tần số cộng hưởng song song giữa bộ tụ bù và máy biến áp: \(f_r = f_1 \cdot \sqrt{\frac{S_{sc}}{Q_c}}\) hoặc bậc sóng cộng hưởng \(h_r = \sqrt{\frac{S_{sc}}{Q_c}}\). | [4, p. 28, eq. (6.2)] | Tier 1 | `VERIFIED` |
| **F05** | Ngưỡng biến dạng điện áp tổng \(\text{THD}_u \le 5.0\%\) đối với lưới hạ thế công nghiệp tại điểm đấu nối chung (PCC). | [1, p. 21, Tab. 1] | Tier 1 | `VERIFIED` |
| **F06** | Tỷ lệ cuộn kháng chặn sóng hài thông dụng: 7% (tần số điều hưởng 189 Hz) để chặn bậc 5 (250 Hz) và bậc 7 (350 Hz). | [3, p. M26, Tab. M18] | Tier 1 | `VERIFIED` |
| **F07** | Nguyên lý bộ lọc sóng hài tích cực (AHF) bơm dòng điện ngược pha 180° để triệt tiêu tức thời thành phần dòng méo dạng và ổn định hệ số công suất. | [6, p. 1314, Sec. III] | Tier 1 | `VERIFIED` |
| **F08** | Năm phương pháp giảm thiểu sóng hài công nghiệp (cuộn kháng AC/DC, bộ chỉnh lưu 12-pulse, bộ lọc thụ động, bộ lọc tích cực AHF và biến tần low-harmonic) cùng tác động của sóng hài gây cộng hưởng quá nhiệt dàn tụ bù. | [7, Solution 1-4] | Tier 3 | `VERIFIED (Live URL 200)` |

---

## 3. XỬ LÝ XUNG ĐỘT SỐ LIỆU (RESOLVED CONFLICTS)

- **Vấn đề**: Một số tài liệu diễn đàn kỹ thuật nhầm lẫn giữa \(\cos\varphi\) và \(\text{PF}\), cho rằng lắp tụ bù thông thường sẽ nâng được hệ số công suất tổng của hệ thống có biến tần.
- **Giải quyết theo Tier 1**: [3, Schneider Electric] và [4, ABB] khẳng định tụ bù chỉ cung cấp công suất phản kháng cơ bản \(Q_1\) cho \(\cos\varphi_1\), hoàn toàn không thể bù công suất biến dạng sóng hài \(D\). Thậm chí, tụ bù điện môi còn làm giảm trở kháng ở tần số cao, hút dòng sóng hài và gây nguy cơ nổ tụ. Bài viết bắt buộc phải giải thích rõ sự khác biệt này.
