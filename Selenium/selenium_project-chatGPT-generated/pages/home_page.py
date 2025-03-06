
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    HomePage represents the home page of the website.
    It contains methods to interact with elements on the home page.
    """
    # Locators for elements on the home page
    SEARCH_INPUT = (By.ID, "search-bar")  # Example, update with actual ID
    SEARCH_BUTTON = (By.ID, "search-button")  # Example, update with actual ID
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")
    SIGN_UP_BUTTON = (By.LINK_TEXT, "Sign up")
    LOGIN_EMAIL_INPUT = (By.ID, "email")  # Example, update with actual ID
    LOGIN_PASSWORD_INPUT = (By.ID, "password")  # Example, update with actual ID
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        """
        Initializes the HomePage with a WebDriver instance and navigates to the home page URL.
        
        :param driver: Instance of WebDriver
        """
        super().__init__(driver)
        self.driver.get("https://www.myheritage.co.il/")

    def search(self, query):
        """
        Performs a search action on the home page.
        
        :param query: Search query string
        """
        self.enter_text(query, *self.SEARCH_INPUT)
        self.click_element(*self.SEARCH_BUTTON)
        
    def sign_in(self, email, password):
        """
        Performs a sign-in action on the home page.
        
        :param email: User email
        :param password: User password
        """
        self.click_element(*self.SIGN_IN_BUTTON)
        self.enter_text(email, *self.LOGIN_EMAIL_INPUT)
        self.enter_text(password, *self.LOGIN_PASSWORD_INPUT)
        self.click_element(*self.LOGIN_SUBMIT_BUTTON)
