- **Học viên:** Nguyễn Thị Hồng Hạnh - 2A202603537
- **Nhánh cá nhân:** NguyenThiHongHanh_03537

## Phase 1 — SCAN: 5 ý tưởng cá nhân
*Prompt 1: "Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho các mảng của tập đoàn Vingroup: VinFast / Xanh SM / Vinhomes / Vinmec, Vinpearl, Vincom,.... Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*
- **AI giúp gì** — Dùng bốn lens để chọn năm quy trình cụ thể. Với mỗi quy trình, AI xác định ai xử lý, thao tác nào tốn thời gian, AI có thể hỗ trợ ở đâu và cách quy đổi khối lượng công việc thành giờ mỗi tháng.
- **AI sai hoặc hallucination ở đâu** — Chưa phát hiện lỗi số học. Số lượt xử lý, số phút mỗi lượt và mức độ thủ công của từng quy trình đều chưa được xác minh bằng dữ liệu nội bộ. Ví dụ, 600 khiếu nại/tháng là giả định của kịch bản Xanh SM.
- **Đã sửa prompt hoặc ranh giới ra sao** — Prompt nội dung được xử lý trong một lượt. Khi soạn câu trả lời, AI ghi rõ các giả định, trình bày công thức và tách thời gian xử lý thủ công khỏi mức tiết kiệm có thể đạt được. 


## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards được chọn
*Prompt 2: "Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: Vingroup (cấp tập đoàn) | Lặp lại | **Trợ lý ảo cho nhân viên mới. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*
- **AI giúp gì** — Phản biện ba điểm về nguyên nhân gây chậm, cách đo lợi ích và sự cần thiết của AI. AI cũng đề xuất cách so sánh LLM + RAG với cổng rule-based trên cùng nguồn tài liệu.
- **AI sai hoặc hallucination ở đâu** — Con số 50 giờ/tháng là ước tính từ đầu vào giả định. Các ngưỡng 30%, 90% và 0 ca lộ tài liệu là mục tiêu đề xuất cho pilot, chưa phải kết quả đo thực tế.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình đặt ranh giới ngay trong yêu cầu: giữ LLM + RAG làm kiến trúc chính cho trợ lý hỏi đáp bằng ngôn ngữ tự nhiên dựa trên tài liệu nội bộ. Phương án rule-based được dùng để đối chứng với nhóm câu hỏi có đáp án chuẩn. Trợ lý chỉ trả lời dựa trên tài liệu đã duyệt mà nhân viên có quyền xem, dẫn nguồn và chuyển câu hỏi cho HR/IT khi thiếu căn cứ.

*Prompt 3: "Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: VinFast | Tốn thời gian | Tìm phụ tùng cho xe đang sửa. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*
- **AI giúp gì** — Tách thời gian tìm nguồn cấp khỏi thời gian chờ kho và vận chuyển, chỉ ra giới hạn của ước tính 80 giờ/tháng, rồi cụ thể hóa cách dùng quy tắc để lọc và xếp hạng kho.
- **AI sai hoặc hallucination ở đâu** — Chưa phát hiện lỗi số học. Hai đầu vào 400 ca/tháng và 12 phút/ca là giả định. Mức độ cập nhật của dữ liệu tồn kho, khả năng tra lịch giao và quy trình xác nhận thực tế tại VinFast đều cần kiểm chứng. Các ngưỡng trong thẻ là mục tiêu thí điểm.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình đặt phạm vi phản biện ở khâu tìm và xác nhận nguồn cấp phụ tùng. AI được xem xét ở bước xếp hạng kho. Mã tương thích phải theo danh mục đã duyệt, còn quyết định điều chuyển thuộc về điều phối viên. Phương án rule-based được đánh giá dựa trên điều kiện dữ liệu tồn kho và lịch giao đủ tin cậy.

*Prompt 4: Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: Vinpearl | AI có thể tốt hơn | Tư vấn vé và gói vui chơi theo nhu cầu. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI*
- **AI giúp gì** — Tách thời gian hỏi nhu cầu khỏi thời gian xác minh giá và điều kiện vé, kiểm tra ước tính 80 giờ/tháng và xác định phần nghiệp vụ có thể xử lý bằng quy tắc.
- **AI sai hoặc hallucination ở đâu** — Chưa phát hiện lỗi số học. Con số 800 lượt/tháng, 6 phút/lượt và quy trình trong thẻ là giả định. Khả năng lấy giá và tình trạng vé theo ngày từ hệ thống Vinpearl cần được xác minh. Các ngưỡng 30%, 90% và 0 lỗi trong bộ kiểm thử là mục tiêu đề xuất.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình giới hạn bài toán ở khâu tư vấn trước đặt vé. Giá, ưu đãi, tình trạng vé và điều kiện áp dụng phải dựa trên dữ liệu nghiệp vụ đã xác nhận. Rule-based được đánh giá cho luồng có đầu vào cấu trúc. LLM được xem xét ở phần hiểu và diễn giải nhu cầu bằng ngôn ngữ tự nhiên.

## Phase 3 - DEEP-DIVE
### 3.1 - Current-state Workload
- **AI giúp gì** — Chuyển mô tả trong Card #3 thành quy trình 5 bước, thảo luận chỉ ra 2 bước bottleneck
- **AI sai hoặc hallucination ở đâu** — Số liệu dùng và cách phân bổ ở bottleneck chưa được xác nhận bằng dữ liệu vận hành của Vinpearl.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình đặt phạm vi ngay từ đầu ở khâu tư vấn trước đặt vé, dùng mức 6 phút/lượt từ Card #3 và tách thời gian thao tác của nhân viên khỏi thời gian chờ khách phản hồi. Điểm nghẽn được ghi là giả thuyết để kiểm chứng khi đo thực tế.

### 3.2. Problem Statement (6-field) — Vin Smart Future Standard
- **AI giúp gì** — AI lượng hóa tỷ trọng thời gian của hai bước nghẽn và chuyển mục tiêu pilot thành tiêu chí đo cụ thể.
- **AI sai hoặc hallucination ở đâu** — Chưa phát hiện sai lệch trong phép tính, thời lượng từng bước là giả định.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình đặt phạm vi ngay từ đầu ở khâu tư vấn trước đặt vé và yêu cầu dùng các giả định đã nêu ở mục 3.1. Phần nghiệp vụ về giá, ưu đãi và điều kiện vé được giao cho rule-based. Nếu thử nghiệm LLM, vai trò của mô hình giới hạn ở hiểu nhu cầu và giải thích phương án đã kiểm tra.

### 3.3. Future-State Flow & AI Fit
- **AI giúp gì** — Chuyển hai điểm nghẽn ở mục 3.1 thành các bước tự động hóa cụ thể, phân vai giữa LLM, bộ quy tắc và nhân viên, đồng thời bổ sung nhánh xử lý khi thiếu dữ liệu hoặc LLM gặp lỗi.
- **AI sai hoặc hallucination ở đâu** — Khả năng truy xuất giá và tình trạng vé theo ngày cần xác minh với Vinpearl. Việc nhân viên duyệt trước khi gửi là lựa chọn đề xuất cho pilot.
- **Đã sửa prompt hoặc ranh giới ra sao** — Mình đặt phạm vi ngay từ đầu ở khâu tư vấn trước đặt vé. Bộ quy tắc kiểm tra điều kiện và tính giá, LLM hỗ trợ hiểu nhu cầu và soạn nháp, còn nhân viên duyệt phản hồi trong pilot.