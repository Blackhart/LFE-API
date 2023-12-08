class BankAccountType:
    """ Bank account types
    
    There are three different bank account types:
        - Classic Account: used for managing everyday budgets and known by various names such as current account, checking account, or deposit account.
        - Savings Account: an interest-bearing account. This category includes:
            - Savings account (e.g., Livret A, Livret Jeune, Livret de développement durable et solidaire – LDDS, Livret d’épargne populaire – LEP, etc.)
            - Industrial development account (Codevi)
            - Home savings plan (PEL) and home savings account (CEL)
            - Retirement savings plan (PERP) and collective retirement savings plan (Perco).
        - Investment Account: a securities account for investment products in the stock market (purchase of mutual funds, stocks, bonds, etc.) and the equity savings plan (PEA).
    """
    STANDARD = 'STANDARD'
    SAVING = 'SAVING'
    TRADING = 'TRADING'