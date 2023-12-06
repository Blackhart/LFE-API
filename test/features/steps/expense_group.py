from behave import *

from api.test.utils.expense_group import create_expense_group


@when('the user creates an expense group')
def step_impl(context):
    context.answer = create_expense_group()
    
    
@when('the user creates an expense group with an empty name')
def step_impl(context):
    group_name = ''
    
    context.answer = create_expense_group(group_name)
    

@then('the system creates the expense group')
def step_impl(context):
    status_code = context.answer.status_code

    assert status_code == 201
    

@then('the system returns an unique identifier for the expense group')
def step_impl(context):
    answer = context.answer.json()

    assert answer['id']