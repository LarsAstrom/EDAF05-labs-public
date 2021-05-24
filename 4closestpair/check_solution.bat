@echo off
for /r %%f in (data\sample\*.in data\more\*.in data\secret\*.in) do (
    echo Running on %%~nxf...
    %* < "%%f" > "%%~pnf.out"
    fc /w "%%~pnf.ans" "%%~pnf.out" > nul
    if errorlevel 1 (
        echo %%~nxf Incorrect!
        exit /B 1
    ) else (
        echo Correct!
    )
)
