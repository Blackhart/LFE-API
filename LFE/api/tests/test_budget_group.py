from api.data.constant import USER_ERR_1, USER_ERR_3, USER_ERR_5

from api.tests.utils.budget import create_budget

from api.tests.utils.budget_group import create_budget_group
from api.tests.utils.budget_group import delete_budget_group
from api.tests.utils.budget_group import rename_budget_group
from api.tests.utils.budget_group import list_budget_groups
from api.tests.utils.budget_group import get_budget_group
from api.tests.utils.budget_group import get_assigned_categories
from api.tests.utils.budget_category import create_budget_category
from api.tests.utils.budget_category import get_budget_category


def test__create_budget_group__empty_name__return_user_error_1():
    empty_name = ''

    result = create_budget_group(name=empty_name).json()

    assert result['name'][0] == USER_ERR_1


def test__create_budget_group__empty_name__return_http_400():
    empty_name = ''

    result = create_budget_group(name=empty_name)

    assert result.status_code == 400


def test__create_budget_group__non_existing_budget__return_user_error_5():
    b = 'non-existing'

    result = create_budget_group(budget=b).json()

    assert result['budget'][0] == USER_ERR_5.format(id=b)


def test__create_budget_group__non_existing_budget__return_http_400():
    b = 'non existing'

    result = create_budget_group(budget=b)

    assert result.status_code == 400


def test__create_budget_group__G1_as_name__create_group_named_G1():
    name = 'G1'

    result = create_budget_group(name=name).json()

    assert result['name'] == name


def test__create_budget_group__B1_as_budget__create_group_linked_to_B1():
    b1 = create_budget(name='B1').json()['id']

    result = create_budget_group(budget=b1).json()

    assert result['budget'] == b1


def test__create_budget_group__valid__return_http_201():
    name = 'G1'

    result = create_budget_group(name=name)

    assert result.status_code == 201


def test__create_budget_group__valid__return_group_schema():
    name = 'G1'

    result = create_budget_group(name=name).json()

    assert 'id' in result
    assert 'name' in result
    assert 'budget' in result


def test__delete_budget_group__non_existing_group__return_user_error_3():
    non_existing_group = 'non-existing'

    result = delete_budget_group(id=non_existing_group).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing_group)


def test__delete_budget_group__non_existing_group__return_http_404():
    non_existing_group = 'non-existing'

    result = delete_budget_group(id=non_existing_group)

    assert result.status_code == 404


def test__delete_budget_group__created_G1_group__delete_group_G1():
    name = 'G1'

    created = create_budget_group(name=name).json()

    delete_budget_group(id=created['id'])

    result = get_budget_group(id=created['id'])

    assert result.status_code == 404


def test__delete_budget_group__group_G1_linked_to_category_C1__delete_category_C1():
    g1 = create_budget_group(name='G1').json()['id']
    c1 = create_budget_category(name='C1', budget_group=g1).json()['id']

    delete_budget_group(id=g1)

    result = get_budget_category(id=c1)

    assert result.status_code == 404


def test__delete_budget_group__valid__return_http_200():
    name = 'G1'

    created = create_budget_group(name=name).json()

    result = delete_budget_group(id=created['id'])

    assert result.status_code == 204


def test__rename_budget_group__non_existing_group__return_user_error_3():
    non_existing_group = 'non-existing'

    result = rename_budget_group(id=non_existing_group).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing_group)


def test__rename_budget_group__non_existing_group__return_http_404():
    non_existing_group = 'non-existing'

    result = rename_budget_group(id=non_existing_group)

    assert result.status_code == 404


def test__rename_budget_group__empty_name__return_user_error_1():
    created = create_budget_group().json()

    empty_name = ''

    result = rename_budget_group(id=created['id'], name=empty_name).json()

    assert result['name'][0] == USER_ERR_1


def test__rename_budget_group__empty_name__return_http_400():
    created = create_budget_group().json()

    empty_name = ''

    result = rename_budget_group(id=created['id'], name=empty_name)

    assert result.status_code == 400


def test__rename_budget_group__from_G1_to_G2__rename_group_to_G2():
    name = 'G1'

    created = create_budget_group(name=name).json()

    new_name = 'G2'

    result = rename_budget_group(id=created['id'], name=new_name).json()

    assert result['name'] == new_name


def test__rename_budget_group__valid__return_http_200():
    created = create_budget_group().json()

    name = 'G2'

    result = rename_budget_group(id=created['id'], name=name)

    assert result.status_code == 200


def test__rename_budget_group__valid__return_group_schema():
    created = create_budget_group().json()

    name = 'G2'

    result = rename_budget_group(id=created['id'], name=name).json()

    assert 'id' in result
    assert 'name' in result


def test__list_budget_group__created_G1_G2_G3__return_G1_G2_G3():
    g1 = create_budget_group(name='G1').json()['id']
    g2 = create_budget_group(name='G2').json()['id']
    g3 = create_budget_group(name='G3').json()['id']

    group_list = list_budget_groups().json()

    idx = [group['id'] for group in group_list]

    assert g1 in idx
    assert g2 in idx
    assert g3 in idx


def test__list_budget_group__valid__return_http_200():
    create_budget_group(name='G1')
    create_budget_group(name='G2')
    create_budget_group(name='G3')

    result = list_budget_groups()

    assert result.status_code == 200


def test__list_budget_group__valid__return_group_schema():
    create_budget_group(name='G1')
    create_budget_group(name='G2')
    create_budget_group(name='G3')

    group_list = list_budget_groups().json()

    for group in group_list:
        assert 'id' in group
        assert 'name' in group


def test__get_budget_group__non_existing_group__return_user_error_3():
    non_existing_group = 'non-existing'

    result = get_budget_group(id=non_existing_group).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing_group)


def test__get_budget_group__non_existing_group__return_http_404():
    non_existing_group = 'non-existing'

    result = get_budget_group(id=non_existing_group)

    assert result.status_code == 404


def test__get_budget_group__created_G1__return_G1():
    g1 = create_budget_group(name='G1').json()

    result = get_budget_group(id=g1['id']).json()

    assert result['id'] == g1['id']
    assert result['name'] == g1['name']


def test__get_budget_group__valid__return_http_200():
    g = create_budget_group().json()

    result = get_budget_group(id=g['id'])

    assert result.status_code == 200


def test__get_budget_group__valid__return_group_schema():
    g = create_budget_group().json()

    result = get_budget_group(id=g['id']).json()

    assert 'id' in result
    assert 'name' in result


def test__get_assigned_categories__non_existing_group__return_user_error_3():
    non_existing_group = 'non-existing'

    result = get_assigned_categories(id=non_existing_group).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing_group)


def test__get_assigned_categories__non_existing_group__return_http_404():
    non_existing_group = 'non-existing'

    result = get_assigned_categories(id=non_existing_group)

    assert result.status_code == 404


def test__get_assigned_categories__assigned_C1_C2__return_C1_C2():
    g = create_budget_group().json()['id']

    c1 = create_budget_category(name='C1', budget_group=g).json()['id']
    c2 = create_budget_category(name='C2', budget_group=g).json()['id']

    categories = get_assigned_categories(id=g).json()

    idx = [category['id'] for category in categories]

    assert c1 in idx
    assert c2 in idx


def test__get_assigned_categories__created_C1_C2_C3_assigned_C1_C2__return_C1_C2():
    g1 = create_budget_group().json()['id']
    g2 = create_budget_group().json()['id']

    c1 = create_budget_category(name='C1', budget_group=g1).json()['id']
    c2 = create_budget_category(name='C2', budget_group=g1).json()['id']
    c3 = create_budget_category(name='C3', budget_group=g2).json()['id']

    categories = get_assigned_categories(id=g1).json()

    idx = [category['id'] for category in categories]

    assert c1 in idx
    assert c2 in idx
    assert c3 not in idx


def test__get_assigned_categories__valid__return_http_200():
    g = create_budget_group().json()

    result = get_assigned_categories(id=g['id'])

    assert result.status_code == 200


def test__get_assigned_categories__valid__return_category_schema():
    g = create_budget_group().json()

    result = get_assigned_categories(id=g['id']).json()

    for category in result:
        assert 'id' in category
        assert 'name' in category
        assert 'budget_group' in category
