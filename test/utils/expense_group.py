import requests

from api.test.constant import STAGGING_BASE_URL
from api.test.constant import CREATE_EXPENSE_GROUP_ENTRY_POINT
from api.test.constant import GET_EXPENSE_GROUP_ENTRY_POINT


def get_create_expense_group_url():
    return STAGGING_BASE_URL + '/' + CREATE_EXPENSE_GROUP_ENTRY_POINT


def get_get_expense_group_url(expense_group_id):
    return STAGGING_BASE_URL + '/' + GET_EXPENSE_GROUP_ENTRY_POINT.format(id=expense_group_id)


def create_expense_group(name="My Expense Group"):
    url = get_create_expense_group_url()
    payload = {
        "name": name
    }

    answer = requests.post(url, json=payload)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code,
            'id': json['id'],
            'name': name
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }


def get_expense_group(expense_group_id):
    url = get_get_expense_group_url(expense_group_id)

    answer = requests.get(url)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code,
            'id': json['id'],
            'name': json['name']
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }
