import requests

from api.data.bank_account_type import BankAccountType

from api.tests.utils.budget import create_budget
from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import CREATE_BANK_ACCOUNT_ENTRY_POINT
from api.tests.data.constant import DELETE_BANK_ACCOUNT_ENTRY_POINT
from api.tests.data.constant import RENAME_BANK_ACCOUNT_ENTRY_POINT
from api.tests.data.constant import LIST_BANK_ACCOUNTS_ENTRY_POINT
from api.tests.data.constant import GET_BANK_ACCOUNT_ENTRY_POINT


def get_create_bank_account_url():
    return STAGGING_BASE_URL + '/' + CREATE_BANK_ACCOUNT_ENTRY_POINT + '/'


def get_delete_bank_account_url(id):
    return STAGGING_BASE_URL + '/' + DELETE_BANK_ACCOUNT_ENTRY_POINT.format(id=id)


def get_rename_bank_account_name_url(id):
    return STAGGING_BASE_URL + '/' + RENAME_BANK_ACCOUNT_ENTRY_POINT.format(id=id)


def get_list_bank_accounts_url():
    return STAGGING_BASE_URL + '/' + LIST_BANK_ACCOUNTS_ENTRY_POINT


def get_get_bank_account_url(id):
    return STAGGING_BASE_URL + '/' + GET_BANK_ACCOUNT_ENTRY_POINT.format(id=id)


def create_bank_account(name="My Bank Account", type=BankAccountType.STANDARD, balance=0.0, budget_id=None):
    if not budget_id:
        budget_id = create_budget().json()['id']
        
    url = get_create_bank_account_url()
    
    payload = {
        "name": name,
        "type": type,
        "balance": float(balance),
        "budget_id": budget_id
    }

    return requests.post(url, json=payload)


def delete_bank_account(id):
    url = get_delete_bank_account_url(id)

    return requests.delete(url)


def rename_bank_account(id, name='My Renamed Account'):
    url = get_rename_bank_account_name_url(id)
    payload = {
        "name": name
    }

    return requests.put(url, json=payload)


def list_bank_accounts():
    url = get_list_bank_accounts_url()

    return requests.get(url)


def get_bank_account(id):
    url = get_get_bank_account_url(id)

    return requests.get(url)