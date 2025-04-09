@echo off
echo Starting PyWeatherClock...
python launch_pyweatherclock.py
if %ERRORLEVEL% NEQ 0 (
  echo Failed to run PyWeatherClock
  echo Try installing dependencies with: pip install -r requirements.txt
  pause
)
