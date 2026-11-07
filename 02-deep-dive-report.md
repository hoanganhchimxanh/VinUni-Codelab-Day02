# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
```text
┌──────────────────────────────────────────────┐
│ BƯỚC 1: THU THẬP                             │
│                                              │
│ Nhân viên mở từng kênh riêng lẻ (Google,     │
│ Booking, TripAdvisor, email, tin nhắn) để    │
│ lấy review/phản ánh mới.                     │
│                                              │
│ ⏱ ~0,5 phút                                  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 🔴 BƯỚC 2: ĐỌC VÀ XÁC ĐỊNH CHỦ ĐỀ            │
│                                              │
│ (Phòng, ăn uống, dịch vụ...) - đọc từng      │
│ nội dung, nhiều văn phong, nhiều ngôn ngữ.   │
│                                              │
│ ⏱ ~1,5 phút                                  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 🔴 BƯỚC 3: ĐÁNH GIÁ CẢM XÚC VÀ MỨC ĐỘ        │
│ NGHIÊM TRỌNG                                 │
│                                              │
│ Dựa vào cảm tính, dễ bỏ sót ca nghiêm trọng. │
│                                              │
│ ⏱ ~1 phút                                    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 🔴 BƯỚC 4a: SOẠN PHẢN HỒI                    │
│                                              │
│ Viết thủ công, phải phù hợp từng kênh và     │
│ văn phong.                                   │
│                                              │
│ ⏱ ~2 phút                                    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 🔄 BƯỚC 4b: GỬI PHẢN HỒI / CHUYỂN BỘ PHẬN   │
│                                              │
│ Chuyển thông tin qua email, tin nhắn, Excel  │
│ đến bộ phận liên quan (buồng phòng, F&B,     │
│ an ninh...).                                 │
│                                              │
│ ⏱ ~0 phút (đã tính vào bước 4a)             │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ HOÀN TẤT                                     │
│                                              │
│ Gửi phản hồi cho khách, bộ phận liên quan    │
│ tiếp nhận và xử lý.                          │
└──────────────────────────────────────────────┘
```

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Bài toán được chọn: 3. Nhân viên đọc review, email, tin nhắn đa kênh rồi phân loại, đánh giá mức độ nghiêm trọng và soạn phản hồi.
| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên CSKH và quản lý trải nghiệm khách hàng tại các cơ sở Vinpearl (resort, khách sạn, khu vui chơi). Khách hàng đang chờ phản hồi chịu ảnh hưởng gián tiếp. |
| **2. Current Workflow** | Khi có review, email hoặc tin nhắn mới, nhân viên mở từng kênh riêng lẻ (Google, Booking, TripAdvisor, email, tin nhắn) để thu thập, đọc và xác định chủ đề (phòng, ăn uống, dịch vụ), đánh giá cảm xúc và mức độ nghiêm trọng, rồi soạn phản hồi và gửi hoặc chuyển bộ phận liên quan. 4 bước, hoàn toàn thủ công, mất ~5 phút/lượt. |
| **3. Bottleneck** | Bước 2-4 (mất ~5 phút): đọc, phân loại chủ đề/cảm xúc/mức độ nghiêm trọng và soạn phản hồi phù hợp với từng kênh và văn phong. Ca nghiêm trọng (an toàn, vệ sinh, thái độ nhân viên) dễ bị chìm trong khối lượng lớn nên phát hiện và xử lý chậm. |
| **4. Business Impact** | Khoảng 10.000 lượt/tháng (giả định). Gây lãng phí ~830 giờ công/tháng của đội CSKH. Phản hồi chậm làm giảm điểm đánh giá trên các nền tảng, ca nghiêm trọng xử lý trễ có nguy cơ thành khủng hoảng truyền thông, chất lượng phản hồi không đồng đều giữa các cơ sở. |
| **5. Success Metric** | 1. Giảm thời gian xử lý từ 5 phút xuống dưới 2 phút/lượt, tiết kiệm ~500 giờ/tháng (Efficiency).<br>2. Ca nghiêm trọng được cảnh báo trong dưới 1 giờ (SLA).<br>3. Tỉ lệ bản nháp được duyệt gần như không cần sửa đạt ≥ 70% (Quality). |
| **6. Operational Boundary** | AI được phép phân loại chủ đề, đánh giá cảm xúc và mức độ nghiêm trọng, cảnh báo ca nghiêm trọng, gợi ý bộ phận cần chuyển và soạn nháp phản hồi (draft). **CẤM:** AI không được tự động gửi phản hồi cho khách mà không có người phê duyệt (Bắt buộc HITL); không được hứa hẹn bồi thường, hoàn tiền, giảm giá hoặc nhận lỗi thay công ty; không được tiết lộ thông tin cá nhân của khách hay nhân viên. Ca nghiêm trọng hoặc độ tin cậy thấp bắt buộc chuyển cho quản lý xử lý. |



## 3.3. Future-State Flow & AI Fit (25 min)

**Lý do chọn LLM Feature:** Bài toán chủ yếu là đọc hiểu và viết văn bản tự do, nên cần LLM. Rule/State-Machine không đủ linh hoạt vì mỗi review, email, tin nhắn một kiểu. Agentic Loop thì không cần, vì quy trình chỉ đi một chiều (phân loại, soạn nháp, người duyệt), AI không phải tự lập kế hoạch hay gọi nhiều công cụ.

* **Quy trình tương lai (Future-State-Flow):**
```text
┌──────────────────────────────────────────────────────────┐
│ Review (Google, Booking, TripAdvisor), email, tin nhắn   │
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ ⚙️ Gom về một hộp thư tập trung (tự động, không dùng AI) │
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ 🔵 AI Step 1: Phân loại chủ đề, cảm xúc, mức độ          │
│    nghiêm trọng, ngôn ngữ                                │
└────────────────────────────┬─────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
┌───────────────────────────┐ ┌───────────────────────────┐
│ Ca nghiêm trọng hoặc      │ │ Ca thông thường           │
│ độ tin cậy thấp           │ │ (độ tin cậy đủ cao)       │
└─────────────┬─────────────┘ └─────────────┬─────────────┘
              ▼                             ▼
┌───────────────────────────┐ ┌───────────────────────────┐
│ 🟢 Human Step A:          │ │ 🔵 AI Step 2: Soạn nháp   │
│ Cảnh báo quản lý xử lý    │ │ phản hồi theo chủ đề,     │
│ trực tiếp (< 1 giờ)       │ │ ngôn ngữ, văn phong       │
│                           │ │ Vinpearl + gợi ý bộ phận  │
│                           │ │ cần chuyển                │
└─────────────┬─────────────┘ └─────────────┬─────────────┘
              │                             ▼
              │               ┌───────────────────────────┐
              │               │ 🟢 Human Step B (HITL):   │
              │               │ Nhân viên CSKH duyệt /    │
              │               │ sửa / từ chối nháp        │
              │               └─────────────┬─────────────┘
              └──────────────┬──────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Gửi phản hồi cho khách + chuyển bộ phận liên quan        │
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Ghi nhận chỉnh sửa của nhân viên để đo chất lượng        │
│ (tỉ lệ nháp được duyệt không cần sửa)                    │
└──────────────────────────────────────────────────────────┘
```