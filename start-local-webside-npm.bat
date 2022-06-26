@echo off
echo.This program starts a local server
echo.Then open your default browser and navigate to this folder of websites
echo.The server will be terminated when the window is closed

@REM set web_port=%random%
set web_port=4096

echo.
echo.Http: 127.0.0.1
echo.Port: %web_port%

echo.
start http://127.0.0.1:%web_port%/
npx http-server -p %web_port%
