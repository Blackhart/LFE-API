from api.core.uuid import generate_time_based_uuid
from api.models.poco.bank_account import BankAccount


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
    uid = generate_time_based_uuid()

    return BankAccount.objects.create(id=uid, name=name, type=type, balance=balance, budget_id=budget_id)


def delete_bank_account(id):
    """ Delete a bank account

    Args:
        id (str): ID of the bank account to delete
    """
    bank_account = get_bank_account(id)
    
    bank_account.delete()


def rename_bank_account(id, name):
    """ Rename a bank account

    Args:
        id (str): ID of the bank account to rename
        name (str): Name of the bank account

    Returns:
        BankAccount: The bank account with the new name
    """
    BankAccount.objects.filter(id=id).update(name=name)

    return BankAccount.objects.get(id=id)


def list_bank_accounts():
    """ Return the list of all bank accounts

    Returns:
        list: List of bank accounts
    """
    return BankAccount.objects.all()


def get_bank_account(id):
    """ Return a bank account

    Args:
        id (str): ID of the bank account

    Returns:
        BankAccount: The bank account
    """
    return BankAccount.objects.get(id=id)


def is_bank_account_exists(id):
    """ Check if the bank account exists

    Args:
        id (str): ID of the bank account

    Returns:
        bool: True if the bank account exists; False otherwise
    """
    return BankAccount.objects.filter(id=id).exists()
