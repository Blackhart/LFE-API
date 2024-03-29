import requests

from api.tests.utils.budget import create_budget

from api.tests.data.constant import STAGGING_BASE_URL
from api.tests.data.constant import CREATE_BUDGET_GROUP_ENTRY_POINT
from api.tests.data.constant import DELETE_BUDGET_GROUP_ENTRY_POINT
from api.tests.data.constant import RENAME_BUDGET_GROUP_ENTRY_POINT
from api.tests.data.constant import LIST_BUDGET_GROUPS_ENTRY_POINT
from api.tests.data.constant import GET_BUDGET_GROUP_ENTRY_POINT
from api.tests.data.constant import GET_ASSIGNED_CATEGORIES_ENTRY_POINT


def get_create_budget_group_url():
    return STAGGING_BASE_URL + '/' + CREATE_BUDGET_GROUP_ENTRY_POINT + '/'


def get_delete_budget_group_url(id):
    return STAGGING_BASE_URL + '/' + DELETE_BUDGET_GROUP_ENTRY_POINT.format(id=id)


def get_rename_budget_group_name_url(id):
    return STAGGING_BASE_URL + '/' + RENAME_BUDGET_GROUP_ENTRY_POINT.format(id=id)


def get_list_budget_groups_url():
    return STAGGING_BASE_URL + '/' + LIST_BUDGET_GROUPS_ENTRY_POINT


def get_get_budget_group_url(id):
    return STAGGING_BASE_URL + '/' + GET_BUDGET_GROUP_ENTRY_POINT.format(id=id)


def get_get_assigned_categories_url(id):
    return STAGGING_BASE_URL + '/' + GET_ASSIGNED_CATEGORIES_ENTRY_POINT.format(id=id)


def create_budget_group(name="My Budget Group", budget_id=None):
    if not budget_id:
        budget_id = create_budget().json()['id']
        
    url = get_create_budget_group_url()
    
    payload = {
        "name": name,
        "budget_id": budget_id
    }

    return requests.post(url, json=payload)


def delete_budget_group(id):
    url = get_delete_budget_group_url(id)

    return requests.delete(url)


def rename_budget_group(id, name='My Renamed Account'):
    url = get_rename_budget_group_name_url(id)
    payload = {
        "name": name
    }

    return requests.put(url, json=payload)


def list_budget_groups():
    url = get_list_budget_groups_url()

    return requests.get(url)


def get_budget_group(id):
    url = get_get_budget_group_url(id)

    return requests.get(url)


def get_assigned_categories(id):
    url = get_get_assigned_categories_url(id)

    return requests.get(url)
