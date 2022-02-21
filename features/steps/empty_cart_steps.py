# steps file
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then


amazon_carts = (By.CSS_SELECTOR, '#nav-cart')
amazon_result = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')


@given('opens amazon.com')
def cart_page(context):
    context.driver.get('https://www.amazon.com/')


@when('clicks on the cart icon')
def cart_icon(context):
    context.driver.find_element(*amazon_carts).send_keys(Keys.ENTER)


@then('verifies that Your Amazon Cart is empty')
def cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(*amazon_result).text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"