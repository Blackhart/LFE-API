from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.data.constant import USER_ERR_2
from api.data.constant import USER_ERR_5
from api.data.constant import SUPPORTED_BANK_ACCOUNT_TYPE
from api.models.poco.bank_account import BankAccount


class InBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['name', 'type', 'balance', 'budget_id']

    def __init__(self, *args, **kwargs):
        super(InBankAccountSerializer, self).__init__(*args, **kwargs)
        if 'data' in kwargs:
            self.fields['budget_id'].error_messages['does_not_exist'] = USER_ERR_5.format(id=kwargs['data']['budget_id'])
            self.fields['name'].error_messages['blank'] = USER_ERR_1
        else:
            self.fields['budget_id'].error_messages['does_not_exist'] = USER_ERR_5.format(id='')
            self.fields['name'].error_messages['blank'] = USER_ERR_1

    def validate_type(self, value):
        if value not in SUPPORTED_BANK_ACCOUNT_TYPE:
            raise serializers.ValidationError(USER_ERR_2.format(
                Type=value, AvailableType=SUPPORTED_BANK_ACCOUNT_TYPE))

        return value


class InBankAccountNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(InBankAccountNameUpdateSerializer,
              self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['blank'] = USER_ERR_1


class OutBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'name', 'type', 'balance', 'budget_id']
