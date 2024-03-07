from rest_framework import serializers

from api.data.constant import USER_ERR_7
from api.validators.bank_account import bank_account_exists
from api.validators.date import start_date_occurs_after_end_date
from api.validators.transaction import transaction_exists


class InReportTransactionSerializer(serializers.Serializer):
    bank_accounts = serializers.ListField(
        child=serializers.CharField(
            validators=[bank_account_exists]),
        required=False
    )

    start_date = serializers.DateField(
        required=False
    )

    end_date = serializers.DateField(
        required=False
    )

    def validate(self, data):
        """
        Validates the data for a transaction.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data.

        Raises:
            serializers.ValidationError: If the end date occurs before the start date.
        """
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)

        if start_date and end_date:
            start_date_occurs_after_end_date(start_date, end_date)

        return data


class InCreateTransactionSerializer(serializers.Serializer):
    date = serializers.DateField(
        required=True
    )

    label = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True
    )

    amount = serializers.FloatField(
        required=True
    )

    bank_account_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists]
    )

    def __init__(self, *args, **kwargs):
        super(InCreateTransactionSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date=kwargs['data'].get('date', ''))
        else:
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date="BANK_ACCOUNT_DATE")


class InDeleteTransactionSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[transaction_exists])


class InGetTransactionSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[transaction_exists])


class InUpdateTransactionSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[transaction_exists])

    date = serializers.DateField(
        required=True
    )

    label = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True
    )

    amount = serializers.FloatField(
        required=True
    )

    bank_account_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[bank_account_exists])

    def __init__(self, *args, **kwargs):
        super(InUpdateTransactionSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date=kwargs['data'].get('date', ''))
        else:
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date="BANK_ACCOUNT_DATE")


class OutTransactionSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True
    )

    date = serializers.DateField(
        required=True
    )

    label = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True
    )

    amount = serializers.FloatField(
        required=True
    )

    bank_account_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True
    )
