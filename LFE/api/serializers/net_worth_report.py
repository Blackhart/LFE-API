from rest_framework import serializers


class outNetWorthReportSerializer(serializers.Serializer):
    daily = serializers.DictField(child=serializers.FloatField())
    monthly = serializers.DictField(child=serializers.FloatField())
    yearly = serializers.DictField(child=serializers.FloatField())
