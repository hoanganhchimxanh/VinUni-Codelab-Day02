# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)

## 3.1. Current-State Workflow Mapping

Quy trình chấm bài tự luận hiện tại của giáo viên Vinschool (tính theo **1 lớp ~40 bài**):

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Thu bài tự   │ ──→ │ Đọc & chấm   │ ──→ │ Nhập điểm    │
│ luận (LMS /  │     │ thủ công theo│     │ vào Excel /  │
│ giấy)        │     │ rubric       │     │ sổ điểm      │
│              │     │              │     │              │
│ Ai: GV/TA    │     │ Ai: GV       │     │ Ai: GV       │
│ ⏱ 5 phút/lớp │     │ ⏱ 8-10 phút/ │     │ ⏱ 2 phút/bài │
│              │     │   bài 🔴     │     │ 🔄 Handoff   │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 6       │     │ Bước 5       │     │ Bước 4       │
│ Trả bài &    │ ◀── │ Viết nhận    │ ◀── │ Tổng hợp     │
│ phản hồi     │     │ xét cá nhân  │     │ điểm & thống │
│ học sinh     │     │ từng HS      │     │ kê lớp       │
│              │     │              │     │              │
│ Ai: GV       │     │ Ai: GV       │     │ Ai: GV       │
│ ⏱ 2 phút/bài │     │ ⏱ 5 phút/bài │     │ ⏱ 30 phút/lớp│
│ 🔄 Handoff   │     │   🔴         │     │ 🔄 Handoff   │
└──────────────┘     └──────────────┘     └──────────────┘

🔴 = Bottleneck
🔄 = Handoff (người ↔ hệ thống / người ↔ người)
⏱ Tổng thời gian thủ công: ~15-17 phút/bài × 40 bài + 30 phút tổng hợp
   ≈ 11-12 giờ/lớp. Một giáo viên dạy 5 lớp ≈ 55-60 giờ/tháng chỉ cho chấm bài.
```

**Bottleneck & Handoff:**
- 🔴 **Bước 2 (Chấm theo rubric)** và **Bước 5 (Viết nhận xét)** là hai điểm nghẽn nặng nhất, chiếm ~13-15 phút/bài.
- 🔄 **Handoff** xảy ra ở bước 3 (bài → Excel) và bước 6 (nhận xét → học sinh), dễ sai sót/trùng lặp dữ liệu.

---

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Giáo viên bộ môn (Ngữ văn / Khoa học xã hội) và trợ giảng tại Vinschool, người trực tiếp chấm bài tự luận và phản hồi học sinh. |
| **2. Current Workflow** | Giáo viên thu bài qua LMS/giấy, đọc và chấm thủ công theo rubric, nhập điểm vào Excel/Google Sheets, tổng hợp thống kê lớp, viết nhận xét riêng cho từng học sinh, rồi trả bài & phản hồi. Công cụ: LMS Vinschool, Excel/Google Sheets, rubric giấy. 6 bước, ~15-17 phút/bài. |
| **3. Bottleneck** | Bước 2 (đọc & chấm theo rubric) và bước 5 (viết nhận xét cá nhân): ~13-15 phút/bài, chiếm phần lớn thời gian và dễ thiếu nhất quán giữa các bài/giáo viên. |
| **4. Business Impact** | Một lớp 40 bài tốn ~11-12 giờ; giáo viên dạy 5 lớp tốn ~55-60 giờ/tháng chỉ để chấm. Thời gian 1-1 với học sinh bị thu hẹp, phản hồi chậm 1-2 tuần, khó phát hiện sớm học sinh sa sút → giảm chất lượng dạy học và mức hài lòng của phụ huynh. |
| **5. Success Metric** | 1. Giảm thời gian chấm mỗi bài từ 10 phút → **dưới 3 phút** (Efficiency).<br>2. **100% điểm cuối do giáo viên duyệt** (Quality/Control).<br>3. **≥85% nhận xét do AI draft** được giáo viên dùng hoặc chỉnh nhẹ (Acceptance).<br>4. Phát hiện **≥90% học sinh cần hỗ trợ** sớm hơn 1 tuần so với hiện tại (Early-warning). |
| **6. Operational Boundary** | AI **được phép**: đọc nội dung bài làm, gợi ý điểm theo từng tiêu chí rubric kèm lý do, draft nhận xét mang tính sư phạm, highlight lỗi và gợi ý lộ trình học tập. **CẤM**: tự công bố/chốt điểm cuối; tự gửi nhận xét cho học sinh hoặc phụ huynh khi chưa có giáo viên duyệt; bịa trích dẫn hoặc dẫn nguồn không có trong bài; so sánh/xếp hạng học sinh này với học sinh khác; đưa ra nhận định về hoàn cảnh cá nhân/năng lực bẩm sinh. Mọi output phải gắn thẻ `[DRAFT_ONLY]` và **bắt buộc HITL (giáo viên phê duyệt)**. |

---

## 3.3. Future-State Flow & AI Fit

* **AI Fit:** ✅ **LLM Feature** — bài toán là task ngôn ngữ có cấu trúc rubric rõ; chỉ cần LLM draft điểm + nhận xét, giáo viên duyệt.
  * **Rule / State-Machine:** ❌ không đủ vì cần hiểu ngữ nghĩa, lập luận, diễn đạt của bài tự luận.
  * **Agentic Loop:** ❌ chưa cần vì không cần AI tự trị nhiều bước; rủi ro cao khi liên quan điểm số học sinh.

### Future-State Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Thu bài tự   │     │ 🔵 AI đọc bài│     │ 🔵 AI draft  │
│ luận qua LMS │ ──→ │ + gợi ý điểm │ ──→ │ nhận xét +   │
│              │     │ theo rubric  │     │ highlight lỗi│
│ Ai: System   │     │ + lý do      │     │ + lộ trình   │
│              │     │              │     │              │
│              │     │ ⏱ ~30 giây/  │     │ ⏱ ~20 giây/  │
│              │     │   bài        │     │   bài        │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 6       │     │ Bước 5       │     │ Bước 4       │
│ Trả bài &    │ ◀── │ System tổng  │ ◀── │ 🟢 Giáo viên │
│ phản hồi HS  │     │ hợp điểm &   │     │ review, chỉnh│
│              │     │ thống kê lớp │     │ & CHỐT điểm  │
│              │     │              │     │              │
│ Ai: System   │     │              │     │ Ai: GV (HITL)│
│              │     │              │     │ ⏱ ~2 phút/bài│
└──────────────┘     └──────────────┘     └──────────────┘

🔵 = AI Step
🟢 = Human Step (Human-in-the-loop)
```

**Human-in-the-loop:** bước 4 — giáo viên xem gợi ý điểm + lý do + nhận xét draft, sau đó sửa/duyệt/từ chối từng tiêu chí và là người chốt điểm cuối. AI không được ghi điểm hay gửi phản hồi khi chưa có thao tác duyệt của giáo viên.

**↩️ Fallback:**
- Nếu bài nằm ngoài rubric, ngôn ngữ lạ/không đọc được, hoặc điểm gợi ý mâu thuẫn giữa các tiêu chí → AI gắn cờ `NEEDS_MANUAL_REVIEW`, không đưa gợi ý điểm.
- Giáo viên chấm tay hoàn toàn như quy trình cũ.
- Nếu dịch vụ AI lỗi/timeout → hệ thống chuyển về danh sách bài chờ chấm thủ công và báo giáo viên, không chặn quy trình.

---

# 🏁 Phase 5 — EVALUATE (Nhóm)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có bài tự luận + rubric của giáo viên trong phạm vi 1 lớp pilot.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — 3/3 adversarial test đều giữ `[DRAFT_ONLY]`, không chốt điểm, không bỏ rubric, không xếp hạng học sinh; AI luôn trả `NEEDS_MANUAL_REVIEW` khi thiếu dữ liệu/ngoài rubric và chờ giáo viên duyệt.
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Giáo viên tham gia review output; chỉ pilot trên 1 lớp, 1 rubric trước khi mở rộng.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
- [x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
- [ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
- [ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Chọn **GO** với scope hẹp (1 lớp, 1 rubric) vì: (1) Phase 4 đã kiểm chứng ranh giới an toàn — 3/3 test tấn công đều thất bại trước system prompt, output luôn có `[DRAFT_ONLY]`, AI từ chối chốt điểm, từ chối bỏ rubric và từ chối so sánh/xếp hạng học sinh; (2) rủi ro được kiểm soát bằng HITL bắt buộc (giáo viên chốt điểm cuối) và Fallback `NEEDS_MANUAL_REVIEW` khi thiếu dữ liệu/ngoài rubric; (3) giải pháp chỉ dùng **LLM Feature** với model free-tier (`gemini-3.8-flash`), chi phí thấp, không cần hạ tầng phức tạp. Điều kiện dừng: nếu pilot không đạt mục tiêu **< 3 phút/bài** hoặc **< 85% nhận xét draft được giáo viên chấp nhận**, sẽ dừng để xác lập baseline trước khi mở rộng.

