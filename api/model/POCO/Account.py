from dataclasses import dataclass


@dataclass
class Account:
    """ An object representing a bank account
    
    A bank account has 3 attributes:
        1. A name
        2. A type
        3. A balance
    
    Attributes
    ----------
    
    1. Account Name
    
    The account name is defined by the user. It allows the user to easily identify this account.

    2. Account Type
    
    The account type is chosen by the user from the following 3 types:
        - Classic Account: used for managing everyday expenses and known by various names such as current account, checking account, or deposit account.
        - Savings Account: an interest-bearing account. This category includes:
            - Savings account (e.g., Livret A, Livret Jeune, Livret de développement durable et solidaire – LDDS, Livret d’épargne populaire – LEP, etc.)
            - Industrial development account (Codevi)
            - Home savings plan (PEL) and home savings account (CEL)
            - Retirement savings plan (PERP) and collective retirement savings plan (Perco).
            - Investment Account: a securities account for investment products in the stock market (purchase of mutual funds, stocks, bonds, etc.) and the equity savings plan (PEA).
    
    3. Account Balance
    
    The account balance in Euro. It is defined by the user at creation and automatically calculated afterward (based on banking transactions).
    """
    id: str
    name: str
    type: str
    balance: int
    
    def __init__(self, id: str, name: str, type: str, balance: int):
        self.id = id
        self.name = name
        self.type = type
        self.balance = balance