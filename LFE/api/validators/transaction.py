from rest_framework import serializers

from api.data.constant import USER_ERR_10
from api.models.dal.transaction import is_transaction_exists


def transaction_exists(value):
    """ Validate transaction exists

    Args:
        value (str): Transaction ID to validate

    Raises:
        serializers.ValidationError: If the transaction does not exist

    Returns:
        bool: True if the transaction exists, False otherwise
    """
    if not is_transaction_exists(value):
        raise serializers.ValidationError(USER_ERR_10.format(id=value))

    return value