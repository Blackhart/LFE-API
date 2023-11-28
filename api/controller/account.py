import uuid

from data.constant import SUPPORTED_BANK_ACCOUNT_TYPE, USER_ERR_1
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from model.db import accounts
from model.poco.account import Account


blp = Blueprint("Accounts",
                __name__,
                description="Operations on bank accounts")


class AccountsSchema(Schema):
    """ Schema for a bank account

    The schema is used for validating input data during a POST request to /account
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    balance = fields.Int(required=True)


@blp.route("/account")
class Accounts(MethodView):

    @blp.response(200, AccountsSchema(many=True))
    def get(self):
        """ Get all bank accounts
        """
        return accounts

    @blp.arguments(AccountsSchema)
    @blp.response(201, AccountsSchema)
    def post(cls, account_data):
        """ Create a bank account

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
        
        Args:
            account_data (dict): Account data
        """
        if account_data['type'] not in SUPPORTED_BANK_ACCOUNT_TYPE:
            abort(422, message=USER_ERR_1)

        account = Account(
            id=uuid.uuid4().hex,
            name=account_data['name'],
            type=account_data['type'],
            balance=account_data['balance']
        )

        accounts.append(account)

        return account
