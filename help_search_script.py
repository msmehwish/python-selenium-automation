from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\mehwi\\Desktop\\cd Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order')

driver.find_element(By.ID, 'helpsearch').send_keys(Keys.ENTER)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, '//h1').text

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"
print('Test case passed')
driver.quit()




