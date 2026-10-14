# Запуск Хермеса по Планировщику (задача «Хермес — пересказ книг», раз в 6 часов).
# Если Хермес уже работает — ничего не делает. Если лимит Ollama кончился — hermes_vse.py сам выйдет после пробного запроса.
$W = 'C:\Users\User\knigi_kupleno'
$run = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -match 'hermes_vse' }
if ($run) { exit }
$env:PYTHONIOENCODING = 'utf-8'
Start-Process cmd -ArgumentList '/c', 'python hermes_vse.py --par 3 >> hermes_vse.log 2>> hermes_vse.err.log' -WorkingDirectory $W -WindowStyle Hidden
