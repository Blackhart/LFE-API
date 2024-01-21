from api.data.constant import USER_ERR_3, USER_ERR_6, USER_ERR_7

from api.tests.utils.transaction import record_transaction
from api.tests.utils.transaction import get_transaction
from api.tests.utils.bank_account import create_bank_account


def test__record_transaction__invalid_date_format__return_user_error_7():
    invalid_date_format = '01-01-2021'

    result = record_transaction(date=invalid_date_format).json()

    assert result['date'][0] == USER_ERR_7.format(date=invalid_date_format)


def test__record_transaction__non_existing_bank_account_id__return_user_error_6():
    non_existing_bank_account_id = "non-existing"

    result = record_transaction(
        bank_account_id=non_existing_bank_account_id).json()

    assert result['bank_account_id'][0] == USER_ERR_6.format(
        id=non_existing_bank_account_id)


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


def test__record_transaction__BA1_as_bank_account_id__record_transaction_with_bank_account_id_BA1():
    bank_account_name = 'BA1'

    bank_account_id = create_bank_account(name=bank_account_name).json()['id']
    result = record_transaction(bank_account_id=bank_account_id).json()

    assert result['bank_account_id'] == bank_account_id


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


def test__get_transaction__non_existing_transaction__return_user_error_3():
    non_existing = 'non-existing'

    result = get_transaction(id=non_existing).json()

    assert result['detail'] == USER_ERR_3.format(id=non_existing)


def test__get_transaction__non_existing_transaction__return_http_404():
    non_existing = 'non-existing'

    result = get_transaction(id=non_existing)

    assert result.status_code == 404


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
