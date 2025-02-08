Feature: To test the register functionalities
@page
  Scenario: Register with mandatory fields
    Given Navigate to register page
    When Enter details into mandatory field
      | firstname | lastname | mobilenumber | password | confirmpassword |
      | Bhuvanes  | waran    | 9994551234   | 12345    | 12345           |
  And CLick on continue button
    Then Account should created

  Scenario: Register with all fields
    Given Navigate to register page
    When Enter details into mandatory field
      | firstname | lastname | mobilenumber | password | confrimpassword |
      | Bhuvanes  | waran    | 9994551234   | 12345    | 12345           |
    And Enter details into optional field
    And CLick on continue button
    Then Account should created

  Scenario: Register with duplicate values
    Given Navigate to register page
    When Enter details into all field expect email fields
    And Enter details into existing email field
    And CLick on continue button
    Then Proper error message should displayed in duplicate email filed

  Scenario: Register with duplicate values
    Given Navigate to register page
    When Should not enter any fields
    And CLick on continue button
    Then Proper error message should displayed in all mandotary filed