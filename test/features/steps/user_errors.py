from behave import *


@then('the system returns error 1')
def step_impl(context):
    answer = context.answer.json()
    status_code = context.answer.status_code
    status = answer['status']
    error_msg = answer['errors']['json']['name'][0]
    
    assert status_code == 422
    assert status == 'Unprocessable Entity'
    assert error_msg == "Name should not be empty."


@then('the system returns error 2')
def step_impl(context):
    answer = context.answer.json()
    status_code = context.answer.status_code
    status = answer['status']
    error_msg = answer['errors']['json']['type'][0]
    
    assert status_code == 422
    assert status == 'Unprocessable Entity'
    assert error_msg == "Bank account type is not supported. Should be one of ['STANDARD', 'SAVING', 'TRADING']."


@then('the system returns error 3')
def step_impl(context):
    answer = context.answer.json()
    status_code = context.answer.status_code
    status = answer['status']
    error_msg = answer['message']

    assert status_code == 404
    assert status == 'Not Found'
    assert error_msg == "Bank account ID not found."