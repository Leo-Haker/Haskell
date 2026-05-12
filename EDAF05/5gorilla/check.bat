@echo off
:: make executable: just run it as check_solution.bat
:: run: check_solution.bat pypy A.py
:: or
:: check_solution.bat java solution
:: check_solution.bat a.exe

for /r data %%f in (*.in) do (
    echo %%f
    set "pre=%%~dpnf"
    set "out=%%~dpnf.out"
    set "ans=%%~dpnf.ans"
    set "verdict=%%~dpnf.verd"

    %* < "%%f" > "%%~dpnf.out"
    python3 output_validator/output_validator.py "%%f" "%%~dpnf.out" "%%~dpnf.ans" > "%%~dpnf.verd"

    echo Checking solution...

    findstr /x "success" "%%~dpnf.verd" > nul
    if !errorlevel! == 0 (
        echo Correct!
    ) else (
        findstr /x "uhoh" "%%~dpnf.verd" > nul
        if !errorlevel! == 0 (
            echo You got better result than the answer key. Please contact a lab instructor.
        ) else (
            echo %%f Incorrect!
            exit /b 1
        )
    )
)