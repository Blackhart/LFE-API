##############
# SERVER URL #
##############

STAGGING_BASE_URL = 'http://127.0.0.1:5000'


################
# ENTRY POINTS #
################

CREATE_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts'
DELETE_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}'
RENAME_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}/name'
LIST_BANK_ACCOUNTS_ENTRY_POINT = 'bank-accounts'
GET_BANK_ACCOUNT_ENTRY_POINT = 'bank-accounts/{id}'

CREATE_BUDGET_GROUP_ENTRY_POINT = 'budget-groups'
DELETE_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}'
RENAME_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}/name'
LIST_BUDGET_GROUPS_ENTRY_POINT = 'budget-groups'
GET_BUDGET_GROUP_ENTRY_POINT = 'budget-groups/{id}'

CREATE_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories'
DELETE_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}'
RENAME_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}/name'
LIST_BUDGET_CATEGORIES_ENTRY_POINT = 'budget-categories'
GET_BUDGET_CATEGORY_ENTRY_POINT = 'budget-categories/{id}'