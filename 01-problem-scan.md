# 01 — Problem Scan & Quick Assessment (Vin Smart Future)

> **Thông tin Cá nhân (Individual Submission)**
> - **Họ và tên:** Phạm Hữu Đức
> - **Mã học viên / Branch:** `PhamHuuDuc_03380`
> - **Vai trò:** AI Product Engineer — Vin Smart Future (Vingroup)

---

# 🔍 Phase 1 — SCAN (Cá nhân)

Sử dụng **4 Lenses** (*Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác*), tôi thực hiện quét qua hoạt động vận hành của các công ty thành viên thuộc hệ sinh thái **Vingroup** và xác định **10 bài toán / điểm nghẽn (bottlenecks)** thực tế:

| # | Subsidiary (Công ty) | Tên bài toán / Bottleneck | Lens | Mô tả ngắn & Thất thoát vận hành thực tế |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **VinFast** *(Hậu mãi & Bảo hành)* | **Thẩm định hồ sơ yêu cầu bảo hành pin & phụ tùng từ xưởng đại lý (Warranty Claim Audit)** | **Tốn thời gian** | Xưởng dịch vụ gửi biên bản kiểm tra + log OBD-II + ảnh hiện trường về hãng. Chuyên viên bảo hành mất **20–25 phút/bộ hồ sơ** đối chiếu thủ công chính sách bảo hành 10 năm để duyệt xuất kho linh kiện thay thế. |
| **2** | **Xanh SM (GSM)** *(CSKH & Vận hành)* | **So khớp & Truy vết hành lý thất lạc trên taxi điện (Smart Lost & Found Matching)** | **Pain từ người khác** | Khách báo quên đồ qua tổng đài nhưng không nhớ mã chuyến (đặt hộ người thân/vẫy xe). Nhân viên CSKH phải đọc mô tả đồ vật rời rạc và đối chiếu thủ công với hàng trăm báo cáo nhặt đồ của tài xế, mất **35–45 phút/vụ**. |
| **3** | **Vinmec** *(Bảo hiểm Y tế)* | **Thẩm định hồ sơ bảo lãnh viện phí bảo hiểm tư nhân (Insurance Pre-Authorization)** | **Tốn thời gian** | Chuyên viên bảo hiểm tại bệnh viện phải đọc chỉ định lâm sàng của bác sĩ và tra cứu điều khoản loại trừ của **30+ hãng bảo hiểm** khác nhau. Bệnh nhân phải ngồi chờ **45–60 phút/lượt** mới biết có được bảo lãnh thanh toán hay không. |
| **4** | **Vinhomes** *(Tài chính BQL)* | **Trợ lý giải trình biến động hóa đơn điện, nước & phí dịch vụ hằng tháng (Billing Explainer)** | **Lặp lại** | Từ ngày 1–5 đầu tháng, BQL nhận hàng nghìn yêu cầu thắc mắc vì sao phí nước/phí sạc xe tháng này tăng. Kế toán viên phải tra lịch sử chỉ số công tơ từng căn và gõ thư giải thích cách tính bậc thang, mất **12 phút/căn**. |
| **5** | **Vincom Retail** *(Pháp chế & Cho thuê)* | **Bóc tách & Kiểm tra điều khoản hợp đồng thuê gian hàng (Commercial Lease Abstraction)** | **Tốn thời gian** | Chuyên viên pháp chế và quản lý mặt bằng phải đọc hợp đồng thuê dài **40–60 trang/gian hàng** để trích xuất lịch tăng giá, thời gian miễn tiền thuê thi công (Fit-out) và công thức chia sẻ doanh thu, mất **50 phút/hợp đồng**. |
| **6** | **Vinpearl** *(Vận hành Resort)* | **Điều phối thứ tự ưu tiên dọn buồng phòng giờ cao điểm (Smart Housekeeping Dispatch)** | **AI có thể tốt hơn** | Khung giờ 11:00–14:00 (khách trả phòng và nhận phòng trùng nhau), giám sát buồng phòng phải đọc ghi chú đặc biệt (khách VIP, gia đình có trẻ sơ sinh xin nhận phòng sớm) để gọi bộ đàm phân công thủ công, gây trễ nhận phòng **18% số ca**. |
| **7** | **VinBus** *(Điều độ Giao thông)* | **Chuẩn hóa biên bản bàn giao ca & nhật ký kỹ thuật xe buýt điện tại Depot** | **Lặp lại** | Cuối mỗi ca chạy, tài xế và phụ xe VinBus viết phiếu giấy báo cáo tình trạng lốp, cửa tự động, máy bán vé, điều hòa. Kỹ thuật viên Depot mất **90 phút/đêm** nhập liệu lại và lọc ra các xe cần bảo dưỡng khẩn cấp trước 5h sáng hôm sau. |
| **8** | **VinFast** *(R&D Phần mềm Xe)* | **Tổng hợp & Phân cụm phản hồi người dùng sau cập nhật phần mềm OTA (Post-OTA Mining)** | **Pain từ người khác** | Sau mỗi đợt tung bản cập nhật firmware mới cho VF6/VF7/VF8/VF9, hàng nghìn phản hồi từ tổng đài, hội nhóm chủ xe và phiếu xưởng đổ về rời rạc. Đội QA mất **3–4 ngày** đọc thủ công để phát hiện lỗi phát sinh theo từng phiên bản phần mềm. |
| **9** | **Vinmec** *(Điều dưỡng Nội trú)* | **Tự động tổng hợp phiếu bàn giao ca trực điều dưỡng theo chuẩn SBAR (Nursing Shift Handoff)** | **Lặp lại** | Khi đổi ca 8 tiếng, điều dưỡng phải đọc lại toàn bộ ghi chú sinh hiệu, lượng dịch truyền và diễn biến của 15–20 bệnh nhân để viết báo cáo bàn giao SBAR cho ca sau, mất **30 phút cuối mỗi ca trực**. |
| **10** | **VinUni** *(Đào tạo & Học vụ)* | **Trợ lý rà soát lộ trình tín chỉ & điều kiện môn tiên quyết (Academic Advising Co-Pilot)** | **AI có thể tốt hơn** | Đầu mỗi học kỳ, Cố vấn học tập (Academic Advisor) phải đối chiếu bảng điểm cá nhân của từng sinh viên với khung chương trình đào tạo và lịch mở lớp để tư vấn đăng ký môn, mất **25–30 phút/sinh viên**. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

Từ danh sách 10 bài toán ở Phase 1, tôi chọn ra **Top 3 bài toán** tiềm năng nhất (**Bài toán #1 — VinFast**, **Bài toán #2 — Xanh SM**, và **Bài toán #3 — Vinmec**) để phân tích chi tiết qua **3 Quick Problem Cards**:

---

### 📌 Card #1 — VinFast: Thẩm định hồ sơ yêu cầu bảo hành pin & phụ tùng từ xưởng đại lý

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                        │
│                                                                              │
│ Bài toán (1 câu): Chuyên viên bảo hành VinFast mất 20–25 phút/hồ sơ để đối   │
│ chiếu thủ công log kỹ thuật và ảnh hiện trường với chính sách bảo hành.      │
│                                                                              │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec       │
│                                                                              │
│ Ai đang đau (Actor)?                                                         │
│ - Chuyên viên thẩm định bảo hành hãng (Warranty Auditor) bị quá tải hồ sơ.   │
│ - Cố vấn dịch vụ tại xưởng & Chủ xe phải chờ duyệt linh kiện thay thế.       │
│                                                                              │
│ Workflow thủ công hiện tại (4 bước):                                         │
│   1. Xưởng dịch vụ tải biên bản kiểm tra, ảnh chụp & log OBD-II lên hệ thống │
│      (⏱ 3 phút)                                                              │
│   ──> 2. Chuyên viên mở từng file, kiểm tra điều kiện ODO & lịch sử bảo dưỡng│
│          định kỳ của xe (⏱ 7 phút)                                           │
│   ──> 3. Tra cứu sổ tay chính sách bảo hành 10 năm và đối chiếu mã lỗi DTC   │
│          với điều khoản loại trừ (⏱ 10 phút)                                 │
│   ──> 4. Gõ kết luận phê duyệt/từ chối hoặc yêu cầu bổ sung ảnh (⏱ 3 phút)   │
│                                                                              │
│ Bước nào tốn thời gian/lỗi nhất?                                             │
│ - Bước 2 & Bước 3 (⏱ 17 phút/lượt — chiếm 74% tổng thời gian xử lý).        │
│ - Dễ xảy ra sai sót khi đối chiếu thủ công giữa log kỹ thuật dài và các điều │
│   khoản ngoại lệ (xe từng ngập nước, va chạm gầm hoặc độ chế phụ kiện).      │
│                                                                              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                        │
│ - Tự động hóa Bước 2 (Rule kiểm tra hạn ODO/thời gian) và Bước 3–4 (LLM +    │
│   RAG đối chiếu mã lỗi OBD-II với chính sách bảo hành để xuất báo cáo thẩm   │
│   định nháp `[DRAFT_ONLY]` kèm trích dẫn điều khoản cho chuyên viên duyệt).  │
│                                                                              │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ - Giảm thời gian thẩm định trung bình từ 23 phút ──> dưới 4 phút/hồ sơ.      │
│ - 100% hồ sơ thiếu chứng cứ bắt buộc được phát hiện tự động ngay khi tải lên.│
│ - Tỷ lệ đồng thuận giữa gợi ý của AI và quyết định của chuyên viên >= 92%.   │
│                                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature (+ Rule)  [ ] Agent │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 📌 Card #2 — Xanh SM: So khớp & Truy vết hành lý thất lạc trên taxi điện (Smart Lost & Found)

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                        │
│                                                                              │
│ Bài toán (1 câu): Nhân viên CSKH Xanh SM mất 35–45 phút/vụ để đối chiếu mô   │
│ tả đồ thất lạc của khách với báo cáo nhặt đồ rời rạc từ hàng nghìn tài xế.   │
│                                                                              │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec       │
│                                                                              │
│ Ai đang đau (Actor)?                                                         │
│ - Nhân viên CSKH & Điều phối viên Xanh SM (phải tìm kiếm thủ công).          │
│ - Hành khách (lo lắng khi để quên ví, điện thoại, giấy tờ trên xe vẫy/đặt hộ)│
│                                                                              │
│ Workflow thủ công hiện tại (4 bước):                                         │
│   1. Khách gọi hotline mô tả đồ để quên, điểm đón/trả ước chừng (⏱ 5 phút)   │
│   ──> 2. CSKH lọc danh sách các chuyến xe đi qua khu vực/khung giờ đó trên   │
│          hệ thống (⏱ 10 phút)                                                │
│   ──> 3. Đọc thủ công từng báo cáo/hình ảnh đồ nhặt được do tài xế gửi về    │
│          hoặc gọi điện xác minh từng tài xế (⏱ 20 phút)                      │
│   ──> 4. Xác nhận khớp thông tin và điều phối trả đồ cho khách (⏱ 5 phút)    │
│                                                                              │
│ Bước nào tốn thời gian/lỗi nhất?                                             │
│ - Bước 2 & Bước 3 (⏱ 30 phút/vụ): Khách thường mô tả bằng ngôn ngữ tự nhiên  │
│   mơ hồ ("túi vải màu kem có móc khóa gấu"), khó khớp với ghi chú ngắn gọn   │
│   của tài xế bằng tìm kiếm từ khóa thông thường.                             │
│                                                                              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                        │
│ - Bước 2 & Bước 3: Kết hợp Rule lọc theo khung giờ/tọa độ GPS với Multimodal │
│   LLM (so khớp ngữ nghĩa mô tả của khách với ảnh chụp + ghi chú của tài xế)  │
│   để gợi ý Top-3 báo cáo đồ thất lạc có điểm tương đồng cao nhất.            │
│                                                                              │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ - Giảm thời gian tra cứu và xác minh từ 40 phút ──> dưới 5 phút/vụ (-87%).   │
│ - Tăng tỷ lệ tìm thấy và kết nối trả lại hành lý thành công trong vòng 2 giờ │
│   từ 65% ──> 90%.                                                            │
│                                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature (+ Rule)  [ ] Agent │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 📌 Card #3 — Vinmec: Thẩm định hồ sơ bảo lãnh viện phí bảo hiểm tư nhân (Insurance Pre-Auth)

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                        │
│                                                                              │
│ Bài toán (1 câu): Chuyên viên bảo hiểm tại Vinmec mất 45–60 phút/lượt để đối │
│ chiếu chỉ định lâm sàng với điều khoản loại trừ của hơn 30 hãng bảo hiểm.    │
│                                                                              │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  [x] Vinmec       │
│                                                                              │
│ Ai đang đau (Actor)?                                                         │
│ - Chuyên viên Bảo lãnh viện phí Vinmec (áp lực tra cứu hàng trăm trang quy   │
│   tắc bảo hiểm dưới áp lực thời gian).                                       │
│ - Bệnh nhân khám/nhập viện (phải chờ đợi lâu tại sảnh trước khi làm thủ tục).│
│                                                                              │
│ Workflow thủ công hiện tại (4 bước):                                         │
│   1. Tiếp nhận thẻ bảo hiểm của bệnh nhân & phiếu chỉ định khám/xét nghiệm   │
│      từ bác sĩ trên hệ thống HIS (⏱ 5 phút)                                  │
│   ──> 2. Mở file PDF hợp đồng/quy tắc của hãng bảo hiểm tương ứng để tra cứu │
│          hạn mức và danh mục loại trừ theo mã bệnh ICD-10 (⏱ 25 phút)        │
│   ──> 3. Soạn công văn/biểu mẫu yêu cầu bảo lãnh gửi sang cổng đối tác bảo   │
│          hiểm (⏱ 15 phút)                                                    │
│   ──> 4. Thông báo kết quả phần chi phí được bảo lãnh cho bệnh nhân (⏱ 5 phút│
│                                                                              │
│ Bước nào tốn thời gian/lỗi nhất?                                             │
│ - Bước 2 & Bước 3 (⏱ 40 phút/lượt): Mỗi hãng bảo hiểm có quy tắc chờ, điều   │
│   khoản loại trừ bệnh có sẵn và biểu mẫu khác nhau; tra cứu thủ công rất dễ  │
│   sót điều khoản dẫn đến bị từ chối bồi hoàn hoặc bắt bệnh nhân chờ lâu.     │
│                                                                              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                        │
│ - Bước 2 & Bước 3: LLM kết hợp RAG tra cứu kho văn bản quy tắc của 30+ hãng  │
│   bảo hiểm theo mã ICD-10, tự động cảnh báo điều khoản loại trừ và điền sẵn  │
│   bản nháp hồ sơ yêu cầu bảo lãnh `[DRAFT_ONLY]` để chuyên viên rà soát.     │
│                                                                              │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ - Giảm thời gian chuẩn bị và thẩm định sơ bộ hồ sơ từ 50 phút ──> dưới 8 phút│
│ - Giảm tỷ lệ hồ sơ phải chỉnh sửa/bổ sung lại với hãng bảo hiểm xuống < 5%.  │
│ - 100% hồ sơ gửi đi đều qua bước chuyên viên bảo hiểm Vinmec xác nhận (HITL).│
│                                                                              │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature (RAG)     [ ] Agent │
└──────────────────────────────────────────────────────────────────────────────┘
```
