from model.poco.account_type import AccountType

################
# BANK ACCOUNT #
################

SUPPORTED_BANK_ACCOUNT_TYPE = [ AccountType.STANDARD_ACCOUNT ]


###############
# USER ERRORS #
###############

USER_ERR_1 = 'Bank account type is not supported. Should be one of {}'.format(SUPPORTED_BANK_ACCOUNT_TYPE)