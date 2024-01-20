import requests

from api.core.date import get_current_date

from api.tests.utils.bank_account import create_bank_account
from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import RECORD_TRANSACTION_ENTRY_POINT


def get_record_transaction_url():
    return STAGGING_BASE_URL + '/' + RECORD_TRANSACTION_ENTRY_POINT + '/'


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
