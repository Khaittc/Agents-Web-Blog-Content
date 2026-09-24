# QUY CHUẨN VẬN HÀNH, PHÊ DUYỆT VÀ KHÓA BÀI VIẾT (ARTICLE LIFECYCLE & APPROVAL PROTOCOL)
**Dự án**: Hệ thống Tự động hóa Đa Agent Sản xuất Nội dung Kỹ thuật (Real Group / TTC)  
**Mục đích**: Quy định nền tảng tương tác ra đề bài, vòng đời bài viết và cơ chế khóa cứng (Locking) chống tự ý chỉnh sửa sau khi bài đã được phê duyệt.

---

## 1. NỀN TẢNG VẬN HÀNH ĐỂ RA ĐỀ BÀI (EXECUTION PLATFORMS)

### Nền tảng Chính thức: Trực tiếp trên Google Antigravity (Đã Phê duyệt & Ban hành)
- **Phương thức**: Người dùng giao tiếp trực tiếp với Orchestrator Agent tại khung chat của Antigravity IDE hoặc CLI. Đây là phương thức vận hành chuẩn mực, liền mạch và tập trung nhất của Real Group.
- **Cú pháp ra đề bài chuẩn**:
  ```text
  Tạo bài viết mới dạng [MÃ_LOẠI_BÀI] về chủ đề: "[TÊN CHỦ ĐỀ]"
  Yêu cầu trọng tâm: [CÁC ĐIỂM KỸ THUẬT CẦN LÀM RÕ]
  ```
  *Ví dụ*:
  > *"Tạo bài viết mới dạng BLOG-T03 trong thư mục 03_Articles/BLOG_03_Chan_doan_qua_dong_bien_tan về chủ đề: 'Khắc phục lỗi quá dòng (Overcurrent) trên biến tần công nghiệp'."*
- **Các Slash Commands hỗ trợ tăng tốc**:
  - `/goal`: Chạy liên tục tự động cho đến khi hoàn thiện bài viết và báo cáo audit.
  - `/boost`: Phân tích sâu các vấn đề tính toán công thức, rà soát logic đa chiều.
  - `/teamwork-preview`: Điều phối và trực quan hóa luồng phối hợp giữa các subagents.

*(Ghi chú: Phương thức Web Dashboard ngoại vi được bảo lưu cho các giai đoạn tự động hóa mở rộng trong tương lai khi có nhu cầu).*

---

## 2. VÒNG ĐỜI BÀI VIẾT (ARTICLE STATE MACHINE)

Mọi bài viết trong `03_Articles/[Tên_Bài]/` bắt buộc phải tuân theo sơ đồ chuyển trạng thái sau:

```text
[Khởi tạo đề bài]
       │
       ▼
   1. DRAFT ◄─────────────────────────┐
       │ (Biên soạn & Thẩm định chéo) │
       ▼                              │ (Yêu cầu hiệu chỉnh)
  2. IN_REVIEW ───────────────────────┤
       │                              │
       ▼ (Người dùng phê duyệt)       │
 3. APPROVED / LOCKED ────────────────┴── [Chỉ mở khi có lệnh: UNLOCK]
       │
       ▼ (Đăng tải thực tế)
  4. PUBLISHED
```

### Ý nghĩa các trạng thái:
1. **DRAFT**: Bản thảo đang được Drafting Agent và Tech Review Agent xây dựng. Các Agent được phép đọc/ghi.
2. **IN_REVIEW**: Hoàn thành gói review (`review_package.md`) kèm báo cáo audit. Chờ người dùng kiểm tra. Agent tạm dừng sửa.
3. **REVISION_REQUESTED**: Người dùng đưa ra phản hồi yêu cầu sửa đổi cụ thể. Agent chỉ sửa các mục được chỉ định.
4. **APPROVED**: Bài viết đã được người dùng phê duyệt nội dung. Kích hoạt cơ chế khóa cứng (Locking).
5. **PUBLISHED**: Bài viết đã được copy sang CKEditor và đăng tải chính thức lên website `real-group.org`.

---

## 3. CƠ CHẾ KHÓA 3 LỚP (3-LAYER LOCKING MECHANISM)

Để đảm bảo không bất kỳ Agent nào có thể tự ý sửa đổi bài viết đã duyệt:

### Lớp 1: File Trạng thái Máy Đọc (`article_status.json`)
Mỗi bài viết bắt buộc phải có file `article_status.json` trong thư mục của nó.
- Cấu trúc chuẩn:
  ```json
  {
    "article_id": "BLOG_01",
    "title": "Tên bài viết",
    "category": "BLOG-T02",
    "status": "APPROVED",
    "is_locked": true,
    "approved_by": "Engineer_Lead",
    "approved_at": "2026-09-23T21:30:00+07:00",
    "html_file": "bai-viet-...-ckeditor.html",
    "notes": "Đã phê duyệt. Nghiêm cấm chỉnh sửa khi chưa có lệnh UNLOCK."
  }
  ```

### Lớp 2: Kiểm soát bằng Guardrail trong `AGENT_GUIDE.md`
- Trước khi thực hiện bất kỳ thao tác ghi đè hoặc chỉnh sửa nào trong thư mục `03_Articles/[Tên_Bài]`, Agent **BẮT BUỘC PHẢI ĐỌC** file `article_status.json`.
- Nếu `status == "APPROVED"` hoặc `is_locked == true`:
  - Agent **TỪ CHỐI THỰC HIỆN** chỉnh sửa.
  - Xuất thông báo cảnh báo rõ ràng cho người dùng.

### Lớp 3: Khóa tệp ở tầng Hệ điều hành (OS Read-Only)
- Khi người dùng ra lệnh phê duyệt, file HTML CKEditor sẽ được đặt thuộc tính Read-Only:
  ```powershell
  Set-ItemProperty -Path "03_Articles/[Tên_Bài]/[file].html" -Name IsReadOnly -Value $true
  ```

---

## 4. GIAO THỨC MỞ KHÓA (UNLOCK PROTOCOL)

Khi bài viết đã ở trạng thái `APPROVED / LOCKED`, nếu người dùng thực sự muốn cập nhật nội dung (ví dụ: cập nhật công nghệ mới hoặc thay đổi thông số):
- **Cú pháp bắt buộc từ người dùng**:
  > *"UNLOCK [MÃ_BÀI_VIẾT]: [LÝ DO MỞ KHÓA VÀ YÊU CẦU SỬA]"*
  *Ví dụ*:
  > *"UNLOCK BLOG_01: Cập nhật thêm thông số dòng khởi động của động cơ IE4."*
- **Hành động của Agent**:
  1. Chuyển `is_locked: false` và `status: "DRAFT"` trong `article_status.json`.
  2. Gỡ bỏ thuộc tính Read-Only trên hệ điều hành.
  3. Ghi log sự kiện mở khóa vào [WORKLOG.md](file:///d:/Agents_Tools/05_WebsiteTTC/WORKLOG.md).
  4. Tiến hành sửa đổi theo đúng yêu cầu đã chỉ định.
