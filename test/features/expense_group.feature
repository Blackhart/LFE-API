Feature: Expense Group Operations

    Scenario: Create an expense group
        When the user creates an expense group
        Then the system creates the expense group
        And the system returns an unique identifier for the expense group

    Scenario: Create an expense group with an empty name
        When the user creates an expense group with an empty name
        Then the system returns error 1

    Scenario: Delete an expense group
        Given an expense group is created
        When the user deletes the expense group
        Then the system deletes the expense group

    Scenario: Delete an expense group using an invalid id
        When the user deletes an expense group using an invalid id
        Then the system returns error 3

    Scenario: Rename an expense group name
        Given an expense group is created
        When the user renames the expense group name to "My Renamed Expense Group"
        Then the system renames the expense group name to "My Renamed Expense Group"

    Scenario: Rename a expense group name with an invalid id
        When the user renames a expense group name using an invalid id
        Then the system returns error 3

    Scenario: Rename a expense group name to an empty name
        Given an expense group is created
        When the user renames the expense group name to an empty name
        Then the system returns error 1

    Scenario: List expense groups
        Given an expense group named "List expense groups - Group 1" is created
        And an expense group named "List expense groups - Group 2" is created
        And an expense group named "List expense groups - Group 3" is created
        When the user list the expense groups
        Then the system returns the three created expense groups

    Scenario: Get an expense group
        Given an expense group named "Get Expense Group - My Group" is created
        When the user gets the expense group
        Then the system returns the expense group

    Scenario: Get an expense group using an invalid id
        When the user gets an expense group using an invalid id
        Then the system returns error 3