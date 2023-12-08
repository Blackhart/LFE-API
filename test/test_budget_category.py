from api.data.constant import USER_ERR_1, USER_ERR_4

from api.test.utils.budget_category import create_budget_category
from api.test.utils.budget_group import create_budget_group


def test__create_budget_category__empty_name__return_user_error_1():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    empty_name = ''
    
    result = create_budget_category(name=empty_name, budget_group_id=g1['id']).json()
    
    assert result['errors']['json']['name'][0] == USER_ERR_1


def test__create_budget_category__empty_name__return_http_422():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    empty_name = ''
    
    result = create_budget_category(name=empty_name, budget_group_id=g1['id'])
    
    assert result.status_code == 422


def test__create_budget_category__non_existing_group__return_user_error_4():
    non_existing_group = 'non existing'
    
    result = create_budget_category(budget_group_id=non_existing_group).json()
    
    assert result['errors']['json']['budget_group_id'][0] == USER_ERR_4


def test__create_budget_category__non_existing_group__return_http_422():
    non_existing_group = 'non existing'
    
    result = create_budget_category(budget_group_id=non_existing_group)
    
    assert result.status_code == 422


def test__create_budget_category__C1_as_name__create_category_named_C1():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    name = 'C1'
    
    result = create_budget_category(name=name, budget_group_id=g1['id']).json()
    
    assert result['name'] == name


def test__create_budget_category__existing_G1_as_group__link_category_to_G1():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    name = 'C1'
    
    result = create_budget_category(name=name, budget_group_id=g1['id']).json()
    
    assert result['budget_group_id'] == g1['id']


def test__create_budget_category__valid__return_http_201():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    name = 'C1'
    
    result = create_budget_category(name=name, budget_group_id=g1['id'])
    
    assert result.status_code == 201


def test__create_budget_category__valid__return_category_schema():
    group_name = 'G1'
    
    g1 = create_budget_group(name=group_name).json()
    
    name = 'C1'
    
    result = create_budget_category(name=name, budget_group_id=g1['id']).json()
    
    assert 'id' in result
    assert 'name' in result
    assert 'budget_group_id' in result
