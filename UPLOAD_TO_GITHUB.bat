@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem Simple GitHub uploader for ekzamen2_test
rem ASCII only. No BOM.

cd /d "%~dp0"

set "REMOTE_URL=https://github.com/TheLER0N/ekzamen2_test.git"

echo.
echo ==========================================
echo  ekzamen2_test - Simple GitHub Upload
echo ==========================================
echo.
echo This script uploads ALL current project changes.
echo Target remote:
echo   %REMOTE_URL%
echo.

if not exist "pyproject.toml" (
    echo ERROR: pyproject.toml not found.
    echo Put this BAT file in the root folder of the ekzamen2 project.
    echo.
    pause
    exit /b 1
)

where git >nul 2>nul
if errorlevel 1 (
    echo ERROR: Git not found.
    echo Install Git for Windows and try again.
    echo.
    pause
    exit /b 1
)

git rev-parse --is-inside-work-tree >nul 2>nul
if errorlevel 1 (
    echo.
    echo Git repository not found. Initializing repository...
    git init
    if errorlevel 1 goto FAIL
)

git remote get-url origin >nul 2>nul
if errorlevel 1 (
    echo.
    echo Adding GitHub remote origin...
    git remote add origin "%REMOTE_URL%"
    if errorlevel 1 goto FAIL
) else (
    for /f "delims=" %%R in ('git remote get-url origin') do set "CURRENT_REMOTE=%%R"
    if /I not "!CURRENT_REMOTE!"=="%REMOTE_URL%" (
        echo.
        echo WARNING: origin points to:
        echo   !CURRENT_REMOTE!
        echo Expected:
        echo   %REMOTE_URL%
        echo.
        set "REMOTE_CONFIRM="
        set /p REMOTE_CONFIRM=Replace origin with expected GitHub URL? Type Y: 
        if /I "!REMOTE_CONFIRM!"=="Y" (
            git remote set-url origin "%REMOTE_URL%"
            if errorlevel 1 goto FAIL
        ) else (
            echo Cancelled.
            echo.
            pause
            exit /b 0
        )
    )
)

echo.
echo Current Git status:
echo ------------------------------------------
git status --short
echo ------------------------------------------
echo.

set "CONFIRM="
set /p CONFIRM=Upload these changes to GitHub? Type Y to continue: 
if /I not "%CONFIRM%"=="Y" (
    echo Cancelled.
    echo.
    pause
    exit /b 0
)

echo.
set "BRANCH=main"
set /p BRANCH=Branch to upload to [main]: 
if "%BRANCH%"=="" set "BRANCH=main"

echo.
set "MSG=update"
set /p MSG=Commit comment [update]: 
if "%MSG%"=="" set "MSG=update"

echo.
echo Upload plan:
echo   Remote: %REMOTE_URL%
echo   Branch: %BRANCH%
echo   Comment: %MSG%
echo.
set "CONFIRM2="
set /p CONFIRM2=Confirm upload? Type Y: 
if /I not "%CONFIRM2%"=="Y" (
    echo Cancelled.
    echo.
    pause
    exit /b 0
)

echo.
echo Switching local branch to %BRANCH%...
git branch -M "%BRANCH%"
if errorlevel 1 goto FAIL

echo.
echo Adding files...
git add -A
if errorlevel 1 goto FAIL

echo.
echo Creating commit...
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "%MSG%"
    if errorlevel 1 goto FAIL
) else (
    echo No staged changes. Skipping commit.
)

echo.
echo Checking GitHub branch origin/%BRANCH%...
git ls-remote --exit-code --heads origin "%BRANCH%" >nul 2>nul
if errorlevel 1 (
    echo Remote branch does not exist yet. Skipping pull.
) else (
    echo Pulling latest changes from origin/%BRANCH%...
    git pull --rebase --autostash origin "%BRANCH%"
    if errorlevel 1 (
        echo.
        echo ERROR: Pull/rebase failed.
        echo Fix conflicts manually, then run this BAT again.
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Pushing to origin/%BRANCH%...
git push -u origin HEAD:"%BRANCH%"
if errorlevel 1 goto FAIL

echo.
echo ==========================================
echo  DONE. Uploaded to GitHub branch: %BRANCH%
echo ==========================================
echo.
pause
exit /b 0

:FAIL
echo.
echo ERROR: Upload failed. Check the message above.
echo.
pause
exit /b 1

