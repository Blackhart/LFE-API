from behave import *

from api.test.utils.expense_group import create_expense_group
from api.test.utils.expense_group import delete_expense_group
from api.test.utils.expense_group import rename_expense_group
from api.test.utils.expense_group import list_expense_groups
from api.test.utils.expense_group import get_expense_group


@given('an expense group named "{name}" is created')
def step_impl(context, name):
    answer = create_expense_group(name)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@given('an expense group is created')
@when('the user creates an expense group')
def step_impl(context):
    name = 'the user creates an expense group'

    answer = create_expense_group(name)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@when('the user creates an expense group with an empty name')
def step_impl(context):
    name = ''

    answer = create_expense_group(name)

    if not hasattr(context, 'created'):
        context.created = []

    context.created.append(answer)
    context.last = answer


@when('the user gets the expense group')
def step_impl(context):
    id = context.last['id']

    answer = get_expense_group(id)

    if not hasattr(context, 'retrieved'):
        context.retrieved = []

    context.retrieved.append(answer)
    context.last = answer


@when('the user gets an expense group using an invalid id')
def step_impl(context):
    id = 'invalid group id'

    answer = get_expense_group(id)

    if not hasattr(context, 'retrieved'):
        context.retrieved = []

    context.retrieved.append(answer)
    context.last = answer


@when('the user list the expense groups')
def step_impl(context):
    answer = list_expense_groups()

    if not hasattr(context, 'listed'):
        context.listed = []

    context.listed.append(answer)
    context.last = answer


@when('the user deletes the expense group')
def step_impl(context):
    id = context.created[0]['id']

    answer = delete_expense_group(id)

    if not hasattr(context, 'deleted'):
        context.deleted = []

    context.deleted.append(answer)
    context.last = answer


@when('the user deletes an expense group using an invalid id')
def step_impl(context):
    id = 'invalid group id'

    answer = delete_expense_group(id)

    if not hasattr(context, 'deleted'):
        context.deleted = []

    context.deleted.append(answer)
    context.last = answer


@when('the user renames the expense group name to "{name}"')
def step_impl(context, name):
    id = context.last['id']

    answer = rename_expense_group(id, name)

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@when('the user renames a expense group name using an invalid id')
def step_impl(context):
    id = 'invalid account id'

    answer = rename_expense_group(id)

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@when('the user renames the expense group name to an empty name')
def step_impl(context):
    id = context.last['id']

    answer = rename_expense_group(id, name='')

    if not hasattr(context, 'renamed'):
        context.renamed = []

    context.renamed.append(answer)
    context.last = answer


@then('the system creates the expense group')
def step_impl(context):
    assert context.last['code'] == 201

    retrieved = get_expense_group(context.last['id'])

    assert retrieved['code'] == 200
    assert context.last['id'] == retrieved['id']
    assert context.last['name'] == retrieved['name']


@then('the system returns an unique identifier for the expense group')
def step_impl(context):
    assert context.last['id']


@then('the system returns the expense group')
def step_impl(context):
    created = context.created[0]
    retrieved = context.retrieved[0]

    assert created['id'] == retrieved['id']
    assert created['name'] == retrieved['name']


@then('the system returns the three created expense groups')
def step_impl(context):
    listed = context.listed
    created = context.created

    for item_created in created:
        found = False

        for item_listed in listed[0]['items']:

            if item_created['id'] == item_listed['id'] and item_created['name'] == item_listed['name']:
                found = True

        if not found:
            assert False

    assert True


@then('the system deletes the expense group')
def step_impl(context):
    assert context.last['code'] == 200


@then('the system renames the expense group name to "{name}"')
def step_impl(context, name):
    code = context.last['code']
    renamed = context.last['name']

    assert code == 200
    assert renamed == name
