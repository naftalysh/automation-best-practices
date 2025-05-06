@echo off
setlocal EnableDelayedExpansion

:: Define the range for the number of test runs
set "startIndex=1"
set "endIndex=10"

:: Clean up any old allure-results directories and create new ones
for /L %%i in (%startIndex%,1,%endIndex%) do (
    if exist allure-results-%%i (
        echo Cleaning up old allure-results-%%i
        rd /s /q allure-results-%%i
    )
    mkdir allure-results-%%i
)

:: Run pytest to generate Allure results for each run
for /L %%i in (%startIndex%,1,%endIndex%) do (
    echo Running pytest for allure-results-%%i
    pytest test_myFirstTestCase-with-Allure-reporting.py --alluredir=allure-results-%%i -v
    echo Completed pytest for allure-results-%%i, check the contents of the directory.
    :: Check if the allure-results-%%i directory contains JSON files
    if exist allure-results-%%i\*.json (
        echo allure-results-%%i contains JSON files, proceeding...
    ) else (
        echo Error: allure-results-%%i does not contain any JSON files! Check the pytest execution.
        exit /b 1
    )
)

:: Initialize the allure generate command with the --clean option
set "allureGenerateCommand=allure generate --clean"

:: Loop from 1 to 10 to build the allure generate command with all directories
for /L %%i in (%startIndex%,1,%endIndex%) do (
    set "allureGenerateCommand=!allureGenerateCommand! allure-results-%%i"
)

:: Add the output directory for merged results
set "allureGenerateCommand=!allureGenerateCommand! -o merged-results"

:: Execute the constructed generate command and check for errors
echo Running: !allureGenerateCommand!
call !allureGenerateCommand!

:: Check if the merged-results directory is created
if exist merged-results (
    echo Merged results generated successfully.
) else (
    echo Error: Merged results directory was not created!
    exit /b 1
)

:: Verify merged-results directory contents
if exist merged-results\data\*.json (
    echo Merged results directory has data.
) else (
    echo Warning: Merged results directory does not have JSON data files!
    exit /b 1
)

:: Serve the merged results if the directory exists
if exist merged-results (
    echo Serving merged results...
    call allure serve merged-results
) else (
    echo Error: Cannot serve the merged results because the directory is missing!
)
