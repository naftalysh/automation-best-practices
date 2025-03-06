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
chrome_options.add_argument('--log-level=3')  # Suppress logs
chrome_options.add_argument('--disable-extensions')
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
--headless: Runs Chrome without displaying the browser window.
--disable-gpu: Turns off GPU hardware acceleration to avoid issues in headless mode.
--no-sandbox: Bypasses Chrome's security model to avoid permission issues, mainly in certain environments like Docker.
--disable-dev-shm-usage: Avoids using shared memory, useful for environments with limited resources.
--log-level=3: Suppresses all logs except for fatal errors.
--disable-extensions: Turns off all browser extensions.
--disable-popup-blocking: Prevents Chrome from blocking pop-up windows.
--disable-notifications: Stops web notifications from appearing.
--disable-infobars: Hides the message that says "Chrome is being controlled by automated test software".
"""