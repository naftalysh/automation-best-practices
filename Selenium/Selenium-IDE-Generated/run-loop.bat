@echo off
setlocal EnableDelayedExpansion

:: Generate test results for each run, creating the directory if it doesn't exist
for /L %%i in (1,1,10) do (
    if not exist allure-results-%%i mkdir allure-results-%%i
    echo Running pytest for allure-results-%%i
    pytest test_myFirstTestCase-with-Allure-reporting.py --alluredir=allure-results-%%i -v
    echo Completed pytest for allure-results-%%i, check the contents of the directory.
)

:: Initialize the allure generate command with the --clean option
set "allureGenerateCommand=allure generate --clean"

:: Loop from 1 to 10 to build the allure generate command with all directories
for /L %%i in (1,1,10) do (
    set "allureGenerateCommand=!allureGenerateCommand! allure-results-%%i"
)

:: Add the output directory for merged results
set "allureGenerateCommand=!allureGenerateCommand! -o merged-results"

:: Execute the constructed generate command
echo Running: !allureGenerateCommand!
call !allureGenerateCommand!

:: Serve the merged results
echo Serving merged results...
call allure serve merged-results
