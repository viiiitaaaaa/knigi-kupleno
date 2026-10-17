# OCR картинок встроенным распознаванием Windows (англ.). ocr_win.ps1 <папка с png> → рядом .txt
param($dir)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null=[Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
$null=[Windows.Media.Ocr.OcrEngine,Windows.Foundation,ContentType=WindowsRuntime]
$null=[Windows.Graphics.Imaging.BitmapDecoder,Windows.Foundation,ContentType=WindowsRuntime]
$asTask=([System.WindowsRuntimeSystemExtensions].GetMethods()|?{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'})[0]
function Await($op,$t){$task=$asTask.MakeGenericMethod($t).Invoke($null,@($op));$task.Wait();$task.Result}
$null=[Windows.Globalization.Language,Windows.Globalization,ContentType=WindowsRuntime]
$eng=[Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new('en-US'))
Get-ChildItem $dir -Filter *.png | ?{-not (Test-Path ($_.FullName -replace '\.png$','.txt'))} | %{
  $f=Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($_.FullName)) ([Windows.Storage.StorageFile])
  $s=Await ($f.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
  $dec=Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($s)) ([Windows.Graphics.Imaging.BitmapDecoder])
  $bmp=Await ($dec.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
  $r=Await ($eng.RecognizeAsync($bmp)) ([Windows.Media.Ocr.OcrResult])
  ($r.Lines|%{$_.Text}) -join "`n" | Out-File ($_.FullName -replace '\.png$','.txt') -Encoding utf8
  $s.Dispose()
}
