from api.data.constant import USER_ERR_6, USER_ERR_7, USER_ERR_10

from api.tests.utils.transaction import record_transaction
from api.tests.utils.transaction import delete_transaction
from api.tests.utils.transaction import get_transaction
from api.tests.utils.transaction import update_transaction
from api.tests.utils.bank_account import create_bank_account
from api.tests.utils.bank_account import get_bank_account


def test__record_transaction__invalid_date_format__return_user_error_7():
    invalid_date_format = '01-01-2021'

    result = record_transaction(date=invalid_date_format).json()

    assert result['date'][0] == USER_ERR_7.format(date=invalid_date_format)


def test__record_transaction__non_existing_bank_account__return_user_error_6():
    non_existing_bank_account = "non-existing"

    result = record_transaction(
        bank_account_id=non_existing_bank_account).json()

    assert result['bank_account_id'][0] == USER_ERR_6.format(
        id=non_existing_bank_account)


def test__record_transaction__2020_01_01_as_date__record_transaction_with_date_2020_01_01():
    date = '2020-01-01'

    result = record_transaction(date=date).json()

    assert result['date'] == date


def test__record_transaction__My_Transaction_1_as_label__record_transaction_with_label_My_Transaction_1():
    label = 'My Transaction 1'

    result = record_transaction(label=label).json()

    assert result['label'] == label


def test__record_transaction__100_as_amount__record_transaction_with_amount_100():
    amount = 100

    result = record_transaction(amount=amount).json()

    assert result['amount'] == float(amount)


def test__record_transaction__minus_100_as_amount__record_transaction_with_amount_minus_100():
    amount = -100

    result = record_transaction(amount=amount).json()

    assert result['amount'] == float(amount)


def test__record_transaction__BA1_as_bank_account__record_transaction_with_bank_account_BA1():
    bank_account_name = 'BA1'

    bank_account = create_bank_account(name=bank_account_name).json()['id']
    result = record_transaction(bank_account_id=bank_account).json()

    assert result['bank_account_id'] == bank_account


def test__record_transaction__bank_account_balance_is_0__record_100_as_amount__balance_is_100():
    bank_account = create_bank_account(balance=0).json()['id']

    record_transaction(bank_account_id=bank_account, amount=100)

    bank_account = get_bank_account(id=bank_account).json()

    assert bank_account['balance'] == 100


def test__record_transaction__bank_account_balance_is_0__record_minus_100_as_amount__balance_is_minus_100():
    bank_account = create_bank_account(balance=0).json()['id']

    record_transaction(bank_account_id=bank_account, amount=-100)

    bank_account = get_bank_account(id=bank_account).json()

    assert bank_account['balance'] == -100


def test__record_transaction__valid__return_http_201():
    result = record_transaction()

    assert result.status_code == 201


def test__record_transaction__valid__return_transaction_schema():
    result = record_transaction().json()

    assert 'id' in result
    assert 'date' in result
    assert 'label' in result
    assert 'amount' in result
    assert 'bank_account_id' in result


def test__delete_transaction__non_existing_transaction__return_user_error_3():
    non_existing = 'non-existing'

    result = delete_transaction(id=non_existing).json()

    assert result['id'][0] == USER_ERR_10.format(id=non_existing)


def test__delete_transaction__non_existing_transaction__return_http_404():
    non_existing = 'non-existing'

    result = delete_transaction(id=non_existing)

    assert result.status_code == 400


def test__delete_transaction__created_T1__delete_T1():
    created = record_transaction().json()

    delete_transaction(id=created['id'])

    result = get_transaction(id=created['id'])

    assert result.status_code == 400


def test__delete_transaction__bank_account_balance_is_100__transaction_amount_is_100__balance_is_0():
    bank_account = create_bank_account(balance=0).json()['id']

    transaction_id = record_transaction(
        bank_account_id=bank_account, amount=100).json()['id']

    delete_transaction(id=transaction_id)

    bank_account = get_bank_account(id=bank_account).json()

    assert bank_account['balance'] == 0


def test__delete_transaction__bank_account_balance_is_minus_100__transaction_amount_is_minus_100__balance_is_0():
    bank_account = create_bank_account(balance=0).json()['id']

    transaction_id = record_transaction(
        bank_account_id=bank_account, amount=-100).json()['id']

    delete_transaction(id=transaction_id)

    bank_account = get_bank_account(id=bank_account).json()

    assert bank_account['balance'] == 0


def test__delete_transaction__valid__return_http_204():
    created = record_transaction().json()

    result = delete_transaction(id=created['id'])

    assert result.status_code == 204


def test__get_transaction__non_existing_transaction__return_user_error_3():
    non_existing = 'non-existing'

    result = get_transaction(id=non_existing).json()

    assert result['id'][0] == USER_ERR_10.format(id=non_existing)


def test__get_transaction__non_existing_transaction__return_http_404():
    non_existing = 'non-existing'

    result = get_transaction(id=non_existing)

    assert result.status_code == 400


def test__get_transaction__created_T1__get_T1():
    created = record_transaction().json()

    result = get_transaction(id=created['id']).json()

    assert result['id'] == created['id']
    assert result['date'] == created['date']
    assert result['label'] == created['label']
    assert result['amount'] == created['amount']
    assert result['bank_account_id'] == created['bank_account_id']


def test__get_transaction__valid__return_http_200():
    result = get_transaction(id=record_transaction().json()['id'])

    assert result.status_code == 200


def test__get_transaction__valid__return_transaction_schema():
    result = get_transaction(id=record_transaction().json()['id']).json()

    assert 'id' in result
    assert 'date' in result
    assert 'label' in result
    assert 'amount' in result
    assert 'bank_account_id' in result


def test__update_transaction__non_existing_transaction__return_user_error_3():
    transaction_id = 'non-existing'
    new_date = '1990-01-01'
    new_label = 'New Label'
    new_amount = 100
    new_bank_account = create_bank_account().json()['id']

    result = update_transaction(transaction_id, new_date, new_label, new_amount, new_bank_account).json()

    assert result['id'][0] == USER_ERR_10.format(id=transaction_id)


def test__update_transaction__non_existing_transaction__return_http_404():
    transaction_id = 'non-existing'
    new_date = '1990-01-01'
    new_label = 'New Label'
    new_amount = 100
    new_bank_account = create_bank_account().json()['id']

    result = update_transaction(transaction_id, new_date, new_label, new_amount, new_bank_account)

    assert result.status_code == 400


def test__update_transaction__invalid_date_format__return_user_error_7():
    transaction = record_transaction().json()

    invalid_date_format = '01-01-2021'
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = transaction['bank_account_id']

    result = update_transaction(transaction['id'], invalid_date_format, new_label, new_amount, new_bank_account).json()

    assert result['date'][0] == USER_ERR_7.format(date=invalid_date_format)


def test__update_transaction__invalid_date_format__return_http_400():
    transaction = record_transaction().json()

    invalid_date_format = '01-01-2021'
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = transaction['bank_account_id']

    result = update_transaction(transaction['id'], invalid_date_format, new_label, new_amount, new_bank_account)

    assert result.status_code == 400


def test__update_transaction__non_existing_bank_account__return_user_error_6():
    transaction = record_transaction().json()

    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = transaction['amount']
    non_existing_bank_account = "non-existing"

    result = update_transaction(transaction['id'], new_date, new_label, new_amount, non_existing_bank_account).json()

    assert result['bank_account_id'][0] == USER_ERR_6.format(
        id=non_existing_bank_account)


def test__update_transaction__non_existing_bank_account__return_http_400():
    transaction = record_transaction().json()

    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = transaction['amount']
    non_existing_bank_account = "non-existing"

    result = update_transaction(transaction['id'], new_date, new_label, new_amount, non_existing_bank_account)

    assert result.status_code == 400


def test__update_transaction__new_date__update_transaction_with_new_date():
    transaction = record_transaction().json()

    new_date = '1990-01-01'
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = transaction['bank_account_id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    transaction = get_transaction(id=transaction['id']).json()

    assert transaction['date'] == new_date


def test__update_transaction__new_label__update_transaction_with_new_label():
    transaction = record_transaction().json()

    new_date = transaction['date']
    new_label = 'new label'
    new_amount = transaction['amount']
    new_bank_account = transaction['bank_account_id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    transaction = get_transaction(id=transaction['id']).json()

    assert transaction['label'] == new_label


def test__update_transaction__new_amount__update_transaction_with_new_amount():
    transaction = record_transaction().json()

    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = 1000
    new_bank_account = transaction['bank_account_id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    transaction = get_transaction(id=transaction['id']).json()

    assert transaction['amount'] == new_amount


def test__update_transaction__bank_account_balance_is_100__previous_amount_is_100__new_amount_is_50__balance_is_50():
    bank_account = create_bank_account(balance=0).json()

    transaction = record_transaction(
        bank_account_id=bank_account['id'], amount=100).json()
    
    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = 50
    new_bank_account = transaction['bank_account_id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    bank_account = get_bank_account(id=bank_account['id']).json()

    assert bank_account['balance'] == 50


def test__update_transaction__bank_account_balance_is_minus_100__previous_amount_is_minus_100__new_amount_is_minus_50__balance_is_minus_50():
    bank_account = create_bank_account(balance=0).json()['id']

    transaction = record_transaction(
        bank_account_id=bank_account, amount=-100).json()
    
    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = -50
    new_bank_account = transaction['bank_account_id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    bank_account = get_bank_account(id=bank_account).json()

    assert bank_account['balance'] == -50


def test__update_transaction__new_bank_account__update_transaction_with_new_bank_account():
    transaction = record_transaction().json()

    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = create_bank_account().json()['id']

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    transaction = get_transaction(id=transaction['id']).json()

    assert transaction['bank_account_id'] == new_bank_account


def test__update_transaction__BA1_balance_is_100__BA2_balance_is_0__transaction_amount_is_100__change_transaction_bank_account_from_BA1_to_BA2__BA1_balance_is_0__BA2_balance_is_100():
    ba1_id = create_bank_account(balance=0).json()['id']
    ba2_id = create_bank_account(balance=0).json()['id']

    transaction = record_transaction(
        bank_account_id=ba1_id, amount=100).json()

    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = ba2_id

    update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    ba1 = get_bank_account(id=ba1_id).json()
    ba2 = get_bank_account(id=ba2_id).json()

    assert ba1['balance'] == 0
    assert ba2['balance'] == 100


def test__update_transaction__valid__return_http_204():
    transaction = record_transaction().json()
    
    new_date = transaction['date']
    new_label = transaction['label']
    new_amount = transaction['amount']
    new_bank_account = transaction['bank_account_id']

    result = update_transaction(transaction['id'], new_date, new_label, new_amount, new_bank_account)

    assert result.status_code == 204
