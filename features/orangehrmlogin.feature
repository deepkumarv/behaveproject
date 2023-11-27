Feature: OrangeHRM Login


  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome Browser
    When I open orange HRM Home Page
    And Enter username "admin" and password "admin123"
    Then User must successfully login to Dashboard page