# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | Lặp lại | Nhân viên đọc mô tả lỗi của khách để phân loại ticket bảo hành/dịch vụ và chuyển đúng xưởng hoặc bộ phận. |
| 2 | **Xanh SM** | AI-upgrade | Kiểm tra hồ sơ onboarding tài xế, tự duyệt hồ sơ rõ ràng và chuyển người duyệt các ca mờ hoặc nghi giả mạo. |
| 3 | **Vinpearl** | Pain từ người khác | Nhân viên đọc review, email, tin nhắn đa kênh rồi phân loại, đánh giá mức độ nghiêm trọng và soạn phản hồi. |
| 4 | **Xanh SM** | AI-upgrade | Hỏi đáp chính sách cho tài xế (Bike, Car, Premium, Limo) vì quy định đổi liên tục, nằm rải rác và hotline dễ trả lời khác nhau giữa các ca. |
| 5 | **VinFast / V-Green** | Lặp lại | Phân loại sự cố trạm sạc từ log thiết bị và phản ánh người dùng để định tuyến đúng đội kỹ thuật. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```text
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                              │
│ Bài toán (1 câu): Tự động phân loại ticket bảo hành/dịch vụ  │
│   từ mô tả lỗi của khách và chuyển đúng xưởng/bộ phận.       │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác: ____________      │
│                                                              │
│ Ai đang đau (Actor)? Nhân viên tiếp nhận ticket bảo hành/    │
│   CSKH (đọc và phân loại thủ công); xưởng dịch vụ            │
│   (nhận ticket sai).                                         │
│                                                              │
│ Workflow thủ công hiện tại:                                  │
│   1. Khách gửi mô tả lỗi (app/hotline/xưởng)                 │
│   ──> 2. Nhân viên đọc, hiểu mô tả                           │
│   ──> 3. Phân loại nhóm lỗi + mức độ ưu tiên                 │
│   ──> 4. Chuyển đúng xưởng/bộ phận                           │
│   ──> 5. Xưởng nhận; nếu sai thì trả lại, chuyển lại         │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3: đọc và phân loại  │
│   (⏱ ~3-5 phút/ticket, giả định)                            
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: đọc mô tả,   │
│   gán nhóm lỗi + mức độ, gợi ý nơi chuyển.                   │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Thời gian phân loại: ~4 min ──> under 30 giây/ticket     │
│   - Độ chính xác định tuyến: >= 90%                          │
│   - Tỷ lệ ticket bị chuyển lại: ~15% ──> under 5% (giả định) │
│                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent  │
│   (LLM phân loại; rule cho định tuyến; ca độ tin cậy thấp    │
│    chuyển nhân viên duyệt)                                   │
└──────────────────────────────────────────────────────────────┘
```

```text
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                              │
│ Bài toán (1 câu): Phân loại, đánh giá mức độ nghiêm trọng    │
│   và soạn nháp phản hồi cho review/email/tin nhắn đa kênh.   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [x] Khác: Vinpearl          │
│                                                              │
│ Ai đang đau (Actor)? Nhân viên CSKH/quản lý trải nghiệm      │
│   khách hàng tại các cơ sở; khách đang chờ phản hồi.         │
│                                                              │
│ Workflow thủ công hiện tại:                                  │
│   1. Thu thập review (Google, Booking, TripAdvisor), email,  │
│      tin nhắn                                                │
│   ──> 2. Đọc và xác định chủ đề (phòng, ăn uống, dịch vụ)    │
│   ──> 3. Đánh giá cảm xúc + mức độ nghiêm trọng              │
│   ──> 4. Soạn phản hồi, gửi/chuyển bộ phận liên quan         │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4: đọc và soạn       │
│   phản hồi (⏱ ~5 phút/lượt; 10.000 lượt/tháng ≈ 830         
│   giờ/tháng, giả định)                                       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: phân loại    │
│   chủ đề/cảm xúc, cảnh báo ca nghiêm trọng, soạn nháp.       │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Thời gian xử lý: 5 min ──> under 2 min/lượt              │
│     (tiết kiệm ~500 giờ/tháng)                               │
│   - Ca nghiêm trọng được cảnh báo: under 1 giờ               │
│   - Tỷ lệ nháp được duyệt gần như không sửa: >= 70%          │
│                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent  │
│   (LLM phân loại + soạn nháp; người duyệt trước khi gửi)     │
└──────────────────────────────────────────────────────────────┘
```

```text
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                              │
│ Bài toán (1 câu): Trợ lý hỏi đáp chính sách cho tài xế       │
│   Xanh SM, trả lời nhất quán, đúng dịch vụ và đúng           │
│   thời điểm hiệu lực.                                        │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác: ____________      │
│                                                              │
│ Ai đang đau (Actor)? Tài xế (~300.000 người, hỏi hotline)    │
│   và nhân viên hotline (phải tra cứu, dễ trả lời lệch nhau). │
│                                                              │
│ Workflow thủ công hiện tại:                                  │
│   1. Tài xế gọi hotline hỏi quy định (phạt, thưởng,          │
│      thu nhập...)                                            │
│   ──> 2. Nhân viên tra cứu nhiều bản tin vận hành/thông báo  │
│   ──> 3. Đối chiếu dịch vụ (Bike/Car/Premium/Limo) +         │
│          ngày hiệu lực                                       │
│   ──> 4. Trả lời; câu trả lời có thể khác nhau giữa các ca   │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3: tra cứu và đối    │
│  chiếu quy định rải rác (⏱ ~5-7 phút/cuộc, giả định)                
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: truy xuất    │
│   đúng quy định, trả lời kèm trích nguồn và ngày hiệu lực.   │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Thời gian xử lý cuộc hỏi chính sách: ~6 min ──> <2 min   │
│   - Nhất quán giữa các lần hỏi: >= 95%                       │
│   - Tài xế tự giải quyết qua chatbot (không gọi): >= 40%     │
│                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent  │
│   (LLM + truy xuất tài liệu có version; câu hỏi mơ hồ        │
│    chuyển nhân viên)                                         │
└──────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---