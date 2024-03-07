from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.validators.budget_category import budget_category_exists
from api.validators.budget_group import budget_group_exists


class InCreateBudgetCategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})

    budget_group_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])


class InRenameBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_category_exists])

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})


class InAssignGroupToBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_category_exists])

    budget_group_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])


class InDeleteBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_category_exists])


class InGetBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_category_exists])


class OutBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    budget_group_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)
