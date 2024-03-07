from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.validators.bank_account import bank_account_type_supported
from api.validators.bank_account import bank_account_exists


class InCreateBankAccountSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})

    type = serializers.CharField(
        max_length=10,
        required=True,
        validators=[bank_account_type_supported])

    balance = serializers.FloatField(
        required=True)


class InRenameBankAccountSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists])

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})


class InDeleteBankAccountSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists])


class InGetBankAccountSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists])


class InListTransactionsByBankAccountSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists])


class OutBankAccountSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    type = serializers.CharField(
        max_length=10,
        required=True)

    balance = serializers.FloatField(
        required=True)
