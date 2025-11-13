@echo off
:: Launch-Windows.bat
setlocal
cd /d "%~dp0"
if not exist ConnectFourCLI.class (
    javac ConnectFourCLI.java
    if errorlevel 1 (
        echo Compilation failed.
        pause
        exit /b 1
    )
)
java ConnectFourCLI --time 15 --ai-first true --ansi true --anim true --anim-delay 40
echo.
pause