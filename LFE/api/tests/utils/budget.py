import requests

from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import CREATE_BUDGET_ENTRY_POINT
from api.tests.data.constant import DELETE_BUDGET_ENTRY_POINT
from api.tests.data.constant import RENAME_BUDGET_ENTRY_POINT
from api.tests.data.constant import LIST_BUDGETS_ENTRY_POINT
from api.tests.data.constant import GET_BUDGET_ENTRY_POINT
from api.tests.data.constant import GET_LINKED_BANK_ACCOUNTS_ENTRY_POINT
from api.tests.data.constant import GET_LINKED_BUDGET_GROUPS_ENTRY_POINT


def get_create_budget_url():
    return STAGGING_BASE_URL + '/' + CREATE_BUDGET_ENTRY_POINT + '/'


def get_delete_budget_url(id):
    return STAGGING_BASE_URL + '/' + DELETE_BUDGET_ENTRY_POINT.format(id=id)


def get_rename_budget_name_url(id):
    return STAGGING_BASE_URL + '/' + RENAME_BUDGET_ENTRY_POINT.format(id=id)


def get_list_budgets_url():
    return STAGGING_BASE_URL + '/' + LIST_BUDGETS_ENTRY_POINT


def get_get_budget_url(id):
    return STAGGING_BASE_URL + '/' + GET_BUDGET_ENTRY_POINT.format(id=id)


def get_get_linked_bank_accounts_url(id):
    return STAGGING_BASE_URL + '/' + GET_LINKED_BANK_ACCOUNTS_ENTRY_POINT.format(id=id)


def get_get_linked_budget_groups_url(id):
    return STAGGING_BASE_URL + '/' + GET_LINKED_BUDGET_GROUPS_ENTRY_POINT.format(id=id)


def create_budget(name="My Budget"):
    url = get_create_budget_url()
    payload = {
        "name": name
    }

    return requests.post(url, json=payload)


def delete_budget(id):
    url = get_delete_budget_url(id)

    return requests.delete(url)


def rename_budget(id, name='My Renamed Budget'):
    url = get_rename_budget_name_url(id)
    payload = {
        "name": name
    }

    return requests.put(url, json=payload)


def list_budgets():
    url = get_list_budgets_url()

    return requests.get(url)


def get_budget(id):
    url = get_get_budget_url(id)

    return requests.get(url)


def get_linked_bank_accounts(id):
    url = get_get_linked_bank_accounts_url(id)

    return requests.get(url)


def get_linked_budget_groups(id):
    url = get_get_linked_budget_groups_url(id)

    return requests.get(url)
