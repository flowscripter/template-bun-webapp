Feature: Webapp

  Scenario: Webapp success
    When the webapp URL "index.html" is loaded
    And the page element with ID "console" is available
    Then the page element with ID "console" should have text "Hello"
    Then the page element with ID "console" should have text "World 6"
