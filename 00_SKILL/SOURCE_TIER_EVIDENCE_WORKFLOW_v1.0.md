# QUY TRÌNH PHÂN TẦNG VÀ THẨM ĐỊNH BẰNG CHỨNG KỸ THUẬT (SOURCE TIER & EVIDENCE WORKFLOW)
Version: 1.0
Trạng thái: Áp dụng chính thức cho Research & Evidence Agent
Phạm vi: Toàn bộ bài viết kỹ thuật (Blog / Solution) cho Real Group (`real-group.org`)

---

## 1. MỤC ĐÍCH

Tài liệu này chuẩn hóa quy trình:
1. Phân loại và xếp tầng độ tin cậy của tài liệu tham khảo kỹ thuật (**Source Tiering**).
2. Xử lý và giải quyết mâu thuẫn số liệu kỹ thuật giữa các nguồn (**Data Conflict Resolution**).
3. Xác minh số định vị cụ thể (**Verified Locator Protocol** — số trang, số chương, bảng biểu).
4. Thiết lập hồ sơ bằng chứng (**Evidence Dossier**) trước khi chuyển giao cho Drafting Agent.

Tài liệu này phối hợp trực tiếp với [IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_CITATION_REFERENCE_MASTER_SUITE_v2.0.md) (đặc biệt là Sub-skill `IEEE-01`) để đảm bảo mọi tuyên bố kỹ thuật (technical claims) đều có thể truy nguyên 100%.

---

## 2. PHÂN CẤP TẦNG NGUỒN (SOURCE TIER HIERARCHY)

Mọi tài liệu phục vụ biên soạn bài viết bắt buộc phải được xếp vào một trong 3 tầng giá trị kỹ thuật sau:

```text
┌─────────────────────────────────────────────────────────────┐
│ TIER 1: TIÊU CHUẨN QUỐC TẾ & TÀI LIỆU CHÍNH HÃNG           │
│ (IEC, IEEE, ISO, NEMA, Datasheets/Manuals Siemens, ABB...)  │
└──────────────────────────────┬──────────────────────────────┘
                               │ Ưu tiên tuyệt đối
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TIER 2: SỔ TAY KỸ THUẬT & TỔ CHỨC NĂNG LƯỢNG QUỐC GIA       │
│ (US DOE, EPRI, Sách chuyên khảo đại học, Báo cáo kiểm định) │
└──────────────────────────────┬──────────────────────────────┘
                               │ Hỗ trợ ngữ cảnh thực nghiệm
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TIER 3: BÀI BÁO KHOA HỌC & PHÂN TÍCH CHUYÊN GIA WEB         │
│ (Tạp chí kỹ thuật, Whitepapers, Web kỹ thuật đã kiểm chứng) │
└─────────────────────────────────────────────────────────────┘
```

### 2.1. Tier 1 — Nguồn Chuẩn Quốc Tế & Nhà Sản Xuất (Primary Engineering Authority)
- **Bao gồm**:
  - Tiêu chuẩn quốc tế: IEC (ví dụ: IEC 60034 cho động cơ), IEEE (ví dụ: IEEE 519 cho sóng hài), ISO, NEMA.
  - Tài liệu kỹ thuật chính hãng: Nameplate, Catalog, Hardware Manual, Technical Guidebook do chính nhà sản xuất thiết bị phát hành (Siemens, ABB, Schneider Electric, Danfoss, Mitsubishi Electric, Rockwell Automation...).
- **Độ tin cậy**: Cao nhất. Số liệu, công thức và ngưỡng kỹ thuật từ Tier 1 được coi là chuẩn tham chiếu mặc định.

### 2.2. Tier 2 — Tài liệu Thể chế & Chuyên khảo Học thuật (Institutional & Textbook Authority)
- **Bao gồm**:
  - Tài liệu của các cơ quan năng lượng/chính phủ: US Department of Energy (DOE - ví dụ: Motor Systems Tip Sheets), Viện Nghiên cứu Điện năng EPRI, Trung tâm Khuyến nông Năng lượng Quốc gia.
  - Giáo trình kỹ thuật đại học chính quy (Electrical Machines, Power Systems Analysis của các NXB: Wiley, McGraw-Hill, Springer, NXB ĐHQG).
  - Báo cáo thử nghiệm độc lập của các phòng lab được công nhận (KEMA, UL, TÜV).
- **Độ tin cậy**: Rất cao. Phù hợp cho việc giải thích nguyên lý, phương pháp đo thực tế và kinh nghiệm vận hành.

### 2.3. Tier 3 — Báo cáo Ngành & Tạp chí Kỹ thuật (Industry Articles & Whitepapers)
- **Bao gồm**:
  - Bài viết chuyên sâu trên các tạp chí ngành: Plant Services, Efficient Plant, Electrical Engineering Portal (EEP), Control Engineering.
  - Whitepaper của các hãng tích hợp hệ thống uy tín.
- **Độ tin cậy**: Khá. Chỉ dùng để bổ sung ví dụ thực tế hoặc góc nhìn vận hành. Không dùng Tier 3 để phủ nhận thông số của Tier 1.

### 2.4. Nguồn Bị Cấm Tuyệt Đối (Unacceptable Sources)
- Bài viết SEO quảng cáo bán hàng chung chung, không có tác giả chuyên môn.
- Trang hỏi đáp không kiểm duyệt (Quora, Reddit, diễn đàn tự do không có trích dẫn tài liệu gốc).
- Nội dung do AI tự tạo ra mà không có trích dẫn nguồn gốc (AI Hallucinated Text).

---

## 3. NGUYÊN TẮC GIẢI QUYẾT XUNG ĐỘT SỐ LIỆU (DATA CONFLICT RESOLUTION)

Khi xuất hiện sự khác biệt về số liệu, công thức hoặc ngưỡng giữa các tài liệu, Agent áp dụng quy tắc:

1. **Quy tắc Phân tầng (Tier Override)**:
   ```text
   Tier 1 > Tier 2 > Tier 3
   ```
   *Ví dụ*: Nếu một bài blog Tier 3 ghi "động cơ dưới 60% là non tải", nhưng tài liệu Tier 2 của DOE xác định ngưỡng suy giảm hiệu suất rõ rệt là dưới 50% tải, Agent **bắt buộc tuân theo Tier 2 (DOE)** và nêu rõ điều kiện áp dụng.

2. **Quy tắc Đồng tầng (Same Tier Precedence)**:
   - **Phiên bản mới hơn ưu tiên hơn**: Tiêu chuẩn IEC 60034-30-1:2014 thay thế cho bản 2008.
   - **Đặc tính chuyên biệt ưu tiên hơn hướng dẫn tổng quát**: Manual cụ thể của dòng biến tần ABB ACS880 ghi đè tài liệu hướng dẫn biến tần chung của hãng.
   - **Nêu rõ giả thiết đo lường**: Nếu 2 nguồn Tier 1 đưa ra giá trị khác nhau do điều kiện thử nghiệm khác nhau (ví dụ: ở 40°C ambient vs 25°C ambient), Agent **bắt buộc phải ghi rõ điều kiện môi trường** thay vì chỉ đưa ra một con số duy nhất.

---

## 4. QUY TRÌNH XÁC MINH SỐ ĐỊNH VỊ (VERIFIED LOCATOR PROTOCOL)

Theo chuẩn [IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md](file:///d:/Agents_Tools/05_WebsiteTTC/00_SKILL/IEEE_02_IN_TEXT_CITATION_AND_LOCATOR_SKILL_v1.1.md):
1. **Không trích dẫn chung chung**: Một cuốn sách 500 trang hoặc tiêu chuẩn 100 trang không được trích dẫn chỉ bằng tên tài liệu nếu tuyên bố mang tính định lượng cụ thể.
2. **Cấu trúc Locator hợp lệ trong hồ sơ nghiên cứu**:
   - Số trang: `p. 45` hoặc `pp. 45–48`
   - Chương / Mục: `Sec. 3.2`
   - Bảng số liệu: `Tab. 4`
   - Công thức: `eq. (3)`
3. **Phân loại trạng thái Locator**:
   - `LOCATOR_VERIFIED`: Đã kiểm tra đối chiếu trực tiếp số trang/bảng/chương trong tài liệu gốc.
   - `LOCATOR_UNAVAILABLE`: Tài liệu không có số trang cố định (bài web, datasheet dạng trang đơn).
   - `LOCATOR_NOT_CHECKED`: Chưa kiểm chứng số trang; chỉ cho phép trích dẫn `[n]` ở cuối câu.
   - `LOCATOR_CONFLICT`: Số trang hoặc bảng có sự mâu thuẫn giữa các phiên bản tài liệu.

---

## 5. CHÍNH SÁCH SỐ LƯỢNG NGUỒN & NGOẠI LỆ THẨM QUYỀN CAO (SOURCE COUNT POLICY & EXCEPTION)

### 5.1. Chính sách Mặc định (Default Policy)
- **Số lượng khuyến nghị**: 4–7 nguồn kỹ thuật.
- **Tỷ lệ ưu tiên Tier 1 + Tier 2**: $\ge 70\%$.
- **Phạm vi áp dụng**:
  - Bài tổng quan kỹ thuật (Overview).
  - So sánh công nghệ / thiết bị (Comparison).
  - Giải thích kỹ thuật diện rộng (Broad Technical Explanation).
  - Chủ đề đa hãng / đa giải pháp (Multi-vendor Topics).
  - Hướng dẫn thực hành kỹ thuật chung (General Engineering Guide).

### 5.2. Ngoại lệ Nguồn Thẩm quyền Cao cho Chủ đề Hẹp (Authoritative-Source Exception)
Cho phép sử dụng **1–3 nguồn kỹ thuật** nếu chủ đề mang tính chuyên sâu, phạm vi hẹp và một hoặc vài nguồn sơ cấp (primary sources) đã đủ thẩm quyền tối cao:
- **Ví dụ áp dụng**:
  - Mã lỗi chuyên biệt của một dòng biến tần (ví dụ: mã lỗi F0001 / Fault 2310 trên Siemens / ABB).
  - Thông số cài đặt hoặc tham số cụ thể của thiết bị OEM.
  - Quy trình thử nghiệm hoặc đóng điện của một hãng sản xuất duy nhất.
  - Một điều khoản hoặc bảng tra cứu cụ thể trong tiêu chuẩn quốc tế IEC / IEEE.

### 5.3. Cửa ải Phê duyệt Ngoại lệ (Exception Approval Gate)
Research Agent chỉ được kích hoạt ngoại lệ nếu thỏa mãn đầy đủ 5 điều kiện:
1. Chủ đề thực sự mang tính hẹp và chuyên biệt.
2. Có ít nhất một nguồn sơ cấp thẩm quyền cao (Tier 1 hoặc Tier 2 từ chính hãng phát hành).
3. Nguồn trực tiếp chứng minh và hỗ trợ 100% các luận điểm kỹ thuật chính.
4. Ghi rõ lý do kích hoạt ngoại lệ trong hồ sơ `evidence.json`.
5. Được **Cổng Kiểm Định Kỹ Thuật (Technical Review Gate)** thẩm tra và chấp thuận (`APPROVE_EXCEPTION`). Nếu Review Agent từ chối (`REJECT_EXCEPTION`), Research Agent phải bổ sung nguồn theo vòng lặp hiệu chỉnh (`REVISION_REQUESTED`).

### 5.4. Không dùng Số lượng Nguồn làm Thước đo Chất lượng
Tuyệt đối xóa bỏ quan niệm "nhiều nguồn hơn = bài viết tốt hơn". Chất lượng nghiên cứu được đánh giá dựa trên:
- **Tính thẩm quyền (Authority)**: Phù hợp cấp độ Tier 1/Tier 2.
- **Tính xác đáng (Relevance)**: Trọng tâm, phục vụ trực tiếp đề tài.
- **Độ bao phủ luận điểm (Claim Coverage)**: Mọi thông số đều có bằng chứng.
- **Độ cập nhật (Freshness)**: Phiên bản tài liệu đang có hiệu lực.
- **Kiểm chứng độc lập (Verification)**: Đã đối chiếu văn bản gốc.
- **Giải quyết xung đột (Conflict Resolution)**: Luận giải rõ ràng nếu có khác biệt.

---

## 6. NGỮ NGHĨA KIỂM CHỨNG URL & LIÊN KẾT TÀI LIỆU (URL VERIFICATION SEMANTICS)

### 6.1. Tách bạch Trạng thái Truy cập Mạng (Network Access Status)
Không đồng nhất `HTTP 200` với "Nguồn đã kiểm chứng". Chuẩn hóa danh mục `access_status`:
- `OK`: Kết nối trực tiếp thành công (HTTP 2xx).
- `REDIRECTED_OK`: Yêu cầu chuyển hướng (HTTP 301/302) đến đúng trang chính thức và trả về HTTP 2xx.
- `ACCESS_RESTRICTED`: Bị giới hạn truy cập theo vùng hoặc tường lửa.
- `AUTH_REQUIRED`: Yêu cầu đăng nhập tài khoản / phân quyền kỹ thuật.
- `NOT_FOUND`: Liên kết hỏng hoặc không tồn tại (HTTP 404).
- `NETWORK_ERROR`: Lỗi phân giải DNS hoặc ngắt kết nối mạng.
- `UNKNOWN`: Chưa thực hiện gửi yêu cầu kiểm tra mạng.

### 6.2. Phân biệt Canonical URL vs Retrieval URL
Mỗi nguồn trong `evidence.json` bắt buộc phân tách 2 loại địa chỉ:
- **`canonical_url`**: URL chính thức, ổn định, định danh tài liệu (landing page sản phẩm, cổng thư viện tiêu chuẩn) dùng cho Danh mục Tài liệu tham khảo công khai.
- **`retrieval_url`**: URL thực tế mà Agent đã truy cập để tải hoặc đọc nội dung (direct link PDF tạm thời, link download portal, tài liệu lưu trữ).

### 6.3. Chính sách Tệp PDF Trực tiếp (Direct PDF Policy)
- Không ép buộc mọi trường hợp phải là link PDF trực tiếp nếu link đó dễ hết hạn hoặc không ổn định.
- Ưu tiên `canonical_url` dẫn tới trang thông tin chính thống của tài liệu nếu trang đó hiển thị rõ thông tin định danh và cho phép tải tài liệu.
- Cho phép kết hợp `canonical_url` (landing page) + `retrieval_url` (link PDF trực tiếp) với điều kiện đã xác minh danh tính tài liệu (`content_identity_verified = true`).

### 6.4. Kiểm chứng Danh tính Nội dung & Thẩm định Luận điểm
- **`content_identity_verified = true`**: Chỉ đánh dấu khi đã đối chiếu tối thiểu: Tiêu đề tài liệu, Nhà xuất bản/Hãng chế tạo, Mã hiệu tài liệu, Phiên bản/Revision, Năm phát hành. Tuyệt đối không đánh dấu chỉ vì URL chứa từ khóa.
- **`claim_verified = true`**: Chỉ đánh dấu khi Agent đã thực sự đọc nội dung bên trong nguồn và xác nhận nguồn hỗ trợ luận điểm kỹ thuật. Tuyệt đối không dựa vào tóm tắt Google Snippet, kết quả tìm kiếm sơ lược hay tên tệp.

---

## 7. HỒ SƠ BẰNG CHỨNG SONG HÀNH (EVIDENCE DOSSIER & EVIDENCE.JSON)

Research Agent bắt buộc phải tạo song song:
1. **`evidence.json`**: Tệp dữ liệu máy đọc canonical tuân thủ `02_AGENT_TEMPLATES/contracts/evidence.schema.json`.
2. **`evidence_dossier.md`**: Báo cáo tổng hợp bằng chứng kỹ thuật dành cho Kỹ sư trưởng đọc và thẩm định.

> [!IMPORTANT]
> **QUY TẮC STABLE SOURCE ID & TÁCH BẠCH HTTP 200 (PHASE 2.5 ARCHITECTURE HARDENING)**:
> 1. **STABLE SOURCE ID (`SRC-xxx`)**: Nghiên cứu chỉ cấp phát mã định danh ổn định `SRC-001`, `SRC-002`, `SRC-003`,... Tuyệt đối KHÔNG gán số trích dẫn IEEE `[1]`, `[2]` ở giai đoạn này. Số IEEE sẽ do Drafting Agent gán dựa trên thứ tự xuất hiện đầu tiên trong bài viết.
> 2. **TÁCH BẠCH KIỂM CHỨNG**:
>    ```text
>    URL ACCESS (HTTP 200) ≠ CONTENT IDENTITY ≠ CLAIM VERIFIED ≠ LOCATOR VERIFIED
>    ```
>    HTTP 200 chỉ chứng minh đường truyền mạng hoạt động, **KHÔNG ĐƯỢC COI HTTP 200 LÀ BẰNG CHỨNG NỘI DUNG CLAIM ĐÃ ĐÚNG**. Phải có xác nhận đối chiếu văn bản gốc.

```markdown
# EVIDENCE DOSSIER — [MÃ BÀI VIẾT]

## 1. Danh sách Nguồn Ổn định (Stable Source Registry)
| Source ID | Phân tầng | Loại hình (Source Type) | Chuẩn trích dẫn IEEE chính thức (Official IEEE Reference) | Năm | Canonical URL | Retrieval URL | Trạng thái Mạng | Content ID | Claim Verified | Locator Status | Bộ định vị kiểm chứng (Locators) |
|:---:|:---:|:---|:---|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|
| `SRC-001` | Tier 1 | `STANDARD` | *IEEE Standard for Harmonic Control in Electric Power Systems*, IEEE Std 519-2022, 2022. | 2022 | `https://ieeexplore...` | `https://ieeexplore...` | OK | YES | YES | LOCATOR_VERIFIED | Tab. 1, p. 12 |
| `SRC-002` | Tier 1 | `MANUAL` | *ACS880 Primary control program Firmware manual*, ABB, 2024. | 2024 | `https://search.abb.com/...` | `https://search.abb.com/...` | OK | YES | YES | LOCATOR_VERIFIED | Fault 2310, p. 504 |

## 2. Bảng Trích xuất Dữ liệu (Fact Registry)
| Fact ID | Tuyên bố / Số liệu / Công thức | Nguồn (Source ID) & Locator | Tier | Trạng thái Thẩm định |
|:---:|:---|:---|:---:|:---:|
| F01 | Công thức tính hệ số tải từ công suất thực P_in | `SRC-002`, p. 2, eq. (2) | Tier 2 | VERIFIED |
| F02 | Ngưỡng quá dòng cắt phần cứng tức thời | `SRC-002`, p. 504 | Tier 1 | VERIFIED |

## 3. Ngoại lệ Nguồn Thẩm quyền Cao (nếu có)
- Trạng thái ngoại lệ: [ENABLED / NONE]
- Lý do: [Giải trình căn cứ kỹ thuật]
- Phán quyết Cổng Kỹ thuật: [PENDING / APPROVE_EXCEPTION / REJECT_EXCEPTION]

## 4. Các Xung đột Đã xử lý (Resolved Conflicts)
- Ghi nhận xung đột và lý do chọn số liệu.
```
