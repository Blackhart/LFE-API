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

CREATE_EXPENSE_GROUP_ENTRY_POINT = 'expense-groups'
DELETE_EXPENSE_GROUP_ENTRY_POINT = 'expense-groups/{id}'
LIST_EXPENSE_GROUPS_ENTRY_POINT = 'expense-groups'
GET_EXPENSE_GROUP_ENTRY_POINT = 'expense-groups/{id}'
