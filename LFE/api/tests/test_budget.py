from api.data.constant import USER_ERR_1
from api.data.constant import USER_ERR_5

from api.tests.utils.budget import create_budget
from api.tests.utils.budget import delete_budget
from api.tests.utils.budget import get_budget
from api.tests.utils.budget import get_linked_budget_groups
from api.tests.utils.budget import list_budgets
from api.tests.utils.budget import rename_budget
from api.tests.utils.budget_group import create_budget_group
from api.tests.utils.budget_group import get_budget_group


def test__create_budget__blank_name__return_user_error_1():
    empty_name = ''

    result = create_budget(name=empty_name).json()

    assert result['name'][0] == USER_ERR_1


def test__create_budget__empty_name__return_http_400():
    empty_name = ''

    result = create_budget(name=empty_name)

    assert result.status_code == 400


def test__create_budget__B1_as_name__create_budget_named_B1():
    name = 'B1'

    result = create_budget(name=name).json()

    assert result['name'] == name


def test__create_budget__valid__return_http_201():
    name = 'B1'

    result = create_budget(name=name)

    assert result.status_code == 201


def test__create_budget__valid__return_budget_schema():
    name = 'B1'

    result = create_budget(name=name).json()

    assert 'id' in result
    assert 'name' in result


def test__delete_budget__non_existing_budget__return_user_error_3():
    non_existing = 'non-existing'

    result = delete_budget(id=non_existing).json()

    assert result['id'][0] == USER_ERR_5.format(id=non_existing)


def test__delete_budget__non_existing_budget__return_http_404():
    non_existing = 'non-existing'

    result = delete_budget(id=non_existing)

    assert result.status_code == 400


def test__delete_budget__created_B1__delete_B1():
    name = 'B1'

    created = create_budget(name=name).json()

    delete_budget(id=created['id'])

    result = get_budget(id=created['id'])

    assert result.status_code == 400


def test__delete_budget__linked_group_G1__delete_group_G1():
    b = create_budget().json()['id']

    g1 = create_budget_group(name='G1', budget_id=b).json()['id']

    delete_budget(id=b)

    result = get_budget_group(id=g1)

    assert result.status_code == 400


def test__delete_budget__valid__return_http_200():
    name = 'B1'

    created = create_budget(name=name).json()

    result = delete_budget(id=created['id'])

    assert result.status_code == 204


def test__rename_budget__non_existing_budget__return_user_error_3():
    non_existing = 'non-existing'

    result = rename_budget(id=non_existing).json()

    assert result['id'][0] == USER_ERR_5.format(id=non_existing)


def test__rename_budget__non_existing_budget__return_http_404():
    non_existing = 'non-existing'

    result = rename_budget(id=non_existing)

    assert result.status_code == 400


def test__rename_budget__empty_name__return_user_error_1():
    created = create_budget().json()

    empty_name = ''

    result = rename_budget(id=created['id'], name=empty_name).json()

    assert result['name'][0] == USER_ERR_1


def test__rename_budget__empty_name__return_http_400():
    created = create_budget().json()

    empty_name = ''

    result = rename_budget(id=created['id'], name=empty_name)

    assert result.status_code == 400


def test__rename_budget__from_B1_to_B2__rename_budget_to_B2():
    name = 'B1'

    created = create_budget(name=name).json()

    new_name = 'B2'

    result = rename_budget(id=created['id'], name=new_name).json()

    assert result['name'] == new_name


def test__rename_budget__valid__return_http_200():
    created = create_budget().json()

    name = 'B2'

    result = rename_budget(id=created['id'], name=name)

    assert result.status_code == 200


def test__rename_budget__valid__return_budget_schema():
    created = create_budget().json()

    name = 'B2'

    result = rename_budget(id=created['id'], name=name).json()

    assert 'id' in result
    assert 'name' in result


def test__list_budget__created_B1_B2_B3__return_B1_B2_B3():
    b1 = create_budget(name='B1').json()['id']
    b2 = create_budget(name='B2').json()['id']
    b3 = create_budget(name='B3').json()['id']

    budget_list = list_budgets().json()

    idx = [group['id'] for group in budget_list]

    assert b1 in idx
    assert b2 in idx
    assert b3 in idx


def test__list_budget__valid__return_http_200():
    create_budget(name='B1')
    create_budget(name='B2')
    create_budget(name='B3')

    result = list_budgets()

    assert result.status_code == 200


def test__list_budget__valid__return_budget_schema():
    create_budget(name='B1')
    create_budget(name='B2')
    create_budget(name='B3')

    budget_list = list_budgets().json()

    for group in budget_list:
        assert 'id' in group
        assert 'name' in group


def test__get_budget__non_existing_budget__return_user_error_3():
    non_existing = 'non-existing'

    result = get_budget(id=non_existing).json()

    assert result['id'][0] == USER_ERR_5.format(id=non_existing)


def test__get_budget__non_existing_budget__return_http_404():
    non_existing = 'non-existing'

    result = get_budget(id=non_existing)

    assert result.status_code == 400


def test__get_budget__created_B1__return_B1():
    b1 = create_budget(name='B1').json()

    result = get_budget(id=b1['id']).json()

    assert result['id'] == b1['id']
    assert result['name'] == b1['name']


def test__get_budget__valid__return_http_200():
    g = create_budget().json()

    result = get_budget(id=g['id'])

    assert result.status_code == 200


def test__get_budget__valid__return_budget_schema():
    g = create_budget().json()

    result = get_budget(id=g['id']).json()

    assert 'id' in result
    assert 'name' in result


def test__get_linked_budget_groups__non_existing_budget__return_user_error_3():
    non_existing = 'non-existing'

    result = get_linked_budget_groups(id=non_existing).json()

    assert result['id'][0] == USER_ERR_5.format(id=non_existing)


def test__get_linked_budget_groups__non_existing_budget__return_http_404():
    non_existing = 'non-existing'

    result = get_linked_budget_groups(id=non_existing)

    assert result.status_code == 400


def test__get_linked_budget_groups__linked_G1__return_G1():
    b = create_budget().json()['id']

    g1 = create_budget_group(budget_id=b).json()['id']

    linked = get_linked_budget_groups(id=b).json()

    idx = [g['id'] for g in linked]

    assert g1 in idx


def test__get_linked_budget_groups__linked_G1_G2_not_linked_G3__return_G1_G2():
    b = create_budget().json()['id']

    g1 = create_budget_group(name='G1', budget_id=b).json()['id']
    g2 = create_budget_group(name='G2', budget_id=b).json()['id']
    g3 = create_budget_group(name='G3').json()['id']

    linked = get_linked_budget_groups(id=b).json()

    idx = [g['id'] for g in linked]

    assert g1 in idx
    assert g2 in idx
    assert g3 not in idx


def test__get_linked_budget_groups__valid__return_http_200():
    b = create_budget().json()['id']

    result = get_linked_budget_groups(id=b)

    assert result.status_code == 200


def test__get_linked_budget_groups__valid__return_budget_group_schema():
    b = create_budget().json()['id']
    
    create_budget_group(name='G1', budget_id=b).json()['id']
    create_budget_group(name='G2', budget_id=b).json()['id']

    result = get_linked_budget_groups(id=b).json()

    for g in result:
        assert 'id' in g
        assert 'name' in g
        assert 'budget_id' in g
