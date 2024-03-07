from api.core.uuid import generate_time_based_uuid
from api.models.poco.budget_category import BudgetCategory


def create_budget_category(name, budget_group):
    """ Create a budget category

    Args:
        name (str): Name of the budget category
        budget_group (BudgetGroup): Budget group to link to

    Returns:
        BudgetCategory: The budget category
    """
    uid = generate_time_based_uuid()

    return BudgetCategory.objects.create(id=uid, name=name, budget_group=budget_group)


def delete_budget_category(id):
    """ Delete a budget category

    Args:
        id (str): ID of the budget category
    """
    budget_category = get_budget_category(id)

    budget_category.delete()


def rename_budget_category(id, name):
    """ Rename a budget category

    Args:
        id (str): ID of the budget category
        name (str): Name of the budget category

    Returns:
        BudgetCategory: The renamed budget category
    """
    BudgetCategory.objects.filter(id=id).update(name=name)

    return BudgetCategory.objects.get(id=id)


def get_budget_category(id):
    """ Get a budget category

    Args:
        id (str): ID of the budget category

    Returns:
        BudgetCategory: The budget category
    """
    return BudgetCategory.objects.get(id=id)


def list_budget_categories():
    """ List the budget categories

    Returns:
        list: The budget categories
    """
    return BudgetCategory.objects.all()


def is_budget_category_exists(id):
    """ Check if a budget category exists

    Args:
        id (str): ID of the budget category

    Returns:
        bool: True if the budget category exists; False otherwise
    """
    return BudgetCategory.objects.filter(id=id).exists()


def assign_budget_group(id, budget_group):
    """ Assign a group to the existing category
    
    The previous group will be overwritten.

    Args:
        id (str): ID of the budget category
        budget_group (BudgetGroup): Budget group to link to

    Returns:
        BudgetCategory: The budget category
    """
    BudgetCategory.objects.filter(id=id).update(budget_group=budget_group)

    return BudgetCategory.objects.get(id=id)
