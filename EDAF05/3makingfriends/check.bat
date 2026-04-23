@echo off
setlocal enabledelayedexpansion

for /R data %%f in (*.in) do (
    echo %%f

    set "pre=%%~dpnf"
    set "out=!pre!.out"
    set "ans=!pre!.ans"

    REM --- start time ---
    set "start=!time!"

    REM run program
    %* < "%%f" > "!out!"

    REM --- end time ---
    set "end=!time!"

    REM --- convert times to centiseconds ---
    call :timeToCS "!start!" startCS
    call :timeToCS "!end!" endCS

    set /a elapsed=!endCS! - !startCS!
    if !elapsed! lss 0 set /a elapsed+=8640000

    REM --- compare output ---
    fc /W "!ans!" "!out!" > nul
    if errorlevel 1 (
        echo Incorrect! Time: !elapsed! cs
        exit /b 1
    ) else (
        echo Correct! Time: !elapsed! cs
    )
)

exit /b

REM --- function to convert HH:MM:SS.cc to centiseconds ---
:timeToCS
setlocal
set "t=%~1"

for /f "tokens=1-4 delims=:." %%a in ("%t%") do (
    set /a cs=((%%a*3600)+(%%b*60)+%%c)*100+%%d
)

endlocal & set "%2=%cs%"
exit /b