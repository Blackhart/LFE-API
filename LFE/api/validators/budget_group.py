from rest_framework import serializers

from api.data.constant import USER_ERR_4
from api.models.dal.budget_group import is_budget_group_exists


def budget_group_exists(value):
    """ Validate budget group exists

    Args:
        value (str): Budget group ID to validate

    Raises:
        serializers.ValidationError: If the budget group does not exist

    Returns:
        bool: True if the budget group exists, False otherwise
    """
    if not is_budget_group_exists(value):
        raise serializers.ValidationError(USER_ERR_4.format(id=value))

    return value
