@echo off
cd C:\service\flask
if not exist "venv" (
    py -m venv venv
)
CALL venv\Scripts\activate

if not exist installed_packages.txt (
    pip install -r requirements.txt
    pip freeze > installed_packages.txt
)

set FLASK_APP=app.py
set FLASK_ENV=development
start python -m flask run --no-reload
pause
