from api.data.constant import USER_ERR_1, USER_ERR_2, USER_ERR_6
from api.data.constant import SUPPORTED_BANK_ACCOUNT_TYPE
from api.data.bank_account_type import BankAccountType

from api.tests.utils.bank_account import create_bank_account
from api.tests.utils.bank_account import delete_bank_account
from api.tests.utils.bank_account import rename_bank_account
from api.tests.utils.bank_account import list_bank_accounts
from api.tests.utils.bank_account import get_bank_account
from api.tests.utils.bank_account import get_transactions_by_bank_account
from api.tests.utils.transaction import record_transaction
from api.tests.utils.transaction import get_transaction


def test__create_bank_account__empty_name__return_user_error_1():
    empty_name = ''

    result = create_bank_account(name=empty_name).json()

    assert result['name'][0] == USER_ERR_1


def test__create_bank_account__empty_name__return_http_400():
    empty_name = ''

    result = create_bank_account(name=empty_name)

    assert result.status_code == 400


def test__create_bank_account__unsupported_type__return_user_error_2():
    unsupported_type = 'WRONG_TYPE'

    result = create_bank_account(type=unsupported_type).json()

    assert result['type'][0] == USER_ERR_2.format(
        Type=unsupported_type, AvailableType=SUPPORTED_BANK_ACCOUNT_TYPE)


def test__create_bank_account__unsupported_type__return_http_400():
    unsupported_type = 'WRONG_TYPE'

    result = create_bank_account(type=unsupported_type)

    assert result.status_code == 400


def test__create_bank_account__BA1_as_name__create_account_named_BA1():
    name = 'BA1'

    result = create_bank_account(name='BA1').json()

    assert result['name'] == name


def test__create_bank_account__100_as_starting_balance__create_account_with_100_as_starting_balance():
    balance = 100

    result = create_bank_account(balance=balance).json()

    assert result['balance'] == balance


def test__create_bank_account__standard_account__create_a_standard_account():
    type = BankAccountType.STANDARD

    result = create_bank_account(type=type).json()

    assert result['type'] == type


def test__create_bank_account__saving_account__create_a_saving_account():
    type = BankAccountType.SAVING

    result = create_bank_account(type=type).json()

    assert result['type'] == type


def test__create_bank_account__trading_account__create_a_trading_account():
    type = BankAccountType.TRADING

    result = create_bank_account(type=type).json()

    assert result['type'] == type



def test__create_bank_account__valid__return_account_schema():
    created = create_bank_account().json()

    assert 'id' in created
    assert 'name' in created
    assert 'type' in created
    assert 'balance' in created


def test__create_bank_account__valid__return_http_201():
    created = create_bank_account()

    assert created.status_code == 201


def test__delete_bank_account__existing_account__delete_the_account():
    created = create_bank_account().json()

    delete_bank_account(created['id'])

    saved = get_bank_account(created['id'])

    assert saved.status_code == 400


def test__delete_bank_account__non_existing_account__return_user_error_3():
    invalid_id = 'invalid-id'

    result = delete_bank_account(invalid_id).json()

    assert result['id'][0] == USER_ERR_6.format(id=invalid_id)


def test__delete_bank_account__non_existing_account__return_http_404():
    invalid_id = 'invalid id'

    result = delete_bank_account(invalid_id)

    assert result.status_code == 400


def test__delete_bank_account__linked_transaction_T1__delete_transaction_T1():
    ba1 = create_bank_account().json()['id']
    t1 = record_transaction(bank_account_id=ba1).json()['id']

    delete_bank_account(ba1)

    result = get_transaction(t1)

    assert result.status_code == 400
    

def test__delete_bank_account__valid__return_http_200():
    created = create_bank_account().json()

    result = delete_bank_account(created['id'])

    assert result.status_code == 204


def test__rename_bank_account__from_BA1_to_BA2__rename_account_to_BA2():
    name = 'BA1'

    created = create_bank_account(name=name).json()

    new_name = 'BA2'

    result = rename_bank_account(id=created['id'], name=new_name).json()

    assert result['name'] == new_name


def test__rename_bank_account__valid__return_http_200():
    name = 'BA1'

    created = create_bank_account(name=name).json()

    new_name = 'BA2'

    result = rename_bank_account(id=created['id'], name=new_name)

    assert result.status_code == 200


def test__rename_bank_account__valid__return_account_schema():
    name = 'BA1'

    created = create_bank_account(name=name).json()

    new_name = 'BA2'

    result = rename_bank_account(id=created['id'], name=new_name).json()

    assert 'id' in result
    assert 'name' in result
    assert 'type' in result
    assert 'balance' in result


def test__rename_bank_account__empty_name__return_user_error_1():
    name = 'BA1'

    created = create_bank_account(name=name).json()

    new_name = ''

    result = rename_bank_account(id=created['id'], name=new_name).json()

    assert result['name'][0] == USER_ERR_1


def test__rename_bank_account__empty_name__return_http_400():
    name = 'BA1'

    created = create_bank_account(name=name).json()

    new_name = ''

    result = rename_bank_account(id=created['id'], name=new_name)

    assert result.status_code == 400


def test__rename_bank_account__non_existing_account__return_user_error_3():
    invalid_id = 'invalid-id'

    result = rename_bank_account(id=invalid_id).json()

    assert result['id'][0] == USER_ERR_6.format(id=invalid_id)


def test__rename_bank_account__non_existing_account__return_http_404():
    invalid_id = 'invalid-id'

    result = rename_bank_account(id=invalid_id)

    assert result.status_code == 400


def test__list_bank_account__BA1_BA2_BA3_created__return_BA1_BA2_BA3():
    ba1 = create_bank_account(name='BA1').json()['id']
    ba2 = create_bank_account(name='BA2').json()['id']
    ba3 = create_bank_account(name='BA3').json()['id']

    account_list = list_bank_accounts().json()

    idx = [account['id'] for account in account_list]

    assert ba1 in idx
    assert ba2 in idx
    assert ba3 in idx


def test__list_bank_account__valid__return_http_200():
    result = list_bank_accounts()

    assert result.status_code == 200


def test__list_bank_account__valid__return_account_schema():
    create_bank_account(name='BA1')
    create_bank_account(name='BA2')
    create_bank_account(name='BA3')

    account_list = list_bank_accounts().json()

    for account in account_list:
        assert 'id' in account
        assert 'name' in account
        assert 'type' in account
        assert 'balance' in account


def test__get_bank_account__created_BA1__return_BA1():
    name = 'BA1'
    type = BankAccountType.TRADING
    balance = 100.5

    ba1 = create_bank_account(name=name, type=type, balance=balance).json()

    result = get_bank_account(id=ba1['id']).json()

    assert result['id'] == ba1['id']
    assert result['name'] == ba1['name']
    assert result['type'] == ba1['type']
    assert result['balance'] == ba1['balance']


def test__get_bank_account__valid__return_http_200():
    ba1 = create_bank_account().json()['id']

    result = get_bank_account(id=ba1)

    assert result.status_code == 200


def test__get_bank_account__valid__return_account_schema():
    ba1 = create_bank_account().json()['id']

    result = get_bank_account(id=ba1).json()

    assert 'id' in result
    assert 'name' in result
    assert 'type' in result
    assert 'balance' in result


def test__get_bank_account__non_existing_account__return_user_error_3():
    invalid_id = 'invalid-id'

    result = get_bank_account(id=invalid_id).json()

    assert result['id'][0] == USER_ERR_6.format(id=invalid_id)


def test__get_bank_account__non_existing_account__return_http_404():
    invalid_id = 'invalid id'

    result = get_bank_account(id=invalid_id)

    assert result.status_code == 400


def test__get_linked_transactions__non_existing_account__return_user_error_3():
    invalid_id = 'invalid-id'

    result = get_transactions_by_bank_account(id=invalid_id).json()

    assert result['id'][0] == USER_ERR_6.format(id=invalid_id)


def test__get_linked_transactions__non_existing_account__return_http_404():
    invalid_id = 'invalid-id'

    result = get_transactions_by_bank_account(id=invalid_id)

    assert result.status_code == 400


def test__get_linked_transactions__linked_T1__return_T1():
    ba1 = create_bank_account().json()['id']
    t1 = record_transaction(bank_account_id=ba1).json()['id']

    result = get_transactions_by_bank_account(id=ba1).json()

    idx = [transaction['id'] for transaction in result]

    assert t1 in idx


def test__get_linked_transactions__linked_T1_T2_not_linked_T3__return_T1_T2():
    ba = create_bank_account().json()['id']

    t1 = record_transaction(bank_account_id=ba).json()['id']
    t2 = record_transaction(bank_account_id=ba).json()['id']
    t3 = record_transaction().json()['id']

    result = get_transactions_by_bank_account(id=ba).json()

    idx = [t['id'] for t in result]

    assert t1 in idx
    assert t2 in idx
    assert t3 not in idx


def test__get_linked_transactions__valid__return_http_200():
    ba1 = create_bank_account().json()['id']

    result = get_transactions_by_bank_account(id=ba1)

    assert result.status_code == 200


def test__get_linked_transactions__valid__return_transaction_schema():
    ba1 = create_bank_account().json()['id']
    t1 = record_transaction(bank_account_id=ba1).json()['id']

    result = get_transactions_by_bank_account(id=ba1).json()

    for transaction in result:
        assert 'id' in transaction
        assert 'date' in transaction
        assert 'label' in transaction
        assert 'amount' in transaction
        assert 'bank_account_id' in transaction
