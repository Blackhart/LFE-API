from rest_framework import serializers

from api.data.constant import USER_ERR_9
from api.models.dal.budget_category import is_budget_category_exists


def budget_category_exists(value):
    """ Validate budget category exists

    Args:
        value (str): Budget category ID to validate

    Raises:
        serializers.ValidationError: If the budget category does not exist

    Returns:
        bool: True if the budget category exists, False otherwise
    """
    if not is_budget_category_exists(value):
        raise serializers.ValidationError(USER_ERR_9.format(id=value))

    return value