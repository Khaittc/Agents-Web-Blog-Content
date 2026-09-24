# BÁO CÁO THẨM ĐỊNH KỸ THUẬT SÓNG HÀI & CHUẨN IEEE STD 519 (CON-002 / RQ-005)
## BLOG_04 — CON-002 HARMONICS / IEEE 519 TECHNICAL REVIEW REPORT
**Thời điểm thực hiện**: 2026-09-24T22:45:00+07:00
**Tác nhân thực hiện**: Antigravity Quality & Architecture Agent
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`
**Chủ đề**: VFD và Soft Starter: So sánh Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Phạm vi Ứng dụng (`BLOG-T04`)
**Commit Baseline**: `68e739f — chore: align BLOG_04 research review state`
**Trạng thái sau thẩm định**:
- `article_status`: `RESEARCHED`
- `research_plan`: `REVIEW_REQUIRED` (chờ xử lý riêng `RQ-006`)
- `RQ-005`: `ANSWERED`
- `RQ-006`: `PARTIALLY_ANSWERED` (`freshness_required: true`)
- `CON-001`: `RESOLVED`
- `CON-002`: `RESOLVED`

---

## 1. MỤC TIÊU VÀ BỐI CẢNH THẨM ĐỊNH

Sau đợt rà soát chất lượng chứng cứ nghiên cứu (Research Evidence Quality Patch), hệ thống ghi nhận hai vấn đề kỹ thuật cần thẩm định độc lập:
1. `CON-002`: Xung đột và sắc thái kỹ thuật liên quan đến phát sinh sóng hài và sự cần thiết của bộ lọc hài theo chuẩn IEEE Std 519 giữa Soft Starter và VFD.
2. `RQ-005`: Bằng chứng nghiên cứu về đặc tính sóng hài cần làm rõ chi tiết cấu trúc VFD thay vì chấp nhận một con số suy diễn chung chung (như "VFD luôn có THD-I = 35–45%").

Mục tiêu duy nhất của nhiệm vụ này là:
- Thu thập nguồn sơ cấp Tier 1 uy tín để phân giải triệt để `CON-002`.
- Hoàn thành đầy đủ câu hỏi nghiên cứu `RQ-005` (`ANSWERED`).
- Giữ nguyên trạng thái `RQ-006` (`PARTIALLY_ANSWERED`, `freshness_required: true`) để xử lý trong đợt nghiên cứu thị trường/freshness riêng biệt.
- Khóa chặt ranh giới kiểm soát: tuyệt đối không gọi Drafting Agent, không sinh ảnh, không tạo mã HTML, không can thiệp các bài đã nghiệm thu (`BLOG_01`, `BLOG_02`, `BLOG_03`).

---

## 2. NGUỒN TÀI LIỆU TIẾP NHẬN BỔ SUNG: SRC-005 (ABB TECHNICAL GUIDE NO. 6)

Để giải quyết thỏa đáng bản chất phát sinh sóng hài của các cấu trúc biến tần và ranh giới áp dụng chuẩn IEEE Std 519, hệ thống đã truy xuất và thẩm định nguồn sơ cấp Tier 1 từ ABB:

- **Tên tài liệu**: *Technical guide No. 6: Guide to harmonics with AC drives*
- **Nhà xuất bản**: ABB Oy, Drives (Helsinki, Finland)
- **Mã định danh tài liệu**: `3AFE64292714 Rev F EN` (2017)
- **Loại hình**: `TECH_REPORT` (Tier 1 OEM Technical Guide)
- **Canonical URL**: `https://library.abb.com/d/3AFE64292714`
- **Retrieval URL**: `https://library.e.abb.com/public/bc35ffb4386c4c039e3a8ec20cef89c5/Technical_guide_No_6_3AFE64292714_RevF_EN.pdf`
- **Tình trạng thẩm định**: Đã tải file PDF đầy đủ (32 trang), kiểm chứng chữ ký số và trích xuất số liệu kỹ thuật gốc theo nguyên tắc **No Snippet Evidence Rule**.
- **Cấp mã định danh ổn định**: `SRC-005` (chuyển đổi từ ứng viên `CAN-008`).

---

## 3. PHÂN TÍCH KỸ THUẬT VÀ NỘI DUNG PHÂN GIẢI CON-002

Nội dung phân giải `CON-002` được cấu trúc trên ba bình diện kỹ thuật độc lập, chặt chẽ và không thể tách rời:

### (A) Hành vi sóng hài của Khởi động mềm (Soft Starter Harmonic Behavior)
- **Giai đoạn tăng tốc / giảm tốc (Starting / Stopping ramp)**:
  Khởi động mềm sử dụng các cặp thyristor (SCR) điều khiển góc kích pha ($\alpha$) để cắt xén dạng sóng điện áp xoay chiều hình sin nhằm điều chỉnh trị số hiệu dụng $U_{rms}$. Trong giai đoạn quá độ này (thường kéo dài vài giây đến vài chục giây), dòng điện bị méo dạng và xuất hiện các thành phần sóng hài. Theo số liệu thực nghiệm đo đạc từ Rockwell Automation (`SRC-002`, p. 12), độ méo sóng hài dòng điện trong giai đoạn này thường nhỏ hơn $10\%$ ($THD_i < 10\%$).
- **Giai đoạn xác lập duy trì (Steady-state bypass)**:
  Khi động cơ đạt tốc độ định mức, các tiếp điểm của contactor bypass (tích hợp bên trong hoặc lắp ngoài) đóng lại, đưa toàn bộ dòng điện chạy qua đường dẫn cơ khí kim loại thuần trở tiếp xúc. Lúc này, thyristor ngừng dẫn hoàn toàn. Do đó, ở chế độ vận hành xác lập, khởi động mềm **hầu như không tạo ra bất kỳ sóng hài nào từ bản thân thiết bị** (*almost no harmonics generated* — `SRC-001`, `SRC-002`).
- **Quy tắc biên tập cho Drafting Agent**: Không tuyên bố tuyệt đối $THD = 0\%$ trong toàn bộ chu kỳ, mà phải phân biệt rạch ròi giữa giai đoạn khởi động ngắn hạn ($THD_i < 10\%$) và giai đoạn bypass xác lập (hầu như không phát sinh sóng hài).

### (B) Hành vi sóng hài của Biến tần (VFD Harmonic Behavior)
- **Cơ chế phát sinh liên tục**:
  Biến tần chuyển đổi năng lượng AC-DC-AC. Tại tầng đầu vào, bộ chỉnh lưu nạp dòng phi tuyến vào tụ điện một chiều DC bus dưới dạng các xung dòng nhọn, tạo ra các dòng sóng hài bậc cao liên tục trong suốt quá trình vận hành (chủ yếu là các bậc $h = 6k \pm 1$ như $h=5, 7, 11, 13...$).
- **Không tồn tại con số THD-I phổ quát**:
  Độ méo sóng hài dòng điện ($THD_i$) tại đầu vào biến tần phụ thuộc chặt chẽ vào cấu trúc chỉnh lưu, mức tải và trang bị cuộn kháng (`SRC-005`, pp. 13-18):
  1. *Chỉnh lưu 6 xung có cuộn kháng (6-pulse diode bridge with AC/DC choke)*: Giá trị điển hình khoảng $40\%$ $THD_i$. Nếu **không có cuộn kháng**, xung dòng cực kỳ nhọn làm $THD_i$ tăng vọt lên rất cao; giá trị tối thiểu lý thuyết cho 25 bậc hài đầu khi có cuộn kháng đủ lớn là $29\%$.
  2. *Chỉnh lưu 12 xung (12-pulse rectifier)*: Kết hợp hai cầu chỉnh lưu 6 xung qua máy biến áp có hai cuộn thứ cấp lệch pha $30^\circ$, triệt tiêu các bậc hài thứ 5 và thứ 7, đưa $THD_i$ điển hình xuống khoảng $10\%$.
  3. *Biến tần nguồn tích cực IGBT (Active Front End - AFE / Low Harmonic Drive)*: Sử dụng cầu van IGBT điều chế độ rộng xung ở đầu vào thay cho diode, triệt tiêu sóng hài chủ động và đưa $THD_i$ xuống khoảng $4\%$, đồng thời có khả năng bù hệ số công suất.
- **Quy tắc biên tập cho Drafting Agent**: Tuyệt đối không được khẳng định "mọi VFD đều có sóng hài 35%–45%". Phải nêu rõ sự khác biệt giữa các cấu hình phần cứng: biến tần tiêu chuẩn 6 xung kèm cuộn kháng (~40%), giải pháp 12 xung (~10%), và biến tần phát xạ thấp AFE (~4%), cũng như khả năng lắp thêm cuộn kháng phụ, bộ lọc thụ động (passive filter) hoặc bộ lọc tích cực (AHF).

### (C) Ranh giới áp dụng chuẩn IEEE Std 519-2022 (Point of Common Coupling Boundary)
- **Ranh giới tiêu chuẩn tại PCC**:
  Chuẩn IEEE Std 519-2022 (Bảng 2, `SRC-004`) quy định giới hạn méo dòng tổng ($TDD$) đối với toàn bộ cơ sở của khách hàng tại Điểm Đấu Nối Chung (Point of Common Coupling — PCC), dựa trên tỷ số giữa dòng ngắn mạch của lưới điện và dòng phụ tải cực đại của toàn cơ sở ($I_{sc}/I_L$). Cụ thể, khi $I_{sc}/I_L < 20$, giới hạn $TDD$ tại PCC là $5.0\%$.
- **Bác bỏ hiểu lầm kỹ thuật phổ biến**:
  ABB Document 3AFE64292714 Rev F (`SRC-005`, p. 10) đã chỉ rõ: *Bảng 2 của IEEE Std 519 thường xuyên bị diễn giải sai thành giới hạn phát xạ cho từng thiết bị đơn lẻ bằng cách sử dụng tỷ số ngắn mạch $R_{sc}$ của riêng thiết bị thay vì $I_{sc}/I_L$ của toàn trạm. Tiêu chuẩn không quy định giới hạn phát xạ trên từng thiết bị riêng biệt mà chỉ áp dụng cho toàn bộ cơ sở tại điểm PCC*.
- **Quy tắc biên tập cho Drafting Agent**: Tiêu chuẩn IEEE Std 519 không áp đặt quy định lọc trực tiếp lên từng cực thiết bị VFD. Sự cần thiết của bộ lọc sóng hài là bài toán đánh giá ở cấp hệ thống (system-level evaluation). Nếu trạm biến áp có công suất lớn (lưới cứng, $I_{sc}/I_L$ cao) và tổng công suất biến tần chiếm tỷ trọng nhỏ trong tổng phụ tải của nhà máy, dòng méo tại PCC vẫn có thể thỏa mãn quy chuẩn mà không cần lắp thêm bộ lọc ngoại vi. Ngược lại, nếu tỷ trọng biến tần lớn trên lưới yếu, các giải pháp lọc (choke, passive/active filter, AFE) là bắt buộc để bảo vệ chất lượng điện chung.

---

## 4. CHI TIẾT CÁC BẰNG CHỨNG BỔ SUNG (EVD-013 & EVD-014)

Hai bằng chứng kỹ thuật định lượng mới đã được trích xuất và lưu vết tại `evidence.json` và `evidence_dossier.md`:

```text
EVD-013:
- Nguồn: SRC-005 (ABB Technical guide No. 6, Ch. 4, pp. 13-18)
- Định vị: Section "Effect of AC drive topology", pp. 16-18; "Using a larger DC or AC choke", p. 13
- Nội dung: THDi điển hình của 6-pulse có choke là ~40% (theoretical minimum 25 components là 29%), 12-pulse là ~10%, IGBT Active Front End là ~4%.
- Phân loại: COMPARISON_POINT

EVD-014:
- Nguồn: SRC-005 (ABB Technical guide No. 6, Ch. 2, p. 10)
- Định vị: Section "Standards for harmonic limits: IEEE 519", p. 10
- Nội dung: IEEE 519 không quy định giới hạn cho thiết bị đơn lẻ mà áp dụng tại PCC cho toàn cơ sở dựa trên Isc/IL; áp dụng Table 2 cho từng thiết bị là diễn giải sai chuẩn.
- Phân loại: STANDARD_REQUIREMENT
```

---

## 5. BẢNG ĐỐI CHIẾU TRẠNG THÁI VÀ ĐỒNG BỘ TÀI LIỆU

| Tệp tài liệu | Trạng thái trước thẩm định | Trạng thái sau thẩm định | Chi tiết cập nhật |
|:---|:---:|:---:|:---|
| `article_status.json` | `RESEARCHED` | `RESEARCHED` | Cập nhật trường `notes` ghi nhận CON-002 đã giải quyết, chờ xử lý RQ-006. |
| `research_plan.json` | `REVIEW_REQUIRED` | `REVIEW_REQUIRED` | Chuyển `RQ-005` sang `ANSWERED`. Giữ nguyên `RQ-006` là `PARTIALLY_ANSWERED` (`freshness_required: true`). |
| `evidence.json` | `CON-002: REVIEW_REQUIRED` | `CON-002: RESOLVED` | Tiếp nhận `SRC-005`, nâng tổng số nguồn lên 5 (80% Tier 1+2), thêm `EVD-013`, `EVD-014`, hoàn tất phân giải `CON-002`. |
| `research_log.json` | 7 truy vấn / 7 ứng viên | 8 truy vấn / 8 ứng viên | Ghi nhận truy vấn `Q-008` và ứng viên `CAN-008` (ACCEPTED $\rightarrow$ `SRC-005`). |
| `evidence_dossier.md` | 4 nguồn / 12 bằng chứng | 5 nguồn / 14 bằng chứng | Đồng bộ đầy đủ nội dung EVD-013, EVD-014, nghị quyết CON-002, nhật ký CAN-008 và tổng kết nghiên cứu. |

---

## 6. HẠNG MỤC CÒN LẠI VÀ KHUYẾN NGHỊ ĐIỀU PHỐI (OUTSTANDING WORK & NEXT STEPS)

1. **Hạng mục duy nhất còn mở tại tầng Nghiên cứu của BLOG_04**:
   - `RQ-006`: Khảo sát dữ liệu tươi mới về chi phí đầu tư ban đầu (CAPEX), kích thước lắp đặt tủ điện (Footprint) và yêu cầu bảo trì vòng đời (`status: PARTIALLY_ANSWERED`, `freshness_required: true`).
2. **Kế hoạch tiếp theo**:
   - Mở task chuyên đề riêng: **BLOG_04 — RQ-006 FRESHNESS & CAPEX RESEARCH** để thu thập dữ liệu giá bán, kích thước mm tủ điện công nghiệp và chu kỳ bảo trì vòng đời mới nhất từ các nhà phân phối hoặc catalog kỹ thuật hiện hành.
   - Sau khi `RQ-006` đạt `ANSWERED`, toàn bộ 7/7 Research Questions sẽ hoàn tất. Lúc đó `research_plan.json` mới được chuyển sang `COMPLETED`, mở cổng để bước vào **Drafting Phase**.
3. **Cảnh báo tuân thủ quy trình**:
   - Hiện tại **DRAFTING READINESS: NOT READY**. Tuyệt đối không khởi động Drafting Agent trước khi nghiệm thu hoàn tất `RQ-006`.
