from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.validators.budget import budget_exists
from api.validators.budget_group import budget_group_exists


class InCreateBudgetGroupSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})

    budget_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_exists])


class InRenameBudgetGroupSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})


class InDeleteBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])


class InGetBudgetCategorySerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])


class InListBudgetCategoriesByBudgetGroupSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_group_exists])


class OutBudgetGroupSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    budget_id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)
