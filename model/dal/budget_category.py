import uuid

from api.core.exceptions import IDNotFound
from api.model.db import budget_categories
from api.model.poco.budget_category import BudgetCategory
from api.data.constant import USER_ERR_3


def create_budget_category(name, budget_group_id):
    """ Create a budget category

    Args:
        name (str): Name of the budget category
        budget_group_id (str): ID of the budget group to link to

    Returns:
        BudgetCategory: The budget category
    """
    category = BudgetCategory(
        id=uuid.uuid4().hex,
        name=name,
        budget_group_id=budget_group_id
    )

    budget_categories.append(category)

    return category


def delete_budget_category(id):
    """ Delete a budget category

    Args:
        id (str): ID of the budget category

    Raises:
        IDNotFound: If the budget category doesn't exist
    """
    idx = [
        idx
        for idx, category
        in enumerate(budget_categories)
        if category.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_remove = next(iter(idx))

    budget_categories.pop(idx_to_remove)


def rename_budget_category(id, name):
    """ Rename a budget category

    Args:
        id (str): ID of the budget category
        name (str): Name of the budget category

    Raises:
        IDNotFound: If the budget category doesn't exist

    Returns:
        BudgetCategory: The renamed budget category
    """
    idx = [
        idx
        for idx, category
        in enumerate(budget_categories)
        if category.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_update = next(iter(idx))

    budget_categories[idx_to_update].name = name

    return budget_categories[idx_to_update]


def get_budget_category(id):
    """ Get a budget category

    Args:
        id (str): ID of the budget category

    Raises:
        IDNotFound: If the budget category doesn't exist

    Returns:
        BudgetCategory: The budget category
    """
    idx = [
        idx
        for idx, category
        in enumerate(budget_categories)
        if category.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_get = next(iter(idx))

    return budget_categories[idx_to_get]


def list_budget_categories():
    """ List the budget categories

    Returns:
        list: The budget categories
    """
    return budget_categories


def is_budget_category_exists(id):
    """ Check if a budget category exists

    Args:
        id (str): ID of the budget category

    Returns:
        bool: True if the budget category exists; False otherwise
    """
    idx = [
        idx
        for idx, category
        in enumerate(budget_categories)
        if category.id == id
    ]

    if not idx:
        return False

    return True


def assign_budget_group(id, group_id):
    """ Rename a budget category

    Args:
        id (str): ID of the budget category
        group_id (str): Group to assign

    Raises:
        IDNotFound: If the budget category doesn't exist

    Returns:
        BudgetCategory: The renamed budget category
    """
    idx = [
        idx
        for idx, category
        in enumerate(budget_categories)
        if category.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_update = next(iter(idx))

    budget_categories[idx_to_update].budget_group_id = group_id

    return budget_categories[idx_to_update]

