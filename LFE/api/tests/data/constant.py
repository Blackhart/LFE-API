##############
# SERVER URL #
##############

STAGGING_BASE_URL = 'http://127.0.0.1:3000'


################
# ENTRY POINTS #
################

CREATE_BUDGET_ENTRY_POINT = 'budgets'
DELETE_BUDGET_ENTRY_POINT = 'budgets/{id}'
RENAME_BUDGET_ENTRY_POINT = 'budgets/{id}/name'
LIST_BUDGETS_ENTRY_POINT = 'budgets'
GET_BUDGET_ENTRY_POINT = 'budgets/{id}'
GET_BUDGET_GROUPS_BY_BUDGET_ENTRY_POINT = 'budgets/{id}/budget-groups'

CREATE_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts'
DELETE_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}'
RENAME_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}/name'
LIST_BANK_ACCOUNTS_ENTRY_POINT = 'bank-accounts'
GET_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}'
GET_TRANSACTIONS_BY_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}/transactions'

CREATE_BUDGET_GROUP_ENTRY_POINT = 'budget-groups'
DELETE_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}'
RENAME_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}/name'
LIST_BUDGET_GROUPS_ENTRY_POINT = 'budget-groups'
GET_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}'
GET_ASSIGNED_CATEGORIES_ENTRY_POINT = 'budget-groups/{id}/budget-categories'

CREATE_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories'
DELETE_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}'
RENAME_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}/name'
LIST_BUDGET_CATEGORIES_ENTRY_POINT = 'budget-categories'
GET_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}'
ASSIGN_BUDGET_GROUP_ENTRY_POINT = 'budget-categories/{id}/budget-group-id'

RECORD_TRANSACTION_ENTRY_POINT = 'transactions'
DELETE_TRANSACTION_ENTRY_POINT = 'transactions/{id}'
GET_TRANSACTION_ENTRY_POINT = 'transactions/{id}'
UPDATE_TRANSACTION_ENTRY_POINT = 'transactions/{id}'

GET_NET_WORTH_REPORT = 'reports/net-worth'