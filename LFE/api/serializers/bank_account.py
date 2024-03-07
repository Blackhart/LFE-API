from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.models.poco.bank_account import BankAccount
from api.validators.bank_account import bank_account_type_supported


class InBankAccountSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField(required=False)
    
    class Meta:
        model = BankAccount
        fields = ['name', 'type', 'balance']

    def __init__(self, *args, **kwargs):
        super(InBankAccountSerializer, self).__init__(*args, **kwargs)
        if 'data' in kwargs:
            self.fields['name'].error_messages['blank'] = USER_ERR_1
        else:
            self.fields['name'].error_messages['blank'] = USER_ERR_1

    def validate_type(self, value):
        """ Validate bank account type

        Args:
            value (str): Bank account type to validate

        Raises:
            serializers.ValidationError: If the bank account type is not supported

        Returns:
            str: The bank account type if it is supported
        """
        return bank_account_type_supported(value)


class InBankAccountNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(InBankAccountNameUpdateSerializer,
              self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['blank'] = USER_ERR_1


class OutBankAccountSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField(required=True)
    
    class Meta:
        model = BankAccount
        fields = ['id', 'name', 'type', 'balance']
