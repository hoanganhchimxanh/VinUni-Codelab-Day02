# 🏗️ Phase 3 — DEEP-DIVE (đề xuất cá nhân: Vinpearl)

**Học viên:** TranAnhTu - 03368

**Nhánh:** TranAnhTu_03368

**Bài toán chọn từ Phase 2:** Card #5 — trích thông tin từ email đặt phòng đoàn.

## 3.1. Current-State Workflow Mapping

**Phạm vi:** một nhân viên đặt phòng đoàn tiếp nhận một email yêu cầu bằng tiếng Việt, lập phiếu thông tin, kiểm tra giá và tồn phòng, rồi phản hồi khách. Xem [sơ đồ các bước](04-workflow-diagram.png). Các số phút dưới đây là **ước tính sơ bộ**, chưa đo tại Vinpearl và chưa phải thời gian vận hành trung bình.

| Bước | Người thực hiện và đầu ra | Thời gian xử lý |
| --- | --- | --- |
| 1. Nhận email 🔄 | Đối tác/khách gửi yêu cầu; nhân viên nhận email | 1 phút (ước lượng) |
| 2. Đọc email 🔴 | Nhân viên tìm ngày nhận/trả, số khách, số phòng, loại phòng, yêu cầu riêng | 5 phút (ước lượng) |
| 3. Nhập phiếu 🔴 | Nhân viên gõ lại các trường, ghi chỗ thiếu hoặc mâu thuẫn | 4 phút (ước lượng) |
| 4. Kiểm tra 🔄 | Nhân viên tra tồn phòng và giá trong hệ thống được phép dùng | 3 phút (ước lượng) |
| 5. Phản hồi 🔄 | Nhân viên duyệt và gửi câu trả lời hoặc câu hỏi làm rõ | 2 phút (ước lượng) |

**Tổng cộng = 15 phút/lượt (ước tính sơ bộ, chưa phải thời gian vận hành trung bình).** Bước 2–3 chiếm 9 phút theo cùng cách ước tính. Cần đo từng bước trên email được phép sử dụng trước khi kết luận điểm nghẽn.

- 🔴 **Bottleneck cần kiểm chứng:** bước 2–3 có nhiều thao tác đọc và nhập lại. Email tự do có thể thiếu trường hoặc đưa nhiều phương án ngày, khiến nhân viên phải đọc lại.
- 🔄 **Handoff:** đối tác → nhân viên ở bước 1; nhân viên ↔ hệ thống đặt phòng ở bước 4; nhân viên → khách ở bước 5.
- **Cần xác minh:** phỏng vấn nhân viên, đo thời gian từng bước trên email được phép sử dụng và ghi tỷ lệ phải hỏi lại để xác định điểm nghẽn thực tế.

## 3.2. Problem Statement (6-field) & Metrics

| Field                       | Nội dung                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Nhân viên kinh doanh/đặt phòng đoàn lập phiếu và phản hồi; đối tác hoặc khách đoàn cung cấp yêu cầu.                                                                                                                                              |
| **2. Current Workflow**     | Nhận email → đọc và trích thông tin → nhập phiếu → kiểm tra tồn phòng/giá → nhân viên gửi phản hồi. Công cụ vận hành cụ thể chưa được xác minh.                                                                                                   |
| **3. Bottleneck**           | Đọc email tự do và nhập lại ở bước 2–3; lỗi có thể là bỏ sót trường, chép sai ngày hoặc chọn nhầm giữa hai phương án. Cần đo thời gian và tần suất lỗi để xác nhận mức độ ảnh hưởng. |
| **4. Business Impact**      | Nhập liệu thủ công có thể kéo dài thời gian phản hồi và tăng tải cho nhân viên. Cần đo số email/ngày, thời gian xử lý, tỷ lệ phải hỏi lại và thời gian duyệt phiếu nháp trước khi ước tính lợi ích. |
| **5. Success Metric**       | Trên tập email có đáp án: ≥95% giá trị của từng trường bắt buộc được trích đúng; 100% trường thiếu hoặc mâu thuẫn được đánh dấu; thời gian đọc và nhập phiếu trung vị <2 phút/email sau khi đo baseline thật. Đây là mục tiêu, chưa phải kết quả. |
| **6. Operational Boundary** | AI chỉ tạo **phiếu nháp** và nêu bằng chứng từ email gốc. AI không được tự báo giá, xác nhận/giữ phòng, gửi email, bịa dữ liệu tồn phòng hay tự chọn giữa các phương án mâu thuẫn. Nhân viên kiểm tra tồn phòng/giá, duyệt và gửi phản hồi.       |

**Cách đo:** tạo tập email mẫu có đáp án để kiểm tra cấu trúc và các trường hợp thiếu/mâu thuẫn; sau đó chỉ dùng email thực khi đã được phép và ẩn danh. So từng trường với nhãn do người chấm xác nhận. Đo riêng thời gian bước 2–3, thời gian nhân viên duyệt/sửa và tỷ lệ fallback. Kết quả trên email mẫu chưa đủ để kết luận hiệu quả vận hành thật.

## 3.3. Future-State Flow & AI Fit

### Lựa chọn giải pháp

**AI-Fit Matrix:** [ ] Rule / State-Machine · [x] LLM Feature · [ ] Agentic Loop

| Phương án                | Vai trò                                                                                        | Kết luận                                                                                                             |
| ------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Rule / State-Machine** | Kiểm tra email trống/quá dài, JSON, ngày hợp lệ, số khách/phòng dương và các hành động bị cấm. | Cần làm lớp kiểm soát; một mình rule khó hiểu email tự do, nhiều phương án và tiếng Việt đa dạng.                    |
| **LLM Feature**          | Trích các trường, giữ câu trích nguồn, đánh dấu thông tin thiếu/mâu thuẫn.                     | **Chọn cho prototype**, nhưng chỉ được đưa phiếu nháp cho nhân viên xem sau khi qua kiểm tra.                        |
| **Agentic Loop**         | Có thể tự đọc hộp thư, tra hệ thống phòng và gửi phản hồi.                                     | **Chưa chọn:** chưa có API, quyền truy cập và quy trình phê duyệt; rủi ro tự giữ phòng/báo giá vượt phạm vi bài lab. |

### Quy trình tương lai đề xuất

**Ký hiệu theo worksheet:** 🔵 AI Step · 🟢 Human Step (HITL) · ↩️ Fallback.

```text
Email được phép xử lý
       ↓
Rule kiểm tra đầu vào; email là dữ liệu không đáng tin
       ↓
🔵 Gemini trích trường → phiếu JSON nháp + câu trích nguồn
       ↓
Rule kiểm tra schema, ngày, số lượng và bằng chứng
       ├── Sai / API lỗi / thông tin mâu thuẫn → ↩️ Nhân viên nhập tay, hỏi khách
       └── Hợp lệ → 🟢 Nhân viên so với email gốc, sửa / duyệt / từ chối
                              ↓
                Nhân viên tự kiểm tra giá và tồn phòng
                              ↓
                    Nhân viên gửi phản hồi cho khách
```

**Human-in-the-loop:** nhân viên đặt phòng là người duyệt cuối cùng, kể cả khi phiếu nháp hợp lệ. Nhân viên quyết định hỏi lại khách, kiểm tra giá/tồn phòng và gửi phản hồi; prototype không có chức năng gửi email hay giữ phòng.

**↩️ Fallback:** email trống, dữ liệu thiếu/mâu thuẫn, Gemini lỗi hoặc trả sai JSON, câu trích không có trong email, hoặc đầu ra nhận đã xác nhận phòng → bỏ phiếu nháp và xử lý thủ công từ email gốc. Chỉ thị giả danh quản lý nằm trong email cũng được xem là dữ liệu, không phải lệnh cho hệ thống.

# 🏁 Phase 5 — EVALUATE

**Bằng chứng kỹ thuật hiện có:** [prototype Vinpearl](starter-code/prompt_prototype.py) hiện đạt **6/6 ca kiểm tra offline** với email tự tạo. Bộ kiểm tra chặn JSON sai cấu trúc, thiếu người duyệt, giá bịa, số khách sai, yêu cầu không có nguồn và phiếu bỏ trống dữ liệu rõ. Đây là kiểm tra Python, chưa phải kết quả gọi Gemini.

Trong các lần thử API trước khi rút gọn, `gemini-2.5-flash` trả lỗi 404 và `gemini-3.8-flash` có lần trả lỗi 504. Với `gemini-3.5-flash-lite`, một lần thử đạt 3/4 ca do model tự chọn ngày nhận phòng mâu thuẫn; sau khi sửa prompt và bộ kiểm tra, lần chạy sau đạt **4/4 ca**. Kết quả 4/4 thuộc phiên bản cũ; bản rút gọn hiện chưa chạy lại với API. Chưa có bằng chứng về độ chính xác trên email thật.

### AI Readiness Checklist

1. [ ] **Có dữ liệu mẫu/log sạch để test?** Có thể tạo email mẫu cho lab; chưa có email vận hành được phép dùng và tập đáp án do nhân viên xác nhận.
2. [x] **Rủi ro khi AI sai có kiểm soát?** Ở mức prototype có rule kiểm tra, người duyệt và fallback. Chưa kiểm chứng đầy đủ với Gemini thật hoặc quy trình vận hành.
3. [ ] **Stakeholders sẵn sàng đổi quy trình?** Chưa phỏng vấn nhân viên đặt phòng, quản lý hoặc chủ hệ thống.

### Quyết định đề xuất cá nhân (theo mẫu Phase 5)

- [ ] **GO (Bắt đầu xây dựng Prototype):** bắt đầu với phạm vi hẹp khi dữ liệu/quy trình đã xác nhận.
- [x] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** bổ sung dữ liệu được phép dùng và đánh giá của người vận hành.
- [ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** dừng đề tài AI nếu kiểm chứng cho thấy rule đơn giản hiệu quả hơn.

**Justification (bằng chứng kỹ thuật và chi phí):** Chọn **NOT YET** cho bước thử nghiệm vận hành vì chưa có dữ liệu được phép dùng, baseline, quyền kết nối hệ thống hoặc xác nhận của nhân viên. Bài lab vẫn có thể thử phiếu nháp trên email mẫu tự tạo để tìm lỗi. Cần đo thời gian duyệt và chi phí API trước khi đánh giá hiệu quả. Nếu nhóm chọn đề tài khác, báo cáo này phải được viết lại theo đề tài chung trước khi đưa vào main.
