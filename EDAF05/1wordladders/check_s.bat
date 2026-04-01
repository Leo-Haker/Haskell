@echo off
setlocal enabledelayedexpansion

REM usage:
REM   check_s.bat script.exe
REM   check_s.bat python A.py

for /R %%f in (*.in) do (
    echo Running %%f

    set "file=%%f"
    set "pre=!file:.in=!"
    set "out=!pre!.out"
    set "ans=!pre!.ans"

    call :getTime start

    %* < "%%f" > "!out!"

    call :getTime end

    set /a elapsed=end-start
    if !elapsed! lss 0 set /a elapsed+=86400000

    fc "!ans!" "!out!" > nul
    if errorlevel 1 (
        echo %%f Incorrect!  Time: !elapsed! ms
        exit /b 1
    ) else (
        echo Correct!  Time: !elapsed! ms
    )

    echo.
)

echo All tests passed.
exit /b 0

:getTime
for /f "tokens=1-4 delims=:.," %%a in ("%TIME%") do (
    set /a "%1=((1%%a-100)*3600 + (1%%b-100)*60 + (1%%c-100))*1000 + (1%%d-100)*10"
)
exit /b