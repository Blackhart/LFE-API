from api.core.uuid import generate_time_based_uuid
from api.models.poco.budget_group import BudgetGroup


def create_budget_group(name, budget_id):
    """ Create a budget group

    Args:
        name (str): Name of the budget group
        budget_id (str): Budget ID to link to

    Returns:
        BudgetGroup: The created budget group
    """
    uid = generate_time_based_uuid()

    return BudgetGroup.objects.create(id=uid, name=name, budget_id=budget_id)


def delete_budget_group(id):
    """ Delete a budget group

    Args:
        id (str): ID of the budget group to delete
    """
    budget_group = get_budget_group(id)

    budget_group.delete()


def rename_budget_group(id, name):
    """ Rename a budget group

    Args:
        id (str): ID of the budget group to rename
        name (str): Name of the budget group

    Returns:
        BudgetGroup: The renamed budget group
    """
    BudgetGroup.objects.filter(id=id).update(name=name)

    return BudgetGroup.objects.get(id=id)


def get_budget_group(id):
    """ Get a budget group

    Args:
        id (str): ID of the budget group

    Returns:
        BudgetGroup: The budget group
    """
    return BudgetGroup.objects.get(id=id)


def list_budget_groups():
    """ Get all budget groups

    Returns:
        list: The budget groups
    """
    return BudgetGroup.objects.all()


def is_budget_group_exists(id):
    """ Check if a budget group exists

    Args:
        id (str): ID of the budget group

    Returns:
        bool: True if the budget group exists; False otherwise
    """
    return BudgetGroup.objects.filter(id=id).exists()


def list_budget_categories_by_budget_group(group_id):
    """ Return all categories linked to a group

    Args:
        group_id (str): Budget group ID

    Returns:
        list: All the linked categories
    """
    return BudgetGroup.objects.get(id=group_id).budgetcategory_set.all()
