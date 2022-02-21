# 1) Find the most optimal locators for Create Account (Registration) page elements:
# https://www.amazon.com/ap/register?openid.return_to=https%3A%%2Ftrack.amazon.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_shippingrecipientcentral_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0

from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# Amazon logo:
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# Create account header:
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# Your name field:
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
# Email field:
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
# Password field:
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
# Password  must be at least 6 characters:
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info')
# Re-enter password field:
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Create your Amazon account button:
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of use link:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_register_notification_condition_of_use']")
# Privacy Notice link:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_register_notification_privacy_notice']")
# Sign in link:
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')