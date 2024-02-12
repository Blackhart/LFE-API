from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.data.constant import USER_ERR_5
from api.models.poco.budget_group import BudgetGroup


class InBudgetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetGroup
        fields = ['name', 'budget']

    def __init__(self, *args, **kwargs):
        super(InBudgetGroupSerializer, self).__init__(*args, **kwargs)
        if 'data' in kwargs:
            self.fields['budget'].error_messages['does_not_exist'] = USER_ERR_5.format(
                id=kwargs['data']['budget'])
            self.fields['name'].error_messages['blank'] = USER_ERR_1
        else:
            self.fields['budget'].error_messages['does_not_exist'] = USER_ERR_5.format(
                id='')
            self.fields['name'].error_messages['blank'] = USER_ERR_1


class InBudgetGroupNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetGroup
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(InBudgetGroupNameUpdateSerializer,
              self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['blank'] = USER_ERR_1


class OutBudgetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetGroup
        fields = ['id', 'name', 'budget']
