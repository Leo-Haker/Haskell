@echo off
setlocal enabledelayedexpansion

REM usage:
REM check_solution.bat pypy A.py
REM check_solution.bat java solution
REM check_solution.bat a.exe

for /r data %%f in (*.in) do (
    echo %%f

    set "pre=%%~dpnf"
    set "out=%%~dpnf.out"
    set "ans=%%~dpnf.ans"
    set "verdict=%%~dpnf.verd"

    REM run solution
    %* < "%%f" > "!out!"

    REM validate
    python output_validator\output_validator.py "%%f" "!out!" "!ans!" > "!verdict!"

    echo Checking solution...

    findstr /x "success" "!verdict!" >nul
    if !errorlevel! == 0 (
        echo Correct!
    ) else (
        findstr /x "uhoh" "!verdict!" >nul
        if !errorlevel! == 0 (
            echo You got better result than the answer key. Please contact a lab instructor.
        ) else (
            echo %%f Incorrect!
            exit /b 1
        )
    )
)

endlocal