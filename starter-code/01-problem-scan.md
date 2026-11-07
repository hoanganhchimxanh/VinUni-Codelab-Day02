# Day 02 — AI Product Scoping
## VinFast — Trợ lý AI đề xuất trạm sạc thông minh

**Đơn vị:** Vin Smart Future  
**Công ty thành viên:** VinFast  
**Đề tài:** Trợ lý AI đề xuất trạm sạc và tối ưu lịch trình sạc cho xe điện VinFast

> **Lưu ý:** Các số liệu về thời gian và hiệu quả trong bài là giả định phục vụ Lab, chưa được xác minh bằng dữ liệu vận hành thực tế.

---

# Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

## Bối cảnh

Trong vai trò AI Product Engineer tại Vin Smart Future, tôi thực hiện phân tích những khó khăn trong hệ sinh thái Vingroup nhằm xác định cơ hội ứng dụng AI.

Đối với VinFast, việc tìm kiếm trạm sạc phù hợp là một nhu cầu quan trọng của người sử dụng xe điện. Người dùng cần cân nhắc nhiều yếu tố như mức pin hiện tại, khoảng cách di chuyển, khả năng tương thích cổng sạc và tình trạng trạm sạc.

Từ đó, tôi đề xuất sáu bài toán tiềm năng dựa trên bốn góc nhìn (4 Lenses).

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | **VinFast** | AI-upgrade | Trợ lý AI đề xuất trạm sạc phù hợp với dòng xe VF5, VF8, VF9, tình trạng trụ sạc và mức pin hiện tại; hỗ trợ tối ưu lịch trình sạc. |
| 2 | VinFast | Tốn thời gian | Nhân viên chăm sóc khách hàng mất nhiều thời gian tra cứu tài liệu kỹ thuật để hỗ trợ khách hàng xử lý cảnh báo và sự cố xe điện. |
| 3 | VinFast | Lặp lại | Nhân viên tổng hợp và phân loại thủ công các phản hồi về pin, trạm sạc, chất lượng xe và dịch vụ bảo dưỡng. |
| 4 | Xanh SM | Pain từ người khác | Tài xế gặp khó khăn khi tìm trạm sạc phù hợp trong giờ cao điểm, ảnh hưởng đến khả năng phục vụ khách hàng. |
| 5 | Vinhomes | AI-upgrade | Ứng dụng AI phân loại yêu cầu của cư dân và đề xuất phương án xử lý sự cố kỹ thuật, giảm công việc thủ công của nhân viên. |
| 6 | Vinpearl | Tốn thời gian | Nhân viên mất nhiều thời gian tư vấn lịch trình tham quan, dịch vụ và hoạt động phù hợp với nhu cầu từng du khách. |

---

# Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Lựa chọn ba bài toán tiềm năng từ Phase 1:

- **Card #1:** VinFast — Trợ lý AI đề xuất trạm sạc thông minh.
- **Card #2:** VinFast — Trợ lý AI hỗ trợ xử lý sự cố xe điện.
- **Card #4:** Xanh SM — Tối ưu tìm kiếm trạm sạc cho tài xế.

## Card #1 — VinFast: Trợ lý AI đề xuất trạm sạc thông minh

**Bài toán:** Người sử dụng xe điện VinFast gặp khó khăn khi tìm kiếm trạm sạc còn chỗ, phù hợp với phương tiện và đủ gần với mức pin hiện tại.

**Công ty thành viên:** VinFast

**Ai đang đau?** Chủ xe điện VinFast, đặc biệt là người sử dụng VF5, VF8 và VF9.

**Workflow thủ công hiện tại (5 bước):**

1. Người dùng kiểm tra mức pin hiện tại.
2. Mở ứng dụng hoặc bản đồ tìm kiếm trạm sạc.
3. Kiểm tra vị trí, khoảng cách và tình trạng trạm sạc.
4. Xác định khả năng tương thích với phương tiện.
5. Lựa chọn trạm và bắt đầu di chuyển.

**Bước nào tốn nhất?** Bước 3–4: Kiểm tra và so sánh các trạm sạc phù hợp, ước tính 5 phút/lượt.

**AI có thể hỗ trợ ở bước nào?** Bước 3–5: AI tổng hợp thông tin, giải thích lựa chọn và đề xuất lịch trình sạc. Thuật toán xác định khoảng cách, khả năng tương thích và mức độ an toàn trước khi đưa đề xuất cho AI diễn giải.

**Success Metrics:**
- Giảm thời gian tìm kiếm trạm sạc từ 5 phút xuống dưới 1 phút.
- Tỷ lệ đề xuất đúng loại cổng sạc đạt 100% trên tập kiểm thử.
- Không đề xuất tuyến đường vượt quá phạm vi di chuyển an toàn được tính toán.

**Quick Architecture:** LLM Feature + Rule-based.

---

## Card #2 — VinFast: Trợ lý AI hỗ trợ xử lý sự cố xe điện

**Bài toán:** Khách hàng gặp khó khăn trong việc tìm hiểu nguyên nhân và cách xử lý các cảnh báo kỹ thuật xuất hiện trên xe.

**Công ty thành viên:** VinFast

**Ai đang đau?** Chủ xe VinFast và nhân viên chăm sóc khách hàng.

**Workflow thủ công hiện tại (4 bước):**

1. Chủ xe phát hiện cảnh báo hoặc sự cố.
2. Tra cứu hướng dẫn sử dụng phương tiện.
3. Liên hệ bộ phận chăm sóc khách hàng.
4. Nhận tư vấn hoặc đặt lịch kiểm tra tại trung tâm dịch vụ.

**Bước nào tốn nhất?** Bước 2–3: Tra cứu tài liệu và hỗ trợ khách hàng, ước tính 10 phút/lượt.

**AI có thể hỗ trợ ở bước nào?** Bước 2–3: Trợ lý AI sử dụng RAG để tìm kiếm nội dung từ tài liệu kỹ thuật đáng tin cậy, giải thích cảnh báo và đưa ra hướng dẫn sơ bộ.

**Success Metrics:**
- Giảm thời gian tra cứu và tư vấn từ 10 phút xuống dưới 3 phút.
- Tỷ lệ câu trả lời có căn cứ từ tài liệu chính thức đạt tối thiểu 95% trên tập đánh giá.

**Quick Architecture:** LLM Feature (RAG).

---

## Card #4 — Xanh SM: Tối ưu tìm kiếm trạm sạc cho tài xế

**Bài toán:** Tài xế taxi điện gặp khó khăn khi tìm kiếm trạm sạc phù hợp trong giờ cao điểm, ảnh hưởng đến thời gian hoạt động và phục vụ khách hàng.

**Công ty thành viên:** Xanh SM (GSM)

**Ai đang đau?** Tài xế taxi điện và điều phối viên.

**Workflow thủ công hiện tại (4 bước):**

1. Tài xế kiểm tra mức pin hiện tại.
2. Tìm kiếm các trạm sạc gần vị trí hoạt động.
3. Kiểm tra khoảng cách và tình trạng trụ sạc.
4. Lựa chọn trạm và di chuyển đến địa điểm sạc.

**Bước nào tốn nhất?** Bước 2–3: Tìm kiếm và so sánh trạm sạc, ước tính 7 phút/lượt.

**AI có thể hỗ trợ ở bước nào?** Bước 2–3: Hệ thống tự động lọc, xếp hạng trạm sạc theo khoảng cách, mức pin và tình trạng trụ sạc.

**Success Metrics:**
- Giảm thời gian lựa chọn trạm sạc từ 7 phút xuống dưới 2 phút.
- Tăng tỷ lệ tìm được trạm phù hợp trong lần đề xuất đầu tiên.

**Quick Architecture:** Rule-based + thuật toán tối ưu.

---

# Quyết định lựa chọn của nhóm (Đề xuất)

**Bài toán được đề xuất lựa chọn: Card #1 — VinFast: Trợ lý AI đề xuất trạm sạc thông minh.**

## Lý do lựa chọn

**Card #1 — VinFast (Được đề xuất):**

Bài toán có mục tiêu cụ thể, quy trình rõ ràng và khả năng đo lường bằng các chỉ số định lượng. Giải pháp có thể kết hợp thuật toán tìm kiếm, Rule-based và LLM Feature để hỗ trợ người dùng lựa chọn trạm sạc an toàn, phù hợp.

Bên cạnh đó, có thể xây dựng prototype bằng bộ dữ liệu trạm sạc giả lập, không nhất thiết phải kết nối trực tiếp với hệ thống vận hành thực tế ở giai đoạn Lab.

**Card #2 — VinFast (Không ưu tiên):**

Bài toán yêu cầu tài liệu kỹ thuật và dữ liệu mã lỗi chính xác. Việc AI đưa ra hướng dẫn sai có thể ảnh hưởng đến an toàn phương tiện, vì vậy cần cơ chế xác minh thông tin chặt chẽ.

**Card #4 — Xanh SM (Không ưu tiên):**

Bài toán có thể được giải quyết phần lớn bằng các thuật toán tìm đường và tối ưu truyền thống. Vai trò của LLM chưa rõ ràng bằng bài toán Card #1.

## Kết luận

Đề tài **VinFast — Trợ lý AI đề xuất trạm sạc thông minh** được đề xuất chuyển sang Phase 3 — DEEP-DIVE để phân tích kỹ quy trình, Business Impact, AI-Fit, Operational Boundary và Human-in-the-loop.