import requests

from api.test.constant import STAGGING_BASE_URL
from api.test.constant import CREATE_EXPENSE_GROUP_ENTRY_POINT


def get_create_expense_group_url():
    return STAGGING_BASE_URL + '/' + CREATE_EXPENSE_GROUP_ENTRY_POINT


def create_expense_group(name = "My Expense Group"):
    url = get_create_expense_group_url()
    payload = {
        "name": name
    }
    
    return requests.post(url, json=payload)