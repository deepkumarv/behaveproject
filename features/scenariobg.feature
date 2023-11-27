Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser

  Scenario: Login to HRM Appication
    When I open applicaiton
    And Enter valid username and password
    Then User must login to the Dashboard page