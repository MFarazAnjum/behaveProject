Feature: OrangeHRM Login


#  Scenario: Login to OrangeHRM with valid parameters
#    Given I launch Chrome browser
#    When I open orangeHRM homepage
#    And Enter username "Admin" and password "admin123"
#    And click on login button
#    Then User must successfully login to the Dashboard page

#  Scenario: Login to OrangeHRM without parameters
#    Given I launch Chrome browser
#    When I open orangeHRM homepage
#    And click on login button
#    Then Proper message should be displayed

  Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch Chrome browser
    When I open orangeHRM homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to the Dashboard page with "<message>"

    Examples:
      | username | password | message |
      | asdsad | asdfasdf | Invalid credentials |
      | Admin | admin123 | Dashboard |
      | empty | empty | Required |