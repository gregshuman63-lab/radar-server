@echo off
set "ROOT=%USERPROFILE%\Downloads\builder-bot-day1"

wt -w 0 ^
  new-tab -d "%ROOT%" cmd /k "cd /d ""%ROOT%"" && call .venv\Scripts\activate.bat && uvicorn app:app --reload" ^
  ; split-pane -H -d "%ROOT%" cmd /k "cd /d ""%ROOT%"" && call .venv\Scripts\activate.bat && python worker.py"

