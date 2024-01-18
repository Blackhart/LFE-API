import requests

from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import CREATE_BUDGET_CATEGORY_ENTRY_POINT
from api.tests.data.constant import DELETE_BUDGET_CATEGORY_ENTRY_POINT
from api.tests.data.constant import RENAME_BUDGET_CATEGORY_ENTRY_POINT
from api.tests.data.constant import LIST_BUDGET_CATEGORIES_ENTRY_POINT
from api.tests.data.constant import GET_BUDGET_CATEGORY_ENTRY_POINT
from api.tests.data.constant import ASSIGN_BUDGET_GROUP_ENTRY_POINT


def get_create_budget_category_url():
    return STAGGING_BASE_URL + '/' + CREATE_BUDGET_CATEGORY_ENTRY_POINT + '/'


def get_delete_budget_category_url(id):
    return STAGGING_BASE_URL + '/' + DELETE_BUDGET_CATEGORY_ENTRY_POINT.format(id=id)


def get_rename_budget_category_name_url(id):
    return STAGGING_BASE_URL + '/' + RENAME_BUDGET_CATEGORY_ENTRY_POINT.format(id=id)


def get_list_budget_categories_url():
    return STAGGING_BASE_URL + '/' + LIST_BUDGET_CATEGORIES_ENTRY_POINT


def get_get_budget_category_url(id):
    return STAGGING_BASE_URL + '/' + GET_BUDGET_CATEGORY_ENTRY_POINT.format(id=id)


def get_assign_budget_group_url(id):
    return STAGGING_BASE_URL + '/' + ASSIGN_BUDGET_GROUP_ENTRY_POINT.format(id=id)


def create_budget_category(name="My Budget Category", budget_group_id=None):
    if not budget_group_id:
        budget_group_id = create_budget_category().json()['id']

    url = get_create_budget_category_url()
    payload = {
        "name": name,
        "budget_group_id": budget_group_id
    }

    return requests.post(url, json=payload)


def delete_budget_category(id):
    url = get_delete_budget_category_url(id)

    return requests.delete(url)


def rename_budget_category(id, name='My Renamed Account'):
    url = get_rename_budget_category_name_url(id)
    payload = {
        "name": name
    }

    return requests.put(url, json=payload)


def list_budget_categories():
    url = get_list_budget_categories_url()

    return requests.get(url)


def get_budget_category(id):
    url = get_get_budget_category_url(id)

    return requests.get(url)


def assign_budget_group(id, group_id):
    url = get_assign_budget_group_url(id)
    payload = {
        "budget_group_id": group_id
    }

    return requests.put(url, json=payload)
