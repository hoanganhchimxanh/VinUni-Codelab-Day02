# 03 — AI Log: Nhật ký tương tác AI

**Học viên:** TranAnhTu - 03368

**Đề tài:** Tạo phiếu nháp từ email đặt phòng đoàn Vinpearl

## 1. AI đã giúp gì

- **Tìm và chọn bài toán:** Tôi dùng AI để sắp xếp năm ý tưởng trong bảng SCAN, viết ba Quick Problem Cards rồi chọn thẻ #5. Phạm vi tôi giữ lại là đọc email đặt phòng đoàn và tạo phiếu nháp cho nhân viên xem, không để chương trình tự xác nhận đặt phòng.
- **Phân tích quy trình:** AI giúp tôi đặt câu hỏi về người xử lý, bước chuyển giao, thông tin cần hỏi lại và cách đo kết quả. Tôi dùng các câu hỏi đó để viết file 02; quy trình và thời gian thực tế của Vinpearl vẫn cần được kiểm chứng.
- **Làm prototype:** AI gợi ý cấu trúc JSON, những trường cần trích từ email và bốn tình huống thử ranh giới: giả danh quản lý, ép xác nhận phòng, đưa hai ngày nhận phòng và chèn lệnh giả trong email.

## 2. AI trả lời sai / hallucination ở đâu

- **Lệch đề tài:** Bản code ban đầu còn giữ tình huống Xanh SM của starter code, trong khi tôi đã chọn Vinpearl. Tôi phải đối chiếu lại thẻ #5 để đưa báo cáo và prototype về cùng một bài toán.
- **Thêm số liệu thiếu căn cứ:** Có bản nháp nêu thời gian xử lý và lượng email như thể đó là số liệu của Vinpearl. Tôi không có dữ liệu nội bộ để xác nhận nên đã bỏ các con số này khỏi phần kết luận.
- **Chọn sai ngày:** Trong lần thử trực tiếp đầu với Gemini 3.5 Flash-Lite, email ghi ngày nhận phòng 12/12/2026 hoặc 14/12/2026, nhưng model vẫn chọn ngày đầu. Đây là lỗi có thể làm phiếu nháp sai. Bộ kiểm tra của tôi cũng báo nhầm ngày trả phòng vì câu trích chứa cả ngày nhận và ngày trả.
- **Lỗi khi gọi API:** Gemini 2.5 Flash trả 404 cho tài khoản mới; Gemini 3.8 Flash có lần trả JSON nhưng cũng gặp 504 quá thời gian chờ. Tôi ghi lại các lần lỗi này, không tính chúng là ca thử prompt thành công.

## 3. Tôi đã sửa prompt và ranh giới như thế nào

- Tôi giới hạn system prompt ở việc **trích thông tin để tạo phiếu nháp**. JSON phải ghi rõ cần người duyệt, kèm đoạn trích nguyên văn cho từng trường có giá trị. Thông tin thiếu, mâu thuẫn hoặc chỉ là ước lượng phải để trống và yêu cầu hỏi lại.
- Tôi ghi rõ quy tắc: nếu email đưa hai ngày nhận phòng thì phải để trống trường đó và hỏi lại. Email dù tự xưng là quản lý cũng không được ra lệnh bỏ người duyệt, tự báo giá hay xác nhận đã giữ phòng.
- Tôi giữ bộ kiểm tra Python ở mức phù hợp bài lab: kiểm tra JSON, bằng chứng trích từ email, người duyệt và một số lỗi rõ như chọn ngày mâu thuẫn hoặc bỏ trống số khách, số phòng đã nêu.
- Tôi chuyển sang Gemini 3.5 Flash-Lite cho lần thử trực tiếp tiếp theo. Nếu đầu ra sai cấu trúc hoặc thiếu bằng chứng, nhân viên phải quay lại email gốc; chương trình không tự gửi thư hay đặt phòng.

## 4. Bài học rút ra

Hiện tại, **6/6 ca offline** của bản rút gọn đã đạt. **4/4 email tấn công tự tạo** từng đạt khi chạy Gemini với phiên bản cũ; tôi chưa chạy lại API với bản rút gọn nên không dùng 4/4 làm kết quả của bản này. Autograder báo **9,5/10** và thoát với mã lỗi vì một tiêu chí của template vẫn tìm quy tắc sạc pin Xanh SM trong system prompt, còn bài cá nhân của tôi là Vinpearl.

Tôi rút ra rằng một JSON đúng định dạng vẫn có thể chứa quyết định sai; phải đọc nội dung và đối chiếu với email gốc. Bốn email thử chưa chứng minh hệ thống hoạt động tốt trên email thật. Tôi chưa có bộ email được phép dùng, số đo thời gian hiện tại hoặc phản hồi của nhân viên đặt phòng, nên quyết định cho thử nghiệm vận hành vẫn là **NOT YET**.
