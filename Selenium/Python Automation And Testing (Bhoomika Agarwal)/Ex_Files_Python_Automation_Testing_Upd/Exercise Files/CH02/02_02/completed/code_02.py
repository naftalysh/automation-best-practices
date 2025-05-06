from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# Properly formatted file path with raw string and escaped spaces
html_file = r"C:\Naftaly\WorkMaterials\automation-best-practices\Selenium\Python Automation And Testing (Bhoomika Agarwal)\Ex_Files_Python_Automation_Testing_Upd\Exercise Files\CH02\html_code_02.html"
# driver.get(html_file)
driver.get("file://" + html_file)

# Find the search box using the name attribute
login_form = driver.find_element(By.ID, "loginForm")
# login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
