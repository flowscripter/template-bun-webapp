Feature: Webapp

  Scenario: Webapp success
    When the webapp URL "index.html" is loaded
    And the page element with ID "console" is available
    Then the page element with ID "console" should have text "INFO Hello"
    Then the page element with ID "console" should have text "INFO World"
    Then the page element with ID "console" should have text "INFO Hello"
    Then the page element with ID "console" should have text "INFO World 4"
