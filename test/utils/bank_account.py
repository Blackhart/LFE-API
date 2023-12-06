import requests

from api.model.poco.bank_account_type import BankAccountType

from api.test.constant import STAGGING_BASE_URL
from api.test.constant import CREATE_BANK_ACCOUNT_ENTRY_POINT
from api.test.constant import DELETE_BANK_ACCOUNT_ENTRY_POINT
from api.test.constant import RENAME_BANK_ACCOUNT_ENTRY_POINT
from api.test.constant import LIST_BANK_ACCOUNTS_ENTRY_POINT
from api.test.constant import GET_BANK_ACCOUNT_ENTRY_POINT


def get_create_bank_account_url():
    return STAGGING_BASE_URL + '/' + CREATE_BANK_ACCOUNT_ENTRY_POINT


def get_delete_bank_account_url(bank_account_id):
    return STAGGING_BASE_URL + '/' + DELETE_BANK_ACCOUNT_ENTRY_POINT.format(id=bank_account_id)


def get_rename_bank_account_name_url(bank_account_id):
    return STAGGING_BASE_URL + '/' + RENAME_BANK_ACCOUNT_ENTRY_POINT.format(id=bank_account_id)


def get_list_bank_accounts_url():
    return STAGGING_BASE_URL + '/' + LIST_BANK_ACCOUNTS_ENTRY_POINT


def get_get_bank_account_url(bank_account_id):
    return STAGGING_BASE_URL + '/' + GET_BANK_ACCOUNT_ENTRY_POINT.format(id=bank_account_id)


def create_bank_account(name="My Bank Account", type=BankAccountType.STANDARD, balance=0.0):
    url = get_create_bank_account_url()
    payload = {
        "name": name,
        "type": type,
        "balance": float(balance)
    }

    answer = requests.post(url, json=payload)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code,
            'id': json['id'],
            'name': name,
            'type': type,
            'balance': balance
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }


def delete_bank_account(bank_account_id):
    url = get_delete_bank_account_url(bank_account_id)

    answer = requests.delete(url)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }


def rename_bank_account(bank_account_id, name='My Renamed Account'):
    url = get_rename_bank_account_name_url(bank_account_id)
    payload = {
        "name": name
    }

    answer = requests.patch(url, json=payload)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code,
            'id': json['id'],
            'name': json['name'],
            'type': json['type'],
            'balance': json['balance']
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }


def list_bank_accounts():
    url = get_list_bank_accounts_url()

    answer = requests.get(url)
    json = answer.json()

    if answer.ok:
        items = []

        for item in json:
            items.append({
                'id': item['id'],
                'name': item['name'],
                'type': item['type'],
                'balance': item['balance']
            })

        return {
            'code': answer.status_code,
            'items': items
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }


def get_bank_account(bank_account_id):
    url = get_get_bank_account_url(bank_account_id)

    answer = requests.get(url)
    json = answer.json()

    if answer.ok:
        return {
            'code': answer.status_code,
            'id': json['id'],
            'name': json['name'],
            'type': json['type'],
            'balance': json['balance']
        }
    else:
        return {
            'code': answer.status_code,
            'status': json['status'],
            'message': json.get('message'),
            'errors': json.get('errors')
        }
