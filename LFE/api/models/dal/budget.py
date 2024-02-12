from api.core.uuid import generate_time_based_uuid
from api.models.poco.budget import Budget
from api.models.dal.bank_account import list_transactions_by_bank_account


def list_budgets():
    """ Get all budgets

    Returns:
        list: The list of budgets
    """
    return Budget.objects.all()


def create_budget(name):
    """ Create a budget

    Args:
        name (str): Name of the budget

    Returns:
        Budget: The created budget
    """
    uid = generate_time_based_uuid()

    return Budget.objects.create(id=uid, name=name)


def delete_budget(id):
    """ Delete a budget

    Args:
        id (str): ID of the budget to delete
    """
    budget = get_budget(id)

    budget.delete()


def rename_budget(id, name):
    """ Rename a budget

    Args:
        id (str): ID of the budget to rename
        name (str): Name of the budget

    Returns:
        Budget: The renamed budget
    """
    Budget.objects.filter(id=id).update(name=name)

    return Budget.objects.get(id=id)


def get_budget(id):
    """ Get a budget

    Args:
        id (str): ID of the budget

    Returns:
        Budget: The budget
    """
    return Budget.objects.get(id=id)


def is_budget_exists(id):
    """ Check if a budget exists

    Args:
        id (str): ID of the budget

    Returns:
        bool: True if the budget exists; False otherwise
    """
    return Budget.objects.filter(id=id).exists()


def list_bank_accounts_by_budget(id):
    """ Return all linked bank accounts

    Args:
        id (str): Budget ID

    Returns:
        list: List of bank accounts
    """
    budget = Budget.objects.get(id=id)
    bank_accounts = budget.bankaccount_set.all()

    return bank_accounts


def list_budget_groups_by_budget(id):
    """ Return all linked budget groups

    Args:
        id (str): Budget ID

    Returns:
        list: List of budget groups
    """
    budget = Budget.objects.get(id=id)
    budget_groups = budget.budgetgroup_set.all()

    return budget_groups


def list_transactions_by_budget(id):
    """ Return all linked transactions

    Transaction list is sorted by date in descending order

    Args:
        id (str): Budget ID

    Returns:
        list: List of transactions
    """
    transactions = []
    bank_accounts = list_bank_accounts_by_budget(id)

    for bank_account in bank_accounts:
        transactions_for_bank_account = list_transactions_by_bank_account(
            bank_account.id)
        transactions.extend(transactions_for_bank_account)

    transactions.sort(key=lambda x: x.date, reverse=True)

    return transactions
