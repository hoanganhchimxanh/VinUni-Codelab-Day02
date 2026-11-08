# Lab 02 — Quét bài toán và chọn cơ hội

**Bài làm cá nhân — Phase 1 và Phase 2**

- **Học viên:** Nguyễn Thị Hồng Hạnh - 2A202603537
- **Nhánh cá nhân:** NguyenThiHongHanh_03537

## Phase 1 — SCAN: 5 ý tưởng cá nhân

#### 📝 List bài toán của tôi

Các quy trình dưới đây là giả thuyết cần kiểm chứng với từng đơn vị. Số giờ trong bảng là thời gian xử lý thủ công ước tính theo kịch bản thí điểm. Mức tiết kiệm thực tế cần được đo sau khi triển khai thử.

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vingroup (cấp tập đoàn) | Lặp lại | **Trợ lý ảo cho nhân viên mới.** HR và IT có thể phải trả lời nhiều lần các câu hỏi về biểu mẫu, tài khoản và đầu mối hỗ trợ. Trợ lý AI tra cứu tài liệu nội bộ đã duyệt, dẫn nguồn và chuyển các câu hỏi về trường hợp cá nhân cho người phụ trách. **Ước tính 50 giờ HR/IT/tháng** (150 nhân viên mới × 4 câu hỏi lặp lại × 5 phút ÷ 60). |
| 2 | VinFast | Tốn thời gian | **Tìm phụ tùng cho xe đang sửa.** Khi xưởng thiếu linh kiện, điều phối viên có thể phải tra tồn kho ở nhiều điểm, đối chiếu mã tương thích và gọi xác nhận. AI có thể xếp hạng các điểm cấp hàng theo khả năng giao kịp lịch sửa. Mã thay thế phải nằm trong danh mục kỹ thuật đã duyệt. **Ước tính 80 giờ điều phối/tháng** (400 ca thiếu phụ tùng × 12 phút ÷ 60). |
| 3 | Xanh SM | Pain từ người khác | **Xác minh chuyến đi bị tính phí bất thường.** Khi khách khiếu nại, nhân viên có thể phải đọc lịch sử hỗ trợ, đối chiếu GPS, thời gian chờ và các khoản phí. AI có thể tóm tắt bằng chứng theo từng chuyến và chỉ ra dữ liệu còn thiếu. Nhân viên đối chiếu biểu phí và quyết định cách xử lý. **Ước tính 100 giờ CSKH/tháng** (600 khiếu nại cần xác minh × 10 phút ÷ 60). |
| 4 | VinUni | Lặp lại | **Sàng lọc hồ sơ tuyển sinh còn thiếu giấy tờ.** Khi ứng viên nộp hồ sơ, nhân viên tuyển sinh có thể phải mở từng tệp, xác định loại giấy tờ và đối chiếu với danh mục yêu cầu của từng chương trình. AI có thể nhận diện tài liệu từ bản scan hoặc ảnh chụp. Hệ thống dùng danh mục đã duyệt để đánh dấu mục còn thiếu và soạn nháp email nhắc bổ sung. Nhân viên kiểm tra các tệp khó đọc và duyệt email trước khi gửi. **Ước tính 60 giờ rà soát thủ công trong tháng cao điểm** (600 hồ sơ × 6 phút ÷ 60). |
| 5 | Vinpearl | AI có thể tốt hơn | **Tư vấn vé và gói vui chơi theo nhu cầu.** Khi khách hỏi theo ngày đi, độ tuổi hoặc chiều cao của trẻ và ngân sách, nhân viên có thể phải tra nhiều bảng giá và điều kiện áp dụng. AI có thể hỏi thêm thông tin còn thiếu rồi gợi ý gói phù hợp dựa trên giá và tình trạng vé từ hệ thống đặt vé. **Ước tính 80 giờ tư vấn/tháng** (800 lượt hỏi cần tra cứu nhiều điều kiện × 6 phút ÷ 60). |

## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards được chọn

Các workflow là giả định cần xác minh. Các con số là mục tiêu
thử nghiệm và cần được đối chiếu với số liệu ban đầu.

### Card #1 — Vingroup: Trợ lý onboarding cho nhân sự mới

```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 — TRỢ LÝ ẢO CHO NHÂN VIÊN MỚI
│
│ Bài toán
│ Giúp nhân viên mới đặt câu hỏi bằng ngôn ngữ tự nhiên và tìm
│ đúng hướng dẫn, biểu mẫu hoặc đầu mối hỗ trợ từ tài liệu nội bộ.
│
│ Công ty thành viên
│ [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec
│ [x] Khác — Vingroup (cấp tập đoàn)
│
│ Lens — Lặp lại
│
│ Ai đang đau (Actor)?
│ Nhân viên mới mất thời gian tìm tài liệu hoặc chờ HR/IT phản hồi.
│ HR/IT phải tra cứu và giải đáp nhiều câu hỏi onboarding tương tự.
│
│ Workflow thủ công hiện tại (giả định)
│    1. Nhân viên mới gửi câu hỏi qua chat hoặc email.
│ -> 2. HR/IT xác định nhu cầu, đơn vị và vai trò của người hỏi.
│ -> 3. HR/IT tra tài liệu và kiểm tra phiên bản đang áp dụng.
│ -> 4. HR/IT gửi hướng dẫn, biểu mẫu hoặc chuyển đúng đầu mối.
│ -> 5. Nhân viên hỏi lại nếu hướng dẫn thiếu hoặc chưa phù hợp.
│
│ Bước nào tốn thời gian hoặc dễ sai nhất?
│ Giả thuyết là bước 2–4, nhất là khi câu hỏi diễn đạt chưa rõ
│ hoặc cùng một thủ tục có hướng dẫn khác nhau theo đơn vị.
│
│ AI hỗ trợ ở bước nào?
│ Bước 2–4. Hệ thống tiếp nhận câu hỏi tự do, truy xuất tài liệu
│ nội bộ đã duyệt mà nhân viên có quyền xem, rồi dùng LLM tổng hợp
│ câu trả lời kèm nguồn. Ví dụ, với câu “Em mới vào, muốn xin
│ quyền truy cập hệ thống thì cần làm gì?”, trợ lý trả về các bước
│ và biểu mẫu áp dụng nếu tài liệu cung cấp đủ căn cứ.
│
│ 3 điểm yếu qua góc nhìn CFO và Trưởng phòng Vận hành
│
│ 1. Logic — Chưa xác định đúng nguyên nhân gây chậm.
│    Cần tách ca mất thời gian vì khó tìm hướng dẫn khỏi ca đã
│    nộp yêu cầu và đang chờ phê duyệt. RAG có thể rút ngắn khâu
│    tra cứu. Nếu phần lớn thời gian nằm ở hàng đợi phê duyệt,
│    phản hồi nhanh chỉ cải thiện một phần nhỏ của quy trình.
│
│ 2. Metric — Ước tính 50 giờ/tháng chưa đủ để duyệt đầu tư.
│    150 nhân viên × 4 câu hỏi × 5 phút ÷ 60 = 50 giờ/tháng
│    xử lý thủ công theo giả định. Khi đo tiết kiệm ròng, cần
│    tính số phút HR/IT vẫn dành cho ca chuyển tiếp, lượt hỏi lại
│    và công duy trì hệ thống. CFO cần tính thêm chi phí triển
│    khai và vận hành trước khi kết luận về ROI.
│
│ 3. Giải pháp — Rule-based có thể hiệu quả hơn với FAQ chuẩn.
│    Nếu chủ đề, đơn vị và vai trò đã đủ để xác định một biểu mẫu
│    hoặc đầu mối, menu kết hợp bảng quy tắc có thể trả trực tiếp
│    nội dung đã duyệt. Kết quả nhất quán, dễ kiểm thử và dễ
│    truy vết khi có sai sót. Giá trị riêng của RAG cần được đo
│    ở nhóm câu hỏi diễn đạt đa dạng hoặc cần tổng hợp nhiều nguồn.
│
│ Đo thành công bằng gì (mục tiêu đề xuất cho pilot)?
│ - Giảm ít nhất 30% số phút HR/IT xử lý trên mỗi 100 yêu cầu
│   trong phạm vi so với quy trình hiện tại. Tính cả các ca
│   chuyển tiếp và lượt hỏi lại liên quan đến yêu cầu ban đầu.
│ - Ít nhất 90% yêu cầu trong phạm vi nhận được hướng dẫn đúng
│   ngay lần đầu, theo đánh giá của HR/IT. Tính cả ca chuyển
│   tiếp vào mẫu số để phản ánh mức độ tự phục vụ thực tế.
│ - 0 ca lộ tài liệu ngoài quyền truy cập trong bộ kiểm thử
│   phân quyền trước pilot.
│ - So sánh LLM + RAG với cổng tra cứu theo menu trên hai nhóm
│   riêng biệt gồm FAQ chuẩn và câu hỏi cần tổng hợp tài liệu.
│   Dùng cùng nguồn tài liệu và cùng tiêu chí chấm.
│
│ Quick Architecture
│ [ ] No AI  [ ] Rule  [x] LLM + RAG  [ ] Agent
│
│ Luồng xử lý đề xuất
│ Câu hỏi tự do → truy xuất tài liệu theo quyền và hiệu lực
│ → LLM tổng hợp hướng dẫn kèm nguồn → trả lời hoặc chuyển HR/IT.
│ Cổng rule-based là phương án đối chứng trong pilot.
│
│ Ranh giới
│ Chỉ hỗ trợ tra cứu biểu mẫu, hướng dẫn xin cấp tài khoản và
│ đầu mối onboarding. Hỏi lại khi thiếu thông tin cần thiết.
│ Khi tài liệu thiếu hoặc mâu thuẫn, chuyển cho HR/IT. Việc cấp
│ quyền và phê duyệt thuộc quy trình hiện hành.
└──────────────────────────────────────────────────────────────────────┘
```

### Card #2 — Vinfast: Tìm phụ tùng cho xe đang sửa

```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2 — TÌM PHỤ TÙNG CHO XE ĐANG SỬA
│
│ Bài toán
│ Rút ngắn thời gian từ lúc xưởng xác nhận thiếu phụ tùng đến
│ lúc điều phối viên xác nhận được nguồn cấp phù hợp.
│
│ Công ty thành viên
│ [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác
│
│ Lens — Tốn thời gian
│
│ Ai đang đau (Actor)?
│ Điều phối viên phải tra nhiều kho và gọi xác nhận. Kỹ thuật
│ viên khó chốt lịch sửa khi chưa biết khi nào có phụ tùng.
│
│ Workflow thủ công hiện tại (giả định)
│    1. Xưởng xác định mã phụ tùng cần cấp cho xe.
│ -> 2. Điều phối viên kiểm tra mã gốc và mã thay thế đã duyệt.
│ -> 3. Tra lượng tồn có thể cấp, kể cả hàng đã được giữ chỗ.
│ -> 4. Xác nhận với kho về khả năng cấp và thời điểm giao.
│ -> 5. Chọn nguồn cấp và gửi yêu cầu điều chuyển.
│
│ Bước nào tốn thời gian hoặc dễ sai nhất?
│ Giả thuyết là bước 2–4. Một kho có thể báo còn hàng nhưng
│ lượng hàng đó đã được giữ cho ca sửa khác. Mã phụ tùng
│ nhìn tương tự cũng có thể thuộc cấu hình xe khác.
│
│ AI hỗ trợ ở bước nào?
│ Trong phương án ban đầu, AI hỗ trợ bước 3–4 bằng cách xếp
│ hạng các kho đủ điều kiện theo khả năng giao kịp lịch sửa.
│ Việc xác định mã tương thích dựa trên danh mục kỹ thuật
│ đã duyệt. Kho vẫn xác nhận khả năng cấp trước khi điều chuyển.
│
│ 3 điểm yếu qua góc nhìn CFO và Trưởng phòng Vận hành
│
│ 1. Logic — Chưa chứng minh khâu tra cứu làm chậm việc sửa xe.
│    Ca sửa có thể chậm vì phải gọi nhiều kho, vì không còn
│    hàng có thể cấp hoặc vì chuyến điều chuyển đã qua giờ
│    chốt. Công cụ tìm kiếm chỉ tác động trực tiếp đến khâu
│    xác định nguồn. Cần đo riêng thời gian tra cứu, chờ kho
│    xác nhận và vận chuyển để biết nút thắt thực sự.
│
│ 2. Metric — 80 giờ/tháng là khối lượng xử lý giả định.
│    400 ca × 12 phút ÷ 60 = 80 giờ tra cứu/tháng. CFO cần
│    đo số phút xử lý thực tế trên mỗi 100 ca, tính cả công
│    xác nhận lại và xử lý đề xuất sai. Số giờ giảm được cần
│    đánh giá cùng chi phí tích hợp và bảo trì. Đo thêm tỷ lệ
│    phụ tùng đến kịp lịch sửa để kiểm tra lợi ích cho xưởng.
│
│ 3. Giải pháp — Rule-based có thể xử lý tốt luồng chuẩn.
│    Khi mã tương thích, lượng tồn có thể cấp, giờ chốt và
│    lịch giao đều có dữ liệu, code có thể lọc mã đã duyệt,
│    loại kho thiếu hàng, rồi xếp theo thời điểm giao dự kiến
│    và chi phí điều chuyển. Mỗi đề xuất có lý do rõ ràng để
│    điều phối viên kiểm tra. AI chỉ có giá trị tăng thêm nếu
│    dữ liệu lịch sử cho thấy mô hình dự báo giao trễ chính
│    xác hơn cách tính từ lịch vận chuyển hiện có.
│
│ Đo thành công bằng gì (mục tiêu đề xuất cho pilot)?
│ - Giảm ít nhất 30% số phút điều phối viên xử lý trên mỗi
│   100 ca thiếu phụ tùng so với quy trình hiện tại, tính cả
│   ca phải gọi lại hoặc đổi nguồn cấp.
│ - Tỷ lệ phụ tùng đến kịp lịch sửa ít nhất bằng baseline.
│   Mẫu số gồm toàn bộ ca trong phạm vi có hạn giao đã chốt,
│   kể cả ca chưa tìm được nguồn cấp.
│ - 0 đề xuất mã không tương thích trong bộ kiểm thử danh
│   mục, bao gồm các biến thể xe và mã thay thế dễ nhầm.
│
│ Quick Architecture — đề xuất sau phản biện
│ [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent
│
│ Luồng xử lý đề xuất
│ Mã phụ tùng + cấu hình xe + số lượng + hạn cần hàng
│ → lọc mã tương thích đã duyệt → lọc kho có hàng có thể cấp
│ → xếp theo thời điểm giao dự kiến, rồi theo chi phí
│ → điều phối viên xác nhận nguồn cấp và yêu cầu điều chuyển.
│
│ Ranh giới
│ Khi tồn kho chưa cập nhật hoặc chưa rõ lịch giao, đánh dấu
│ cần xác minh. Nếu thiếu mã tương thích đã duyệt, chuyển bộ
│ phận kỹ thuật kiểm tra. Điều phối viên xác nhận với kho
│ trước khi dùng nguồn cấp để chốt lịch sửa.
└──────────────────────────────────────────────────────────────────────┘
```

### Card #3 — Vinpearl: Tư vấn vé và gói vui chơi


```text
┌──────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3 — TƯ VẤN VÉ VÀ GÓI VUI CHƠI
│
│ Bài toán
│ Giúp khách tìm được vé hoặc gói vui chơi phù hợp với ngày đi,
│ thành phần nhóm và ngân sách, với giá và điều kiện rõ ràng.
│
│ Công ty thành viên
│ [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec
│ [x] Khác — Vinpearl
│
│ Lens — AI có thể tốt hơn
│
│ Ai đang đau (Actor)?
│ Khách phải hỏi nhiều lượt để biết nhóm mình mua được vé nào
│ và tổng chi phí bao nhiêu. Nhân viên tư vấn phải hỏi lại,
│ kiểm tra điều kiện áp dụng và đối chiếu giá theo ngày đi.
│
│ Workflow thủ công hiện tại (giả định)
│    1. Khách hỏi về vé hoặc gói vui chơi qua kênh hỗ trợ.
│ -> 2. Nhân viên hỏi ngày đi, điểm đến, thành phần nhóm và
│       ngân sách. Hỏi tuổi hoặc chiều cao nếu điều kiện vé cần.
│ -> 3. Tra giá, tình trạng vé và điều kiện của từng gói.
│ -> 4. Tính tổng giá cho cả nhóm và so sánh các gói phù hợp.
│ -> 5. Gửi lựa chọn và chuyển khách sang kênh đặt vé.
│
│ Bước nào tốn thời gian hoặc dễ sai nhất?
│ Giả thuyết là bước 2–4, nhất là khi một nhóm có nhiều hạng
│ vé hoặc giá và ưu đãi thay đổi theo ngày. Cần đo riêng thời
│ gian hỏi bổ sung và thời gian tra cứu, đối chiếu thông tin.
│
│ AI hỗ trợ ở bước nào?
│ Trong phương án ban đầu, LLM hỗ trợ bước 2 bằng cách hiểu
│ câu hỏi tự do và hỏi thêm dữ liệu còn thiếu. Ở bước 4–5,
│ LLM có thể giải thích sự khác nhau giữa các gói đã được hệ
│ thống kiểm tra. Giá, tình trạng vé và điều kiện áp dụng
│ lấy từ nguồn nghiệp vụ đã được xác nhận.
│
│ 3 điểm yếu qua góc nhìn CFO và Trưởng phòng Vận hành
│
│ 1. Logic — Chưa chứng minh khâu tư vấn là nút thắt.
│    Khách có thể mất thời gian vì chưa rõ nhu cầu, vì thông
│    tin giá nằm ở nhiều nơi, hoặc vì hệ thống đặt vé chưa có
│    dữ liệu cập nhật. Mỗi nguyên nhân cần cách xử lý khác
│    nhau. Nếu nhân viên mất phần lớn thời gian để xác minh
│    giá hoặc tình trạng vé, chatbot chỉ cải thiện phần hỏi
│    đáp. Vận hành cần đo thời gian theo từng bước.
│
│ 2. Metric — Ước tính 80 giờ/tháng chưa đủ để duyệt đầu tư.
│    800 lượt × 6 phút ÷ 60 = 80 giờ tư vấn/tháng theo giả
│    định. CFO cần đo số phút nhân viên xử lý trên mỗi 100
│    yêu cầu, gồm cả ca chuyển tiếp, hỏi lại và sửa báo giá.
│    Khi tính ROI, cần đưa chi phí tích hợp và cập nhật danh
│    mục vào phép tính. Nếu dùng tỷ lệ đặt vé để đánh giá,
│    cần so sánh các nhóm tương đồng về ngày đi, khuyến mãi
│    và tình trạng vé để tránh quy hết chênh lệch cho công cụ.
│
│ 3. Giải pháp — Rule-based có thể tốt hơn cho luồng chuẩn.
│    Khi khách chọn điểm đến, ngày đi và khai thông tin nhóm,
│    code có thể kiểm tra từng điều kiện vé, áp dụng ưu đãi
│    hợp lệ, tính tổng giá và lọc theo ngân sách. Cùng đầu
│    vào và cùng dữ liệu giá sẽ cho cùng kết quả. Nhân viên
│    có thể truy vết gói bị loại vì hết vé, vượt ngân sách
│    hay sai điều kiện. LLM cần chứng minh giá trị tăng thêm
│    ở các câu hỏi tự do hoặc nhu cầu khó diễn đạt bằng form.
│
│ Đo thành công bằng gì (mục tiêu đề xuất cho pilot)?
│ - Giảm ít nhất 30% số phút nhân viên xử lý trên mỗi 100
│   yêu cầu trong phạm vi so với quy trình hiện tại, tính
│   cả ca chuyển tiếp, lượt hỏi lại và công sửa sai.
│ - Ít nhất 90% yêu cầu trong phạm vi nhận được ít nhất một
│   gói hợp lệ hoặc thông báo đúng rằng chưa có gói phù hợp.
│   Nhân viên đối chiếu theo dữ liệu tại thời điểm tư vấn.
│   Ca chuyển tiếp vì công cụ chưa xử lý được vẫn vào mẫu số.
│ - 0 báo giá sai hoặc gợi ý gói sai điều kiện trong bộ kiểm
│   thử trước pilot, gồm ca sát ngưỡng tuổi hoặc chiều cao,
│   ưu đãi hết hiệu lực và vé hết chỗ.
│
│ Quick Architecture — đề xuất cho luồng chuẩn
│ [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent
│
│ Luồng xử lý đề xuất
│ Form thu nhu cầu → lấy giá và tình trạng vé theo ngày
│ → kiểm tra điều kiện, ưu đãi và tổng giá cho cả nhóm
│ → hiển thị gói phù hợp và dẫn sang kênh đặt vé.
│ Nếu thử nghiệm LLM, dùng cùng bộ quy tắc nghiệp vụ để
│ so sánh riêng lợi ích của giao diện hỏi đáp tự nhiên.
│
│ Ranh giới
│ Chỉ báo giá và tình trạng vé khi có dữ liệu đủ mới từ
│ nguồn đã xác nhận. Nếu thiếu dữ liệu hoặc chưa xác minh
│ được điều kiện áp dụng, chuyển nhân viên tư vấn. Việc
│ giữ chỗ và xác nhận đặt vé thực hiện trên hệ thống đặt vé.
└──────────────────────────────────────────────────────────────────────┘
```