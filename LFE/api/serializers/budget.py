from rest_framework import serializers

from api.data.constant import USER_ERR_1
from api.validators.budget import budget_exists


class InCreateBudgetSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})


class InRenameBudgetSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_exists])

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={'blank': USER_ERR_1})


class InDeleteBudgetSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_exists])


class InGetBudgetSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_exists])


class InListBudgetGroupsByBudgetSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        validators=[budget_exists])


class OutBudgetSerializer(serializers.Serializer):
    id = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True)

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True)
