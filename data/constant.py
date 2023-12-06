from api.model.poco.bank_account_type import BankAccountType


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

USER_ERR_1 = 'Name should not be empty.'
USER_ERR_2 = 'Bank account type is not supported. Should be one of {Type}.'.format(Type=SUPPORTED_BANK_ACCOUNT_TYPE)
USER_ERR_3 = 'ID not found.'