# Lab 02 — Quét bài toán và chọn cơ hội

**Bài làm cá nhân — Phase 1 và Phase 2**  
**Học viên:** TranAnhTu - 03368  
**Nhánh cá nhân:** `TranAnhTu-03368`

## Phase 1 — SCAN: Năm ý tưởng cá nhân

| #   | Subsidiary | Lens               | Mô tả ngắn bài toán                                                                                                                     |
| --- | ---------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | VinFast    | AI-upgrade         | Hỗ trợ chọn trạm sạc theo loại cổng của xe, mức pin và nhu cầu chuyến đi; chỉ gợi ý khi dữ liệu trụ trống và khoảng cách được xác minh. |
| 2   | VinFast    | Pain từ người khác | Phân loại mô tả lỗi xe bằng tiếng Việt đời thường để chuyển đúng kỹ thuật viên; AI không tự kết luận xe có an toàn để chạy hay không.   |
| 3   | Vinhomes   | Lặp lại            | Soạn nháp hướng dẫn thủ tục thi công nội thất theo khu/tòa và hỏi giấy tờ còn thiếu; người phụ trách vẫn duyệt hồ sơ.                   |
| 4   | Vinpearl   | Pain từ người khác | Gom các đánh giá khách sạn theo chủ đề và mức cần phản hồi; nhân viên kiểm tra nội dung gốc trước khi gửi phản hồi công khai.           |
| 5   | Vinpearl   | Tốn thời gian      | Trích ngày, số khách, loại phòng và yêu cầu đặc biệt từ email đặt phòng đoàn; nhân viên xác minh tồn phòng và giá trước khi báo khách.  |

## Phase 2 — QUICK-ASSESS: Ba Quick Problem Cards được chọn

### Card #2 — VinFast: Phân loại mô tả lỗi xe

```text
┌────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                          │
│                                                                │
│ Bài toán: Phân loại mô tả lỗi xe bằng tiếng Việt đời thường    │
│           để chuyển đúng kỹ thuật viên.                        │
│ Công ty thành viên: [x] VinFast                                │
│                                                                │
│ Ai đang đau? Chủ xe; nhân viên CSKH/điều phối; kỹ thuật viên.  │
│                                                                │
│ Workflow thủ công hiện tại (5 bước, giả định):                 │
│   1. Chủ xe gọi/nhắn mô tả lỗi                                 │
│   → 2. CSKH ghi mô tả vào phiếu                                │
│   → 3. CSKH tự phân nhóm lỗi                                   │
│   → 4. Chuyển phiếu cho kỹ thuật viên/xưởng                    │
│   → 5. Nếu sai chuyên môn thì chuyển lại, hỏi thêm             │
│                                                                │
│ Bước nào tốn nhất? Bước 3 và 5; chưa đo thời gian thực.        │
│ AI hỗ trợ ở đâu? Bước 3: gợi ý nhóm lỗi, câu hỏi làm rõ.       │
│ Nhân viên xác nhận trước khi chuyển phiếu.                     │
│                                                                │
│ Đo thành công bằng gì? Giả định: chuyển đúng lần đầu           │
│ từ ~70% lên ≥90%; số phiếu chuyển lại giảm 50%.                │
│ Cần đo baseline thực tế trước khi thử nghiệm.                  │
│                                                                │
│ Quick Architecture: [x] LLM Feature + Rule.                    │
│ Ranh giới: AI không kết luận xe có an toàn để chạy;            │
│ người có chuyên môn quyết định.                                │
└────────────────────────────────────────────────────────────────┘
```

### Card #3 — Vinhomes: Hướng dẫn thủ tục thi công nội thất

```text
┌────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                          │
│                                                                │
│ Bài toán: Soạn nháp hướng dẫn thủ tục thi công nội thất        │
│           theo khu/tòa và hỏi giấy tờ còn thiếu.               │
│ Công ty thành viên: [x] Vinhomes                               │
│                                                                │
│ Ai đang đau? Cư dân/nhà thầu; nhân viên ban quản lý.           │
│                                                                │
│ Workflow thủ công hiện tại (5 bước, giả định):                 │
│   1. Cư dân/nhà thầu hỏi thủ tục                               │
│   → 2. Nhân viên xác định khu/tòa, quy định áp dụng            │
│   → 3. Soạn danh sách giấy tờ, lịch và quy định                │
│   → 4. Kiểm tra hồ sơ, nhắn bổ sung giấy tờ                    │
│   → 5. Người phụ trách duyệt hồ sơ                             │
│                                                                │
│ Bước nào tốn nhất? Bước 3–4 (~20 phút/hồ sơ, giả định).        │
│ AI hỗ trợ ở đâu? Bước 3–4: tra quy định đã duyệt,              │
│ soạn nháp hướng dẫn và liệt kê giấy tờ thiếu.                  │
│                                                                │
│ Đo thành công bằng gì? Giả định: ~20 → <5 phút/hồ sơ;          │
│ số lần bổ sung hồ sơ từ ~3 xuống ≤1 lần.                       │
│ Cần đo baseline thực tế trước khi thử nghiệm.                  │
│                                                                │
│ Quick Architecture: [x] LLM Feature + Rule/RAG.                │
│ Ranh giới: thiếu căn cứ thì chuyển nhân viên;                  │
│ người phụ trách duyệt, AI không tự phê duyệt.                  │
└────────────────────────────────────────────────────────────────┘
```

### Card #5 — Vinpearl: Trích yêu cầu đặt phòng đoàn

```text
┌────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                          │
│                                                                │
│ Bài toán: Trích ngày, số khách, loại phòng và yêu cầu          │
│           đặc biệt từ email đặt phòng đoàn.                    │
│ Công ty thành viên: [x] Vinpearl                               │
│                                                                │
│ Ai đang đau? Nhân viên đặt phòng đoàn; đối tác/khách đoàn.     │
│                                                                │
│ Workflow thủ công hiện tại (5 bước, giả định):                 │
│   1. Nhận email yêu cầu                                        │
│   → 2. Đọc và tìm các trường thông tin                         │
│   → 3. Nhập tay vào hệ thống/bảng theo dõi                     │
│   → 4. Kiểm tra tồn phòng và giá                               │
│   → 5. Soạn phản hồi để nhân viên duyệt, gửi                   │
│                                                                │
│ Bước nào tốn nhất? Bước 2–3 (10–15 phút/email, giả định).      │
│ AI hỗ trợ ở đâu? Bước 2–3: trích trường có cấu trúc,           │
│ đánh dấu thông tin thiếu/mâu thuẫn để nhân viên xác nhận.      │
│                                                                │
│ Đo thành công bằng gì? Giả định: ~12 → <2 phút/email;          │
│ độ chính xác trường chính ≥95% trên tập gắn nhãn.              │
│ Cần đo baseline thực tế trước khi thử nghiệm.                  │
│                                                                │
│ Quick Architecture: [x] LLM Feature + Rule.                    │
│ Ranh giới: nhân viên xác minh tồn phòng và giá;                │
│ AI không tự báo giá hoặc xác nhận đặt phòng.                   │
└────────────────────────────────────────────────────────────────┘
```

