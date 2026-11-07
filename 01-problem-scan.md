# Lab 02 — Quét bài toán và chọn cơ hội

**Bài làm cá nhân — Phase 1 và Phase 2**

- **Học viên:** Nguyễn Thị Hồng Hạnh - 2A202603537
- **Nhánh cá nhân:** NguyenThiHongHanh_03537

## Phase 1 — SCAN: Năm ý tưởng cá nhân

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | AI-upgrade | Đọc tin nhắn của tài xế báo pin yếu, trích mức pin và vị trí để soạn nháp phương án hỗ trợ cho điều phối viên. |
| 2 | VinFast | Pain từ người khác | Phân loại mô tả lỗi xe từ khách hàng để chuyển yêu cầu đến đúng nhóm kỹ thuật. |
| 3 | Vinhomes | Lặp lại | Đọc yêu cầu sửa chữa của cư dân, nhận diện căn hộ và nhóm sự cố để tạo phiếu xử lý. |
| 4 | Vinmec | Tốn thời gian | Tổng hợp các lịch khám bị dời và soạn nháp thông báo để nhân viên xác nhận trước khi gửi. |
| 5 | Vingroup | Lặp lại | Trợ lý onboarding cho nhân sự mới. Nhân viên thường phải hỏi HR hoặc đồng nghiệp về cách xin cấp tài khoản, đăng ký thiết bị và tìm tài liệu đào tạo. LLM trả lời dựa trên tài liệu nội bộ đã duyệt, dẫn nguồn và chuyển cho HR khi thiếu thông tin. |

## Phase 2 — QUICK-ASSESS: Ba Quick Problem Cards được chọn

Các workflow là giả định cần xác minh. Các con số là mục tiêu
thử nghiệm và cần được đối chiếu với số liệu ban đầu.

### Card #1 — Xanh SM: Hỗ trợ điều phối khi xe báo pin yếu

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1
│
│ Bài toán (1 câu): Rút ngắn thời gian từ lúc tài xế báo pin yếu
│ đến lúc điều phối viên có phương án hỗ trợ để duyệt.
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
│                    [ ] Vinmec   [ ] Khác
│
│ Ai đang đau (Actor)? Tài xế phải chờ phản hồi. Điều phối viên
│ phải đọc tin nhắn, hỏi lại thông tin và soạn phương án.
│
│ Workflow thủ công hiện tại (giả định):
│    1. Nhận tin tài xế báo pin yếu
│ -> 2. Xác nhận mức pin và vị trí
│ -> 3. Kiểm tra quy tắc xử lý
│ -> 4. Soạn phương án hỗ trợ
│ -> 5. Điều phối viên duyệt và thực hiện
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–4, nhất là khi
│ tin nhắn thiếu mức pin hoặc vị trí.
│ AI hỗ trợ ở bước nào? Bước 2 và 4. Trích thông tin, nêu
│ dữ liệu cần bổ sung và soạn nháp cho điều phối viên.
│
│ Đo thành công bằng gì (Metric có số)?
│ - Giảm 30% thời gian trung vị từ lúc nhận tin đến khi
│   có bản nháp hợp lệ so với số liệu ban đầu.
│ - 100% ca pin dưới 5% trong tập kiểm thử trả về
│   hành động `dispatch_mobile_charger`.
│
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
│ LLM trích thông tin và soạn nháp. Rule kiểm tra ngưỡng pin
│ và định dạng phản hồi.
│
│ Ranh giới: Mọi phản hồi bắt đầu bằng [DRAFT_ONLY]. Khi pin
│ dưới 5%, đề xuất điều xe sạc di động và không chỉ đường đến
│ trạm sạc. Điều phối viên duyệt trước khi gửi tin hoặc điều xe.
└──────────────────────────────────────────────────────────────────────────┘
```

### Card #2 — Vingroup: Trợ lý onboarding cho nhân sự mới

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2
│
│ Bài toán (1 câu): Giúp nhân sự mới tìm nhanh hướng dẫn về
│ tài khoản, thiết bị và đào tạo bắt buộc trong quá trình onboarding.
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes
│                    [ ] Vinmec   [x] Khác (Vingroup)
│
│ Ai đang đau (Actor)? Nhân sự mới mất thời gian tìm tài liệu.
│ HR, IT và Hành chính phải trả lời nhiều câu hỏi lặp lại.
│
│ Workflow thủ công hiện tại (giả định):
│    1. Nhân sự mới phát sinh câu hỏi
│ -> 2. Tìm trong email, tài liệu hoặc nhóm chat
│ -> 3. Hỏi bộ phận phụ trách nếu chưa tìm được
│ -> 4. Bộ phận phụ trách tìm và gửi hướng dẫn phù hợp
│ -> 5. Nhân sự mới thực hiện theo hướng dẫn
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–4 khi tài liệu
│ nằm ở nhiều nơi hoặc quy trình khác nhau theo đơn vị.
│ AI hỗ trợ ở bước nào? Bước 2–4. Tra tài liệu đã duyệt,
│ trả lời theo từng bước, dẫn nguồn và hỏi thêm khi cần.
│
│ Đo thành công bằng gì (Metric có số)?
│ - Giảm 30% thời gian trung vị từ lúc đặt câu hỏi đến khi
│   nhận được hướng dẫn đúng so với số liệu ban đầu.
│ - Ít nhất 90% câu trả lời đúng và có nguồn phù hợp trên
│   bộ câu hỏi kiểm thử do HR xác nhận.
│
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
│ RAG truy xuất tài liệu theo quyền truy cập. LLM tổng hợp
│ hướng dẫn và đính kèm nguồn.
│
│ Ranh giới: Chỉ dùng tài liệu đã duyệt mà nhân viên được
│ phép xem. Thiếu nguồn hoặc tài liệu mâu thuẫn thì chuyển
│ bộ phận phụ trách. Việc cấp quyền và phê duyệt do người
│ có thẩm quyền thực hiện.
└──────────────────────────────────────────────────────────────────────────┘
```

### Card #3 — Vinhomes: Phân loại yêu cầu sửa chữa của cư dân

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3
│
│ Bài toán (1 câu): Giảm thời gian đọc và nhập tay yêu cầu
│ sửa chữa của cư dân từ nhiều kênh.
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes
│                    [ ] Vinmec   [ ] Khác
│
│ Ai đang đau (Actor)? Cư dân chờ xử lý. Ban quản lý nhập
│ phiếu thủ công và đội bảo trì có thể nhận nhầm yêu cầu.
│
│ Workflow thủ công hiện tại (giả định):
│    1. Nhận yêu cầu từ cư dân
│ -> 2. Xác định tòa và căn hộ
│ -> 3. Phân loại nhóm sự cố
│ -> 4. Nhập phiếu xử lý
│ -> 5. Chuyển phiếu cho đội bảo trì
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–4, đặc biệt khi
│ yêu cầu viết tự do hoặc thiếu thông tin căn hộ.
│ AI hỗ trợ ở bước nào? Bước 2–4. Trích thông tin căn hộ,
│ tóm tắt sự cố, đề xuất đội bảo trì và đánh dấu trường thiếu.
│
│ Đo thành công bằng gì (Metric có số)?
│ - Giảm 30% thời gian trung vị để tạo phiếu đủ thông tin
│   so với số liệu ban đầu.
│ - Theo dõi tỷ lệ phiếu chuyển đúng nhóm ngay lần đầu.
│
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
│ LLM trích và phân loại nội dung. Rule kiểm tra các trường
│ bắt buộc trước khi chuyển phiếu.
│
│ Ranh giới: Ban quản lý xác nhận mức ưu tiên và đội xử lý
│ trước khi giao việc.
└──────────────────────────────────────────────────────────────────────────┘
```