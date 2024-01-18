from api.data.bank_account_type import BankAccountType


################
# BANK ACCOUNT #
################

SUPPORTED_BANK_ACCOUNT_TYPE = [
    BankAccountType.STANDARD,
    BankAccountType.SAVING,
    BankAccountType.TRADING
]


###############
# USER ERRORS #
###############

USER_ERR_1 = 'Name should not be blank.'
USER_ERR_2 = 'Bank account type {Type} is not supported. Should be one of {AvailableType}.'
USER_ERR_3 = 'ID {id} not found.'
USER_ERR_4 = 'Budget group ID {id} not found.'
USER_ERR_5 = 'Budget ID {id} not found.'
