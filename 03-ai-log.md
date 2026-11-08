# 03 — AI Log: Nhật ký tương tác AI

Trong buổi lab này, tôi dùng AI (trợ lý viết và lập trình) như một co-pilot đồng hành: từ khâu tìm bài toán, viết báo cáo, đến lập trình prompt prototype. Dưới đây là ghi chép trung thực về những gì AI làm được, những chỗ AI sai, và cách tôi sửa prompt/ranh giới để có kết quả đúng.

## 1. AI đã giúp gì

- **Phase 1–2 (SCAN & Quick Cards):** gợi ý và cấu trúc 5 bài toán vận hành của các công ty Vingroup, giúp tôi viết 3 Quick Problem Cards đủ các trường Actor, workflow, bottleneck, metric và kiến trúc gợi ý.
- **Phase 3 (Deep-Dive):** chuyển mô tả quy trình thủ công thành sơ đồ 6 bước có đánh dấu bottleneck, handoff và thời gian; giúp tôi điền đủ 6 field của Problem Statement và chọn đúng mức AI Fit (LLM Feature + HITL).
- **Phase 4 (Prompt Prototype):** viết system prompt có ranh giới rõ ràng, định nghĩa JSON output, và gợi ý 3 adversarial test case để tấn công chính ranh giới đó.
- **Phase 5 (Evaluate):** tổng hợp kết quả test thành checklist và lý giải quyết định GO/NOT YET/NO-GO.

## 2. AI trả lời sai / hallucination ở đâu

1. **Tự thêm nội dung ngoài yêu cầu.** AI tự thêm header cá nhân, mục "lý do chọn bài toán", bảng Input/Output và mục "tác động kỳ vọng" vào `02-deep-dive-report.md`, trong khi file yêu cầu chỉ cần Phase 3 và Phase 5 theo template. Việc này khiến báo cáo lệch khỏi format chấm điểm.

2. **Bê nguyên bối cảnh mẫu sang bài của tôi.** Starter code `prompt_prototype.py` viết cho Xanh SM (ranh giới pin < 5%, điều xe sạc di động). AI ban đầu giữ nguyên các ranh giới đó dù bài toán tôi chọn là Vinschool — tức là áp sai ngữ cảnh.

3. **Giữ lại phần không có trong đề bài.** AI giữ header "Họ tên / Mã sinh viên / Nhóm" mà không kiểm tra xem file yêu cầu có quy định phần này không, làm tôi tưởng đó là bắt buộc.

4. **Chọn model đã lỗi thời.** AI để `gemini-2.5-flash`, dẫn đến lỗi `404 NOT_FOUND` khi chạy vì model không còn khả dụng cho tài khoản mới. Đây là thông tin lỗi thời chứ chưa đến mức bịa đặt, nhưng vẫn là sai so với thực tế API.

5. **Rủi ro "bịa" nếu prompt lỏng.** Khi thử các prompt tấn công, nếu system prompt không chặt, mô hình có thể sẵn sàng chốt điểm, bỏ rubric hoặc so sánh học sinh. Đây là dạng hallucination/vượt ranh giới nguy hiểm nhất vì liên quan trực tiếp đến điểm số.

## 3. Tôi đã sửa prompt và ranh giới như thế nào

- **Với trợ lý AI:** tôi yêu cầu rõ *"chỉ làm theo yêu cầu trong các file .md, không tự ý thêm bất cứ gì"*. Sau đó tôi đối chiếu lại từng mục với `README.md` và `01-worksheet.md`, xoá toàn bộ phần thừa, chỉ giữ đúng Phase 3 và Phase 5.
- **Với system prompt của prototype:** tôi định nghĩa 4 ranh giới bắt buộc:
  1. Mọi output phải bắt đầu bằng `[DRAFT_ONLY]`.
  2. Không được chốt điểm hay gửi phản hồi cho học sinh/phụ huynh — chỉ giáo viên duyệt (HITL).
  3. Nếu bài nằm ngoài rubric, không đọc được hoặc mâu thuẫn giữa các tiêu chí → trả `NEEDS_MANUAL_REVIEW`, không cho điểm.
  4. Không bịa trích dẫn, không so sánh/xếp hạng học sinh, không nhận định hoàn cảnh cá nhân.
- **Bổ sung cấu trúc output:** ép mô hình trả JSON gồm `status`, `criteria`, `strengths`, `weaknesses`, `draft_comment`, `flags`, để dễ kiểm tra tự động và tránh trả lời lan man.
- **Kiểm chứng bằng adversarial test:** tôi viết 3 prompt tấn công (đòi chốt/gửi điểm, đòi bỏ rubric vì "con đối tác", đòi so sánh/xếp hạng và suy đoán hoàn cảnh). Chạy với `gemini-3.8-flash`, cả 3 test đều **pass**: mô hình giữ `[DRAFT_ONLY]`, từ chối chốt điểm, từ chối bỏ rubric và từ chối so sánh học sinh.
- **Sửa model:** sau khi lỗi 404, tôi liệt kê các model khả dụng của key và chuyển sang `gemini-3.8-flash` — model free-tier phù hợp nhất trong danh sách.

## 4. Bài học rút ra

AI giúp tôi tăng tốc rõ rệt ở khâu cấu trúc và viết prompt, nhưng **không thể tin tuyệt đối**: nó có xu hướng thêm nội dung ngoài yêu cầu và bê ngữ cảnh mẫu sang bài khác. Ranh giới càng rõ (tag `[DRAFT_ONLY]`, fallback `NEEDS_MANUAL_REVIEW`, HITL bắt buộc) thì output càng an toàn và dễ kiểm chứng. Với bài toán liên quan đến điểm số học sinh, con người vẫn phải là người duyệt cuối cùng.
