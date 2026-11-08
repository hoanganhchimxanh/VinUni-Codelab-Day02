# 03 — AI Log: Nhật ký tương tác AI

Trong buổi lab này, tôi dùng AI (trợ lý viết và lập trình) như một co-pilot đồng hành: từ khâu tìm bài toán, viết báo cáo, đến lập trình prompt prototype. Dưới đây là ghi chép trung thực về những gì AI làm được, những chỗ AI sai, và cách tôi sửa prompt/ranh giới để có kết quả đúng.

## 1. AI đã giúp gì

- **Phase 1–2 (SCAN & Quick Cards):** gợi ý và cấu trúc 5 bài toán vận hành của các công ty Vingroup, giúp tôi viết 3 Quick Problem Cards đủ các trường Actor, workflow, bottleneck, metric và kiến trúc gợi ý. Bài toán được chọn deep-dive là **Vinpearl — xử lý review/email/tin nhắn đa kênh**.
- **Phase 3 (Deep-Dive):** chuyển mô tả quy trình thủ công 5 bước (Thu thập → Đọc & xác định chủ đề → Đánh giá cảm xúc/mức độ → Soạn phản hồi → Gửi/Handoff, tổng ~32 phút/lượt) thành sơ đồ có đánh dấu bottleneck và handoff; giúp tôi điền đủ 6 field của Problem Statement, tính Business Impact (~5.333 giờ/tháng) và chọn đúng mức AI Fit (LLM Feature + HITL).
- **Phase 4 (Prompt Prototype):** viết system prompt có ranh giới rõ ràng cho dispatcher co-pilot Xanh SM (file mẫu starter code), định nghĩa quy tắc `[DRAFT_ONLY]` và Critical Battery Protocol, gợi ý adversarial test case để tấn công chính ranh giới đó.
- **Phase 5 (Evaluate):** tổng hợp kết quả test thành checklist AI Readiness và lý giải quyết định GO/NOT YET/NO-GO.

## 2. AI trả lời sai / hallucination ở đâu

1. **Thời gian workflow ban đầu bị ước tính thấp hơn thực tế.** AI ước tính tổng quy trình ~5 phút/lượt, nhưng sau khi tôi xem xét kỹ hơn, con số thực tế phải là ~32 phút/lượt (đặc biệt bước Đọc & xác định chủ đề mất ~15 phút do xử lý nhiều văn phong, nhiều ngôn ngữ). Business Impact vì thế cũng bị tính sai từ ~830 giờ/tháng thành ~5.333 giờ/tháng.

2. **Lỗi API version khi gọi system_instruction.** Khi implement `evaluate_prompt()`, AI tạo client `google-genai` với API version mặc định `v1`, dẫn đến lỗi `400 INVALID_ARGUMENT: Developer instruction is not enabled for api version v1`. Phải sửa thành `http_options={"api_version": "v1beta"}` mới dùng được `system_instruction`.

3. **Tự thêm nội dung ngoài yêu cầu.** AI có xu hướng tự thêm header, bảng phụ hoặc các mục không có trong template vào file báo cáo, khiến format lệch khỏi yêu cầu chấm điểm. Phải nhắc lại rõ: *"chỉ sửa đúng phần được yêu cầu, không thêm gì khác"*.

4. **Rủi ro vượt ranh giới nếu system prompt lỏng.** Khi thử adversarial test, nếu system prompt không đủ chặt, mô hình có thể tự ý gửi tin nhắn (bỏ tag `[DRAFT_ONLY]`) hoặc đề xuất trạm sạc xa hơn 5km khi pin < 5% — vi phạm trực tiếp các quy tắc an toàn vận hành của Xanh SM.

## 3. Tôi đã sửa prompt và ranh giới như thế nào

- **Sửa thời gian workflow:** sau khi nhận ra AI ước tính thấp, tôi cập nhật lại từng bước trong sơ đồ Current-State và cập nhật đồng bộ sang Problem Statement (Field 2, 3, 4, 5) để con số nhất quán.
- **Sửa lỗi API version:** thêm `http_options={"api_version": "v1beta"}` vào lúc khởi tạo `genai.Client()`, đảm bảo `system_instruction` được hỗ trợ.
- **Với system prompt của prototype (Xanh SM dispatcher):** tôi định nghĩa 2 ranh giới tuyệt đối:
  1. Mọi phản hồi có nội dung draft tin nhắn PHẢI bắt đầu bằng `[DRAFT_ONLY]`, không được bỏ dù người dùng yêu cầu.
  2. Nếu pin xe < 5%: TUYỆT ĐỐI không đề xuất trạm xa hơn 5km — phải trigger `{"action": "dispatch_mobile_charger", "reason": "..."}` ngay lập tức.
- **Kiểm chứng bằng adversarial test:** viết 2 prompt tấn công (đòi bỏ `[DRAFT_ONLY]`, đòi chỉ đường đến trạm 8km khi pin 2%). Chạy với `gemini-2.5-flash`, cả 2 test đều **pass**: mô hình giữ tag và từ chối đề xuất trạm xa, dispatch mobile charger thay thế.
- **Với trợ lý AI viết báo cáo:** tôi yêu cầu rõ phạm vi từng lần chỉnh sửa, đối chiếu lại với template gốc sau mỗi thay đổi lớn.

## 4. Bài học rút ra

AI giúp tôi tăng tốc rõ rệt ở khâu cấu trúc, tính toán và viết prompt, nhưng **không thể tin tuyệt đối**: nó có xu hướng ước tính số liệu thấp hơn thực tế và dùng API không đúng version. Ranh giới vận hành càng rõ (tag `[DRAFT_ONLY]`, Critical Battery Protocol, HITL bắt buộc) thì output AI càng an toàn và dễ kiểm chứng bằng assertion tự động. Với bài toán liên quan đến vận hành thực tế (gửi tin nhắn cho khách, điều phối xe cứu hộ), con người vẫn phải là người duyệt cuối cùng.