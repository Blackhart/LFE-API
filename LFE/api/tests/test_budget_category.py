from api.data.constant import USER_ERR_1, USER_ERR_3, USER_ERR_4

from api.tests.utils.budget_category import create_budget_category
from api.tests.utils.budget_category import delete_budget_category
from api.tests.utils.budget_category import rename_budget_category
from api.tests.utils.budget_category import list_budget_categories
from api.tests.utils.budget_category import get_budget_category
from api.tests.utils.budget_category import assign_budget_group
from api.tests.utils.budget_group import create_budget_group


def test__create_budget_category__empty_name__return_user_error_1():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    empty_name = ''

    result = create_budget_category(
        name=empty_name,
        budget_group=g1['id']
    ).json()

    assert result['name'][0] == USER_ERR_1


def test__create_budget_category__empty_name__return_http_400():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    empty_name = ''

    result = create_budget_category(
        name=empty_name,
        budget_group=g1['id']
    )

    assert result.status_code == 400


def test__create_budget_category__non_existing_group__return_user_error_4():
    non_existing_group = 'non-existing'

    result = create_budget_category(budget_group=non_existing_group).json()

    assert result['budget_group'][0] == USER_ERR_4.format(id=non_existing_group)


def test__create_budget_category__non_existing_group__return_http_400():
    non_existing_group = 'non-existing'

    result = create_budget_category(budget_group=non_existing_group)

    assert result.status_code == 400


def test__create_budget_category__C1_as_name__create_category_named_C1():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    name = 'C1'

    result = create_budget_category(name=name, budget_group=g1['id']).json()

    assert result['name'] == name


def test__create_budget_category__existing_G1_as_group__link_category_to_G1():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    name = 'C1'

    result = create_budget_category(name=name, budget_group=g1['id']).json()

    assert result['budget_group'] == g1['id']


def test__create_budget_category__valid__return_http_201():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    name = 'C1'

    result = create_budget_category(name=name, budget_group=g1['id'])

    assert result.status_code == 201


def test__create_budget_category__valid__return_category_schema():
    group_name = 'G1'

    g1 = create_budget_group(name=group_name).json()

    name = 'C1'

    result = create_budget_category(
        name=name,
        budget_group=g1['id']
    ).json()

    assert 'id' in result
    assert 'name' in result
    assert 'budget_group' in result


def test__delete_budget_category__non_existing_category__return_user_error_3():
    id = 'non-existing'

    result = delete_budget_category(id=id).json()

    assert result['detail'] == USER_ERR_3.format(id=id)


def test__delete_budget_category__non_existing_category__return_http_404():
    id = 'non-existing'

    result = delete_budget_category(id=id)

    assert result.status_code == 404


def test__delete_budget_category__existing_category_named_C1__delete_category_C1():
    group_name = 'G1'
    category_name = 'C1'

    g1 = create_budget_group(name=group_name).json()
    c1 = create_budget_category(
        name=category_name,
        budget_group=g1['id']
    ).json()

    delete_budget_category(id=c1['id'])

    result = get_budget_category(id=c1['id'])

    assert result.status_code == 404


def test__delete_budget_category__valid__return_http_200():
    group_name = 'G1'
    category_name = 'C1'

    g1 = create_budget_group(name=group_name).json()
    c1 = create_budget_category(
        name=category_name,
        budget_group=g1['id']
    ).json()

    result = delete_budget_category(id=c1['id'])

    assert result.status_code == 204


def test__rename_budget_category__non_existing_category__return_user_error_3():
    id = 'non-existing'

    result = rename_budget_category(id=id).json()

    assert result['detail'] == USER_ERR_3.format(id=id)


def test__rename_budget_category__non_existing_category__return_http_404():
    id = 'non-existing'

    result = rename_budget_category(id=id)

    assert result.status_code == 404


def test__rename_budget_category__empty_name__return_user_error_1():
    g = create_budget_group().json()
    c = create_budget_category(budget_group=g['id']).json()

    name = ''

    result = rename_budget_category(id=c['id'], name=name).json()

    assert result['name'][0] == USER_ERR_1


def test__rename_budget_category__empty_name__return_http_400():
    g = create_budget_group().json()
    c = create_budget_category(budget_group=g['id']).json()

    name = ''

    result = rename_budget_category(id=c['id'], name=name)

    assert result.status_code == 400


def test__rename_budget_category__from_C1_to_C2__rename_category_to_C2():
    name = 'C1'
    new_name = 'C2'

    g = create_budget_group().json()
    c1 = create_budget_category(
        name=name,
        budget_group=g['id']
    ).json()

    result = rename_budget_category(id=c1['id'], name=new_name).json()

    assert result['name'] == new_name


def test__rename_budget_category__valid__return_http_200():
    name = 'C1'
    new_name = 'C2'

    g = create_budget_group().json()
    c1 = create_budget_category(
        name=name,
        budget_group=g['id']
    ).json()

    result = rename_budget_category(id=c1['id'], name=new_name)

    assert result.status_code == 200


def test__rename_budget_category__valid__return_category_schema():
    name = 'C1'
    new_name = 'C2'

    g = create_budget_group().json()
    c1 = create_budget_category(
        name=name,
        budget_group=g['id']
    ).json()

    result = rename_budget_category(id=c1['id'], name=new_name).json()

    assert 'id' in result
    assert 'name' in result
    assert 'budget_group' in result


def test__list_budget_categories__created_C1_C2_C3__return_C1_C2_C3():
    g = create_budget_group().json()['id']
    c1 = create_budget_category(name='C1', budget_group=g).json()['id']
    c2 = create_budget_category(name='C2', budget_group=g).json()['id']
    c3 = create_budget_category(name='C3', budget_group=g).json()['id']

    category_list = list_budget_categories().json()

    idx = [category['id'] for category in category_list]

    assert c1 in idx
    assert c2 in idx
    assert c3 in idx


def test__list_budget_categories__valid__return_http_200():
    g = create_budget_group().json()['id']
    c1 = create_budget_category(name='C1', budget_group=g).json()['id']
    c2 = create_budget_category(name='C2', budget_group=g).json()['id']
    c3 = create_budget_category(name='C3', budget_group=g).json()['id']

    result = list_budget_categories()

    assert result.status_code == 200


def test__list_budget_categories__valid__return_category_schema():
    g = create_budget_group().json()['id']
    c1 = create_budget_category(name='C1', budget_group=g).json()['id']
    c2 = create_budget_category(name='C2', budget_group=g).json()['id']
    c3 = create_budget_category(name='C3', budget_group=g).json()['id']

    category_list = list_budget_categories().json()

    for category in category_list:
        assert 'id' in category
        assert 'name' in category
        assert 'budget_group' in category


def test__get_budget_category__non_existing_category__return_user_error_3():
    non_existing_category = 'non-existing'

    result = get_budget_category(id=non_existing_category).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing_category)


def test__get_budget_category__non_existing_category__return_http_404():
    non_existing_category = 'non-existing'

    result = get_budget_category(id=non_existing_category)

    assert result.status_code == 404


def test__get_budget_category__created_C1__return_C1():
    g = create_budget_group().json()['id']
    c1 = create_budget_category(name='C1', budget_group=g).json()

    result = get_budget_category(id=c1['id']).json()

    assert result['id'] == c1['id']
    assert result['name'] == c1['name']
    assert result['budget_group'] == c1['budget_group']


def test__get_budget_category__valid__return_http_200():
    g = create_budget_group().json()['id']
    c = create_budget_category(budget_group=g).json()['id']

    result = get_budget_category(id=c)

    assert result.status_code == 200


def test__get_budget_category__valid__return_category_schema():
    g = create_budget_group().json()['id']
    c = create_budget_category(budget_group=g).json()['id']

    result = get_budget_category(id=c).json()

    assert 'id' in result
    assert 'name' in result
    assert 'budget_group' in result


def test__assign_budget_group__non_existing_category__return_user_error_3():
    g = create_budget_group().json()['id']

    id = 'non-existing'

    result = assign_budget_group(id=id, group_id=g).json()

    assert result['detail'] == USER_ERR_3.format(id=id)


def test__assign_budget_group__non_existing_category__return_http_404():
    g = create_budget_group().json()['id']

    id = 'non-existing'

    result = assign_budget_group(id=id, group_id=g)

    assert result.status_code == 404


def test__assign_budget_group__non_existing_group__return_user_error_4():
    g1 = create_budget_group().json()['id']
    g2 = 'non-existing'
    c = create_budget_category(budget_group=g1).json()

    result = assign_budget_group(id=c['id'], group_id=g2).json()

    assert result['budget_group'][0] == USER_ERR_4.format(id=g2)


def test__assign_budget_group__non_existing_group__return_http_400():
    g1 = create_budget_group().json()['id']
    g2 = 'non-existing'
    c = create_budget_category(budget_group=g1).json()

    result = assign_budget_group(id=c['id'], group_id=g2)

    assert result.status_code == 400


def test__assign_budget_group__from_G1_to_G2__assign_G2():
    g1 = create_budget_group().json()['id']
    g2 = create_budget_group().json()['id']

    c1 = create_budget_category(
        budget_group=g1
    ).json()

    result = assign_budget_group(id=c1['id'], group_id=g2).json()

    assert result['budget_group'] == g2


def test__assign_budget_group__valid__return_http_200():
    g1 = create_budget_group().json()['id']
    g2 = create_budget_group().json()['id']

    c1 = create_budget_category(
        budget_group=g1
    ).json()

    result = assign_budget_group(id=c1['id'], group_id=g2)

    assert result.status_code == 200


def test__assign_budget_group__valid__return_category_schema():
    g1 = create_budget_group().json()['id']
    g2 = create_budget_group().json()['id']

    c1 = create_budget_category(
        budget_group=g1
    ).json()

    result = assign_budget_group(id=c1['id'], group_id=g2).json()

    assert 'id' in result
    assert 'name' in result
    assert 'budget_group' in result
