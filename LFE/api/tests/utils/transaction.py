import requests

from api.core.date import get_current_date

from api.tests.utils.bank_account import create_bank_account
from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import RECORD_TRANSACTION_ENTRY_POINT
from api.tests.data.constant import DELETE_TRANSACTION_ENTRY_POINT
from api.tests.data.constant import GET_TRANSACTION_ENTRY_POINT
from api.tests.data.constant import UPDATE_TRANSACTION_ENTRY_POINT


def get_record_transaction_url():
    return STAGGING_BASE_URL + '/' + RECORD_TRANSACTION_ENTRY_POINT + '/'


def get_delete_transaction_url(id):
    return STAGGING_BASE_URL + '/' + DELETE_TRANSACTION_ENTRY_POINT.format(id=id)


def get_get_transaction_url(id):
    return STAGGING_BASE_URL + '/' + GET_TRANSACTION_ENTRY_POINT.format(id=id)


def get_update_transaction_url(id):
    return STAGGING_BASE_URL + '/' + UPDATE_TRANSACTION_ENTRY_POINT.format(id=id)


def record_transaction(date=get_current_date(), label="My Transaction", amount="1", bank_account_id=None):
    if not bank_account_id:
        bank_account_id = create_bank_account().json()['id']

    url = get_record_transaction_url()

    payload = {
        "date": date,
        "label": label,
        "amount": float(amount),
        "bank_account_id": bank_account_id
    }

    return requests.post(url, json=payload)


def delete_transaction(id):
    url = get_delete_transaction_url(id)

    return requests.delete(url)


def get_transaction(id):
    url = get_get_transaction_url(id)

    return requests.get(url)


def update_transaction(id, date, label, amount, bank_account_id):
    url = get_update_transaction_url(id)

    payload = {
        "date": date,
        "label": label,
        "amount": float(amount),
        "bank_account_id": bank_account_id
    }

    return requests.put(url, json=payload)
