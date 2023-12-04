Feature: Bank Account Operations

    Scenario: Create a standard bank account
        When the user creates a standard bank account
        Then the system creates the bank account
        And the system returns an unique identifier for the bank account

    Scenario: Create a trading bank account
        When the user creates a trading bank account
        Then the system creates the bank account
        And the system returns an unique identifier for the bank account

    Scenario: Create a saving bank account
        When the user creates a saving bank account
        Then the system creates the bank account
        And the system returns an unique identifier for the bank account

    Scenario: Create a bank account with an empty name
        When the user creates a bank account with an empty name
        Then the system returns error 1

    Scenario: Create a bank account with an invalid type
        When the user creates a bank account with an invalid type
        Then the system returns error 2

    Scenario: Delete a standard bank account
        Given a standard bank account is created
        When the user deletes the bank account
        Then the system deletes the bank account

    Scenario: Delete a trading bank account
        Given a trading bank account is created
        When the user deletes the bank account
        Then the system deletes the bank account

    Scenario: Delete a saving bank account
        Given a saving bank account is created
        When the user deletes the bank account
        Then the system deletes the bank account

    Scenario: Delete a bank account with an invalid id
        When the user deletes a bank account with an invalid id
        Then the system returns error 3

    Scenario: Rename a bank account name
        Given a bank account is created
        When the user renames the bank account name to "My Renamed Bank Account"
        Then the system renames the bank account name to "My Renamed Bank Account"

    Scenario: Rename a bank account name with an invalid id
        When the user renames a bank account name using an invalid id
        Then the system returns error 3

    Scenario: Rename a bank account name to an empty name
        Given a bank account is created
        When the user renames the bank account name to an empty name
        Then the system returns error 1

    Scenario: List bank accounts
        Given a standard bank account named "List bank accounts - Standard Account" is created
        And a trading bank account named "List bank accounts - Trading Account" is created
        And a saving bank account named "List bank accounts - Saving Account" is created
        When the user list the bank accounts
        Then the system returns the three created accounts

    Scenario: Get a bank account
        Given a bank account named "Get bank account - My Account" is created
        When the user gets the bank account
        Then the system returns the bank account

    Scenario: Get a bank account using invalid id
        When the user gets a bank account using an invalid id
        Then the system returns error 3