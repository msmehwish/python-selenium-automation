# steps file
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

help_search = (By.ID, 'helpsearch')
RESULT = (By.XPATH, '//h1')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search for "Cancel order"')
def cancel_order(context):
    context.driver.find_element(*help_search).send_keys('Cancel order')
    context.driver.find_element(*help_search).send_keys(Keys.ENTER)


@then('Verify Cancel Items or Orders text')
def verify_result(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"