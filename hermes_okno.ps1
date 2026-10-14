# Живое окно «Хермес — что делает сейчас»: обновляется само каждые 10 секунд. Закрыть — крестиком.
$W = 'C:\Users\User\knigi_kupleno'
$ALL = 847
$Host.UI.RawUI.WindowTitle = 'Хермес — что делает сейчас'

# названия книг из TITLES в hermes_vse.py
$titles = @{}
foreach ($l in Get-Content "$W\hermes_vse.py" -Encoding UTF8) {
    if ($l -match "^\s*'([^']+)':\s*['""](.+)['""],\s*$") { $titles[$Matches[1]] = $Matches[2] }
}
function Title($slug) { if ($titles.ContainsKey($slug)) { $titles[$slug] } else { $slug } }

# порядок кусков — как в hermes_vse.py (txt, потом txt13; книги по алфавиту)
function Jobs {
    $list = New-Object System.Collections.ArrayList
    foreach ($d in 'txt', 'txt13') {
        $fs = @(Get-ChildItem "$W\$d" -Filter *.txt | Where-Object { $_.Length -ge 20000 })
        $names = [string[]]($fs | ForEach-Object { $_.BaseName.ToLowerInvariant() + '|' + $_.BaseName })
        [Array]::Sort($names, [StringComparer]::Ordinal)
        foreach ($n in $names) {
            $slug = $n.Split('|', 2)[1]
            $ch = @(Get-ChildItem "$W\chunks_vse" -Filter "${slug}_??.txt" | Sort-Object Name)
            foreach ($c in $ch) { [void]$list.Add([pscustomobject]@{ Slug = $slug; Stem = $c.BaseName; K = [int]$c.BaseName.Substring($c.BaseName.Length - 2); M = $ch.Count }) }
        }
    }
    $list
}
$jobs = Jobs
$bySlug = @{}; foreach ($j in $jobs) { $bySlug[$j.Stem] = $j }

function Piece($stem) {
    $j = $bySlug[$stem]
    if ($j) { "$(Title $j.Slug) — кусок $($j.K) из $($j.M)" } else { $stem }
}

while ($true) {
    $md = @{}; Get-ChildItem "$W\pereskaz_vse" -Filter *.md -ErrorAction SilentlyContinue | ForEach-Object { $md[$_.BaseName] = 1 }
    $er = @{}; Get-ChildItem "$W\pereskaz_vse" -Filter *.err -ErrorAction SilentlyContinue | ForEach-Object { if (-not $md.ContainsKey($_.BaseName)) { $er[$_.BaseName] = 1 } }
    $done = $md.Count
    $log = @(); if (Test-Path "$W\hermes_vse.log") { $log = @(Get-Content "$W\hermes_vse.log" -Encoding UTF8 | Where-Object { $_ -match ' из \d+ \| ' }) }
    $proc = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -match 'hermes_(vse|gemini)' }

    Clear-Host
    $pct = [math]::Round($done * 100 / $ALL, 1)
    $bar = [int][math]::Floor($done * 40 / $ALL)
    Write-Host ''
    Write-Host '   ХЕРМЕС ПЕРЕСКАЗЫВАЕТ КНИГИ' -ForegroundColor Cyan
    Write-Host ''
    Write-Host "   Готово: $done из $ALL ($pct%)" -ForegroundColor Green
    Write-Host ('   [' + ('█' * $bar) + ('░' * (40 - $bar)) + ']') -ForegroundColor Green
    Write-Host ''

    # состояние
    $last = @($log | Select-Object -Last 3)
    $limit = $last.Count -gt 0 -and @($last | Where-Object { $_ -match '429|quota|exhausted' }).Count -eq $last.Count
    if (-not $proc) {
        if ($done -ge $ALL) { Write-Host '   Состояние: ЗАКОНЧИЛ — все куски готовы' -ForegroundColor Green }
        else { Write-Host '   Состояние: Хермес НЕ работает — напиши Claude «продолжи хермес»' -ForegroundColor Red }
    } elseif ($limit) {
        Write-Host '   Состояние: Ждёт — кончился лимит (Ollama или Gemini), продолжит сам' -ForegroundColor Yellow
    } else {
        Write-Host '   Состояние: Работает' -ForegroundColor Green
    }
    Write-Host ''

    if ($proc) {
        Write-Host '   Сейчас пересказывает:' -ForegroundColor Cyan
        $now = @($jobs | Where-Object { -not $md.ContainsKey($_.Stem) -and -not $er.ContainsKey($_.Stem) } | Select-Object -First 3)
        foreach ($j in $now) { Write-Host "     • $(Title $j.Slug) — кусок $($j.K) из $($j.M)" }
        Write-Host ''
    }

    Write-Host '   Последние готовые:' -ForegroundColor Cyan
    $ok = @($log | Where-Object { $_ -match '\| ок (\d+)' } | Select-Object -Last 5)
    if ($ok.Count -eq 0) { Write-Host '     пока нет' }
    foreach ($l in $ok) {
        $p = $l.Split('|'); $stem = $p[1].Trim()
        $k = [math]::Round([int]([regex]::Match($l, 'ок (\d+)').Groups[1].Value) / 1000)
        Write-Host "     • $(Piece $stem) — ок, $k тыс. знаков"
    }
    Write-Host ''
    if ($er.Count -gt 0) { Write-Host "   Кусков с ошибкой: $($er.Count) (перегоним позже)" -ForegroundColor Yellow }
    else { Write-Host '   Кусков с ошибкой: 0' }
    Write-Host ''
    Write-Host "   Обновлено $(Get-Date -Format 'HH:mm:ss'), само обновляется каждые 10 секунд." -ForegroundColor DarkGray
    Start-Sleep 10
}
