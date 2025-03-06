
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    BasePage acts as a parent class for all page classes.
    It contains common methods for interacting with web elements.
    """

    def __init__(self, driver):
        """
        Initializes the BasePage with a WebDriver instance.
        
        :param driver: Instance of WebDriver
        """
        self.driver = driver

    def find_element(self, *locator):
        """
        Finds a web element using the specified locator.
        
        :param locator: Locator tuple to identify the element
        :return: WebElement found
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, *locator):
        """
        Clicks on a web element identified by the locator.
        
        :param locator: Locator tuple to identify the element
        """
        self.find_element(*locator).click()

    def enter_text(self, text, *locator):
        """
        Enters text into a web element identified by the locator.
        
        :param text: Text to enter
        :param locator: Locator tuple to identify the element
        """
        self.find_element(*locator).send_keys(text)
        
    def get_text(self, *locator):
        """
        Gets the text of a web element identified by the locator.
        
        :param locator: Locator tuple to identify the element
        :return: Text of the web element
        """
        return self.find_element(*locator).text
