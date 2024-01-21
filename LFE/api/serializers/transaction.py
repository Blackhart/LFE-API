from rest_framework import serializers

from api.data.constant import USER_ERR_6, USER_ERR_7
from api.models.poco.transaction import Transaction


class InTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['date', 'label', 'amount', 'bank_account_id']

    def __init__(self, *args, **kwargs):
        super(InTransactionSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            self.fields['bank_account_id'].error_messages['does_not_exist'] = USER_ERR_6.format(
                id=kwargs['data']['bank_account_id'])
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date=kwargs['data']['date'])
        else:
            self.fields['bank_account_id'].error_messages['does_not_exist'] = USER_ERR_6.format(
                id='')
            self.fields['date'].error_messages['invalid'] = USER_ERR_7.format(
                date="")


class OutTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'date', 'label', 'amount', 'bank_account_id']


class OutTransactionsByBudgetSerializer(serializers.ModelSerializer):
    budget_id = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'date', 'label', 'amount',
                  'bank_account_id', 'budget_id']

    def get_budget_id(self, obj):
        return obj.bank_account_id.budget_id.id
