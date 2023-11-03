Feature: OrangeHRM Login
  Background: common steps
    Given I launch browser
    When I open orangeHRM
    And Enter valid username and password
    And click on login


  Scenario: Login to OrangeHRM
    Then User must login to the Dashboard page


  Scenario: Search User
    When navigate to search page
    Then search page should display


  Scenario: Advanced Search User
    When navigate to advanced search page
    Then advanced search page should display