#1. Go over your code and remove sleep(). Replace sleep() with wait.until if needed.

# from selenium import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path="C:\\Users\\mehwi\\Desktop\\cd Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()


# Explicit wait
driver.wait = WebDriverWait(driver, 5)


# open the url
driver.get('https://www.google.com/')


search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# click search
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn)).click()


# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')


driver.quit()