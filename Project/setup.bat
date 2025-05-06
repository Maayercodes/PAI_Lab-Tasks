@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing required packages...
pip install -r requirements.txt

echo.
echo ✅ Setup Complete!
echo 💡 To start the app, run:
echo streamlit run app.py
pause
