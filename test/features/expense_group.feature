Feature: Expense Group Operations

    Scenario: Create an expense group
        When the user creates an expense group
        Then the system creates the expense group
        And the system returns an unique identifier for the expense group

    Scenario: Create an expense group with an empty name
        When the user creates an expense group with an empty name
        Then the system returns error 1

    Scenario: Get an expense group
        Given an expense group named "Get Expense Group - My Group" is created
        When the user gets the expense group
        Then the system returns the expense group

    Scenario: Get an expense group using an invalid id
        When the user gets an expense group using an invalid id
        Then the system returns error 3