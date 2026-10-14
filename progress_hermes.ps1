# Прогресс Хермеса: сколько кусков книг пересказано (запускается из progress_hermes.bat)
$W = 'C:\Users\User\knigi_kupleno'
$all = 847
$done = (Get-ChildItem "$W\pereskaz_vse" -Filter *.md -ErrorAction SilentlyContinue).Count
$errs = @(Get-ChildItem "$W\pereskaz_vse" -Filter *.err -ErrorAction SilentlyContinue | Where-Object { -not (Test-Path ($_.FullName -replace '\.err$', '.md')) }).Count
$errLog = 0; if (Test-Path "$W\hermes_vse.err.log") { $errLog = (Get-Item "$W\hermes_vse.err.log").Length }
$proc = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -match 'hermes_(vse|gemini)' }
$pct = [math]::Round($done * 100 / $all, 1)
Write-Host ''
Write-Host "  Готово $done из $all ($pct%)" -ForegroundColor Green
if ($errs -eq 0) { Write-Host '  Ошибок: 0' } else { Write-Host "  Ошибок: $errs (куски не пересказаны, напиши Claude «продолжи хермес»)" -ForegroundColor Red }
if ($errLog -gt 0) { Write-Host "  В hermes_vse.err.log есть записи ($errLog байт)" -ForegroundColor Yellow }
if ($proc) { Write-Host '  Хермес работает' -ForegroundColor Green }
elseif ($done -ge $all) { Write-Host '  Хермес закончил: все куски готовы' -ForegroundColor Green }
else { Write-Host '  Хермес НЕ работает — напиши Claude «продолжи хермес»' -ForegroundColor Red }
Write-Host ''
