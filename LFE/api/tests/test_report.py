import calendar

from api.data.constant import USER_ERR_6, USER_ERR_8

from api.tests.utils.report import get_net_worth_report
from api.tests.utils.bank_account import create_bank_account
from api.tests.utils.transaction import record_transaction


def test__get_net_worth__non_existing_bank_account__return_user_error_6():
    non_existing = 'non-existing-bank-account'

    response = get_net_worth_report([non_existing]).json()

    assert response['bank_accounts']['0'][0] == USER_ERR_6.format(
        id=non_existing)


def test__get_net_worth__non_existing_bank_account__return_http_400():
    non_existing = 'non-existing-bank-account'

    response = get_net_worth_report([non_existing])

    assert response.status_code == 400


def test__get_net_worth__empty_bank_accounts__return_empty_daily():
    response = get_net_worth_report([])

    assert response.json()['daily'] == {}


def test__get_net_worth__empty_bank_accounts__return_empty_monthly():
    response = get_net_worth_report([])

    assert response.json()['monthly'] == {}


def test__get_net_worth__empty_bank_accounts__return_empty_yearly():
    response = get_net_worth_report([])

    assert response.json()['yearly'] == {}


def test__get_net_worth__bank_account_without_transactions__return_empty_daily():
    ba = create_bank_account().json()['id']

    response = get_net_worth_report([ba]).json()

    assert response['daily'] == {}


def test__get_net_worth__bank_account_without_transactions__return_empty_monthly():
    ba = create_bank_account().json()['id']

    response = get_net_worth_report([ba]).json()

    assert response['monthly'] == {}


def test__get_net_worth__bank_account_without_transactions__return_empty_yearly():
    ba = create_bank_account().json()['id']

    response = get_net_worth_report([ba]).json()

    assert response['yearly'] == {}


def test__get_net_worth__record_100_a_day__return_daily_100():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['daily']['2024-01-01'] == 100


def test__get_net_worth__record_100_twice_a_day__return_daily_200():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['daily']['2024-01-01'] == 200


def test__get_net_worth__record_100_every_day__return_daily_adding_up_100_per_days():
    ba = create_bank_account().json()['id']

    num_days = calendar.monthrange(2024, 1)[1]
    for i in range(1, num_days + 1):
        record_transaction(amount=100, bank_account=ba, date=f'2024-01-{i}')

    response = get_net_worth_report([ba]).json()

    for day in response['daily']:
        assert response['daily'][day] == 100 * (int(day.split('-')[2]))


def test__get_net_worth__record_100_a_month__return_monthly_100():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['monthly']['2024-01'] == 100


def test__get_net_worth__record_100_twice_a_month__return_monthly_200():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['monthly']['2024-01'] == 200


def test__get_net_worth__record_100_every_month__return_monthly_adding_up_100_per_month():
    ba = create_bank_account().json()['id']

    for i in range(1, 13):
        record_transaction(amount=100, bank_account=ba,
                           date=f'2024-{str(i).zfill(2)}-01')

    response = get_net_worth_report([ba]).json()

    for month in response['monthly']:
        assert response['monthly'][month] == 100 * (int(month.split('-')[1]))


def test__get_net_worth__record_100_a_year__return_yearly_100():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['yearly']['2024'] == 100


def test__get_net_worth__record_100_twice_a_year__return_yearly_200():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba)

    response = get_net_worth_report([ba]).json()

    assert response['yearly']['2024'] == 200


def test__get_net_worth__record_100_every_year__return_yearly_adding_up_100_per_year():
    ba = create_bank_account().json()['id']

    for i in range(1990, 2024):
        record_transaction(amount=100, bank_account=ba, date=f'{i}-01-01')

    response = get_net_worth_report([ba]).json()

    for year in response['yearly']:
        assert response['yearly'][year] == 100 * \
            (int(year.split('-')[0]) - 1989)


def test__get_net_worth__record_100_a_day_in_2_bank_accounts__return_daily_200():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['daily']['2024-01-01'] == 200


def test__get_net_worth__record_100_twice_a_day_in_2_bank_accounts__return_daily_400():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['daily']['2024-01-01'] == 400


def test__get_net_worth__record_100_every_day_in_2_bank_accounts__return_daily_adding_up_200_per_days():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    num_days = calendar.monthrange(2024, 1)[1]
    for i in range(1, num_days + 1):
        record_transaction(amount=100, bank_account=ba1, date=f'2024-01-{i}')
        record_transaction(amount=100, bank_account=ba2, date=f'2024-01-{i}')

    response = get_net_worth_report([ba1, ba2]).json()

    for day in response['daily']:
        assert response['daily'][day] == 200 * (int(day.split('-')[2]))


def test__get_net_worth__record_100_a_month_in_2_bank_accounts__return_monthly_200():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['monthly']['2024-01'] == 200


def test__get_net_worth__record_100_twice_a_month_in_2_bank_accounts__return_monthly_400():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['monthly']['2024-01'] == 400


def test__get_net_worth__record_100_every_month_in_2_bank_accounts__return_monthly_adding_up_200_per_month():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    for i in range(1, 13):
        record_transaction(amount=100, bank_account=ba1,
                           date=f'2024-{str(i).zfill(2)}-01')
        record_transaction(amount=100, bank_account=ba2,
                           date=f'2024-{str(i).zfill(2)}-01')

    response = get_net_worth_report([ba1, ba2]).json()

    for month in response['monthly']:
        assert response['monthly'][month] == 200 * (int(month.split('-')[1]))


def test__get_net_worth__record_100_a_year_in_2_bank_accounts__return_yearly_200():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['yearly']['2024'] == 200


def test__get_net_worth__record_100_twice_a_year_in_2_bank_accounts__return_yearly_400():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba1)
    record_transaction(date='2024-01-01', amount=100, bank_account=ba2)
    record_transaction(date='2024-01-02', amount=100, bank_account=ba2)

    response = get_net_worth_report([ba1, ba2]).json()

    assert response['yearly']['2024'] == 400


def test__get_net_worth__record_100_every_year_in_2_bank_accounts__return_yearly_adding_up_200_per_year():
    ba1 = create_bank_account().json()['id']
    ba2 = create_bank_account().json()['id']

    for i in range(1990, 2024):
        record_transaction(amount=100, bank_account=ba1, date=f'{i}-01-01')
        record_transaction(amount=100, bank_account=ba2, date=f'{i}-01-01')

    response = get_net_worth_report([ba1, ba2]).json()

    for year in response['yearly']:
        assert response['yearly'][year] == 200 * \
            (int(year.split('-')[0]) - 1989)


def test__get_net_worth__record_100_in_2024_01_01__start_date_2024_01_02__does_not_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], start_date='2024-01-02').json()

    assert response['daily'] == {}


def test__get_net_worth__record_100_in_2024_01_01__start_date_2024_01_01__does_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], start_date='2024-01-01').json()

    assert response['daily']['2024-01-01'] == 100


def test__get_net_worth__record_100_in_2024_01_01__start_date_is_none__does_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-01', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], start_date=None).json()

    assert response['daily']['2024-01-01'] == 100


def test__get_net_worth__record_100_in_2024_01_02__end_date_2024_01_01__does_not_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-02', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], end_date='2024-01-01').json()

    assert response['daily'] == {}


def test__get_net_worth__record_100_in_2024_01_02__end_date_2024_01_02__does_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-02', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], end_date='2024-01-02').json()

    assert response['daily']['2024-01-02'] == 100


def test__get_net_worth__record_100_in_2024_01_02__end_date_is_none__does_take_transaction_in_net_worth():
    ba = create_bank_account().json()['id']

    record_transaction(date='2024-01-02', amount=100, bank_account=ba)

    response = get_net_worth_report([ba], end_date=None).json()

    assert response['daily']['2024-01-02'] == 100


def test__get_net_worth__start_date_occurs_after_end_date__return_user_error_8():
    ba = create_bank_account().json()['id']

    response = get_net_worth_report(
        [ba], start_date='2024-01-02', end_date='2024-01-01').json()

    assert response['non_field_errors'][0] == USER_ERR_8.format(
        start_date='2024-01-02', end_date='2024-01-01')


def test__get_net_worth__start_date_occurs_after_end_date__return_http_400():
    ba = create_bank_account().json()['id']

    response = get_net_worth_report(
        [ba], start_date='2024-01-02', end_date='2024-01-01')

    assert response.status_code == 400


def test__get_net_worth__valid__return_http_200():
    ba = create_bank_account().json()['id']
    t = record_transaction(amount=100, bank_account=ba)

    response = get_net_worth_report([ba])

    assert response.status_code == 200
