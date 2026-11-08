param([Parameter(Mandatory=$true)][string]$OutputPath)

# Render the current-state diagram with installed Windows fonts; no network.
# On Windows PowerShell 5, read this UTF-8 file explicitly before invoking it.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$diagram = New-Object System.Drawing.Bitmap 1600,1320
$canvas = [System.Drawing.Graphics]::FromImage($diagram)
$canvas.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$canvas.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$canvas.Clear([System.Drawing.ColorTranslator]::FromHtml('#F5F7FB'))
$titleFont = New-Object System.Drawing.Font 'Segoe UI',32,([System.Drawing.FontStyle]::Bold),([System.Drawing.GraphicsUnit]::Pixel)
$headingFont = New-Object System.Drawing.Font 'Segoe UI',23,([System.Drawing.FontStyle]::Bold),([System.Drawing.GraphicsUnit]::Pixel)
$bodyFont = New-Object System.Drawing.Font 'Segoe UI',21,([System.Drawing.FontStyle]::Regular),([System.Drawing.GraphicsUnit]::Pixel)
$smallFont = New-Object System.Drawing.Font 'Segoe UI',18,([System.Drawing.FontStyle]::Regular),([System.Drawing.GraphicsUnit]::Pixel)
$ink = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#172C46'))
$muted = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#4C6078'))
$red = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#A72E3D'))
$arrowPen = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml('#64748B')),3
$arrowPen.CustomEndCap = New-Object System.Drawing.Drawing2D.AdjustableArrowCap 5,6
$borderPen = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml('#CCD5E1')),2

function Text-Block([string]$Text,[single]$X,[single]$Y,[single]$Width,[single]$Height,$Font=$bodyFont,$Brush=$ink) {
    $rect = New-Object System.Drawing.RectangleF $X,$Y,$Width,$Height
    $canvas.DrawString($Text,$Font,$Brush,$rect)
}

Text-Block 'QUY TRÌNH HIỆN TẠI' 70 35 1450 55 $titleFont
Text-Block 'VinFast | Tìm và lựa chọn trạm sạc — mô hình giả định phục vụ Lab 02' 70 99 1450 45 $bodyFont

$nodes = @(
    @{Y=180;Title='1. KIỂM TRA PIN';Body='Người dùng đọc mức pin trên màn hình xe.';Time='0,5 phút';Hot=$false},
    @{Y=380;Title='2. TÌM DANH SÁCH TRẠM';Body='Người dùng mở bản đồ / ứng dụng để tìm trạm.';Time='1 phút';Hot=$false},
    @{Y=580;Title='3. SO SÁNH TRẠM';Body='Đọc khoảng cách, tình trạng trụ và số chỗ trống.';Time='2,5 phút';Hot=$true},
    @{Y=780;Title='4. KIỂM TRA TƯƠNG THÍCH';Body='Tra tài liệu / hỏi hỗ trợ; kiểm tra khả năng đến trạm.';Time='2,5 phút';Hot=$true},
    @{Y=980;Title='5. CHỌN TRẠM';Body='Người dùng tổng hợp thông tin và tự quyết định.';Time='0,5 phút';Hot=$false}
)
$handoffs = @(
    'HANDOFF: thông tin từ xe → ứng dụng / bản đồ',
    'HANDOFF: danh sách trạm → người dùng so sánh',
    'HANDOFF: người dùng → tài liệu / kênh hỗ trợ',
    'HANDOFF: thông tin đã đối chiếu → quyết định của người dùng'
)

for ($index=0; $index -lt $nodes.Count; $index++) {
    $node = $nodes[$index]
    $fillHex = if ($node.Hot) {'#FFF0F1'} else {'#FFFFFF'}
    $fill = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml($fillHex))
    $rect = New-Object System.Drawing.Rectangle 70,([int]$node.Y),950,135
    $canvas.FillRectangle($fill,$rect)
    $canvas.DrawRectangle($borderPen,$rect)
    Text-Block $node.Title 95 ($node.Y+17) 710 38 $headingFont
    Text-Block $node.Time 815 ($node.Y+20) 180 35 $headingFont
    Text-Block $node.Body 95 ($node.Y+68) 890 55 $bodyFont
    if ($node.Hot) { $canvas.FillRectangle($red,70,([int]$node.Y),8,135) }
    if ($index -lt $nodes.Count-1) {
        $canvas.DrawLine($arrowPen,545,([int]$node.Y+137),545,([int]$node.Y+185))
        Text-Block $handoffs[$index] 95 ($node.Y+146) 430 47 $smallFont $muted
    }
    $fill.Dispose()
}

$panelBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#E7EDF6'))
$canvas.FillRectangle($panelBrush,1070,180,460,935)
Text-Block 'TỔNG THỜI GIAN' 1100 208 400 42 $headingFont
Text-Block '7 phút / lượt' 1100 263 400 60 $titleFont
Text-Block '0,5 + 1 + 2,5 + 2,5 + 0,5' 1100 329 400 55 $bodyFont
Text-Block 'BOTTLENECK' 1100 425 400 42 $headingFont $red
Text-Block 'Bước 3–4: 5 phút / lượt' 1100 478 400 72 $headingFont $red
Text-Block 'Thông tin phân tán; khó kiểm chứng còn chỗ, tương thích và phạm vi di chuyển.' 1100 557 395 135 $bodyFont
Text-Block 'PHẠM VI ĐO' 1100 743 400 42 $headingFont
Text-Block 'Từ kiểm tra pin đến chọn trạm. Không gồm lái xe, chờ hoặc sạc.' 1100 799 395 130 $bodyFont
Text-Block 'Chưa có AI trong current-state workflow này.' 1100 975 395 95 $bodyFont

Text-Block 'LƯU Ý: Các thời gian là giả định cho lab; chưa phải số liệu đo từ hoạt động VinFast.' 70 1170 1460 45 $smallFont $red
Text-Block 'Trường hợp dữ liệu không kiểm chứng được: quay lại tìm trạm / hỏi hỗ trợ. Chưa tính thời gian lặp vào baseline.' 70 1222 1460 60 $smallFont $muted

try {
    $diagram.Save($OutputPath,[System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output "Workflow diagram saved: $OutputPath"
} finally {
    $canvas.Dispose()
    $diagram.Dispose()
    $titleFont.Dispose()
    $headingFont.Dispose()
    $bodyFont.Dispose()
    $smallFont.Dispose()
    $ink.Dispose()
    $muted.Dispose()
    $red.Dispose()
    $panelBrush.Dispose()
    $arrowPen.Dispose()
    $borderPen.Dispose()
}
