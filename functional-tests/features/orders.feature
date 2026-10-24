Feature: Order submission
  Scenario: Submit a small order
    Given the OrderFlow API is available
    When I submit a valid order
    Then the order should be created
