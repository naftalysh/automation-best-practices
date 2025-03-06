from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU rendering
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Add additional arguments to suppress warnings
chrome_options.add_argument('--log-level=3')  # Suppress logs
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')

# Path to your downloaded ChromeDriver
chrome_driver_path = r"C:\Naftaly\WorkMaterials\automation-best-practices\Selenium\selenium-drivers\win\chromedriver-win64\chromedriver.exe"

# Set up the Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google's homepage
driver.get("https://www.google.com/")
print("Navigated to Google")

# Locate the search input field by its NAME attribute
element = driver.find_element(By.NAME, "q")
print("Found search box")
element.send_keys("Selenium")
print("Entered text into search box")
element.submit()
print("Submitted the search form")

# Close the browser
driver.quit()
print("Closed the browser")



"""
Explanation of Added Arguments
--log-level=3: Suppresses all logs except for fatal errors.
--disable-extensions: Disables extensions which might trigger warnings.
--disable-dev-shm-usage: Overcomes limited resource problems.
--disable-popup-blocking: Disables popup blocking.
--disable-notifications: Disables notifications.
--disable-infobars: Disables infobars that may appear.
"""