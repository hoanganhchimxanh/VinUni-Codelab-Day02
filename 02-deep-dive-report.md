# 02 — Deep-Dive Report & Evaluation (Vin Smart Future)

> **Thông tin Cá nhân (Individual Submission)**
> - **Họ và tên:** Phạm Hữu Đức
> - **Mã học viên / Branch:** `PhamHuuDuc_03380`
> - **Vai trò:** AI Product Engineer — Vin Smart Future (Vingroup)
> - **Bài toán lựa chọn từ Phase 2:** **Card #1 — VinFast: Thẩm định hồ sơ yêu cầu bảo hành pin & phụ tùng từ xưởng đại lý (Warranty Claim Audit Co-Pilot)**

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình thẩm định và phê duyệt hồ sơ yêu cầu bảo hành pin cao áp & phụ tùng xe điện từ hơn 120 xưởng dịch vụ/đại lý gửi về Trung tâm Hậu mãi **VinFast** hiện tại:

```text
┌───────────────────┐  🔄 Handoff 1  ┌───────────────────┐  🔄 Handoff 2  ┌───────────────────┐
│ Bước 1            │ ─────────────► │ Bước 2            │ ─────────────► │ Bước 3            │
│ Tiếp nhận hồ sơ   │                │ Kiểm tra điều kiện│                │ Đọc log OBD-II &  │
│ bảo hành từ xưởng │                │ ODO & lịch sử xe  │                │ tra cứu chính sách│
│                   │                │                   │                │                   │
│ Ai: Cố vấn dịch vụ│                │ Ai: Chuyên viên BH│                │ Ai: Chuyên viên BH│
│ ⏱ 3 phút          │                │ ⏱ 4 phút          │                │ ⏱ 9 phút 🔴       │
│ In: Phiếu + Ảnh   │                │ In: Số VIN, ODO   │                │ In: Mã lỗi DTC    │
│ Out: Hồ sơ trên   │                │ Out: Xác nhận còn │                │ Out: Điều khoản   │
│      cổng DMS     │                │      hạn bảo hành │                │      bảo hành khớp│
└───────────────────┘                └───────────────────┘                └─────────┬─────────┘
                                                                                    │
                                                                                    ▼ 🔄 Handoff 3
┌───────────────────┐                ┌───────────────────┐                ┌───────────────────┐
│ Bước 5            │  🔄 Handoff 4  │ Bước 4            │                │ Bước 3b (Song song│
│ Phê duyệt xuất kho│ ◄───────────── │ Soạn kết luận &   │ ◄───────────── │ Đối chiếu ảnh chụp│
│ phụ tùng thay thế │                │ giải trình duyệt/ │  🔄 Handoff 3b │ hiện trường với   │
│                   │                │ từ chối bảo hành  │                │ điều khoản loại trừ
│ Ai: Kho Phụ tùng  │                │ Ai: Chuyên viên BH│                │ Ai: Chuyên viên BH│
│ ⏱ 1 phút          │                │ ⏱ 3 phút          │                │ ⏱ 3 phút 🔴       │
│ In: Lệnh duyệt    │                │ In: Kết quả rà    │                │ In: Ảnh gầm/giắc  │
│ Out: Xuất linh    │                │ Out: Biên bản     │                │ Out: Phát hiện va │
│      kiện về xưởng│                │      thẩm định    │                │      chạm/độ chế  │
└───────────────────┘                └───────────────────┘                └───────────────────┘

🔴 = Bottlenecks (Bước 3 & Bước 3b mất 12/23 phút — tra cứu mã lỗi DTC & đối chiếu điều khoản loại trừ thủ công)
🔄 = Handoffs (4 điểm chuyển giao giữa Xưởng dịch vụ ──> Hệ thống DMS ──> Chuyên viên Bảo hành ──> Kho Phụ tùng)
⏱ Tổng thời gian xử lý thủ công trung bình: 23 phút / bộ hồ sơ bảo hành.
```

*(Sơ đồ trực quan hóa chi tiết được đính kèm tại file `04-workflow-diagram.png`).*

### Phân tích chi tiết từng bước hiện tại:

| Bước | Tác vụ | Người thực hiện | Công cụ / Hệ thống | Thời gian | Ghi chú Handoff / Bottleneck |
| :-: | :--- | :--- | :--- | :-: | :--- |
| **1** | Tạo yêu cầu bảo hành (RO), tải lên biên bản kiểm tra, file log chẩn đoán OBD-II và 5–10 ảnh hiện trường. | Cố vấn dịch vụ tại Xưởng | Cổng Dealer Management System (DMS) | ⏱ 3 phút | 🔄 **Handoff 1:** Hồ sơ đôi khi thiếu ảnh chụp tem niêm phong hoặc log lỗi bị cắt cụt. |
| **2** | Mở hồ sơ theo số VIN, tra cứu ngày giao xe, số ODO hiện tại và lịch sử bảo dưỡng định kỳ. | Chuyên viên Bảo hành hãng | Hệ thống SAP / ERP & DMS | ⏱ 4 phút | 🔄 **Handoff 2:** Phải copy-paste số VIN qua lại giữa 2 màn hình hệ thống. |
| **3** | Đọc file log mã lỗi kỹ thuật (DTC/BMS) và tra cứu sổ tay chính sách bảo hành 10 năm theo từng dòng xe (VF5/VF6/VF7/VF8/VF9). | Chuyên viên Bảo hành hãng | File PDF Chính sách & Sổ tay kỹ thuật | ⏱ **9 phút** | 🔴 **Bottleneck chính:** Tài liệu dài hàng trăm trang, mã lỗi phức tạp, tốn thời gian đọc hiểu nhất. |
| **3b** | Xem từng ảnh hiện trường (gầm pin, cổng sạc, khoang máy) để kiểm tra dấu hiệu ngoại lực, ngập nước hoặc đấu nối phụ kiện ngoài. | Chuyên viên Bảo hành hãng | Trình xem ảnh trên DMS | ⏱ **3 phút** | 🔴 **Bottleneck phụ:** Dễ bỏ sót vết cạ gầm nhỏ hoặc dấu hiệu can thiệp dây điện nếu xem vội giờ cao điểm. |
| **4** | Gõ biên bản kết luận (Chấp thuận bảo hành / Từ chối kèm trích dẫn điều khoản / Yêu cầu xưởng bổ sung chứng cứ). | Chuyên viên Bảo hành hãng | Form nhập liệu DMS | ⏱ 3 phút | 🔄 **Handoff 3–4:** Gõ tay lặp đi lặp lại các đoạn trích dẫn quy định bảo hành. |
| **5** | Phát lệnh xuất kho linh kiện bảo hành gửi về xưởng đại lý. | Hệ thống ERP / Kho | SAP Warehouse | ⏱ 1 phút | Phụ thuộc hoàn toàn vào nút bấm duyệt ở Bước 4. |

---

## 3.2. Problem Statement (6-Field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
| :--- | :--- |
| **1. Actor / Operator** | **Chuyên viên thẩm định bảo hành hãng (Warranty Auditor)** tại Trung tâm Hậu mãi VinFast và **Cố vấn dịch vụ (Service Advisor)** tại các xưởng dịch vụ trên toàn quốc. |
| **2. Current Workflow** | Xưởng dịch vụ tải biên bản kiểm tra, log chẩn đoán OBD-II và ảnh chụp hiện trường lên cổng DMS ──> Chuyên viên bảo hành mở từng hồ sơ, tra cứu số VIN/ODO trên SAP ──> Đọc thủ công bảng mã lỗi DTC và tra cứu sổ tay chính sách bảo hành 10 năm để đối chiếu điều khoản loại trừ ──> Xem ảnh hiện trường ──> Gõ văn bản phê duyệt/từ chối để xuất kho phụ tùng. Quy trình gồm **5 bước thủ công, mất trung bình 23 phút/bộ hồ sơ**. |
| **3. Bottleneck** | **Bước 3 & Bước 3b (mất 12 phút/hồ sơ — chiếm 52% tổng thời gian):** Đọc hiểu tổ hợp mã lỗi kỹ thuật (DTC/BMS), tra cứu chéo với hàng trăm trang quy định bảo hành theo từng đời xe và rà soát điều khoản loại trừ (va chạm gầm, ngập nước, độ chế phụ kiện). |
| **4. Business Impact** | Mỗi ngày hệ thống tiếp nhận **600–800 hồ sơ bảo hành** trên toàn quốc, tiêu tốn **~250–300 giờ công/ngày** của đội ngũ kỹ sư thẩm định. Vào khung giờ cao điểm, thời gian chờ duyệt linh kiện bị kéo dài lên **4–8 giờ**, làm chậm tiến độ giao trả xe cho khách hàng (giảm CSAT hậu mãi) và tiềm ẩn rủi ro duyệt nhầm các ca thuộc diện loại trừ bảo hành (thất thoát chi phí phụ tùng hàng tỷ VNĐ/năm). |
| **5. Success Metric** | 1. **Efficiency:** Giảm thời gian thẩm định trung bình từ **23 phút xuống dưới 3.5 phút/hồ sơ** (**giảm 85% thời gian xử lý**).<br>2. **Quality:** **>= 92%** bản nháp biên bản thẩm định (`[DRAFT_ONLY]`) do AI tạo ra được chuyên viên đồng ý duyệt ngay mà không cần sửa lại điều khoản trích dẫn; **100%** hồ sơ thiếu ảnh/log bắt buộc được cảnh báo tự động trong **< 10 giây**. |
| **6. Operational Boundary** | • **AI ĐƯỢC PHÉP:** Tự động kiểm tra tính đầy đủ của hồ sơ, đối chiếu mã lỗi DTC với kho tài liệu chính sách bảo hành (RAG), phân tích sơ bộ mô tả/ảnh hiện trường và soạn thảo bản nháp kết luận thẩm định gắn nhãn **`[DRAFT_ONLY]`** kèm trích dẫn điều khoản chính xác.<br>• **AI TUYỆT ĐỐI CẤM:** Không được tự động bấm nút phê duyệt xuất kho phụ tùng (đặc biệt các cụm linh kiện giá trị cao như Pin cao áp, Động cơ điện, Bộ sạc OBC); không được tự động gửi thông báo từ chối bảo hành thẳng cho khách hàng/xưởng khi chưa có **Chuyên viên bảo hành xác nhận (Bắt buộc HITL)**; không được tự suy diễn điều khoản ngoài văn bản chính thức của VinFast. |

---

## 3.3. Future-State Flow & AI Fit

### Ma trận lựa chọn kiến trúc (AI-Fit Matrix):

| Phương án kiến trúc | Mức độ phù hợp | Lý do kỹ thuật & vận hành |
| :--- | :---: | :--- |
| **Rule / State-Machine** | ⚠️ **Một phần (Bước 1–2)** | Rule-based rất tốt để kiểm tra điều kiện cứng (Số ODO `< 200.000 km`, thời hạn `< 10 năm`, đủ 5 ảnh bắt buộc), nhưng **không thể** đọc hiểu biên bản mô tả triệu chứng tự do của kỹ thuật viên hay đối chiếu ngữ nghĩa điều khoản bảo hành phức tạp. |
| **LLM Feature (+ Rule & RAG)** | ✅ **CHỌN CHÍNH** | Kết hợp **Rule Engine** (lọc hạn bảo hành & kiểm tra đủ file) với **LLM Feature (Gemini 3.8 Flash + RAG Sổ tay bảo hành)** để tóm tắt mã lỗi DTC, trích dẫn điều khoản và xuất biên bản nháp `[DRAFT_ONLY]` cho chuyên viên duyệt. Chi phí thấp, độ trễ `< 10 giây`, kiểm soát 100% rủi ro tài chính. |
| **Agentic Loop (Autonomous)** | ❌ **Loại bỏ** | Quyết định bảo hành liên quan trực tiếp đến chi phí linh kiện hàng chục đến hàng trăm triệu đồng/ca và quyền lợi pháp lý của chủ xe. Không cho phép Agent tự trị tự duyệt xuất kho hay tự từ chối khách hàng. |

### Quy trình tương lai có tích hợp AI (Future-State Flow):

```text
┌────────────────────┐     ┌────────────────────┐     ┌────────────────────┐     ┌────────────────────┐
│ Bước 1 (Rule Gate) │     │ Bước 2             │     │ Bước 3             │     │ Bước 4             │
│ Xưởng tải hồ sơ ──►│     │ 🔵 AI đọc log DTC  │     │ 🔵 AI soạn biên bản│     │ 🟢 Chuyên viên BH  │
│ Rule tự động kiểm  │ ──► │ & đối chiếu RAG    │ ──► │ thẩm định nháp     │ ──► │ kiểm tra 1 màn hình│
│ tra ODO, hạn 10 năm│     │ Sổ tay Bảo hành    │     │ [DRAFT_ONLY] kèm   │     │ & Click Phê duyệt  │
│ & đủ ảnh bắt buộc  │     │ VinFast            │     │ trích dẫn điều mục │     │ (HITL bắt buộc)    │
│ ⏱ 5 giây           │     │ ⏱ 10 giây          │     │ ⏱ 10 giây          │     │ ⏱ 3 phút           │
└────────────────────┘     └─────────┬──────────┘     └────────────────────┘     └────────────────────┘
                                     │
                                     ▼ (Nếu mã lỗi lạ / Độ tự tin < 85% / Nghi ngờ ngập nước, va chạm)
                           ┌────────────────────┐
                           │ ↩️ Fallback:       │
                           │ Gắn cờ             │
                           │ [MANUAL_INSPECTION]│
                           │ Chuyển thẳng về    │
                           │ Kỹ sư trưởng chấm  │
                           │ thẩm định thủ công │
                           └────────────────────┘

🔵 = AI Step (Gemini 3.8 Flash + RAG xử lý trong ~20 giây)
🟢 = Human Step / HITL (Chuyên viên bảo hành rà soát và bấm nút chốt cuối cùng trong ~3 phút)
↩️ = Fallback (Chuyển luồng kiểm tra kỹ thuật thủ công khi dữ liệu bất thường hoặc độ tự tin < 85%)
⏱ Tổng thời gian xử lý mới: ~3.5 phút / bộ hồ sơ (Giảm 85% so với 23 phút hiện tại).
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] **Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?**
   * **Có.** VinFast đã số hóa toàn bộ Sổ tay Chính sách Bảo hành (PDF/Markdown), bảng danh mục mã lỗi chuẩn OBD-II/DTC của các dòng xe VF5, VF6, VF7, VF8, VF9 và hàng chục nghìn hồ sơ bảo hành lịch sử trên hệ thống DMS.
2. [x] **Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?**
   * **Hoàn toàn trong tầm kiểm soát.** Mọi đầu ra của AI đều bị khóa bởi tiền tố `[DRAFT_ONLY]` và chỉ hiển thị trên màn hình nội bộ của Chuyên viên bảo hành. AI không có quyền gọi API xuất kho SAP. Các ca phức tạp (pin cao áp hoặc độ tự tin `< 85%`) tự động kích hoạt Fallback `MANUAL_INSPECTION`.
3. [x] **Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?**
   * **Rất sẵn sàng.** Chuyên viên bảo hành không phải thay đổi hệ thống làm việc mà được tích hợp ngay khung gợi ý AI bên cạnh màn hình DMS hiện tại, giúp họ giải phóng khỏi việc tra cứu PDF thủ công nhàm chán.

---

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
- [x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp (Pilot giai đoạn 1 cho nhóm linh kiện ắc-quy 12V, hệ thống điều hòa, màn hình giải trí và bộ sạc trên dòng xe VF5 & VF8).
- [ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
- [ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Bài toán có điểm nghẽn định lượng cực kỳ rõ ràng (**23 phút/hồ sơ**, gây ùn ứ 600–800 hồ sơ/ngày tại trung tâm hậu mãi). Về mặt kỹ thuật, việc kết hợp **Rule Engine** (kiểm tra điều kiện cứng ODO/thời hạn) với **Gemini 3.8 Flash + RAG** (đối chiếu mã lỗi DTC với văn bản chính sách bảo hành) giải quyết trúng đích 12 phút tra cứu thủ công nặng nhọc nhất. Chi phí suy luận API trên **Gemini 3.8 Flash** chỉ tốn **~15–25 VNĐ/hồ sơ**, nhưng giúp tiết kiệm **hơn 19 phút lao động kỹ sư/hồ sơ** (tương đương tiết kiệm >200 giờ công/ngày trên toàn hệ thống), đồng thời cơ chế chốt chặn **`[DRAFT_ONLY]` + HITL** triệt tiêu hoàn toàn rủi ro duyệt sai linh kiện.
