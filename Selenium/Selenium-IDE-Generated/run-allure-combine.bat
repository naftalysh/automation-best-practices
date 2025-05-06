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

:: Serve the generated results from all directories
echo Serving combined results from all directories...
allure serve allure-results-1 allure-results-2 allure-results-3 allure-results-4 allure-results-5 allure-results-6 allure-results-7 allure-results-8 allure-results-9 allure-results-10
