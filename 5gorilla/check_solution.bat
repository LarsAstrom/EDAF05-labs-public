@echo off
for /r %%f in (data\sample\*.in data\secret\*.in) do (
    echo Running on %%~nxf...
    %* < "%%f" > "%%~pnf.out"
    echo Checking...
    del "%%~pnf.verd"
    python3 output_validator/output_validator.py "%%f" "%%~pnf.out" "%%~pnf.ans" > "%%~pnf.verd"
    find "success" "%%~pnf.verd" > nul
    if errorlevel 1 (
        echo %%~nxf Incorrect!
        exit /B 1
    ) else (
        echo Correct!
    )
)
