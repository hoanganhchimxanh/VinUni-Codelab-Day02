# Bản bài làm để review tại máy — chưa push Git

## 1. Những file đã hoàn thiện

| Yêu cầu của lab | Bài làm tại thư mục gốc repo |
|---|---|
| SCAN: tối thiểu 5 bài toán và 3 cards | [01-problem-scan.md](01-problem-scan.md): 6 bài toán, 4 lenses, 3 cards, metric và lý do lựa chọn |
| Deep Dive và Evaluate | [02-deep-dive-report.md](02-deep-dive-report.md): current flow, 6-field, AI Fit, future flow, HITL, fallback, metrics, quyết định có căn cứ |
| Current-state workflow dạng ảnh | [04-workflow-diagram.png](04-workflow-diagram.png): 5 bước, thời gian, handoff, bottleneck; tổng giả định 7 phút |
| AI Log cá nhân | [03-ai-log.md](03-ai-log.md): nhật ký dựa trên phiên làm việc; cần học viên xác nhận phần phản ánh cá nhân |
| Prompt prototype | [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py): Gemini 3.8 Flash, 4 adversarial inputs, raw prefix, JSON và validator |
| Kết quả kiểm thử | [05-test-results.json](05-test-results.json): lần chạy trực tiếp hoàn chỉnh đã đạt 4/4; [06-verification-results.json](06-verification-results.json): kiểm tra kỹ thuật và lần chạy riêng của autograder |

Thư mục dự án là thư mục **bên trong** `VinUni_Codelab_Day02_Template-main`, có `README.md` và `autograder/`. `.venv` nằm ở thư mục ngoài. Bài làm được lưu trên nhánh cá nhân `nguyentuanhieu_03374`; chưa push lên GitHub.

## 2. Khác biệt model so với đề

Đề chỉ định **Gemini 2.5 Flash**. Lần chạy thực tế nhận bốn lỗi 404: model không còn khả dụng cho người dùng mới, API đề nghị 3.8 Flash. Bằng chứng gốc được giữ tại [evidence/05-test-results-gemini-2.5-flash.json](evidence/05-test-results-gemini-2.5-flash.json).

**Học viên đã yêu cầu chuyển sang `gemini-3.8-flash` trong phiên làm việc.** Bản hiện tại dùng model này; không ghi rằng giảng viên đã chấp thuận ngoại lệ vì chưa có thông tin đó. Khi nộp, cần trình bày rõ lý do thay model và kèm bằng chứng 404.

SDK dùng `thinking_level="low"` cho 3.8, thay `thinking_budget=0` của cấu hình 2.5. Tham khảo [hướng dẫn Google về thinking với GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=en). Giữ nguyên prompt, test và ranh giới nghiệp vụ khi chuyển model.

## 3. Chạy tại máy

Nhập key trong `.env` cùng cấp `README.md`, dưới dạng `GEMINI_API_KEY=...`. Script tự nạp hai tên biến `GEMINI_API_KEY` / `GOOGLE_API_KEY`; biến môi trường đã có sẽ được ưu tiên hơn `.env`. File `.env` đã có trong `.gitignore`.

Từ thư mục có `README.md`:

```powershell
# Test offline: không gọi API.
..\.venv\Scripts\python.exe -B -m unittest discover -s starter-code -v

# Test live: bốn request độc lập, gọi Google bằng key trong .env.
..\.venv\Scripts\python.exe -B starter-code/prompt_prototype.py

# Toàn bộ autograder gốc; phần code sẽ thực hiện thêm một lần chạy live.
..\.venv\Scripts\python.exe -B autograder/autograder.py
```

Nếu đã kích hoạt venv, có thể thay đường dẫn Python bằng `python`. Không lưu key trong code hoặc báo cáo. Chạy live sẽ cập nhật `05-test-results.json`; dùng `--report ten-khac.json` nếu muốn lưu riêng một lần chạy.

## 4. Kết quả xác minh ngày 08/11/2026

| Kiểm tra | Kết quả thực tế |
|---|---|
| Offline (`unittest`) | **24/24 đạt**, gồm 20 test contract, 2 test đọc `.env`, 2 test runner với output giả lập |
| File nộp | **4/4 file có mặt**, đặt đúng thư mục gốc |
| Ba kiểm tra source của autograder | Đạt SYSTEM_PROMPT, Gemini SDK và khai báo adversarial tests |
| Autograder đầy đủ lần gần nhất | **8/10 theo cơ chế kiểm tra tự động**, exit code 1: timeout 30 giây và chưa có kết quả assertion live; không phải điểm rubric nội dung |
| Chạy trực tiếp Gemini 3.8 sau khoảng nghỉ | **4/4 test live đạt**, exit code 0; không có lỗi API hoặc validation, tổng thời gian 33,302 giây |

Ở lần chạy thành công: A1 và A3 đề xuất mobile charger; A2 giữ tag và đề xuất LAB_A với approval=true; A4 không bịa trạm và yêu cầu human review. Cả bốn raw output giữ tiền tố và đúng JSON contract. Đây là kết quả của bốn tình huống giả lập trong một lần chạy, không phải bảo đảm an toàn với mọi input.

Không coi `status: failed` ở các lần lỗi API là chứng cứ mô hình vi phạm ranh giới. Các log 404/504/503 vẫn được giữ riêng; không thay output lỗi bằng output giả. Kết quả offline không thay thế phản hồi Gemini.

**Xử lý timeout:** lần đầu 3.8 gặp 504 với timeout request 20 giây; autograder dừng sau 30 giây. Đã đổi timeout mỗi request thành 60 giây và chạy bốn request độc lập đồng thời, lưu report sau từng case. Tổng thời gian vẫn phụ thuộc Google; autograder có thể dừng script trước khi các request hoàn tất. Không sửa giới hạn của autograder để nhận điểm giả.

**Bằng chứng các lần thử:**

- [Lần đầu 3.8](evidence/05-test-results-gemini-3.8-attempt-1.json): report chưa hoàn tất, có một lỗi 504 trước khi autograder dừng; không phải bộ 4 test hoàn chỉnh.
- [Autograder lần đầu](evidence/06-verification-attempt-1.json).
- [Lần thứ hai 3.8](evidence/05-test-results-gemini-3.8-attempt-2.json): report chưa hoàn tất khi hết 30 giây.
- [Autograder lần thứ hai](evidence/06-verification-attempt-2.json).
- [Lần 3.8 gặp bốn lỗi 503](evidence/05-test-results-gemini-3.8-attempt-3.json).
- [Lần chạy trực tiếp thành công](05-test-results.json): bốn raw output và thời gian; [bản lưu độc lập](evidence/05-test-results-gemini-3.8-success-1.json).
- Lần gọi model riêng trong autograder được lưu tách biệt tại [evidence/05-test-results-gemini-3.8-autograder-final.json](evidence/05-test-results-gemini-3.8-autograder-final.json); xem kết luận autograder tại [06-verification-results.json](06-verification-results.json).

## 5. Các việc chỉ học viên / nhóm có thể xác nhận

- Đọc lại AI Log và sửa phần phản ánh thành trải nghiệm thật của mình; không tự nhận đã họp hoặc có kết quả kinh doanh nếu chưa có.
- Ghi rõ ngoại lệ dùng 3.8 thay 2.5 khi nộp; chưa có xác nhận giảng viên trong phiên này.
- Đã có output thật và bảng Phase 4. Khi cần chạy lại, giữ bằng chứng hiện tại và đọc cả kết quả lẫn thời gian; API vẫn có thể quá tải hoặc vượt giới hạn autograder.
- Xác nhận đề tài, số liệu giả định, nguồn dữ liệu và người chịu trách nhiệm duyệt với nhóm. Không tự điền stakeholder đã sẵn sàng.
- Sau khi review, nộp theo Git workflow của lab: code ở nhánh cá nhân; tài liệu nhóm được chọn lọc lên main; trưởng nhóm điền form. Phiên này chưa push, merge vào main hoặc điền form.

Nguồn sơ đồ: [tools/render-workflow.ps1](tools/render-workflow.ps1). Vẽ lại bằng Windows PowerShell:

```powershell
$drawingSource = [IO.File]::ReadAllText((Join-Path (Get-Location) 'tools\render-workflow.ps1'), [Text.Encoding]::UTF8)
& ([scriptblock]::Create($drawingSource)) -OutputPath (Join-Path (Get-Location) '04-workflow-diagram.png')
```
