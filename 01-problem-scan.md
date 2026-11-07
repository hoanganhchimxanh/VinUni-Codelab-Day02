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

### Card #1 — Xanh SM: Hỗ trợ điều phối khi xe báo pin yếu

- **Bài toán:** Rút ngắn thời gian từ lúc tài xế báo pin yếu đến lúc điều phối viên có phương án để duyệt.
- **Ai đang đau?** Tài xế cần phản hồi nhanh. Điều phối viên phải đọc tin nhắn, hỏi lại và soạn phản hồi.
- **Workflow thủ công giả định:** (1) Nhận tin báo → (2) hỏi mức pin và vị trí → (3) kiểm tra quy tắc xử lý → (4) soạn phương án → (5) điều phối viên duyệt và thực hiện.
- **Bước nào tốn nhất?** Bước 2–4, đặc biệt khi tin nhắn thiếu mức pin hoặc vị trí. Cần đo thời gian thực tế.
- **AI hỗ trợ ở đâu?** Trích mức pin và vị trí từ tin nhắn tự do, hỏi thêm khi thiếu dữ liệu và soạn nháp cho điều phối viên.
- **Đo thành công bằng gì?** Đo thời gian trung vị từ lúc nhận tin đến lúc có bản nháp hợp lệ. Mục tiêu thử nghiệm là giảm 30% so với baseline. Mọi ca pin dưới 5% trong tập kiểm thử phải trả về `dispatch_mobile_charger`.
- **Quick Architecture:** LLM Feature + Rule. LLM đọc tin nhắn và soạn nháp. Rule kiểm tra ngưỡng pin và định dạng đầu ra.
- **Ranh giới:** Phản hồi bắt đầu bằng `[DRAFT_ONLY]`. Pin dưới 5% thì đề xuất điều xe sạc di động và không hướng dẫn tài xế đến trạm sạc. Điều phối viên duyệt trước khi gửi tin hoặc điều xe.

### Card #2 — VinFast: Chuyển yêu cầu đến đúng nhóm kỹ thuật

- **Bài toán:** Giảm số phiếu hỗ trợ phải chuyển lại vì phân sai nhóm lỗi.
- **Ai đang đau?** Chủ xe, nhân viên CSKH và kỹ thuật viên.
- **Workflow thủ công giả định:** (1) Nhận mô tả lỗi → (2) ghi phiếu → (3) phân nhóm lỗi → (4) chuyển cho kỹ thuật viên → (5) chuyển lại nếu sai nhóm.
- **Bước nào tốn nhất?** Bước 3 và 5. Cần đo thời gian phân loại và số lần chuyển lại.
- **AI hỗ trợ ở đâu?** Đề xuất nhóm lỗi từ mô tả tiếng Việt tự do và gợi ý câu hỏi làm rõ.
- **Đo thành công bằng gì?** Tỷ lệ phiếu chuyển đúng nhóm ngay lần đầu, do nhóm kỹ thuật xác nhận. Mục tiêu thử nghiệm là đạt ít nhất 90% sau khi đo baseline.
- **Quick Architecture:** LLM Feature + Rule. AI chọn nhóm từ danh mục có sẵn.
- **Ranh giới:** Nhân viên xác nhận nhóm trước khi chuyển. Kỹ thuật viên quyết định xe có thể tiếp tục vận hành hay không.

### Card #3 — Vinhomes: Phân loại yêu cầu sửa chữa của cư dân

- **Bài toán:** Giảm thời gian đọc và nhập tay yêu cầu sửa chữa từ nhiều kênh.
- **Ai đang đau?** Cư dân, nhân viên ban quản lý và đội bảo trì.
- **Workflow thủ công giả định:** (1) Nhận yêu cầu → (2) xác định tòa và căn hộ → (3) phân nhóm sự cố → (4) nhập phiếu → (5) chuyển đội bảo trì.
- **Bước nào tốn nhất?** Bước 2–4 khi yêu cầu viết tự do hoặc thiếu thông tin.
- **AI hỗ trợ ở đâu?** Trích thông tin căn hộ, tóm tắt sự cố, đề xuất nhóm bảo trì và đánh dấu trường còn thiếu.
- **Đo thành công bằng gì?** Đo thời gian trung vị để tạo phiếu đủ thông tin. Mục tiêu thử nghiệm là giảm 30% so với baseline.
- **Quick Architecture:** LLM Feature + Rule. Rule kiểm tra các trường bắt buộc trước khi chuyển phiếu.
- **Ranh giới:** Ban quản lý xác nhận mức ưu tiên và đội xử lý trước khi giao việc.