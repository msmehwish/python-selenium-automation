from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when,then


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
CLICK_ADD = (By.CSS_SELECTOR, '#add-to-cart-button')
CART = (By.ID, 'nav-cart-count')


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for {keyword}')
def search_product(context, keyword):
    context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def CLICK_ADD(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').send_keys(Keys.ENTER)


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f"expected {expected_count}, but got {actual_text}"