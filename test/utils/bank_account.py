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


def create_bank_account(name = "My Bank Account", type = BankAccountType.STANDARD, balance = 0.0):
    url = get_create_bank_account_url()
    payload = {
        "name": name,
        "type": type,
        "balance": float(balance)
    }
    
    return requests.post(url, json=payload)


def create_standard_account(name = 'My Standard Account', balance = 0.0):
    return create_bank_account(name, BankAccountType.STANDARD, balance)


def create_saving_account(name = 'My Saving Account', balance = 0.0):
    return create_bank_account(name, BankAccountType.SAVING, balance)


def create_trading_account(name = 'My Trading Account', balance = 0.0):
    return create_bank_account(name, BankAccountType.TRADING, balance)


def delete_bank_account(bank_account_id):
    url = get_delete_bank_account_url(bank_account_id)
    
    return requests.delete(url)


def rename_bank_account(bank_account_id, name = 'My Renamed Account'):
    url = get_rename_bank_account_name_url(bank_account_id)
    payload = {
        "name": name
    }
    
    return requests.patch(url, json=payload)


def list_bank_accounts():
    url = get_list_bank_accounts_url()
    
    return requests.get(url)


def get_bank_accounts_list(json_answer):
    names = []
    
    for s in json_answer:
        names.append(s['name'])
        
    return names


def get_bank_account(bank_account_id):
    url = get_get_bank_account_url(bank_account_id)
    
    return requests.get(url)