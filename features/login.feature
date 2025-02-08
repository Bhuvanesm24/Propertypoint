Feature: To test the login functionalities

  Scenario Outline: login with valid creditianls
    Given Navigate to login page
    When Enter the valid user name as "<email>"
    And Enter the valid password as "<password>"
    And Click on login button
    Then Moving to login page
    Examples:
      | email             | password |
      | bhuvi@gmail.com   | 12345    |
      | bhuvi100@gmai.com | 12345    |
      | bhuvi43@gmai.com  | 12345    |


  Scenario: login with valid user and invalid password
    Given Navigate to login page
    When Enter the valid user name as "bhuvi@gmail.com"
    And Enter the Invalid password
    And Click on login button
    Then Error message should be displayed

   Scenario: login with Invalid user and valid password
    Given Navigate to login page
    When Enter the Invalid user name
    And Enter the valid password as "12345"
    And Click on login button
    Then Error message should be displayed

  Scenario: login without entering the creaditals
    Given Navigate to login page
    When Click on login button
    Then Error message should be displayed