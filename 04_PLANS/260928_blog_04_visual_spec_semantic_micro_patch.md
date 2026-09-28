# BÁO CÁO VI CHỈNH NGỮ NGHĨA QUY CÁCH THỊ GIÁC (VISUAL SPECIFICATION SEMANTIC MICRO-PATCH REPORT) — BLOG_04

**Mã bài viết**: `BLOG_04`  
**Tiêu đề bài viết**: *VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải*  
**Thể loại bài viết**: `BLOG-T04` — Comparison  
**Tác nhân thực hiện**: Visual Agent (`visual_agent`) — Real Group  
**Ngày thực hiện**: 28/09/2026  
**Baseline Git**: `b35fbe2` — *docs: prepare BLOG_04 visual specifications*  

---

## 1. TỔNG QUAN & MỤC TIÊU NHIỆM VỤ (EXECUTIVE SUMMARY & OBJECTIVE)

Sau khi hoàn thành đợt lập hồ sơ quy cách thị giác ban đầu tại baseline `b35fbe2`, Visual Agent thực hiện nhiệm vụ **Visual Specification Semantic Micro-Patch** nhằm rà soát và thu hẹp toàn diện mọi mô tả thị giác, câu lệnh prompt AI và lời bình hình ảnh trong `image_specifications.md` về đúng ranh giới của các bằng chứng kỹ thuật đã được phê duyệt (`EVD-001` đến `EVD-017`).

Mục tiêu cốt lõi:
- Đảm bảo tính nhất quán tuyệt đối theo nguyên tắc:
  $$\text{VISUAL SPECIFICATION} \le \text{APPROVED EVIDENCE} \le \text{VERIFIED SOURCE}$$
- Loại bỏ các suy diễn kỹ thuật chưa được chứng thực trực tiếp trong hồ sơ bằng chứng (như cấu trúc bán dẫn chi tiết Diode/IGBT, thời điểm đóng contactor bypass, động cơ bảo vệ lưới điện, dải điện áp phần trăm $0-100\%$).
- Chuẩn bị nền tảng đặc tả thị giác chuẩn xác, không có ảo giác kỹ thuật trước khi bước vào giai đoạn tạo ảnh thực tế (Controlled Visual Asset Generation).

---

## 2. XÁC MINH TRẠNG THÁI ĐẦU VÀO (BASELINE & PREREQUISITE VERIFICATION)

Visual Agent đã thẩm định hiện trạng trước khi thực hiện hiệu chỉnh:
- **Baseline Git**: `b35fbe2` (commit đã tích hợp `image_specifications.md`).
- **Trạng thái bài viết (`article_status.json`)**: `status == "TECH_APPROVED"`, `is_locked == false`.
- **Cổng phê duyệt kỹ thuật Cổng 1 (`audit.json`)**: `gate == "TECHNICAL_REVIEW_GATE"`, `verdict == "PASS"`, `revision_request_file == null`.
- **Bản thảo kỹ thuật (`draft_review_package.md`)**: Đã hoàn tất 2 vòng sửa đổi (`REV-001` đến `REV-009`) và được nghiệm thu toàn diện.

---

## 3. PHẠM VI TUYỆT ĐỐI & RÀNG BUỘC KỶ LUẬT (SCOPE BOUNDARIES & STRICT CONSTRAINTS)

Để đảm bảo an toàn tuyệt đối cho kiến trúc và quy trình xuất bản:
1. **Nghiêm cấm tạo tệp ảnh nhị phân**: Không tạo bất kỳ tệp ảnh nào (`.png`, `.webp`, `.jpg`, `.svg`) trong task này.
2. **Nghiêm cấm gọi Packaging Agent**: Chưa kích hoạt công đoạn đóng gói HTML.
3. **Nghiêm cấm gán `VISUAL_READY`**: Bài viết duy trì trạng thái `TECH_APPROVED` theo nguyên tắc đóng lỗi an toàn (fail-closed protocol).
4. **Bảo toàn 100% hồ sơ kỹ thuật đã khóa**: Không sửa đổi dù chỉ một ký tự trong các tệp:
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/draft_review_package.md`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/claim_source_map.json`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/evidence.json`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/audit.json`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/technical_audit_report.md`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/revision_request.json`
5. **Tệp được phép chỉnh sửa duy nhất**:
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/image_specifications.md`
   - `03_Articles/BLOG_04_VFD_vs_Soft_Starter/article_status.json` (chỉ cập nhật trường `notes`)
   - `04_PLANS/260928_blog_04_visual_spec_semantic_micro_patch.md` (báo cáo này)

---

## 4. RÀ SOÁT CÁC YẾU TỐ VƯỢT QUY ĐỊNH CHỨNG CỨ (AUDIT OF OVEREXTENDED VISUAL CLAIMS)

Qua đối chiếu từng dòng giữa `image_specifications.md` và `evidence.json`, Visual Agent đã xác định các điểm vượt ranh giới ngữ nghĩa cần hiệu chỉnh:
1. **Tại `IMG-FEATURED`**:
   - Thiếu `EVD-015` trong mục căn cứ kỹ thuật (mặc dù prompt có so sánh kích thước bao ngoài giữa VFD và Soft Starter).
   - Prompt tiếng Anh chứa cụm từ *"hardware complexity comparison"* có thể hướng AI vẽ các chi tiết linh kiện giả định bên trong.
2. **Tại `IMG-001`**:
   - Sử dụng các tên linh kiện bán dẫn cụ thể: *"Diode Rectifier"* và *"IGBT Inverter"*, trong khi `EVD-001` chỉ xác định hai phần chuyển đổi: chuyển AC sang DC và chuyển DC ngược lại thành AC với tần số biến thiên $0-250\text{ Hz}$.
   - Sử dụng dải điện áp *"0 - 100%"* cho Soft Starter, trong khi `EVD-002` chỉ xác nhận điện áp hiệu dụng RMS tăng dần đến điện áp nguồn ở tần số giữ nguyên $50/60\text{ Hz}$.
   - Mô tả contactor bypass *"đóng mạch khi kết thúc dốc khởi động"*, trong khi `EVD-006` và `EVD-007` chỉ xác định bypass được sử dụng trong chế độ vận hành xác lập (steady-state).
   - Thiếu `EVD-006` trong danh sách Approved Technical Basis.
3. **Tại `IMG-002`**:
   - Mục tiêu kỹ thuật chứa cụm từ *"để bảo vệ lưới điện"* là động cơ suy diễn không có trong `EVD-003`.
4. **Tại `IMG-003`**:
   - Nhánh điều kiện câu hỏi 2 ghi chú *"VFD đáp ứng 100% Tn tại 0 rpm; Soft Starter sụt mô-men"*, cần tinh chỉnh sát từng chữ với `EVD-004`: *"VFD cung cấp đầy đủ mô-men tại 0 rpm; Soft Starter không đáp ứng"*.
5. **Tại Section 9 & 13**:
   - Khung HTML snippet cho Hình 1 chưa đồng bộ lời bình mới; danh sách kiểm định checklist thiếu `EVD-006`.

---

## 5. NỘI DUNG HIỆU CHỈNH CHI TIẾT CHO IMG-FEATURED

- **Căn cứ chứng cứ kỹ thuật bổ sung**: Đã bổ sung `EVD-015` (kích thước bao ngoài của Soft Starter nhỏ hơn so với VFD cùng công suất) vào mục căn cứ của `IMG-FEATURED` bên cạnh `EVD-001`, `EVD-002`, `EVD-005`.
- **Hiệu chỉnh Prompt AI (Prompt Neutralization)**:
  - Cụm từ ban đầu: `Balanced side-by-side composition highlighting hardware complexity comparison...`
  - Cụm từ sau hiệu chỉnh: `Balanced side-by-side composition providing a clear visual distinction and relative physical size comparison between the two motor-control technologies...`
- **Kết quả**: Prompt tập trung vào phân định trực quan công nghệ và tương quan kích thước lắp đặt, không kích hoạt AI vẽ cấu trúc vi mạch phức tạp hay suy diễn độ phức tạp phần cứng.

---

## 6. NỘI DUNG HIỆU CHỈNH CHI TIẾT CHO IMG-001

- **Căn cứ chứng cứ kỹ thuật bổ sung**: Bổ sung `EVD-006` vào danh mục (`EVD-001`, `EVD-002`, `EVD-005`, `EVD-006`, `EVD-007`).
- **Thu hẹp cấu trúc tầng VFD**:
  - Ban đầu: `[Khối Chỉnh lưu Rectifier]` $\rightarrow$ `[Khối DC Bus tụ điện phẳng]` $\rightarrow$ `[Khối Nghịch lưu Inverter IGBT]`.
  - Sau hiệu chỉnh: `[Khối Chuyển đổi AC-sang-DC (AC-to-DC Stage)]` $\rightarrow$ `[Khối Trung gian DC (DC Intermediate Stage)]` $\rightarrow$ `[Khối Chuyển đổi DC-sang-AC (DC-to-AC Stage)]` với ngõ ra tần số biến thiên $0-250\text{ Hz}$ theo đúng câu chữ của `EVD-001`.
- **Thu hẹp nguyên lý Soft Starter**:
  - Ban đầu: `U tăng dần 0 - 100%`.
  - Sau hiệu chỉnh: `tần số nguồn giữ nguyên 50/60 Hz, điện áp RMS tăng dần đến định mức` theo đúng `EVD-002`.
- **Thu hẹp vai trò Contactor Bypass**:
  - Ban đầu: `đóng mạch khi kết thúc dốc khởi động`.
  - Sau hiệu chỉnh: `sử dụng trong chế độ vận hành xác lập (steady-state operation)` theo đúng `EVD-006` và `EVD-007`.
- **Đồng bộ hóa Prompt AI và Tiêu chí nghiệm thu**: Toàn bộ prompt phôi đồ họa tiếng Anh và checklist nghiệm thu của `IMG-001` đã được đồng bộ chuẩn xác với cấu trúc ngữ nghĩa mới.

---

## 7. NỘI DUNG HIỆU CHỈNH CHI TIẾT CHO IMG-002

- **Loại bỏ động cơ suy diễn**: Đã xóa bỏ cụm từ `"để bảo vệ lưới điện"` trong phần mô tả mục tiêu kỹ thuật.
- **Khóa chặt phạm vi thực nghiệm Bảng 1 Rockwell (`EVD-003`)**:
  - Giữ nguyên vẹn 100% các giá trị đo rời rạc đã được chứng thực:
    - DOL: Dòng $600\%$, Điện áp $100\%$, Mô-men $100\%$.
    - Soft Start Điểm 1: Giới hạn dòng $150\%$, Điện áp $25\%$, Mô-men $6\%$.
    - Soft Start Điểm 2: Giới hạn dòng $300\%$, Điện áp $50\%$, Mô-men $25\%$.
    - Soft Start Điểm 3: Giới hạn dòng $450\%$, Điện áp $75\%$, Mô-men $56\%$.
  - Duy trì cảnh báo nghiêm ngặt cấm vẽ đường cong liên tục và cấm tạo cột dữ liệu cho VFD.

---

## 8. NỘI DUNG HIỆU CHỈNH CHI TIẾT CHO IMG-003

- **Đồng bộ lưu đồ với `EVD-004`**:
  - Ban đầu: `├── [CÓ] ──> [CÂN NHẮC CHỌN VFD] (VFD đáp ứng 100% Tn tại 0 rpm; Soft Starter sụt mô-men)`.
  - Sau hiệu chỉnh: `├── [CÓ] ──> [CÂN NHẮC CHỌN VFD] (VFD cung cấp đầy đủ mô-men tại 0 rpm; Soft Starter không đáp ứng)`.
- **Bảo toàn văn phong có điều kiện**: Giữ vững các nhánh đánh giá IEEE Std 519 tại PCC (dựa trên $I_{\text{sc}}/I_L$ cơ sở, không áp đặt lọc riêng) và so sánh CAPEX tương đối.

---

## 9. ĐỒNG BỘ KHUNG HTML VÀ DANH MỤC KIỂM TRA (SECTIONS 9 & 13)

- **Mục 9 (Responsive HTML Placeholders)**: Đã cập nhật chú thích (caption) của Hình 1 trong khung thẻ HTML mẫu:
  > *"So sánh sơ đồ khối chuyển đổi năng lượng giữa Biến tần VFD (chuyển đổi gián tiếp AC-DC-AC để thay đổi tần số ngõ ra từ 0 Hz đến 250 Hz) và Khởi động mềm Soft Starter (cặp thyristor phản song song điều khiển điện áp hiệu dụng RMS tăng dần ở tần số lưới cố định 50/60 Hz kèm nhánh bypass trong vận hành xác lập)."*
- **Mục 13 (Technical Verification Checklist)**: Đã cập nhật chuỗi truy xuất nguồn gốc đầy đủ bao gồm `EVD-006`: `EVD-001`, `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`, `EVD-006`, `EVD-007`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`.

---

## 10. MA TRẬN TRUY XUẤT CHỨNG CỨ THỊ GIÁC (VISUAL EVIDENCE TRACEABILITY MATRIX)

| Mã Tài sản | Căn cứ Chứng cứ đã Duyệt | Nội dung Kỹ thuật Bắt buộc Bám sát | Ranh giới Cấm Vi phạm |
|:---|:---|:---|:---|
| **`IMG-FEATURED`** | `EVD-001`, `EVD-002`, `EVD-005`, `EVD-015` | So sánh kích thước và phân định công nghệ VFD vs Soft Starter trong tủ điện công nghiệp | Cấm vẽ cấu trúc bán dẫn chi tiết bên trong; cấm đưa logo hãng giả mạo |
| **`IMG-001`** | `EVD-001`, `EVD-002`, `EVD-005`, `EVD-006`, `EVD-007` | Chuỗi AC-DC-AC (0-250 Hz); 3 cặp SCR phản song song điều khiển điện áp RMS tăng dần (50/60 Hz); Contactor bypass xác lập | Cấm định danh chi tiết bán dẫn (Diode, IGBT) ngoài chứng cứ; cấm gán dải 0-100% U; cấm suy diễn thời điểm đóng bypass |
| **`IMG-002`** | `EVD-003` | 4 điểm khảo sát thực nghiệm Table 1 Rockwell (600/100/100, 150/25/6, 300/50/25, 450/75/56) minh họa $T \propto U^2$ | Cấm vẽ đường cong liên tục; cấm vẽ cột dữ liệu dòng cho VFD; cấm thêm động cơ bảo vệ lưới điện |
| **`IMG-003`** | `EVD-003`, `EVD-004`, `EVD-005`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015` | Lưu đồ 3 câu hỏi tuần tự: tốc độ liên tục $\rightarrow$ mô-men tại 0 rpm $\rightarrow$ ràng buộc hệ thống & kinh tế | Cấm dùng văn phong áp đặt tuyệt đối; cấm ngụ ý mọi VFD đều phải có bộ lọc sóng hài riêng |

---

## 11. KIỂM ĐỊNH TÍNH TOÀN VẸN HỆ THỐNG (SYSTEM INTEGRITY CHECKS)

Visual Agent đã thực hiện kiểm tra đối chiếu:
- Không tạo ra bất kỳ tệp nhị phân rác nào trong workspace.
- Không can thiệp vào mã nguồn kiểm tra kiến trúc (`scripts/`).
- Bản thảo kỹ thuật `draft_review_package.md` hoàn toàn nguyên vẹn.

---

## 12. CẬP NHẬT TRẠNG THÁI BÀI VIẾT (ARTICLE STATUS)

Tệp `03_Articles/BLOG_04_VFD_vs_Soft_Starter/article_status.json` được cập nhật như sau:
```json
{
  "article_id": "BLOG_04",
  "title": "VFD và Soft Starter: So sánh Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Phạm vi Ứng dụng",
  "category": "BLOG-T04",
  "status": "TECH_APPROVED",
  "is_locked": false,
  "created_at": "2026-09-24T21:30:00+07:00",
  "evidence_dossier_file": "evidence_dossier.md",
  "notes": "Visual specifications semantic boundary cleanup completed. Final visual assets remain pending controlled rendering. VISUAL_READY not assigned."
}
```
- Trạng thái `status`: Duy trì `TECH_APPROVED`.
- `VISUAL_READY`: Không được gán (tuân thủ fail-closed).

---

## 13. KẾT LUẬN & ĐỀ XUẤT BƯỚC KẾ TIẾP (CONCLUSION & NEXT STEP)

Hồ sơ quy cách thị giác `image_specifications.md` đã được dọn sạch toàn diện các yếu tố ngữ nghĩa vượt ranh giới, sẵn sàng làm căn cứ thiết kế đồ họa vector và prompt AI chính xác cho:

**Nhiệm vụ tiếp theo đề xuất**:
`BLOG_04 — Controlled Visual Asset Generation` (Khởi tạo các tệp hình ảnh thực tế theo quy chuẩn đã hiệu chỉnh).

---
*Báo cáo được lập bởi: Visual Agent — Real Group*  
*Chữ ký số: `visual_agent:blog_04:semantic_cleanup_pass`*
