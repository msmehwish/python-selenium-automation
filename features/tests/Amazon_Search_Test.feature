# Created by mehwi at 3/8/2022
Feature: # Tests case for Amazon search

  Scenario: User can add a product to the cart
    Given Open Amazon
    When Search for HP Laptop i7
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)