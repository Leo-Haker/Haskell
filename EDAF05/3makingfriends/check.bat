@echo off
REM Run: check_solution.bat python A.py
REM or: check_solution.bat java Solution
REM or: check_solution.bat a.exe

for /R data %%f in (*.in) do (
echo %%f
set "file=%%f"

```
REM ta bort .in
set "pre=%%~dpnf"

set "out=!pre!.out"
set "ans=!pre!.ans"

REM kör programmet
%* < "%%f" > "!out!"

REM jämför filer
fc /W "!ans!" "!out!" > nul
if errorlevel 1 (
    echo %%f Incorrect!
    exit /b 1
) else (
    echo Correct!
)
```

)
