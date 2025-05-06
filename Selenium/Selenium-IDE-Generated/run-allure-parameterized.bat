@echo off
setlocal EnableDelayedExpansion

:: Prompt user for the parameter range limit
set /p rangeLimit=Enter the range limit for the test parameter (e.g., 10):

:: Clean up the old allure-results directory
if exist allure-results (
    echo Cleaning up old allure-results
    rd /s /q allure-results
)
mkdir allure-results

:: Run pytest with parameterized tests using the input range limit
echo Running pytest with parameterized tests using range limit of %rangeLimit%
pytest test_myFirstTestCase-with-Allure-reporting-with-param.py --alluredir=allure-results -v --range-limit %rangeLimit%

:: Serve the generated results
echo Serving the results from allure-results directory...
allure serve allure-results
