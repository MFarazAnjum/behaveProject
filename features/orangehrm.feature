Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orangehrm homepage
    Then verify that the logo present on page
    And close browser