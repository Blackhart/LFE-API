from model.poco.account_type import AccountType

################
# BANK ACCOUNT #
################

SUPPORTED_BANK_ACCOUNT_TYPE = [
    AccountType.STANDARD_ACCOUNT,
    AccountType.SAVING_ACCOUT,
    AccountType.TRADING_ACCOUNT
]


###############
# USER ERRORS #
###############

USER_ERR_1 = 'Bank account type is not supported. Should be one of {}'.format(
    SUPPORTED_BANK_ACCOUNT_TYPE)
USER_ERR_2 = 'Name should not be empty'
USER_ERR_3 = 'Bank account not found'