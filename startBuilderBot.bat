@echo off
setlocal
set "ROOT=%USERPROFILE%\Downloads\builder-bot-day1"
cd /d "%ROOT%" || (echo [ERROR] Folder not found: %ROOT% & pause & exit /b 1)

if not exist ".venv" (
  echo [INFO] Creating venv...
  python -m venv .venv || (echo [ERROR] Could not create venv & pause & exit /b 1)
)

call .venv\Scripts\activate.bat || (echo [ERROR] Could not activate venv & pause & exit /b 1)

echo [INFO] Python/Pip:
python -V
pip -V

echo [INFO] Installing requirements (first run may take a moment)...
pip install -r requirements.txt

echo [INFO] Launching server at http://127.0.0.1:8000
python -m uvicorn app:app --reload

echo.
echo Server stopped. Press any key to close this window...
pause >nul
