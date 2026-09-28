# BÁO CÁO VI CHỈNH TRUY XUẤT CHỨNG CỨ THỊ GIÁC CÒN SÓT (RESIDUAL VISUAL TRACEABILITY PATCH REPORT) — BLOG_04

**Mã bài viết**: `BLOG_04`  
**Tiêu đề bài viết**: *VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải*  
**Thể loại bài viết**: `BLOG-T04` — Comparison  
**Tác nhân thực hiện**: Visual Agent (`visual_agent`) — Real Group  
**Ngày thực hiện**: 28/09/2026  

---

## 1. BASELINE

- **Baseline commit**: `679f55b` (*fix: tighten BLOG_04 visual evidence boundaries*).
- **Trạng thái bài viết**: `article_status.status = TECH_APPROVED`, `is_locked = false`.
- **Cổng phê duyệt kỹ thuật**: Cổng 1 đạt `PASS` (`audit.json` không có revision request).
- **Hồ sơ quy cách thị giác**: `image_specifications.md` đã được dọn dẹp ngữ nghĩa kỹ thuật.
- **Tài sản nhị phân**: Chưa khởi tạo (NOT GENERATED), `VISUAL_READY = NO`.

---

## 2. RESIDUAL MISMATCH (NGUYÊN NHÂN GỐC)

Trong lưu đồ logic của `IMG-003` (Khung quyết định lựa chọn tuần tự) tại Câu hỏi 3:
```text
Không gian tủ điện hẹp & chạy mát?
→ Soft Starter ưu thế (kích thước nhỏ, bypass AC-1)
```
Các visual claims này tương ứng với các chứng cứ kỹ thuật đã được phê duyệt:
- Kích thước Soft Starter nhỏ hơn VFD: `EVD-015`
- Chạy mát hơn trong chế độ bypass xác lập: `EVD-006`
- Contactor bypass định mức điển hình AC-1: `EVD-007`

Tuy nhiên, trong hồ sơ `image_specifications.md`, mục **Approved Technical Basis** của `IMG-003` trước patch chỉ liệt kê:
`EVD-003`, `EVD-004`, `EVD-005`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`.
Mục này bị thiếu `EVD-006` và `EVD-007`, dẫn đến lỗi **Visual Traceability Mismatch** giữa nội dung trực quan hóa và cơ sở chứng cứ được liên kết.

---

## 3. IMG-003 EVIDENCE MAPPING BEFORE

Trước khi hiệu chỉnh:
```text
IMG-003 Approved Technical Basis:
  EVD-003, EVD-004, EVD-005, EVD-009, EVD-010, EVD-014, EVD-015
(Thiếu: EVD-006, EVD-007)
```

---

## 4. IMG-003 EVIDENCE MAPPING AFTER

Sau khi hiệu chỉnh:
```text
IMG-003 Approved Technical Basis:
  EVD-003, EVD-004, EVD-005, EVD-006, EVD-007, EVD-009, EVD-010, EVD-014, EVD-015
(Đầy đủ 100% chứng cứ cho toàn bộ các nhánh quyết định)
```

---

## 5. EVD-006 SEMANTIC BOUNDARY

- **Nguồn chứng cứ**: Schneider Electric Blog (`SRC-003`).
- **Nội dung được phê duyệt**: Khởi động mềm có bypass tích hợp chạy mát hơn và hiệu quả hơn biến tần khi vận hành ở tốc độ tối đa định mức (full speed) và tải đủ (adequately loaded), bởi vì dòng điện được dẫn qua tiếp điểm contactor thay vì van bán dẫn.
- **Ranh giới khống chế**:
  - Không suy diễn thành "luôn luôn chạy mát hơn trong mọi điều kiện vận hành".
  - Không bịa đặt phần trăm hiệu suất cụ thể ngoài hồ sơ.
  - Ngữ cảnh lưu đồ `IMG-003` đặt trong câu hỏi có điều kiện tại Câu hỏi 3 ("Không gian tủ điện hẹp & chạy mát?"), bảo đảm an toàn ngữ nghĩa.

---

## 6. EVD-007 SEMANTIC BOUNDARY

- **Nguồn chứng cứ**: Rockwell Automation White Paper 150-WP007A-EN-P, p. 7 (`SRC-002`).
- **Nội dung được phê duyệt**: Contactor bypass tích hợp thường được chọn theo định mức AC-1 vì contactor này không phải đóng hoặc ngắt dòng điện có tải (quá trình đóng/ngắt do thyristor phụ trách).
- **Ranh giới khống chế**:
  - Không suy diễn về tuổi thọ cơ khí cụ thể hay kích thước vật lý cụ thể của contactor.
  - Không mô tả chuỗi thời gian đóng ngắt micro-giây ngoài chứng cứ.
  - Ngữ cảnh lưu đồ `IMG-003` chỉ ghi nhận nhãn kỹ thuật rút gọn `(kích thước nhỏ, bypass AC-1)` hoàn toàn trung thực với tài liệu.

---

## 7. TRACEABILITY MATRIX SYNCHRONIZATION

Đã đồng bộ hóa bảng **Visual Evidence Traceability Matrix** trực tiếp vào Mục 8 của [`image_specifications.md`](file:///d:/Agents_Tools/05_WebsiteTTC/03_Articles/BLOG_04_VFD_vs_Soft_Starter/image_specifications.md):

| Mã Tài sản | Căn cứ Chứng cứ đã Phê duyệt (Approved Technical Basis) | Tóm tắt Ranh giới Nội dung Kỹ thuật |
|:---|:---|:---|
| **`IMG-FEATURED`** | `EVD-001`, `EVD-002`, `EVD-005`, `EVD-015` | So sánh kích thước bao ngoài và bối cảnh lắp đặt tủ điện công nghiệp giữa VFD và Soft Starter |
| **`IMG-001`** | `EVD-001`, `EVD-002`, `EVD-005`, `EVD-006`, `EVD-007` | Chuỗi chuyển đổi AC-DC-AC (0-250 Hz); 3 cặp SCR phản song song điều khiển RMS (50/60 Hz); Contactor bypass xác lập |
| **`IMG-002`** | `EVD-003` | 4 điểm khảo sát thực nghiệm Bảng 1 Rockwell (600%, 150%, 300%, 450%) minh họa $T \propto U^2$ |
| **`IMG-003`** | `EVD-003`, `EVD-004`, `EVD-005`, `EVD-006`, `EVD-007`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015` | Lưu đồ 3 câu hỏi tuần tự: điều chỉnh tốc độ $\rightarrow$ mô-men zero speed $\rightarrow$ đánh giá tổng hợp ràng buộc & kinh tế |

Hoàn toàn triệt tiêu mismatch giữa asset specification và traceability matrix.

---

## 8. TECHNICAL ARTIFACT INTEGRITY

- `draft_review_package.md`: **UNCHANGED** (nguyên vẹn 100%).
- `claim_source_map.json`: **UNCHANGED** (nguyên vẹn 100%).
- `evidence.json` / `evidence_dossier.md`: **UNCHANGED** (nguyên vẹn 100%).
- `audit.json` / `technical_audit_report.md`: **UNCHANGED** (nguyên vẹn 100%).
- `article_status.json`: **UNCHANGED** (duy trì `status == "TECH_APPROVED"`).

---

## 9. LIFECYCLE STATUS

- Trạng thái vòng đời hiện tại: **`TECH_APPROVED`**.
- Cổng 2 (Visual Handoff): Quy cách hoàn chỉnh, sẵn sàng tạo phôi ảnh có kiểm soát.
- Cờ `VISUAL_READY`: **`NO`** (duy trì quy tắc fail-closed cho đến khi các tệp nhị phân được kết xuất thực tế).

---

## 10. CONTROLLED ASSET-GENERATION READINESS

Hồ sơ thị giác đã đạt độ nhất quán và truy xuất nguồn gốc 100%, sẵn sàng bước vào:
**`BLOG_04 — Controlled Visual Asset Generation`**.

---
*Báo cáo được lập bởi: Visual Agent — Real Group*  
*Chữ ký số: `visual_agent:blog_04:traceability_patch_pass`*
