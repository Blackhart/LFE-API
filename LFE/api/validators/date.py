from rest_framework import serializers

from api.data.constant import USER_ERR_8


def start_date_occurs_after_end_date(start_date, end_date):
    if start_date and end_date and start_date > end_date:
        raise serializers.ValidationError(USER_ERR_8.format(
            start_date=start_date, end_date=end_date))
