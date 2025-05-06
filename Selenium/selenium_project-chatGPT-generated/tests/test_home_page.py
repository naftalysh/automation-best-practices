import pytest
from selenium import webdriver
from pages.home_page import HomePage


@pytest.fixture(scope="module")
def driver():
    """
    Pytest fixture to initialize and clean up the WebDriver instance.

    :return: Instance of WebDriver
    """
    driver = (
        webdriver.Chrome()
    )  # Ensure the chromedriver is in your PATH or provide the executable path
    yield driver
    driver.quit()


def test_search_functionality(driver, benchmark):
    """
    Test to verify the search functionality on the home page.

    :param driver: Instance of WebDriver
    :param benchmark: Pytest-benchmark fixture
    """
    home_page = HomePage(driver)

    def search():
        home_page.search("family tree")
        assert "Results" in driver.page_source

    benchmark(search)


def test_sign_in(driver, benchmark):
    """
    Test to verify the sign-in functionality on the home page.

    :param driver: Instance of WebDriver
    :param benchmark: Pytest-benchmark fixture
    """
    home_page = HomePage(driver)

    # Use test credentials (replace with valid test credentials if available)
    email = "test@example.com"
    password = "password"

    def sign_in():
        home_page.sign_in(email, password)
        assert (
            "Welcome" in driver.page_source
        )  # Adjust the assertion based on the actual success message

    benchmark(sign_in)
