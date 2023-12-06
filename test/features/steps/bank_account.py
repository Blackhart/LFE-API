from behave import *

from api.model.poco.bank_account_type import BankAccountType

from api.test.utils.bank_account import create_bank_account
from api.test.utils.bank_account import delete_bank_account
from api.test.utils.bank_account import rename_bank_account
from api.test.utils.bank_account import list_bank_accounts
from api.test.utils.bank_account import get_bank_account


@given('a bank account named "{name}" is created')
@given('a standard bank account named "{name}" is created')
def step_impl(context, name):
    type = BankAccountType.STANDARD
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('a trading bank account named "{name}" is created')
def step_impl(context, name):
    type = BankAccountType.TRADING
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('a saving bank account named "{name}" is created')
def step_impl(context, name):
    type = BankAccountType.SAVING
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('a bank account is created')
@given('a standard bank account is created')
@when('the user creates a standard bank account')
def step_impl(context):
    name = "My Standard Account"
    type = BankAccountType.STANDARD
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('a trading bank account is created')
@when('the user creates a trading bank account')
def step_impl(context):
    name = "My Trading Account"
    type = BankAccountType.TRADING
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('a saving bank account is created')
@when('the user creates a saving bank account')
def step_impl(context):
    name = "My Saving Account"
    type = BankAccountType.SAVING
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@when('the user creates a bank account with an empty name')
def step_impl(context):
    name = ''
    type = BankAccountType.SAVING
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@when('the user creates a bank account with an invalid type')
def step_impl(context):
    name = 'My Bank Account'
    type = 'INVALID_TYPE'
    balance = 0

    answer = create_bank_account(name, type, balance)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@when('the user deletes the bank account')
def step_impl(context):
    id = context.created[0]['id']

    answer = delete_bank_account(id)

    if not hasattr(context, 'deleted'):
        context.deleted = []

    context.deleted.append(answer)
    context.last = answer


@when('the user deletes a bank account with an invalid id')
def step_impl(context):
    id = 'invalid account id'

    answer = delete_bank_account(id)

    if not hasattr(context, 'deleted'):
        context.deleted = []

    context.deleted.append(answer)
    context.last = answer


@when('the user renames the bank account name to "{name}"')
def step_impl(context, name):
    id = context.created[0]['id']

    answer = rename_bank_account(id, name)

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@when('the user renames a bank account name using an invalid id')
def step_impl(context):
    id = 'invalid account id'

    answer = rename_bank_account(id)

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@when('the user renames the bank account name to an empty name')
def step_impl(context):
    id = context.last['id']

    answer = rename_bank_account(id, name='')

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@when('the user list the bank accounts')
def step_impl(context):
    answer = list_bank_accounts()

    if not hasattr(context, 'listed'):
        context.listed = []

    context.listed.append(answer)
    context.last = answer


@when('the user gets the bank account')
def step_impl(context):
    id = context.last['id']

    answer = get_bank_account(id)

    if not hasattr(context, 'retrieved'):
        context.retrieved = []

    context.retrieved.append(answer)
    context.last = answer


@when('the user gets a bank account using an invalid id')
def step_impl(context):
    id = 'invalid account id'

    answer = get_bank_account(id)

    if not hasattr(context, 'retrieved'):
        context.retrieved = []

    context.retrieved.append(answer)
    context.last = answer


@then('the system creates the bank account')
def step_impl(context):
    assert context.last['code'] == 201
    
    retrieved = get_bank_account(context.last['id'])

    assert retrieved['code'] == 200
    assert context.last['id'] == retrieved['id']
    assert context.last['name'] == retrieved['name']


@then('the system returns an unique identifier for the bank account')
def step_impl(context):
    assert context.last['id']


@then('the system deletes the bank account')
def step_impl(context):
    assert context.last['code'] == 200


@then('the system renames the bank account name to "{name}"')
def step_impl(context, name):
    code = context.last['code']
    renamed = context.last['name']

    assert code == 200
    assert renamed == name


@then('the system returns the three created accounts')
def step_impl(context):
    listed = context.listed
    created = context.created

    for item_created in created:
        found = False

        for item_listed in listed[0]['items']:

            if item_created['id'] == item_listed['id'] and item_created['name'] == item_listed['name'] and item_created['type'] == item_listed['type'] and item_created['balance'] == item_listed['balance']:
                found = True
                
        if not found:
            assert False

    assert True


@then('the system returns the bank account')
def step_impl(context):
    created = context.created[0]
    retrieved = context.retrieved[0]

    assert created['id'] == retrieved['id']
    assert created['name'] == retrieved['name']
    assert created['type'] == retrieved['type']
    assert created['balance'] == retrieved['balance']
