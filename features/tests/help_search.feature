# Created by mehwi at 2/20/2022
Feature: Tests for help search
  # Enter feature description here

  Scenario: User can search for solutions of Canceling an order on Amazon
    Given Open Amazon page
    When Search for "Cancel order"
    Then Verify Cancel Items or Orders text

