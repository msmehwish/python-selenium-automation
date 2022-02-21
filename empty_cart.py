# 3. Your Amazon Cart is empty.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\mehwi\\Desktop\\cd Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.CSS_SELECTOR, '#nav-cart').send_keys(Keys.ENTER)

expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"
print('Test case passed')
driver.quit()


