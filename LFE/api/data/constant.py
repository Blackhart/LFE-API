from api.data.bank_account_type import BankAccountType


################
# BANK ACCOUNT #
################

SUPPORTED_BANK_ACCOUNT_TYPE = [
    BankAccountType.STANDARD,
    BankAccountType.SAVING,
    BankAccountType.TRADING
]

########
# DATE #
########

DATE_FORMAT = '%Y-%m-%d'


###############
# USER ERRORS #
###############

USER_ERR_1 = 'Name should not be blank.'
USER_ERR_2 = 'Bank account type {Type} is not supported. Should be one of {AvailableType}.'
USER_ERR_4 = 'Budget group ID {id} not found.'
USER_ERR_5 = 'Budget ID {id} not found.'
USER_ERR_6 = 'Bank account ID {id} not found.'
USER_ERR_7 = 'Invalid date format {date}. Date should be of the form AAAA-MM-DD.'
USER_ERR_8 = 'start_date {start_date} occurs after end_date {end_date}.'
USER_ERR_9 = 'Budget category ID {id} not found.'
USER_ERR_10 = 'Transaction ID {id} not found.'