@echo off
cls
REM Change to the directory where the .bat file is located
cd /d "%~dp0"

start cmd /k ts-desktop100.exe

pause