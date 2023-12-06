from behave import *

from api.test.utils.bank_account import create_bank_account
from api.test.utils.bank_account import create_standard_account
from api.test.utils.bank_account import create_saving_account
from api.test.utils.bank_account import create_trading_account
from api.test.utils.bank_account import delete_bank_account
from api.test.utils.bank_account import rename_bank_account
from api.test.utils.bank_account import list_bank_accounts
from api.test.utils.bank_account import get_bank_accounts_list
from api.test.utils.bank_account import get_bank_account


@given('a bank account named "{name}" is created')
@given('a standard bank account named "{name}" is created')
def step_impl(context, name):
    context.answer = create_standard_account(name=name)
    
    if not hasattr(context, 'names'):
        context.names = []
        
    context.names.append(name)
    

@given('a trading bank account named "{name}" is created')
def step_impl(context, name):
    context.answer = create_trading_account(name=name)
    
    if not hasattr(context, 'names'):
        context.names = []
        
    context.names.append(name)
    

@given('a saving bank account named "{name}" is created')
def step_impl(context, name):
    context.answer = create_saving_account(name=name)
    
    if not hasattr(context, 'names'):
        context.names = []
        
    context.names.append(name)
    

@given('a bank account is created')
@given('a standard bank account is created')
@when('the user creates a standard bank account')
def step_impl(context):
    context.answer = create_standard_account()


@given('a trading bank account is created')
@when('the user creates a trading bank account')
def step_impl(context):
    context.answer = create_trading_account()


@given('a saving bank account is created')
@when('the user creates a saving bank account')
def step_impl(context):
    context.answer = create_saving_account()


@when('the user creates a bank account with an empty name')
def step_impl(context):
    context.answer = create_standard_account(name="")


@when('the user creates a bank account with an invalid type')
def step_impl(context):
    context.answer = create_bank_account(type="INVALID_TYPE")


@when('the user deletes the bank account')
def step_impl(context):
    answer = context.answer.json()
    bank_account_id = answer['id']

    context.answer = delete_bank_account(bank_account_id)


@when('the user deletes a bank account with an invalid id')
def step_impl(context):
    invalid_account_id = 'invalid account id'

    context.answer = delete_bank_account(invalid_account_id)


@when('the user renames the bank account name to "{name}"')
def step_impl(context, name):
    answer = context.answer.json()
    bank_account_id = answer['id']
    bank_account_name = name

    context.answer = rename_bank_account(bank_account_id, bank_account_name)


@when('the user renames a bank account name using an invalid id')
def step_impl(context):
    invalid_account_id = 'invalid account id'

    context.answer = rename_bank_account(invalid_account_id)
    

@when('the user renames the bank account name to an empty name')
def step_impl(context):
    answer = context.answer.json()
    bank_account_id = answer['id']
    
    context.answer = rename_bank_account(bank_account_id, name='')


@when('the user list the bank accounts')
def step_impl(context):
    context.answer = list_bank_accounts()
    

@when('the user gets the bank account')
def step_impl(context):
    answer = context.answer.json()
    bank_account_id = answer['id']
    
    context.answer = get_bank_account(bank_account_id)
    
    
@when('the user gets a bank account using an invalid id')
def step_impl(context):
    invalid_account_id = 'invalid account id'
    
    context.answer = get_bank_account(invalid_account_id)


@then('the system creates the bank account')
def step_impl(context):
    status_code = context.answer.status_code

    assert status_code == 201


@then('the system returns an unique identifier for the bank account')
def step_impl(context):
    answer = context.answer.json()

    assert answer['id']


@then('the system deletes the bank account')
def step_impl(context):
    status_code = context.answer.status_code

    assert status_code == 200


@then('the system renames the bank account name to "{name}"')
def step_impl(context, name):
    answer = context.answer.json()
    status_code = context.answer.status_code
    renamed = answer['name']

    assert status_code == 200
    assert renamed == name


@then('the system returns the three created accounts')
def step_impl(context):
    answer = context.answer.json()
    names = get_bank_accounts_list(answer)
    
    for name in context.names:
        if name not in names:
            assert False
            
    assert True
    
    
@then('the system returns the bank account')
def step_impl(context):
    answer = context.answer.json()
    name_from_the_db = answer['name']
    name_recorded = context.names[0]
    
    assert name_recorded == name_from_the_db