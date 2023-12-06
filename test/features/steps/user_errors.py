from behave import *


@then('the system returns error 1')
def step_impl(context):
    code = context.last['code']
    status = context.last['status']
    error = context.last['errors']['json']['name'][0]
    
    assert code == 422
    assert status == 'Unprocessable Entity'
    assert error == "Name should not be empty."


@then('the system returns error 2')
def step_impl(context):
    code = context.last['code']
    status = context.last['status']
    error = context.last['errors']['json']['type'][0]
    
    assert code == 422
    assert status == 'Unprocessable Entity'
    assert error == "Bank account type is not supported. Should be one of ['STANDARD', 'SAVING', 'TRADING']."


@then('the system returns error 3')
def step_impl(context):
    code = context.last['code']
    status = context.last['status']
    error = context.last['message']

    assert code == 404
    assert status == 'Not Found'
    assert error == "ID not found."