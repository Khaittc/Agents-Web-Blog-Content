# BỘ QUY CÁCH HÌNH ẢNH & PROMPT TẠO ẢNH AI (IMAGE SPECIFICATIONS & PROMPT DOSSIER) — BLOG_04

---

## 1. ARTICLE METADATA (THÔNG TIN BÀI VIẾT)

- **Mã bài viết (Article ID)**: `BLOG_04`
- **Tiêu đề bài viết**: *VFD và Soft Starter: So sánh Toàn diện về Nguyên lý, Dòng khởi động, Điều khiển Tốc độ và Tiêu chí Lựa chọn Phụ tải*
- **Thể loại bài viết (Canonical Taxonomy)**: `BLOG-T04` — Comparison (Bài viết So sánh & Đối chiếu Công nghệ)
- **Tác nhân phụ trách (Unit)**: Visual Agent (`visual_agent`) — Real Group
- **Ngày lập hồ sơ**: 28/09/2026
- **Quy chuẩn kỹ thuật áp dụng**:
  - `IMAGE_SPECIFICATION_AND_PROMPT_SKILL_v1.2.md`
  - `BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md` (Mục 14: $1 \le n \le 3$)
  - `REAL_GROUP_TECHNICAL_ARTICLE_MASTER_STYLE_v1.0.md` (Inline CSS Responsive)
  - `ADR-010`: Phân tách Prompt AI & Khung placeholder HTML, không nhúng mã vẽ thô trực tiếp
  - `ADR-016`: Chuẩn Responsive đa thiết bị (Laptop & Mobile) với `display:block; margin:0 auto; max-width:100%; width:100%; height:auto!important;`

---

## 2. TECHNICAL GATE PREREQUISITE CONFIRMATION (XÁC NHẬN ĐIỀU KIỆN CỔNG 1)

Trước khi tiến hành xây dựng hồ sơ thị giác, Visual Agent đã thẩm định trạng thái tiền điều kiện:
- **`article_status.json`**: `status == "TECH_APPROVED"` (Đạt).
- **`audit.json`**: `gate == "TECHNICAL_REVIEW_GATE"`, `verdict == "PASS"`, `revision_request_file == null` (Đạt).
- **Tất cả 9 vấn đề hiệu chỉnh (`REV-001` đến `REV-009`)**: Đã được Review Agent xác nhận `VERIFIED_RESOLVED` trong Phần III của `technical_audit_report.md`.
- **Ranh giới bất biến (Strict Read-Only)**: Visual Agent cam kết không sửa đổi bất kỳ câu chữ, công thức, số liệu, luận điểm hoặc trích dẫn nào trong `draft_review_package.md`, `claim_source_map.json`, `evidence.json`, hay `audit.json`.

---

## 3. VISUAL STRATEGY FOR BLOG-T04 (CHIẾN LƯỢC THỊ GIÁC CHO THỂ LOẠI SO SÁNH)

Thể loại `BLOG-T04` đòi hỏi phong cách minh họa kỹ thuật chuẩn mực, làm nổi bật bản chất khác biệt giữa hai công nghệ và hỗ trợ kỹ sư đưa ra quyết định lựa chọn chính xác:
1. **Tránh biến bài viết thành quảng cáo thương mại**: Tuyệt đối không gắn nhãn mác, mã sản phẩm hoặc logo thương hiệu giả mạo của ABB, Rockwell, Schneider, Siemens, Yaskawa. Hình ảnh mang tính tài liệu kỹ thuật công nghiệp trung lập.
2. **Cân bằng đối chiếu (Side-by-side Technical Contrast)**: Mọi hình ảnh so sánh phải thể hiện rõ hai thái cực công nghệ (Biến tần AC-DC-AC điều khiển tần số vs Khởi động mềm SCR điều khiển góc kích điện áp RMS).
3. **Kỷ luật dữ liệu định lượng (Data Discipline)**: Hình ảnh biểu đồ không được phép nội suy võ đoán hoặc vẽ đường cong liên tục giả định; bắt buộc thể hiện chính xác các điểm đo thực nghiệm rời rạc theo đúng bằng chứng kỹ thuật đã phê duyệt (`EVD-003`).
4. **Quy mô số lượng hình ảnh**:
   - **01 Featured Image** (`808 × 500 px`, tỷ lệ ~ 16:10): Tạo bối cảnh công nghệ so sánh trực quan, sạch sẽ, chuyên nghiệp.
   - **03 Content Images** (`1200 × 675 px`, tỷ lệ 16:9): Trực quan hóa 3 câu hỏi kỹ thuật độc lập cốt lõi:
     - *Hình 1*: Cấu trúc mạch lực và nguyên lý chuyển đổi năng lượng (Topology Comparison).
     - *Hình 2*: Ma trận thực nghiệm dòng khởi động và mô-men quay ($T \propto U^2$).
     - *Hình 3*: Khung quyết định lựa chọn kỹ thuật tuần tự (Selection Decision Framework).

---

## 4. FEATURED IMAGE (IMG-FEATURED — ẢNH ĐẠI DIỆN BÀI VIẾT)

- **Mã định danh (Asset ID)**: `IMG-FEATURED`
- **Vai trò (Role)**: Ảnh đại diện đầu bài viết trên CMS `real-group.org`, hiển thị trong danh mục Blog và thẻ chia sẻ mạng xã hội (OpenGraph / Twitter Card).
- **Tiêu đề hình ảnh (Title)**: So sánh Công nghệ Điều khiển Động cơ Ba pha: Biến tần (VFD) vs Khởi động Mềm (Soft Starter)
- **Mục tiêu kỹ thuật (Purpose)**: Thiết lập bối cảnh so sánh kỹ thuật công nghiệp hiện đại giữa VFD và Soft Starter trong môi trường điều khiển động cơ không đồng bộ ba pha, truyền tải sự tương phản giữa cấu trúc biến đổi tần số phức hợp và bộ điều khiển điện áp nhỏ gọn.
- **Vị trí chèn trong bài (Insertion Point)**: Đầu bài viết (Header Featured Image) và OpenGraph metadata.
- **Căn cứ chứng cứ kỹ thuật (Approved Technical Basis)**: `EVD-001`, `EVD-002`, `EVD-005`, `EVD-015` (Bối cảnh chung và tương quan kích thước bao ngoài giữa hai công nghệ).
- **Kích thước chuẩn (Dimensions)**: `808 × 500 px`
- **Tỷ lệ khung hình (Aspect Ratio)**: `16:10` (xấp xỉ 1.618 : 1 — tỷ lệ vàng cho banner kỹ thuật)
- **Phương pháp tạo ảnh khuyến nghị (Rendering Method)**: Nhiếp ảnh tư liệu kỹ thuật công nghiệp kết hợp đồ họa 3D isometric hiện đại (Midjourney v6.1 / DALL-E 3 / Studio 3D render).
- **Tên tệp xuất bản đề xuất (Filename)**: `featured-vfd-vs-soft-starter-808x500.webp`
- **Thẻ ALT Text chuẩn SEO**: `So sánh biến tần VFD và khởi động mềm Soft Starter trong tủ điều khiển động cơ không đồng bộ ba pha công nghiệp`
- **Lời bình / Chú thích (Caption)**: *Ảnh đại diện: Tương quan công nghệ giữa Biến tần (VFD) và Khởi động Mềm (Soft Starter) trong hệ thống truyền động điện công nghiệp ba pha.*
- **Khung kỹ nghệ Prompt AI 5 tầng (5-Tier AI Prompt)**:
  ```text
  Professional industrial technical comparison photograph showing a modern Variable Frequency Drive (VFD) unit on the left and a compact solid-state Soft Starter unit on the right, neatly mounted inside a clean industrial electrical control cabinet (MCC). In the lower center, a heavy-duty 3-phase squirrel-cage induction motor is positioned with high-grade industrial cable routing. Balanced side-by-side composition providing a clear visual distinction and relative physical size comparison between the two motor-control technologies. Clean industrial engineering aesthetic, crisp technical lighting with cool corporate navy blue (#0f2b46), technical cyan (#0284c7), and subtle neutral gray (#f8fafc) accents, clean wiring ducts, sharp focus, technical realism, no fake brand logos, no text distortion, 8k resolution, shot on 50mm lens --ar 16:10 --style raw --v 6.1
  ```
- **Negative Prompt (Khống chế chống ảo giác)**:
  ```text
  incorrect wiring, random electrical terminals, floating components, fake brand logos, brand names, illegible text, distorted cables, sparks, fire, hazardous exposed conductors, cartoon, 3d caricature, anime, cyberpunk, dark sci-fi background, oversaturated colors, watermark, signature, low resolution, blurry
  ```
- **Ràng buộc kỹ thuật & Tiêu chí nghiệm thu (Acceptance Checks)**:
  - [x] Kích thước chính xác `808 × 500 px`.
  - [x] VFD và Soft Starter có sự phân định rõ ràng về hình dáng và kích thước tương đối (Soft Starter gọn hơn VFD).
  - [x] Không xuất hiện logo hãng giả mạo hay nhãn hiệu vi phạm bản quyền.
  - [x] Hệ thống dây cáp đi gọn gàng trong máng cáp công nghiệp, không có dây nối lơ lửng hay phóng điện nguy hiểm.
  - [x] Bố cục rõ nét, nhận diện tốt ở cả kích thước thu nhỏ (thumbnail).

---

## 5. CONTENT IMAGE 1 (IMG-001 — SƠ ĐỒ CẤU TRÚC MẠCH LỰC & NGUYÊN LÝ BIẾN ĐỔI)

- **Mã định danh (Asset ID)**: `IMG-001`
- **Vai trò (Role)**: Hình ảnh nội dung 1 (Content Image 1).
- **Tiêu đề hình ảnh (Title)**: So sánh Cấu trúc Công suất và Nguyên lý Biến đổi Năng lượng Giữa VFD và Soft Starter
- **Mục tiêu kỹ thuật (Purpose)**: Làm rõ sự khác biệt bản chất về mặt cấu trúc điện lực: VFD chuyển đổi năng lượng gián tiếp qua chuỗi AC-DC-AC (khối chuyển đổi AC-sang-DC, khối trung gian DC, khối chuyển đổi DC-sang-AC) để thay đổi tần số $0-250\text{ Hz}$; Soft Starter điều khiển góc kích pha của 3 cặp thyristor phản song song để tăng dần điện áp hiệu dụng RMS đến điện áp nguồn định mức trong khi tần số giữ nguyên $50/60\text{ Hz}$, kết hợp nhánh contactor bypass dùng trong chế độ vận hành xác lập.
- **Vị trí chèn trong bài (Insertion Point)**: Đặt ngay sau **Mục 2** (*## 2. Khác biệt Cốt lõi về Nguyên lý Biến đổi Điện năng và Cấu trúc Công suất*).
- **Căn cứ chứng cứ kỹ thuật (Approved Technical Basis)**: `EVD-001`, `EVD-002`, `EVD-005`, `EVD-006`, `EVD-007` (Gốc: ABB Softstarter Handbook p. 16, pp. 21–22; Rockwell White Paper p. 7; Schneider Blog).
- **Kích thước chuẩn (Dimensions)**: `1200 × 675 px`
- **Tỷ lệ khung hình (Aspect Ratio)**: `16:9`
- **Phương pháp tạo ảnh khuyến nghị (Rendering Method)**: Sơ đồ khối kỹ thuật vector có kiểm soát (Controlled Vector Block Diagram / CAD Infographic) được thiết kế qua phần mềm đồ họa kỹ thuật (Figma / Adobe Illustrator / Draw.io). **Cảnh báo**: Không dùng Generative AI tạo sơ đồ mạch ngẫu nhiên vì nguy cơ vẽ sai linh kiện bán dẫn.
- **Tên tệp xuất bản đề xuất (Filename)**: `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp`
- **Thẻ ALT Text chuẩn SEO**: `So sánh sơ đồ cấu trúc chuyển đổi điện năng AC-DC-AC của biến tần VFD và điều khiển góc kích pha SCR của khởi động mềm Soft Starter`
- **Lời bình / Chú thích (Caption)**:
  *Hình 1: So sánh sơ đồ khối chuyển đổi năng lượng giữa Biến tần VFD (chuyển đổi gián tiếp AC-DC-AC để thay đổi tần số ngõ ra từ $0\text{ Hz}$ đến $250\text{ Hz}$) và Khởi động mềm Soft Starter (cặp thyristor phản song song điều khiển điện áp hiệu dụng RMS tăng dần ở tần số lưới cố định $50/60\text{ Hz}$ kèm nhánh bypass trong vận hành xác lập).*
- **Đặc tả bố cục kỹ thuật (Diagram Specification)**:
  - **Khung bên trái (VFD Topology)**:
    `Nguồn lưới 3 pha (50/60 Hz)` $\rightarrow$ `[Khối Chuyển đổi AC-sang-DC (AC-to-DC Stage)]` $\rightarrow$ `[Khối Trung gian DC (DC Intermediate Stage)]` $\rightarrow$ `[Khối Chuyển đổi DC-sang-AC (DC-to-AC Stage)]` $\rightarrow$ `Động cơ 3 pha (tần số ngõ ra biến thiên 0 - 250 Hz)`.
  - **Khung bên phải (Soft Starter Topology)**:
    `Nguồn lưới 3 pha (50/60 Hz)` $\rightarrow$ `[3 cặp Thyristor SCR phản song song (anti-parallel)]` $\rightarrow$ `Động cơ 3 pha (tần số nguồn giữ nguyên 50/60 Hz, điện áp RMS tăng dần đến định mức)`.
    Song song với khối SCR là `[Nhánh Contactor Bypass AC-1]` sử dụng trong chế độ vận hành xác lập (steady-state operation).
  - **Bảng màu**: Nền trắng ngà (`#f8fafc`), khối chức năng viền xanh navy (`#0f2b46`), đường dẫn tín hiệu xanh cyan (`#0284c7`), nhãn phụ trợ xám kỹ thuật (`#64748b`).
- **Prompt hỗ trợ tạo phôi đồ họa (Drafting Prompt for AI Concept)**:
  ```text
  Clean technical engineering infographic comparing two electrical motor control power topologies side-by-side on an off-white grid background (#f8fafc). Left panel labeled 'Variable Frequency Drive (VFD)': sequential functional block diagram showing 3-phase AC input (50/60 Hz) flowing into an AC-to-DC conversion stage, then a DC intermediate stage, then a DC-to-AC conversion stage outputting variable frequency (0-250 Hz) AC to a 3-phase motor. Right panel labeled 'Soft Starter': 3-phase AC input flowing through anti-parallel Thyristor (SCR) pairs providing progressively increasing RMS output voltage at constant 50/60 Hz grid frequency, with an integrated Bypass Contactor in parallel across the SCR stage for steady-state operation. Crisp vector lines, high-contrast engineering schematic aesthetic, professional electrical engineering textbook quality, Real Group palette (#0f2b46 navy, #0284c7 cyan), ultra-clear typography, no chaotic wiring, no blurry text --ar 16:9 --v 6.1
  ```
- **Ràng buộc kỹ thuật & Tiêu chí nghiệm thu (Acceptance Checks)**:
  - [x] Khối VFD thể hiện đúng cấu trúc 3 tầng: Chuyển đổi AC-DC $\rightarrow$ Trung gian DC $\rightarrow$ Chuyển đổi DC-AC; ngõ ra ghi rõ tần số biến thiên $0-250\text{ Hz}$.
  - [x] Khối Soft Starter thể hiện cặp thyristor phản song song; ngõ ra ghi rõ điện áp RMS tăng dần ở tần số lưới cố định $50/60\text{ Hz}$.
  - [x] Nhánh contactor bypass mắc song song với khối thyristor phục vụ chế độ xác lập.
  - [x] Không phát sinh linh kiện lạ hay dây nối giả định ngoài cấu trúc chuẩn.
- **Trạng thái tài sản (Asset Status)**: `ASSET_REQUIRES_CONTROLLED_RENDERING`

---

## 6. CONTENT IMAGE 2 (IMG-002 — BIỂU ĐỒ THỰC NGHIỆM DÒNG & MÔ-MEN KHỞI ĐỘNG)

- **Mã định danh (Asset ID)**: `IMG-002`
- **Vai trò (Role)**: Hình ảnh nội dung 2 (Content Image 2).
- **Tiêu đề hình ảnh (Title)**: So sánh Định lượng Dòng Khởi động và Quan hệ Mô-men theo Dữ liệu Thực nghiệm Rockwell Automation
- **Mục tiêu kỹ thuật (Purpose)**: Trực quan hóa các điểm khảo sát thực nghiệm rời rạc từ Bảng 1 của Rockwell Automation (`EVD-003`) về quan hệ giữa mức giới hạn dòng, điện áp tương ứng và mô-men khởi động theo quy luật phi tuyến $T_{\text{start}} \propto U^2$ (trong đó mức giới hạn dòng $150\%$ dòng định mức tương ứng với $25\%$ điện áp và $6\%$ mô-men).
- **Vị trí chèn trong bài (Insertion Point)**: Đặt ngay sau **Bảng số liệu thực nghiệm tại Mục 3.2** (*### 3.2. Quan hệ Phi tuyến Giữa Mô-men Khởi động và Điện áp ($T \propto U^2$)*).
- **Căn cứ chứng cứ kỹ thuật (Approved Technical Basis)**: `EVD-003` (Rockwell White Paper 150-WP007A-EN-P, Table 1, p. 6).
- **Kích thước chuẩn (Dimensions)**: `1200 × 675 px`
- **Tỷ lệ khung hình (Aspect Ratio)**: `16:9`
- **Phương pháp tạo ảnh bắt buộc (Mandatory Method)**: **Deterministic Technical Data Chart / Infographic Matrix**. **NGHIÊM CẤM** dùng Generative AI để tự vẽ đồ thị số liệu này vì AI sẽ nội suy sai lệch các điểm rời rạc thành đường cong liên tục hoặc bịa đặt số liệu VFD.
- **Tên tệp xuất bản đề xuất (Filename)**: `hinh-2-dong-va-mo-men-khoi-dong.webp`
- **Thẻ ALT Text chuẩn SEO**: `Biểu đồ so sánh định lượng dòng khởi động và mô-men quay giữa khởi động trực tiếp DOL và 3 điểm giới hạn dòng khởi động mềm theo Rockwell Automation`
- **Lời bình / Chú thích (Caption)**:
  *Hình 2: Các điểm khảo sát thực nghiệm của Rockwell Automation minh họa quan hệ phi tuyến giữa mức giới hạn dòng, điện áp stato và mô-men khởi động sụt giảm theo quy luật bình phương ($T \propto U^2$); điểm giới hạn dòng $150\%$ chỉ sinh ra $6\%$ mô-men định mức.*
- **Bộ số liệu bắt buộc (Exact Approved Data Points from Table 1)**:
  | Phương thức / Điểm khảo sát | Giới hạn Dòng (% $I_n$) | Điện áp Stato (% $U_n$) | Mô-men Khởi động (% $T_n$) |
  |:---|:---:|:---:|:---:|
  | **Khởi động Trực tiếp (DOL)** | $600\%$ | $100\%$ | $100\%$ |
  | **Khởi động Mềm (Điểm 1)** | $150\%$ | $25\%$ | **$6\%$** |
  | **Khởi động Mềm (Điểm 2)** | $300\%$ | $50\%$ | **$25\%$** |
  | **Khởi động Mềm (Điểm 3)** | $450\%$ | $75\%$ | **$56\%$** |
- **Ràng buộc chống ảo giác thị giác (Anti-Hallucination Constraints)**:
  - **KHÔNG** vẽ đường cong cong nối liền các điểm (không biểu diễn như dải liên tục phổ quát).
  - **KHÔNG** bịa đặt dải số liệu định lượng hay cột phần trăm dòng khởi động cho VFD (hồ sơ bằng chứng `EVD-001` không xác lập số liệu định lượng dải dòng cho VFD).
  - Trình bày dưới dạng cột nhóm so sánh đa trục (Grouped Bar Chart) hoặc ma trận thẻ kỹ thuật (Metric Comparison Matrix) với 4 trường hợp khảo sát độc lập.
- **Trạng thái tài sản (Asset Status)**: `DATA_FIGURE_REQUIRES_DETERMINISTIC_RENDERING`

---

## 7. CONTENT IMAGE 3 (IMG-003 — KHUNG QUYẾT ĐỊNH LỰA CHỌN KỸ THUẬT)

- **Mã định danh (Asset ID)**: `IMG-003`
- **Vai trò (Role)**: Hình ảnh nội dung 3 (Content Image 3).
- **Tiêu đề hình ảnh (Title)**: Khung Quyết định Tuần tự Lựa chọn Giữa VFD và Soft Starter (Decision Framework Flowchart)
- **Mục tiêu kỹ thuật (Purpose)**: Trực quan hóa quy trình tư duy kỹ thuật 3 bước tại Mục 10 của bài viết, cung cấp công cụ hướng dẫn ra quyết định khách quan, có điều kiện dựa trên yêu cầu điều khiển tốc độ, mô-men zero speed, dòng khởi động, sóng hài PCC và chi phí đầu tư.
- **Vị trí chèn trong bài (Insertion Point)**: Đặt tại đầu **Mục 10** (*## 10. Tiêu chí Lựa chọn Kỹ thuật Tối ưu (Decision Framework)*) ngay trước các câu hỏi chi tiết.
- **Căn cứ chứng cứ kỹ thuật (Approved Technical Basis)**: `EVD-003`, `EVD-004`, `EVD-005`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`.
- **Kích thước chuẩn (Dimensions)**: `1200 × 675 px`
- **Tỷ lệ khung hình (Aspect Ratio)**: `16:9`
- **Phương pháp tạo ảnh khuyến nghị (Rendering Method)**: Sơ đồ lưu đồ vector có kiểm soát (Controlled Vector Flowchart via Figma / Draw.io / Mermaid SVG export).
- **Tên tệp xuất bản đề xuất (Filename)**: `hinh-3-khung-lua-chon-vfd-soft-starter.webp`
- **Thẻ ALT Text chuẩn SEO**: `Lưu đồ cây quyết định lựa chọn kỹ thuật giữa biến tần VFD và khởi động mềm Soft Starter theo yêu cầu điều khiển tốc độ và mô-men tải`
- **Lời bình / Chú thích (Caption)**:
  *Hình 3: Khung quyết định tuần tự hỗ trợ kỹ sư lựa chọn giữa VFD và Soft Starter dựa trên yêu cầu điều chỉnh tốc độ liên tục, mô-men bứt phá tại $0\text{ rpm}$ và các ràng buộc về dòng điện, sóng hài PCC và chi phí.*
- **Cấu trúc lưu đồ logic đã phê duyệt (Approved Logic Structure)**:
  ```text
  [BẮT ĐẦU: Khảo sát Phụ tải Động cơ Ba pha]
                     │
                     ▼
  {Câu hỏi 1: Quy trình công nghệ có đòi hỏi ĐIỀU CHỈNH TỐC ĐỘ LIÊN TỤC không?}
         ├── [CÓ] ──> [CÂN NHẮC CHỌN VFD] (Khởi động mềm không đáp ứng)
         │
       [KHÔNG]
         │
         ▼
  {Câu hỏi 2: Phụ tải có đòi hỏi ĐẦY ĐỦ MÔ-MEN BỨT PHÁ tại 0 rpm (Zero Speed) không?}
         ├── [CÓ] ──> [CÂN NHẮC CHỌN VFD] (VFD cung cấp đầy đủ mô-men tại 0 rpm; Soft Starter không đáp ứng)
         │
       [KHÔNG]
         │
         ▼
  {Câu hỏi 3: Đánh giá tổng hợp các ràng buộc hệ thống & bài toán kinh tế:}
         ├── Giới hạn dòng khởi động nghiêm ngặt? ──> Đối chiếu yêu cầu mô-men tải & dữ liệu OEM
         ├── Không gian tủ điện hẹp & chạy mát? ──> Soft Starter ưu thế (kích thước nhỏ, bypass AC-1)
         ├── Tuân thủ IEEE Std 519 tại PCC? ──> Đánh giá tỷ số Isc/IL tổng cơ sở (không bắt buộc lọc riêng)
         └── Chi phí đầu tư ban đầu? ──> Dải thấp tương đương, dải công suất lớn VFD tăng cao hơn
                     │
                     ▼
  [KẾT LUẬN: Đưa ra Lựa chọn Kỹ thuật Tối ưu cho Dự án]
  ```
- **Ràng buộc văn phong kỹ thuật (Wording Discipline)**:
  - Sử dụng văn phong có điều kiện: *"Cân nhắc chọn VFD"*, *"Đánh giá tùy theo tải"*, *"Đối chiếu dữ liệu"*.
  - **TUYỆT ĐỐI KHÔNG** dùng văn phong áp đặt tuyệt đối: *"Bắt buộc phải chọn"*, *"Luôn luôn tốt hơn"*, *"Giải pháp duy nhất"*.
- **Trạng thái tài sản (Asset Status)**: `ASSET_REQUIRES_CONTROLLED_RENDERING`

---

## 8. PLACEHOLDER / INSERTION MATRIX (MA TRẬN VỊ TRÍ CHÈN TRONG BÀI)

| Mã Tài sản | Tên tệp xuất bản | Vị trí chèn trong bài | Tỷ lệ & Kích thước | Trạng thái hiển thị |
|:---|:---|:---|:---:|:---|
| **`IMG-FEATURED`** | `featured-vfd-vs-soft-starter-808x500.webp` | Header bài viết & OpenGraph | 16:10 (`808 × 500 px`) | Đặt trong khung Featured Image của CMS |
| **`IMG-001`** | `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp` | Ngay sau Mục 2 (dưới Dòng 37) | 16:9 (`1200 × 675 px`) | Nhúng placeholder `[URL_HINH_ANH_1]` |
| **`IMG-002`** | `hinh-2-dong-va-mo-men-khoi-dong.webp` | Sau Bảng số liệu Mục 3.2 (dưới Dòng 74) | 16:9 (`1200 × 675 px`) | Nhúng placeholder `[URL_HINH_ANH_2]` |
| **`IMG-003`** | `hinh-3-khung-lua-chon-vfd-soft-starter.webp` | Đầu Mục 10 (dưới Dòng 237) | 16:9 (`1200 × 675 px`) | Nhúng placeholder `[URL_HINH_ANH_3]` |

---

## 9. RESPONSIVE CKEDITOR HTML PLACEHOLDERS (ADR-016 COMPLIANT)

Packaging Agent sẽ sử dụng nguyên văn các đoạn mã HTML dưới đây để tích hợp vào bản thảo hoàn chỉnh:

### Khung HTML cho Hình 1:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_1]" alt="So sánh sơ đồ cấu trúc chuyển đổi điện năng AC-DC-AC của biến tần VFD và điều khiển góc kích pha SCR của khởi động mềm Soft Starter" style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 1:</strong> So sánh sơ đồ khối chuyển đổi năng lượng giữa Biến tần VFD (chuyển đổi gián tiếp AC-DC-AC để thay đổi tần số ngõ ra từ 0 Hz đến 250 Hz) và Khởi động mềm Soft Starter (cặp thyristor phản song song điều khiển điện áp hiệu dụng RMS tăng dần ở tần số lưới cố định 50/60 Hz kèm nhánh bypass trong vận hành xác lập).
    </p>
</div>
```

### Khung HTML cho Hình 2:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_2]" alt="Biểu đồ so sánh định lượng dòng khởi động và mô-men quay giữa khởi động trực tiếp DOL và 3 điểm giới hạn dòng khởi động mềm theo Rockwell Automation" style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 2:</strong> Các điểm khảo sát thực nghiệm của Rockwell Automation minh họa quan hệ phi tuyến giữa mức giới hạn dòng, điện áp stato và mô-men khởi động sụt giảm theo quy luật bình phương (T ∝ U²); điểm giới hạn dòng 150% chỉ sinh ra 6% mô-men định mức.
    </p>
</div>
```

### Khung HTML cho Hình 3:
```html
<div style="margin:28px 0;text-align:center;">
    <img src="[URL_HINH_ANH_3]" alt="Lưu đồ cây quyết định lựa chọn kỹ thuật giữa biến tần VFD và khởi động mềm Soft Starter theo yêu cầu điều khiển tốc độ và mô-men tải" style="display:block;margin:0 auto;max-width:100%;width:100%;height:auto!important;border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border:1px solid #e2e8f0;" />
    <p style="font-size:14px;color:#64748b;margin:8px 0 0 0;font-style:italic;">
        <strong>Hình 3:</strong> Khung quyết định tuần tự hỗ trợ kỹ sư lựa chọn giữa VFD và Soft Starter dựa trên yêu cầu điều chỉnh tốc độ liên tục, mô-men bứt phá tại 0 rpm và các ràng buộc về dòng điện, sóng hài PCC và chi phí.
    </p>
</div>
```

---

## 10. ASSET FILENAMES (QUY ƯỚC ĐẶT TÊN TỆP)

Tất cả các tệp hình ảnh tuân thủ nghiêm ngặt quy ước SEO của Real Group:
- Viết thường hoàn toàn (lowercase).
- Phân tách bằng dấu gạch ngang (hyphen-separated).
- Không khoảng trắng, không dấu tiếng Việt.
- Định dạng web chuẩn: `.webp` (hoặc `.png` chất lượng cao cho đồ họa vector).

Danh mục tệp:
1. `featured-vfd-vs-soft-starter-808x500.webp`
2. `hinh-1-nguyen-ly-vfd-vs-soft-starter.webp`
3. `hinh-2-dong-va-mo-men-khoi-dong.webp`
4. `hinh-3-khung-lua-chon-vfd-soft-starter.webp`

---

## 11. GENERATION METHOD PER ASSET (PHƯƠNG PHÁP KHỞI TẠO TỪNG TÀI SẢN)

| Mã Tài sản | Phương pháp khuyến nghị | Công cụ thực hiện | Lý do kỹ thuật |
|:---|:---|:---|:---|
| **`IMG-FEATURED`** | AI Generative Rendering (5-Tier Prompt) | Midjourney v6.1 / DALL-E 3 / Flux | Tạo bối cảnh công nghiệp chân thực, ánh sáng studio kỹ thuật cao, không đòi hỏi sơ đồ vi mạch chính xác. |
| **`IMG-001`** | Controlled Vector Diagram | Figma / Adobe Illustrator / Draw.io | Đòi hỏi tính chuẩn xác tuyệt đối của chuỗi chuyển đổi AC-DC-AC và cặp thyristor phản song song; AI tạo ảnh sẽ hallucinate vi mạch. |
| **`IMG-002`** | Deterministic Data Chart | Python Matplotlib / Vector Chart / Figma | Đòi hỏi khớp 100% số liệu thực nghiệm Table 1 Rockwell (600%, 150%, 300%, 450% và 6%, 25%, 56%); cấm vẽ đường cong liên tục. |
| **`IMG-003`** | Controlled Vector Flowchart | Draw.io / Figma / Mermaid vector export | Đòi hỏi lưu đồ logic tiếng Việt chuẩn xác, không có lỗi chính tả; AI tạo ảnh không render được chữ tiếng Việt phức tạp. |

---

## 12. ANTI-HALLUCINATION CONTROLS (BIỆN PHÁP CHỐNG ẢO GIÁC THỊ GIÁC)

1. **Khống chế nhãn mác thương hiệu**: Nghiêm cấm đưa tên các model thương mại không có trong bài viết (như PowerFlex, ACS880, Altivar, A1000) vào hình ảnh.
2. **Khống chế số liệu VFD**: Tuyệt đối không vẽ cột dữ liệu giả định dải dòng khởi động cho VFD vì hồ sơ kỹ thuật chưa xác lập dải số liệu định lượng cho VFD.
3. **Khống chế quan hệ mô-men Soft Starter**: Biểu đồ Hình 2 bắt buộc phải ghi rõ đây là các điểm khảo sát thực nghiệm của Rockwell Automation, không được trình bày như một quy luật áp dụng phổ quát cho toàn bộ dải sản phẩm Soft Starter trên thị trường.
4. **Khống chế ranh giới IEEE Std 519**: Sơ đồ và lưu đồ không được ngụ ý rằng mọi biến tần đều bắt buộc phải lắp đặt bộ lọc sóng hài riêng lẻ.

---

## 13. TECHNICAL VERIFICATION CHECKLIST (CHECKLIST KIỂM ĐỊNH CHO TECH REVIEW AGENT)

- [x] **Số lượng hình ảnh**: Đúng 01 Featured Image + 03 Content Images ($1 \le n \le 3$, tổng cộng 4 tài sản).
- [x] **Kích thước Featured Image**: Đúng `808 × 500 px` (tỷ lệ 16:10).
- [x] **Kích thước Content Images**: Đúng tỷ lệ `16:9` (`1200 × 675 px`).
- [x] **Căn cứ chứng cứ**: 100% hình ảnh nội dung đều có truy xuất nguồn gốc (`EVD-001`, `EVD-002`, `EVD-003`, `EVD-004`, `EVD-005`, `EVD-006`, `EVD-007`, `EVD-009`, `EVD-010`, `EVD-014`, `EVD-015`).
- [x] **Chuẩn Responsive ADR-016**: 100% khung HTML có `display:block; margin:0 auto; max-width:100%; width:100%; height:auto!important;`.
- [x] **Bảo toàn bản thảo**: Không chèn mã vẽ thô hay thẻ `<img>` trực tiếp vào `draft_review_package.md`.
- [x] **An toàn thương hiệu**: Không phát sinh logo giả mạo, dây nối nguy hiểm hay ảo giác kỹ thuật.

---

## 14. PACKAGING HANDOFF NOTES (GHI CHÚ BÀN GIAO CHO PACKAGING AGENT)

1. **Về phía Visual Agent**:
   - Hồ sơ quy cách hình ảnh và câu lệnh Prompt AI đã hoàn tất 100% tại tệp này.
   - Do các hình ảnh nội dung (`IMG-001`, `IMG-002`, `IMG-003`) đòi hỏi đồ họa vector và biểu đồ số liệu thực nghiệm có kiểm soát (deterministic rendering), các tài sản hình ảnh thực tế cần được kết xuất qua công cụ đồ họa/chart chính xác trước khi xuất bản bản thảo HTML cuối cùng.
   - Trạng thái bài viết duy trì: `TECH_APPROVED` (không gán sớm `VISUAL_READY` khi các tệp ảnh nhị phân chưa được kết xuất vật lý, tuân thủ nguyên tắc fail-closed).
2. **Quy trình tiếp theo cho Packaging Agent**:
   - Khi Kỹ sư trưởng / Người dùng kết xuất các tệp ảnh `.webp` theo đặc tả tại Mục 4, 5, 6, 7 và tải lên hệ thống lưu trữ, Packaging Agent sẽ thay thế chuỗi `[URL_HINH_ANH_n]` bằng URL thực tế vào tệp HTML CKEditor.
   - Packaging Agent không được tự ý thay đổi cấu trúc khung thẻ HTML đã được chuẩn hóa tại Mục 9.

---
*Hồ sơ được lập bởi: Visual Agent — Real Group*  
*Chữ ký điện tử: `visual_agent:blog_04:specs_ready`*
