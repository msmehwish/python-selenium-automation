# 2. Make a test case with a loop. You can use color selection for any product page you like.
# It should loop through colors and click on each color and verify that color has been selected.

from selenium.webdriver.common.by import By
from behave import given, when,then


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id}')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify user can click through each color')
def verify_color_clicks(context):
    expected_colors = ['A-Pink', 'A-Rainbow']

    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []
    for color in color_options:
        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color_name]

    print('\nActual colors:', actual_colors)
    assert expected_colors == actual_colors, f'Actual {actual_colors} do not match expected {expected_colors}'
