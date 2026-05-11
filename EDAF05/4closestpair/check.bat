@echo off
setlocal enabledelayedexpansion

:: run like:
:: check_solution.bat python A.py
:: check_solution.bat pypy A.py
:: check_solution.bat java solution
:: check_solution.bat a.exe

for %%f in (data\sample\*.in data\more\*.in data\secret\*.in) do (
    echo %%f

    set "pre=%%~dpnf"
    set "out=%%~dpnf.out"
    set "ans=%%~dpnf.ans"

    :: run program
    %* < "%%f" > "!out!"

    :: compare files (ignore whitespace differences)
    fc /W "!ans!" "!out!" >nul

    if errorlevel 1 (
        echo %%f Incorrect!
        exit /b 1
    ) else (
        echo Correct!
    )
)

endlocal