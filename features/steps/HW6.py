from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then, when


@given('Open Amazon T&C page')
def open_amazon_tnc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_amazon_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def amazon_app_page_opened(context):
    context.driver.find_element(By.CSS_SELECTOR, '.help-content')


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    current_window = context.driver.window_handles
    print('\nCurrent:', current_window)
    context.driver.switch_to.window(context.original_window)