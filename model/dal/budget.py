from api.model.dal.bank_account import delete_bank_account
from api.model.dal.budget_group import delete_budget_group
from api.model.poco.budget import Budget
from api.model.poco.bank_account import BankAccount
from api.model.poco.budget_group import BudgetGroup
from api.model.db import budgets
from api.model.db import bank_accounts
from api.model.db import budget_groups
from api.core.uuid import generate_time_based_uuid
from api.data.constant import USER_ERR_3
from api.core.exceptions import IDNotFound


def create_budget(name):
    """ Create a budget

    Args:
        name (str): Name of the budget

    Returns:
        Budget: The created budget
    """
    budget = Budget(
        id=generate_time_based_uuid(),
        name=name
    )

    budgets.append(budget)

    return budget


def delete_budget(id):
    """ Delete a budget

    Args:
        id (str): ID of the budget to delete

    Raises:
        IDNotFound: If the budget doesn't exist
    """
    idx = [
        idx
        for idx, budget
        in enumerate(budgets)
        if budget.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    _delete_linked_bank_accounts(id=id)
    _delete_linked_budget_groups(id=id)

    idx_to_remove = next(iter(idx))

    budgets.pop(idx_to_remove)


def _delete_linked_bank_accounts(id):
    linked_bank_accounts = get_linked_bank_accounts(id=id)

    for account in linked_bank_accounts:
        delete_bank_account(id=account.id)


def _delete_linked_budget_groups(id):
    linked_budget_groups = get_linked_budget_groups(id=id)

    for groups in linked_budget_groups:
        delete_budget_group(id=groups.id)


def rename_budget(id, name):
    """ Rename a budget

    Args:
        id (str): ID of the budget to rename
        name (str): Name of the budget

    Raises:
        IDNotFound: If the budget doesn't exist

    Returns:
        BudgetGroup: The renamed budget
    """
    idx = [
        idx
        for idx, budget
        in enumerate(budgets)
        if budget.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_update = next(iter(idx))

    budgets[idx_to_update].name = name

    return budgets[idx_to_update]


def get_budget(id):
    """ Get a budget

    Args:
        id (str): ID of the budget

    Raises:
        IDNotFound: If the budget doesn't exist

    Returns:
        BudgetGroup: The budget
    """
    idx = [
        idx
        for idx, budget
        in enumerate(budgets)
        if budget.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_get = next(iter(idx))

    return budgets[idx_to_get]


def list_budgets():
    """ Get all budgets

    Returns:
        list: The list of budgets
    """
    return budgets


def is_budget_exists(id):
    """ Check if a budget exists

    Args:
        id (str): ID of the budget

    Returns:
        bool: True if the budget exists; False otherwise
    """
    idx = [
        idx
        for idx, budget
        in enumerate(budgets)
        if budget.id == id
    ]

    if not idx:
        return False

    return True


def get_linked_bank_accounts(id):
    """ Return all linked bank accounts

    Args:
        id (str): Budget ID

    Raises:
        IDNotFound: If budget doesn't exist

    Returns:
        list: List of bank accounts
    """
    if not is_budget_exists(id):
        raise IDNotFound(USER_ERR_3)

    accounts = [
        account
        for account
        in bank_accounts
        if account.budget_id == id
    ]

    return accounts


def get_linked_budget_groups(id):
    """ Return all linked budget groups

    Args:
        id (str): Budget ID

    Raises:
        IDNotFound: If budget doesn't exist

    Returns:
        list: List of budget groups
    """
    if not is_budget_exists(id):
        raise IDNotFound(USER_ERR_3)

    groups = [
        group
        for group
        in budget_groups
        if group.budget_id == id
    ]

    return groups
