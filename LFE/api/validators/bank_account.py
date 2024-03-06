from rest_framework import serializers

from api.data.constant import USER_ERR_2
from api.data.constant import USER_ERR_6
from api.data.constant import SUPPORTED_BANK_ACCOUNT_TYPE
from api.models.dal.bank_account import is_bank_account_exists


def bank_account_type_supported(value):
    """ Validate bank account type

    Args:
        value (str): Bank account type to validate

    Raises:
        serializers.ValidationError: If the bank account type is not supported

    Returns:
        str: The bank account type if it is supported
    """
    if value not in SUPPORTED_BANK_ACCOUNT_TYPE:
        raise serializers.ValidationError(USER_ERR_2.format(
            Type=value, AvailableType=SUPPORTED_BANK_ACCOUNT_TYPE))

    return value


def bank_account_exists(value):
    """ Validate bank account exists

    Args:
        value (str): Bank account ID to validate

    Raises:
        serializers.ValidationError: If the bank account does not exist

    Returns:
        bool: True if the bank account exists, False otherwise
    """
    if not is_bank_account_exists(value):
        raise serializers.ValidationError(USER_ERR_6.format(id=value))

    return value
