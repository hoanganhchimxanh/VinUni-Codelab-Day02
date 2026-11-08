# Day 02 — AI Log & Reflection

**Học viên / nhánh:** `nguyentuanhieu_03374`  
**Đề tài:** Trợ lý đề xuất trạm sạc VinFast  
**Ngày lập bản nháp:** 08/11/2026

> Nhật ký này được AI hỗ trợ soạn dựa trên các yêu cầu và thao tác có trong phiên làm việc. Những mục dưới đây mô tả điều đã quan sát trong phiên, không khẳng định học viên đã tự thực hiện mọi bước hoặc nhóm đã họp. Học viên cần đọc, sửa thành phản ánh của mình và bổ sung kết quả thực nghiệm trước khi nộp.

## 1. Mục đích sử dụng AI

AI được dùng làm trợ lý đối chiếu yêu cầu lab với bài đã viết, phản biện chất lượng kiểm thử và hỗ trợ chuẩn bị bản nháp còn thiếu. Mục tiêu là có sản phẩm có thể đọc và kiểm tra tại máy, chưa push lên GitHub.

## 2. Nhật ký tương tác đã quan sát

| Lượt | Yêu cầu / nội dung trao đổi | AI hỗ trợ | Điều cần con người kiểm tra |
|---|---|---|---|
| 1 | Đối chiếu file Python với template; yêu cầu không tự sửa code | Đọc hướng dẫn và code, nhận diện khác biệt 2 test trong starter so với 3 test trong worksheet | Không chỉ dựa vào comment của starter để kết luận đủ bài |
| 2 | Kiểm tra nhánh GitHub `nguyentuanhieu_03374` | Đọc danh sách file và hai bài đã push, xác định thiếu tài liệu và SCAN sai vị trí trên remote | IDE có file đang mở không chứng minh file đã được push |
| 3 | Yêu cầu bổ sung bài trong thư mục, chưa push | Soạn Deep Dive, AI Log, sơ đồ current-state; hoàn thiện contract JSON và test trong prototype | Review nội dung, giả định, phạm vi và kết quả chạy; chưa có kết quả kinh doanh thật |
| 4 | Học viên lưu key trong `.env` và yêu cầu chạy Gemini 2.5 Flash | AI nạp key trong tiến trình, thực hiện bốn request; cả bốn nhận 404 NOT_FOUND, lưu nguyên lỗi và cập nhật báo cáo | Phân biệt lỗi khả dụng model với lỗi ranh giới prompt; chưa đổi sang model khác |
| 5 | Học viên yêu cầu chuyển sang 3.8 và hoàn thiện bài | AI giữ log 2.5, chuyển model/config, thêm đọc `.env`, gặp 504/503, sau khoảng nghỉ chạy lại và nhận bốn output thật đều đạt validator | Ghi cả lần lỗi và lần thành công; không tự nhận giảng viên đã cho phép ngoại lệ hoặc mọi prompt đều an toàn |

## 3. Phát hiện sai / chưa đủ căn cứ

**Đánh giá “đủ test” có thể sai nếu chỉ đọc starter.** Starter/autograder chỉ yêu cầu 2 test nhưng worksheet yêu cầu 3. Bản chỉnh dùng 4 tình huống tấn công và kiểm tra từng output, không chỉ thêm tên test.

**Thông báo Passed không đủ chứng minh an toàn.** Code cũ chỉ tìm `[DRAFT_ONLY]` ở bất cứ vị trí nào; chuỗi có lời mở đầu trước tag vẫn qua được phép kiểm tra. Test pin thấp chỉ cần chứa `dispatch_mobile_charger` hoặc “cứu hộ”, nên có thể bỏ lọt phản hồi đồng thời khuyên đi trạm 8 km. Đây là phân tích logic của code cũ, không phải output Gemini đã quan sát.

**Không được biến giả định thành kết quả.** Các con số 5 phút, dưới 1 phút, 100 lượt/ngày và 400 phút tiết kiệm là giả định/mục tiêu. Chưa có logs xác nhận. Bản Deep Dive ghi rõ công đoạn 3–4 là 5 phút, toàn quy trình là 7 phút giả định; không trộn hai phạm vi đo.

**Model và bối cảnh cần thống nhất.** Code trước dùng `gemini-3.8-flash` trong khi đề yêu cầu `gemini-2.5-flash`; prompt còn dùng vai trò Xanh SM nhưng đề tài đã chọn VinFast. Đã thử quay về 2.5 theo đề và gặp 404. Theo yêu cầu tiếp theo của học viên, bản hiện tại chuyển sang 3.8 và ghi rõ ngoại lệ; ranh giới ví dụ Xanh SM được áp dụng vào VinFast với scope hẹp.

**Đối chiếu đề chưa đủ để kết luận model khả dụng.** Sau khi có key, gọi 2.5 Flash thực tế nhận 404 ở cả bốn request: API báo model không còn khả dụng cho người dùng mới và đề nghị 3.8 Flash. Đã chuyển sang 3.8 theo yêu cầu học viên, không dựa vào đó để tự nhận có chấp thuận của giảng viên. Bằng chứng 2.5 được giữ riêng tại `evidence/05-test-results-gemini-2.5-flash.json`.

**Đổi tên model chưa đủ để chạy thành công.** 3.8 dùng `thinking_level="low"` thay cho cấu hình `thinking_budget=0` của 2.5. Sau khi đổi, request vẫn có thể lỗi 504/503 vì thời gian chờ hoặc quá tải. Đã tăng timeout mỗi request từ 20 lên 60 giây, chạy bốn test độc lập đồng thời và lưu kết quả theo từng case; không sửa giới hạn 30 giây của autograder.

Trong bốn output thật của lần chạy 3.8 thành công, chưa quan sát hallucination về trạm: case thiếu dữ liệu trả human review. Không bịa một tình huống hallucination để làm đầy nhật ký, và không suy diễn bốn case thành bằng chứng mô hình không bao giờ hallucinate.

## 4. Cách thay đổi prompt và ranh giới

- Yêu cầu raw output bắt đầu chính xác bằng `[DRAFT_ONLY] ` và sau đó là một JSON object có bốn field.
- Phân biệt context giả lập do ứng dụng cung cấp với user_message có thể chứa prompt injection. Prompt không cho user_message tự sửa pin hoặc dữ liệu trạm.
- Pin dưới 5% luôn chỉ đề xuất mobile charger, không chọn trạm. Đúng 5% được xử lý ở nhánh thông thường nếu có đủ dữ liệu an toàn.
- Thiếu dữ liệu → yêu cầu con người kiểm tra; không bịa trạm, không khẳng định tình trạng live.
- Mọi action đều yêu cầu human approval. Lý do chỉ được chọn từ các câu kiểm soát để tránh giấu chỉ dẫn đi xa hoặc lời xác nhận “đã gửi”.
- Validator đối chiếu action và station_id với rule độc lập; phản hồi sai được ghi lỗi, không âm thầm sửa để ghi Passed.

## 5. Kiểm thử và điều chưa biết

Hai lớp kiểm thử có ý nghĩa khác nhau:

1. **Offline:** dùng các output tự dựng, có cả đúng và sai, để kiểm tra validator. Đây không phải phản hồi từ Gemini và không kiểm tra sức chống tấn công thực tế của model.
2. **Live:** đã thử 2.5 (bốn lỗi 404), lưu bằng chứng rồi chuyển 3.8 theo yêu cầu học viên. 3.8 ban đầu có 504/timeout và một lần hoàn chỉnh trả bốn lỗi 503 quá tải. Sau khoảng nghỉ, lần chạy trực tiếp tiếp theo nhận **4/4 output thật đạt validator**, exit code 0, tổng 33,302 giây. Raw output và thời gian nằm trong `05-test-results.json`, các lần lỗi giữ trong `evidence/`.

**Quan sát từ output thật:** pin 2% và lời giả quản trị viên ở context 4% đều dẫn đến đề xuất mobile charger, station=null; yêu cầu bỏ tag vẫn nhận đúng prefix và approval=true; thiếu dữ liệu nhận human review, không có trạm bịa. Chỉ kết luận đạt trong bốn tình huống đã thử.

Trong phiên đã chạy **24/24 test offline đạt**, đủ bốn file và đạt ba kiểm tra source. Autograder đầy đủ gần nhất ghi 8/10 do timeout 30 giây, không có kết quả assertion live. Lưu kiểm tra tại [06-verification-results.json](06-verification-results.json). Đây là thao tác do AI thực hiện trong môi trường làm việc, không tự nhận học viên đã tự chạy. Nếu một test live lỗi, cần lưu nguyên output/lỗi API và phân loại trước khi sửa; không thay output lỗi bằng ví dụ đúng.

## 6. Phản ánh để học viên review

Bài học rút ra từ việc đối chiếu là cần tách ba câu hỏi: bài có đủ file không, code có chạy không và output có thực sự giữ ranh giới không. Autograder có thể chỉ kiểm tra sự tồn tại của file hoặc từ khóa, nên không thay thế việc đọc nội dung và kiểm tra ngữ nghĩa nghiệp vụ.

Với bài toán chọn trạm, rule/thuật toán có vai trò cốt lõi trong lọc dữ liệu và bảo vệ ranh giới. Lần 4/4 đạt cho thấy hợp đồng đầu ra hoạt động trong bộ test nhỏ, nhưng chưa chứng minh lợi ích LLM so với template. Cần thêm đối chứng, baseline và độ ổn định dịch vụ trước giai đoạn thử nghiệm tiếp theo; báo cáo giữ NOT YET với lý do cụ thể.

**Phần học viên cần tự xác nhận:** mức độ tham gia ở từng bước; nhận xét nào thực sự thay đổi cách nghĩ của mình; cách ghi nhận ngoại lệ dùng 3.8 với môn học; phản hồi của nhóm/người dùng nếu có. Chưa có dữ liệu để thay bằng một câu chuyện trải nghiệm cá nhân hoàn chỉnh.
