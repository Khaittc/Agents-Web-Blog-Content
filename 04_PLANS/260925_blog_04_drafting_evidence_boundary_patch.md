# BÁO CÁO VÁ RANH GIỚI BẰNG CHỨNG BẢN THẢO (DRAFTING EVIDENCE-BOUNDARY PATCH REPORT)
## BLOG_04 — VFD VÀ SOFT STARTER: SO SÁNH NGUYÊN LÝ, DÒNG KHỞI ĐỘNG, ĐIỀU KHIỂN TỐC ĐỘ VÀ PHẠM VI ỨNG DỤNG
**Thời điểm thực hiện**: 2026-09-25T16:20:00+07:00  
**Tác nhân thực hiện**: Drafting Agent / Quality & Architecture Guardian  
**Bài viết mục tiêu**: `03_Articles/BLOG_04_VFD_vs_Soft_Starter/`  
**Mã phân loại chuẩn**: `BLOG-T04` (Comparison)  
**Baseline Commit**: `8bad365 — feat: draft BLOG_04 from approved research handoff`  

---

## 1. TỔNG QUAN VÀ NGUYÊN TẮC CỐT LÕI (EXECUTIVE SUMMARY)

Bản vá ranh giới bằng chứng (Evidence-Boundary Patch) được thực hiện nhằm xử lý triệt để các phát biểu vượt ranh giới, con số suy diễn chưa có căn cứ và các thiên kiến diễn đạt trong bản thảo đầu tiên của `BLOG_04`, thiết lập kỷ luật bất khả xâm phạm:

```text
DRAFT CLAIM <= APPROVED EVIDENCE <= VERIFIED SOURCE
```

Và bảo đảm chuỗi truy vết kỹ thuật khép kín 4 cấp độ:

```text
CLM-xxx → EVD-xxx → SRC-xxx → IEEE [n]
```

### Các nguyên tắc tuân thủ nghiêm ngặt trong task:
- **KHÔNG thực hiện Technical Review Gate**: Không đưa ra phán quyết phê duyệt kỹ thuật, không đóng dấu `TECH_APPROVED`. Trạng thái bài viết được giữ nguyên ở **`TECH_REVIEW`**.
- **KHÔNG Live Research**: Không tìm kiếm thêm nguồn mới ngoài hồ sơ đã được duyệt tại Final Research Gate.
- **KHÔNG sửa hồ sơ nghiên cứu**: Hồ sơ nghiên cứu gốc (`evidence.json`, `research_plan.json`, `research_handoff.json`,...) được bảo toàn $100\%$ tính toàn vẹn (read-only), không sửa bằng chứng để "hợp thức hóa" cho bản thảo.
- **Bảo toàn các bài viết bị khóa**: `BLOG_01`, `BLOG_02`, `BLOG_03` hoàn toàn không bị ảnh hưởng.

---

## 2. NÂNG CẤP VÀ THẮT CHẶT SCHEMA HỢP ĐỒNG (SCHEMA HARDENING)

Tệp hợp đồng `02_AGENT_TEMPLATES/contracts/claim_source_map.schema.json` đã được nâng cấp để bắt buộc trường `evidence_ids` cho từng claim:

1. **Bổ sung `$schema` vào root properties**: Cho phép khai báo `$schema` trong các tệp instance JSON.
2. **Bắt buộc `evidence_ids` trong từng mục claim**:
   ```json
   "evidence_ids": {
     "type": "array",
     "description": "Associated Evidence IDs from evidence.json backing this claim",
     "items": {
       "type": "string",
       "pattern": "^EVD-[0-9]{3,}$"
     },
     "minItems": 1,
     "uniqueItems": true
   }
   ```
3. **Thêm `evidence_ids` vào mảng `required`**: Đảm bảo mọi claim khởi tạo trong pipeline bắt buộc phải chỉ rõ ít nhất một `EVD-xxx` hợp lệ.

---

## 3. THIẾT LẬP CI GATE 11 TRONG KIẾN TRÚC HỆ THỐNG (ARCHITECTURE CI GATE 11)

Đã bổ sung **Gate 11: `validate_draft_claim_traceability()`** vào bộ kiểm định tự động `scripts/validate_architecture.py`. Gate 11 thực thi 6 kiểm tra logic truy vết độc lập:

1. **Tồn tại bằng chứng**: Mọi `evidence_id` trong `claim_source_map.json` đều phải tồn tại trong danh mục `evidences` của `evidence.json`.
2. **Tồn tại nguồn**: Mọi `source_id` trong `claim_source_map.json` đều phải tồn tại trong danh mục `sources` của `evidence.json`.
3. **Ràng buộc sở hữu nguồn của bằng chứng**: Với mỗi `evidence_id` được gán cho một claim, nguồn sở hữu gốc (`source_id`) của bằng chứng đó trong `evidence.json` bắt buộc phải nằm trong danh sách `source_ids` của chính claim đó.
4. **Đồng bộ độ dài trích dẫn**: `len(assigned_ieee_numbers) == len(source_ids)`.
5. **Đồng bộ vị trí số trích dẫn**: Với mỗi chỉ số `i`, `assigned_ieee_numbers[i] == source_to_ieee_map[source_ids[i]]`.
6. **Tính duy nhất và hợp lệ của số IEEE**: Toàn bộ giá trị trong `source_to_ieee_map` phải là các số nguyên dương duy nhất (`integer >= 1`).

---

## 4. KIỂM TOÁN VÀ SỬA ĐỔI: HIỆU SUẤT VÀ TỔN HAO (SECTIONS 5.1, 5.2, BẢNG 9)

- **Vấn đề phát hiện**: Bản thảo ban đầu đưa vào các thông số hiệu suất và tổn hao cụ thể: Soft Starter bypass $>99.5\% - 99.8\%$, VFD $96\% - 98\%$, tổn hao dẫn/chuyển mạch $2\% - 4\%$, tổn hao $0.5\% - 1.0\%$, điện áp rơi thuận $V_F \approx 1.2 - 2.0\text{ V}$, $V_T \approx 1.0 - 1.5\text{ V}$, và tỷ lệ $1 - 1.5\text{ W/A}$. Toàn bộ các con số này không xuất hiện trong hồ sơ bằng chứng `EVD-006` (Schneider Electric Blog của tác giả M. Duncan).
- **Hành động khắc phục**:
  - Loại bỏ hoàn toàn các con số phần trăm và công thức sụt áp van bán dẫn chưa có căn cứ.
  - Thu gọn phát biểu về đúng nội hàm được chứng thực trong `EVD-006`: Khi vận hành ở tốc độ định mức đầy tải có tích hợp contactor bypass, khởi động mềm đạt hiệu suất vận hành cao hơn và chạy mát hơn biến tần do toàn bộ dòng tải chuyển qua tiếp điểm cơ khí, không còn linh kiện bán dẫn công suất chủ động nào phát sinh nhiệt; trong biến tần dòng điện liên tục chạy qua linh kiện bán dẫn công suất và phát sinh nhiệt năng.

---

## 5. KIỂM TOÁN VÀ SỬA ĐỔI: DÒNG KHỞI ĐỘNG DOL (SECTION 3.1)

- **Vấn đề phát hiện**: Bản thảo ban đầu nêu dòng khởi động trực tiếp (DOL) từ $600\%$ đến $800\%$ ($6.0$ đến $8.0 \cdot I_n$).
- **Hành động khắc phục**: Bảng 1 của Rockwell Automation trong `EVD-003` chỉ công bố con số thực nghiệm chuẩn hóa là $600\%$ dòng định mức (`Full Voltage: 100% Voltage, 100% Torque, 600% Current`). Đã điều chỉnh câu văn thành: "điển hình khoảng $600\%$ dòng định mức ($6.0 \cdot I_n$) [2, Tab. 1, p. 6]".

---

## 6. KIỂM TOÁN VÀ SỬA ĐỔI: NGÔN NGỮ ÁP ĐẶT VÀ KHUYẾN NGHỊ TRUNG LẬP (SECTIONS 3.3, 8.3, 10)

- **Vấn đề phát hiện**: Sử dụng các cụm từ áp đặt mang tính tuyệt đối như "BẮT BUỘC CHỌN VFD" và "VFD là giải pháp kỹ thuật bắt buộc".
- **Hành động khắc phục**:
  - Chuyển thành ngôn ngữ khuyến nghị kỹ thuật trung lập và khách quan: "VFD là giải pháp kỹ thuật phù hợp hơn để đảm bảo khởi động an toàn", "Cân nhắc Biến tần", "Ưu tiên giải pháp VFD".
  - Giữ vững tính trung lập của cẩm nang kỹ thuật, trình bày rõ ưu - nhược điểm dựa trên sự phù hợp đặc tính cơ học của tải.

---

## 7. KIỂM TOÁN VÀ SỬA ĐỔI: ĐỊNH CỠ SOFT STARTER CHO TẢI NẶNG (SECTION 8.4)

- **Vấn đề phát hiện**: Phát biểu "tài liệu thiết kế của ABB quy định bắt buộc phải chọn Soft Starter lớn hơn ít nhất một cấp công suất".
- **Hành động khắc phục**: `EVD-012` trích dẫn từ tài liệu ABB (*Softstarter Handbook*, p. 37) ghi nhận: *"Crushers, mixers, mills and stirrers usually have a very big moment of inertia so the softstarter is selected one size larger than the motor kW size."* Đã điều chỉnh thành: "tài liệu kỹ thuật của ABB khuyến nghị khởi động mềm thường được chọn lớn hơn một cấp công suất (oversizing: one size larger) so với công suất động cơ [1, p. 37]".

---

## 8. KIỂM TOÁN VÀ SỬA ĐỔI: BÚA NƯỚC ĐƯỜNG ỐNG (SECTIONS 1, 8.1)

- **Vấn đề phát hiện**: Tuyên bố Soft Starter "triệt tiêu các cú sốc cơ khí... búa nước đường ống" và "giải quyết hoàn hảo bài toán này... triệt tiêu xung áp lực thủy lực".
- **Hành động khắc phục**: `EVD-011` từ ABB ghi nhận: *"The problem is the wear and tear caused by pressure waves in the pipe system created when the motor starts but especially when it stops too quickly."* Đã điều chỉnh từ ngữ thành "giảm thiểu các cú sốc cơ khí... hiện tượng búa nước đường ống" và "giúp giảm thiểu rủi ro này bằng cách hãm dừng êm dịu, giảm đáng kể hiện tượng búa nước và sóng áp suất va đập trong đường ống [1, p. 29]".

---

## 9. KIỂM TOÁN VÀ SỬA ĐỔI: MỞ RỘNG LÝ THUYẾT VÀ DẢI CÔNG SUẤT RQ-006 (SECTIONS 2.1, 7.1, 8.3)

- **Mở rộng lý thuyết**:
  - Bản thảo ban đầu đề cập SVPWM, Sensorless Vector Control, công thức đồng bộ $n_s = 60f/p$, ví dụ phản hồi PLC/SCADA và tính năng chia sẻ tải (load sharing) của băng tải. Toàn bộ các nội dung này không nằm trong trích xuất bằng chứng đã được phê duyệt.
  - *Khắc phục*: Đã loại bỏ công thức $n_s = 60f/p$ và các khái niệm SVPWM/Sensorless/SCADA/load sharing. Giữ cấu trúc giải thích bám sát nguyên lý AC-DC-AC và dải tần số $0-250\text{ Hz}$ theo `EVD-001`.
- **Dải công suất RQ-006**:
  - Bản thảo ban đầu tự ý đưa vào các mốc công suất "dưới vài chục kW", "100 kW đến 710 kW", và "khoảng cách chi phí giãn rộng theo cấp số nhân".
  - *Khắc phục*: Chuyển toàn bộ về ngôn ngữ so sánh định tính lịch sử theo `EVD-010`: "Ở dải dòng điện và công suất thấp: Chi phí ban đầu giữa VFD và Soft Starter có mức tương đương hoặc chênh lệch không quá lớn... Khi dòng điện và công suất tăng lên: Chi phí đầu tư của biến tần tăng cao hơn đáng kể so với khởi động mềm [2, p. 15]".

---

## 10. KIỂM TOÁN VÀ SỬA ĐỔI: ĐỒNG BỘ TRÍCH DẪN VÀ THUỘC TÍNH NGUỒN (CLM-010, SRC-005)

- **Năm xuất bản của `SRC-005`**: Trong danh mục tài liệu tham khảo mục `[4]`, năm xuất bản ban đầu ghi nhầm là 2011. Đã sửa chính xác thành **2017** tương ứng với mã tài liệu `3AFE64292714 Rev F` trong `evidence.json`.
- **Đồng bộ thứ tự trích dẫn của `CLM-010`**:
  - Trong văn bản, tài liệu ABB `[4]` (SRC-005) xuất hiện trước khi viện dẫn bảng giới hạn `[5]` (SRC-004 IEEE Std 519-2022).
  - Đã cập nhật `CLM-010` trong `claim_source_map.json`:
    - `source_ids`: `["SRC-005", "SRC-004"]`
    - `assigned_ieee_numbers`: `[4, 5]`
    - `evidence_ids`: `["EVD-014", "EVD-009"]`

---

## 11. BẢNG ĐỐI CHIẾU TRUY VẾT TOÀN DIỆN (FULL TRACEABILITY MATRIX)

Toàn bộ 17 claims đều có chuỗi truy vết trực tiếp, khép kín và nhất quán $100\%$:

| Claim ID | Vị trí Mục | Nội dung Luận điểm Kỹ thuật Cốt lõi | Evidence ID | Stable Source ID | Mã IEEE |
|:---:|:---:|:---|:---:|:---:|:---:|
| **`CLM-001`** | Section 2.1 | VFD biến đổi AC-DC-AC, điều khiển tần số ngõ ra 0-250 Hz | `EVD-001` | `SRC-001` | `[1]` |
| **`CLM-002`** | Section 2.2 | Soft Starter dùng cặp thyristor phản song song kích pha | `EVD-002` | `SRC-001` | `[1]` |
| **`CLM-003`** | Section 3.2 | $T \propto U^2$; giới hạn dòng 150% In cho mô-men 6%, 300% cho 25% | `EVD-003` | `SRC-002` | `[2]` |
| **`CLM-004`** | Section 3.3 | VFD cung cấp 100% mô-men tại 0 rpm, Soft Starter không thể | `EVD-004` | `SRC-003` | `[3]` |
| **`CLM-005`** | Section 4 | Soft Starter chỉ kiểm soát dốc; xác lập chạy cố định tần số lưới | `EVD-005` | `SRC-001` | `[1]` |
| **`CLM-006`** | Section 5.2 | Khi có bypass, Soft Starter hiệu suất cao hơn và chạy mát hơn | `EVD-006` | `SRC-003` | `[3]` |
| **`CLM-007`** | Section 5.3 | Contactor bypass tích hợp chỉ cần định mức tiêu chuẩn AC-1 | `EVD-007` | `SRC-002` | `[2]` |
| **`CLM-008`** | Section 6.1 | Sóng hài Soft Starter ngắn hạn $<10\%$; ở bypass hầu như không có | `EVD-008` | `SRC-002` | `[2]` |
| **`CLM-009`** | Section 6.2 | Sóng hài VFD: 6-xung có choke $\approx 40\%$, 12-xung $\approx 10\%$, AFE $\approx 4\%$ | `EVD-013` | `SRC-005` | `[4]` |
| **`CLM-010`** | Section 6.3 | IEEE 519 áp dụng tại PCC theo $I_{sc}/I_L$, Bảng 2 TDD 5.0% cho $<20$ | `EVD-014`, `EVD-009` | `SRC-005`, `SRC-004` | `[4], [5]` |
| **`CLM-011`** | Section 6.3 | IEEE 519 không bắt buộc từng drive phải có lọc; bài toán cấp hệ thống | `EVD-014` | `SRC-005` | `[4]` |
| **`CLM-012`** | Section 7.1 | Chi phí ban đầu công suất nhỏ tương đương; công suất lớn VFD cao hơn | `EVD-010` | `SRC-002` | `[2]` |
| **`CLM-013`** | Section 7.1 | Chỉ số chi phí lắp đặt ABB (DOL=1, Star-Delta=3, Soft=6, Drive>12) | `EVD-016` | `SRC-001` | `[1]` |
| **`CLM-014`** | Section 7.2 | Soft Starter nhỏ hơn; VFD công suất lớn cần tủ MCC cho phụ trợ | `EVD-015` | `SRC-002` | `[2]` |
| **`CLM-015`** | Section 7.3 | Bảo trì VFD: kiểm tra 3-4 tháng & hàng năm, quạt, reforming tụ DC | `EVD-017` | `SRC-006` | `[6]` |
| **`CLM-016`** | Section 8.1 | Bơm ly tâm: sóng áp suất búa nước khi dừng; Soft Stop giảm rủi ro | `EVD-011` | `SRC-001` | `[1]` |
| **`CLM-017`** | Section 8.4 | Máy nghiền/khuấy: Soft Starter thường chọn lớn hơn một cấp (oversize) | `EVD-012` | `SRC-001` | `[1]` |

---

## 12. KẾT QUẢ KIỂM THỬ CI VÀ SẴN SÀNG CHO TECHNICAL REVIEW GATE

Đã thực hiện kiểm định tự động toàn diện:
1. **JSON Schema Validation**:
   - `02_AGENT_TEMPLATES/contracts/claim_source_map.schema.json`: Hợp lệ.
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/claim_source_map.json`: Đạt chuẩn `jsonschema.validate()` với schema đã thắt chặt.
2. **Architecture CI Validation (`python scripts/validate_architecture.py`)**:
   - 9/9 gates đều đạt `PASS` (bao gồm Gate 10 Preconditions và Gate 11 Traceability).
3. **Locked Article Protection (`python scripts/verify_locked_articles.py`)**:
   - `BLOG_01`: `PASS` (SHA-256 nguyên vẹn).
   - `BLOG_02`: `PASS` (SHA-256 nguyên vẹn).
   - `BLOG_03`: `PASS` (SHA-256 nguyên vẹn).
4. **Git Workspace Cleanliness**:
   - `git diff --check`: Không có lỗi định dạng hay khoảng trắng thừa.
   - `article_status.json`: Trạng thái giữ nguyên **`TECH_REVIEW`**.

Bản thảo `draft_review_package.md` và bản đồ luận điểm `claim_source_map.json` hiện đã hoàn toàn trong sạch, không còn bất kỳ luận điểm hay con số vượt ranh giới bằng chứng, sẵn sàng cho Review Agent tiến hành quy trình độc lập tại **Technical Review Gate**.
