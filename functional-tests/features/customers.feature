Feature: Customer directory
  Scenario: Customer search endpoint responds
    Given the customer directory API is available
    When I search for a customer
    Then the response should be successful
