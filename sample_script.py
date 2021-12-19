from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="C:\\Users\\mehwi\\Desktop\\cd Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')
sleep(3)

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()
sleep(3)

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
