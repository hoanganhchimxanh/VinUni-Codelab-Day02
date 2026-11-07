# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 📝 List bài toán của tôi:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | Tốn thời gian & Lặp lại | Dự báo và tối ưu tồn kho linh kiện/phụ tùng xe điện: kỹ sư và đội supply chain phải đối chiếu dữ liệu sản xuất, chuỗi cung ứng và lịch bảo dưỡng thủ công bằng Excel, dẫn đến dư thừa linh kiện chậm luân chuyển hoặc thiếu hụt phụ tùng thay thế, gây thất thoát chi phí lưu kho hàng triệu USD/năm. |
| 2 | **Vinhomes** | Pain từ người khác & Lặp lại | Tự động hóa xử lý sự cố & khiếu nại của cư dân qua App/Hotline: cư dân thường xuyên gặp tình trạng phản hồi chậm khi báo cáo sự cố kỹ thuật (điện, nước, thang máy) hoặc phí dịch vụ. Tổng đài viên và ban quản lý quá tải vào giờ cao điểm, gây sụt giảm CSAT và tăng chi phí nhân sự vận hành. |
| 3 | **Vinmec** | AI có thể tốt hơn & Tốn thời gian | Trợ lý ảo tổng hợp bệnh án & tối ưu lịch hẹn bác sĩ thông minh: bác sĩ mất nhiều thời gian đọc lại hàng chục trang bệnh án cũ để tìm điểm bất thường trước khi khám. Việc xếp lịch thủ công gây ùn tắc tại phòng khám và lãng quên các khung giờ trống của thiết bị y tế chuyên sâu. |
| 4 | **Vinpearl** | AI có thể tốt hơn & Lặp lại | Hệ thống định giá động (Dynamic Pricing) phòng khách sạn & dịch vụ: đội Revenue Management điều chỉnh giá phòng và dịch vụ vui chơi dựa trên kinh nghiệm và dữ liệu lịch sử thô, bỏ lỡ doanh thu tiềm năng trong các khung giờ vàng/thấp điểm do thiếu mô hình dự báo thời gian thực theo biến động thị trường. |
| 5 | **Vinschool** | Tốn thời gian & Lặp lại | Chấm bài tự luận hỗ trợ giáo viên & phân tích lộ trình học tập cá nhân: giáo viên tốn quá nhiều thời gian cho công việc hành chính, chấm bài tập và tổng hợp điểm số, khiến thời gian tương tác 1-1 với học sinh bị thu hẹp và khó phát hiện sớm học sinh gặp khó khăn trong tiếp thu kiến thức. |

> **Ghi chú lựa chọn:** Top 3 bài toán phù hợp để làm Quick Card và chuyển sang Prompt Prototype (task ngôn ngữ / LLM) là **#2 (Vinhomes)**, **#3 (Vinmec)**, **#5 (Vinschool)**. Hai bài **#1 (VinFast)** và **#4 (Vinpearl)** là bài toán dự báo/tối ưu số liệu (ML/forecasting), vẫn giữ trong bảng SCAN nhưng không phù hợp để xây dựng prompt prototype LLM.

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 bài toán: **#2 (Vinhomes)**, **#3 (Vinmec)**, **#5 (Vinschool)**.

## 🃏 QUICK PROBLEM CARD #2 — Vinhomes

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại & điều hướng phản ánh   │
│ sự cố/khiếu nại của cư dân qua App/Hotline tới đúng bộ phận │
│ và draft phản hồi cho tổng đài viên duyệt.                  │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (chờ lâu), Tổng đài viên (quá   │
│ tải giờ cao điểm), Ban quản lý tòa nhà (nghẽn handoff).     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân gửi sự cố qua App Vinhomes Resident / Hotline   │
│   → 2. Tổng đài viên đọc & phân loại thủ công (điện/nước/   │
│        thang máy/phí dịch vụ)                               │
│   → 3. Chuyển tay cho đúng Ban quản lý / tổ kỹ thuật tòa    │
│   → 4. BQL xử lý & soạn phản hồi                            │
│   → 5. Gửi lại cư dân & đóng ticket                         │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4 (⏱ ~12 phút/lượt, │
│ thời gian phản hồi thực tế tới ~12 giờ) 🔴                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (phân loại + route tự động) và draft phản hồi ở bước 4.     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian phản hồi từ 12 giờ ──> dưới 2 giờ.       │
│   - Phân loại đúng >90% ticket dưới 5 giây.                 │
│   - Giảm 40% khối lượng xử lý thủ công của tổng đài.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature (classify + route +      │
│ draft), Rule-based router làm fallback. HITL bắt buộc duyệt. │
└─────────────────────────────────────────────────────────────┘
```

## 🃏 QUICK PROBLEM CARD #3 — Vinmec

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý AI tóm tắt bệnh án cũ & highlight  │
│ điểm bất thường trước khi khám, đồng thời gợi ý lịch hẹn    │
│ tối ưu theo khung giờ thiết bị y tế còn trống.              │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ (quá tải đọc hồ sơ), lễ tân/    │
│ điều dưỡng (xếp lịch thủ công), bệnh nhân (chờ lâu).        │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ mở bệnh án điện tử (nhiều chục trang)           │
│   → 2. Đọc thủ công tìm tiền sử, xét nghiệm cũ, bất thường  │
│   → 3. Tự tổng hợp ghi chú trước khám                       │
│   → 4. Khám & ghi nhận kết quả                              │
│   → 5. Lễ tân xếp lịch thủ công, dễ bỏ sót giờ thiết bị     │
│        chuyên sâu còn trống                                 │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 20-30 phút/    │
│ bệnh nhân) 🔴                                               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tóm tắt +   │
│ highlight) và bước 5 (gợi ý khung giờ trống).               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian đọc hồ sơ từ 25 phút ──> dưới 5 phút.    │
│   - 100% tóm tắt phải có bác sĩ duyệt (HITL).               │
│   - Tăng tỉ lệ sử dụng thiết bị y tế thêm 15%.              │
│                                                             │
│ Quick Architecture: [x] LLM Feature + RAG trên bệnh án,      │
│ HITL bắt buộc. CẤM chẩn đoán/kê đơn, chỉ tóm tắt.           │
└─────────────────────────────────────────────────────────────┘
```

## 🃏 QUICK PROBLEM CARD #5 — Vinschool

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                       │
│                                                             │
│ Bài toán (1 câu): AI draft nhận xét & gợi ý điểm bài tự luận │
│ theo rubric, đồng thời phân tích lỗi để giáo viên phát hiện  │
│ sớm học sinh gặp khó khăn.                                   │
│ Công ty thành viên: [x] Vinschool                           │
│                                                             │
│ Ai đang đau (Actor)? Giáo viên (quá tải chấm bài & hành     │
│ chính), học sinh (thiếu phản hồi cá nhân hóa kịp thời).     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Thu bài tự luận (online/giấy)                          │
│   → 2. Đọc & chấm thủ công theo rubric                      │
│   → 3. Nhập điểm vào Excel                                  │
│   → 4. Tổng hợp điểm & thống kê lớp                         │
│   → 5. Viết nhận xét riêng cho từng học sinh                │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 8-10 phút/bài, │
│ lớp 40 bài ~ 6 giờ) 🔴                                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (draft nhận    │
│ xét + gợi ý điểm theo rubric) và bước 5 (nhận xét cá nhân). │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian chấm từ 10 phút ──> dưới 3 phút/bài.     │
│   - 100% điểm cuối do giáo viên duyệt (HITL).               │
│   - ≥85% nhận xét do AI draft được giáo viên dùng/chỉnh nhẹ.│
│                                                             │
│ Quick Architecture: [x] LLM Feature + rubric-based scoring,  │
│ HITL bắt buộc. CẤM tự công bố điểm, không thay giáo viên.   │
└─────────────────────────────────────────────────────────────┘
```
