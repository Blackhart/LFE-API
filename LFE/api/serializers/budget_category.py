from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.data.constant import USER_ERR_4
from api.models.poco.budget_category import BudgetCategory


class InBudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ['name', 'budget_group_id']

    def __init__(self, *args, **kwargs):
        super(InBudgetCategorySerializer, self).__init__(*args, **kwargs)
        
        if 'data' in kwargs:
            self.fields['budget_group_id'].error_messages['does_not_exist'] = USER_ERR_4.format(id=kwargs['data']['budget_group_id'])
            self.fields['name'].error_messages['blank'] = USER_ERR_1
        else:
            self.fields['budget_group_id'].error_messages['does_not_exist'] = USER_ERR_4.format(id='')
            self.fields['name'].error_messages['blank'] = USER_ERR_1


class InBudgetCategoryNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(InBudgetCategoryNameUpdateSerializer, self).__init__(*args, **kwargs)
        
        self.fields['name'].error_messages['blank'] = USER_ERR_1
        

class InBudgetCategoryGroupIdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ['budget_group_id']

    def __init__(self, *args, **kwargs):
        super(InBudgetCategoryGroupIdUpdateSerializer, self).__init__(*args, **kwargs)
        
        if 'data' in kwargs:
            self.fields['budget_group_id'].error_messages['does_not_exist'] = USER_ERR_4.format(id=kwargs['data']['budget_group_id'])
        else:
            self.fields['budget_group_id'].error_messages['does_not_exist'] = USER_ERR_4.format(id='')


class OutBudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'budget_group_id']
