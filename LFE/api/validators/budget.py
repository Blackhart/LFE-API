from rest_framework import serializers

from api.data.constant import USER_ERR_5
from api.models.dal.budget import is_budget_exists


def budget_exists(value):
    """ Validate budget exists

    Args:
        value (str): Budget ID to validate

    Raises:
        serializers.ValidationError: If the budget does not exist

    Returns:
        bool: True if the budget exists, False otherwise
    """
    if not is_budget_exists(value):
        raise serializers.ValidationError(USER_ERR_5.format(id=value))

    return value
