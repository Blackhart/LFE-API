from rest_framework import serializers

from api.data.constant import USER_ERR_6, USER_ERR_7, USER_ERR_8
from api.models.poco.transaction import Transaction
from api.validators.bank_account import bank_account_exists
from api.validators.date import start_date_occurs_after_end_date


class InReportTransactionSerializer(serializers.Serializer):
    """
    Serializer for the InReportTransaction model.

    Args:
        serializers (Type): The serializer class used for serializing and deserializing data.
    """

    bank_accounts = serializers.ListField(
        child=serializers.CharField(
            validators=[bank_account_exists]),
        required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)

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


class InTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for incoming transactions.
    """

    class Meta:
        model = Transaction
        fields = ['date', 'label', 'amount', 'bank_account']

    def __init__(self, *args, **kwargs):
        super(InTransactionSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            self.fields['bank_account'].error_messages['does_not_exist'] = USER_ERR_6.format(
                id=kwargs['data']['bank_account'])
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date=kwargs['data']['date'])
        else:
            self.fields['bank_account'].error_messages['does_not_exist'] = USER_ERR_6.format(
                id='BANK_ACCOUNT_ID')
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date="BANK_ACCOUNT_DATE")


class OutTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for outgoing transactions.
    """
    class Meta:
        model = Transaction
        fields = ['id', 'date', 'label', 'amount', 'bank_account']


class OutTransactionsByBudgetSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving outgoing transactions by budget.
    """

    budget = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'date', 'label', 'amount',
                  'bank_account', 'budget']

    def get_budget(self, obj):
        return obj.bank_account.budget.id
