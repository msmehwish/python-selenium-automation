# Created by mehwi at 2/20/2022
Feature: Tests for Amazon empty cart

  Scenario: User can search for empty cart
    Given opens amazon.com
    When clicks on the cart icon
    Then verifies that Your Amazon Cart is empty

