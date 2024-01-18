from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.models.poco.budget import Budget


class InBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(InBudgetSerializer, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['blank'] = USER_ERR_1


class OutBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'name']
