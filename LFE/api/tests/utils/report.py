import requests

from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import GET_NET_WORTH_REPORT


def get_get_net_worth_report_url():
    return STAGGING_BASE_URL + '/' + GET_NET_WORTH_REPORT


def get_net_worth_report(bank_accounts=[], start_date=None, end_date=None):
    url = get_get_net_worth_report_url()

    filters = {}

    if len(bank_accounts) != 0:
        filters['bank_accounts'] = bank_accounts

    if start_date is not None:
        filters['start_date'] = start_date

    if end_date is not None:
        filters['end_date'] = end_date

    return requests.get(url, params=filters)
