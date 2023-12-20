from api.core.exceptions import IDNotFound
from api.core.uuid import generate_time_based_uuid
from api.model.db import bank_accounts
from api.model.poco.bank_account import BankAccount
from api.data.constant import USER_ERR_3


def create_bank_account(name, type, balance, budget_id):
    """ Create a bank account

    Args:
        name (str): Name of the bank account
        type (str): Type of the bank account
        balance (float): Starting balance of the bank account
        budget_id (str): Budget ID to link to

    Returns:
        BankAccount: The created bank account
    """
    account = BankAccount(
        id=generate_time_based_uuid(),
        name=name,
        type=type,
        balance=balance,
        budget_id=budget_id
    )

    bank_accounts.append(account)

    return account


def delete_bank_account(id):
    """ Delete a bank account

    Args:
        id (str): ID of the bank account to delete

    Raises:
        IDNotFound: If the bank account doesn't exist
    """
    idx = [
        idx
        for idx, account
        in enumerate(bank_accounts)
        if account.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_remove = next(iter(idx))

    bank_accounts.pop(idx_to_remove)


def rename_bank_account(id, name):
    """ Rename a bank account

    Args:
        id (str): ID of the bank account to rename
        name (str): Name of the bank account

    Raises:
        IDNotFound: If the bank account doesn't exist

    Returns:
        BankAccount: The bank account with the new name
    """
    idx = [
        idx
        for idx, account
        in enumerate(bank_accounts)
        if account.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_update = next(iter(idx))

    bank_accounts[idx_to_update].name = name

    return bank_accounts[idx_to_update]


def list_bank_accounts():
    """ Return the list of all bank accounts

    Returns:
        list: List of bank accounts
    """
    return bank_accounts


def get_bank_account(id):
    """ Return a bank account

    Args:
        id (str): ID of the bank account

    Raises:
        IDNotFound: If the bank account doesn't exist

    Returns:
        BankAccount: The bank account
    """
    idx = [
        idx
        for idx, account
        in enumerate(bank_accounts)
        if account.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_get = next(iter(idx))

    return bank_accounts[idx_to_get]


def is_bank_account_exists(id):
    """ Check if the bank account exists

    Args:
        id (str): ID of the bank account

    Returns:
        bool: True if the bank account exists; False otherwise
    """
    idx = [
        idx
        for idx, account
        in enumerate(bank_accounts)
        if account.id == id
    ]

    if not idx:
        return False

    return True
