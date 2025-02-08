Feature: To test the search functionalities

  Scenario: Search the valid product
    Given Navigate to home page
    When Enter the valid product into the search box
    And Click on search button
    Then Valid product should displayed

  Scenario: Search the invalid product
    Given Navigate to home page
    When Enter the invalid product into the search box
    And Click on search button
    Then Proper error message should be displayed

  Scenario: Search without enter the product name
    Given Navigate to home page
    When Search without entering the product name in search filed
    And Click on search button
    Then Proper error message should be displayed