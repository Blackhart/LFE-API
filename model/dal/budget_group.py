from api.model.dal.budget_category import delete_budget_category
from api.data.constant import USER_ERR_3
from api.core.exceptions import IDNotFound
from api.core.uuid import generate_time_based_uuid
from api.model.db import budget_groups
from api.model.db import budget_categories
from api.model.poco.budget_group import BudgetGroup


def create_budget_group(name, budget_id):
    """ Create a budget group

    Args:
        name (str): Name of the budget group
        budget_id (str): Budget ID to link to

    Returns:
        BudgetGroup: The created budget group
    """
    group = BudgetGroup(
        id=generate_time_based_uuid(),
        name=name,
        budget_id=budget_id
    )

    budget_groups.append(group)

    return group


def delete_budget_group(id):
    """ Delete a budget group

    Args:
        id (str): ID of the budget group to delete

    Raises:
        IDNotFound: If the budget group doesn't exists
    """
    idx = [
        idx
        for idx, group
        in enumerate(budget_groups)
        if group.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    _delete_linked_budget_categories(id=id)

    idx_to_remove = next(iter(idx))

    budget_groups.pop(idx_to_remove)


def _delete_linked_budget_categories(id):
    categories = get_linked_categories(id)

    for category in categories:
        delete_budget_category(category.id)


def rename_budget_group(id, name):
    """ Rename a budget group

    Args:
        id (str): ID of the budget group to rename
        name (str): Name of the budget group

    Raises:
        IDNotFound: If the budget group doesn't exist

    Returns:
        BudgetGroup: The renamed budget group
    """
    idx = [
        idx
        for idx, group
        in enumerate(budget_groups)
        if group.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_update = next(iter(idx))

    budget_groups[idx_to_update].name = name

    return budget_groups[idx_to_update]


def get_budget_group(id):
    """ Get a budget group

    Args:
        id (str): ID of the budget group

    Raises:
        IDNotFound: If the budget group doesn't exist

    Returns:
        BudgetGroup: The budget group
    """
    idx = [
        idx
        for idx, group
        in enumerate(budget_groups)
        if group.id == id
    ]

    if not idx:
        raise IDNotFound(USER_ERR_3)

    idx_to_get = next(iter(idx))

    return budget_groups[idx_to_get]


def list_budget_groups():
    """ Get all budget groups

    Returns:
        list: The budget groups
    """
    return budget_groups


def is_budget_group_exists(id):
    """ Check if a budget group exists

    Args:
        id (str): ID of the budget group

    Returns:
        bool: True if the budget group exists; False otherwise
    """
    idx = [
        idx
        for idx, group
        in enumerate(budget_groups)
        if group.id == id
    ]

    if not idx:
        return False

    return True


def get_linked_categories(group_id):
    """ Return all categories linked to a group

    Args:
        group_id (str): Budget group ID

    Returns:
        list: All the linked categories
    """
    if not is_budget_group_exists(group_id):
        raise IDNotFound(USER_ERR_3)

    categories = [
        category
        for category
        in budget_categories
        if category.budget_group_id == group_id
    ]

    return categories
