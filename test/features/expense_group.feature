Feature: Expense Group Operations

    Scenario: Create an expense group
        When the user creates an expense group
        Then the system creates the expense group
        And the system returns an unique identifier for the expense group

    Scenario: Create an expense group with an empty name
        When the user creates an expense group with an empty name
        Then the system returns error 1