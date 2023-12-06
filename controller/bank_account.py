import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.model.db import bank_accounts
from api.model.poco.bank_account import BankAccount
from api.data.constant import SUPPORTED_BANK_ACCOUNT_TYPE
from api.data.constant import USER_ERR_2, USER_ERR_1, USER_ERR_3


blp = Blueprint("Bank Accounts",
                __name__,
                description="Operations on bank accounts")


class BankAccountSchema(Schema):
    """ Schema for a bank account
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    balance = fields.Float(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)

    @validates('type')
    def validate_type(self, type):
        if type not in SUPPORTED_BANK_ACCOUNT_TYPE:
            raise ValidationError(USER_ERR_2)


@blp.route("/bank-accounts")
class BankAccounts(MethodView):

    @blp.response(200, BankAccountSchema(many=True))
    def get(self):
        """ Get all bank accounts
        """
        return bank_accounts

    @blp.arguments(BankAccountSchema, as_kwargs=True)
    @blp.response(201, BankAccountSchema(only=["id"]))
    def post(self, name, type, balance):
        """ Create a bank account

        A bank account has 3 attributes:
            1. A name
            2. A type
            3. A balance

        Attributes:

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

        -----

        Args:
            name (str): Name of the bank account
            type (str): Type of the bank account
            balance (float): Starting balance of the bank account
        """
        account = BankAccount(
            id=uuid.uuid4().hex,
            name=name,
            type=type,
            balance=balance
        )

        bank_accounts.append(account)

        return account


@blp.route("/bank-accounts/<id>")
class BankAccountsByUid(MethodView):

    @blp.response(200, BankAccountSchema)
    def get(self, id):
        """ Get a bank account

        -----

        Args:
            id (str): Account uid to get
        """
        idx = [
            idx
            for idx, account
            in enumerate(bank_accounts)
            if account.id == id
        ]

        if not idx:
            abort(404, message=USER_ERR_3)

        idx_to_get = next(iter(idx))

        return bank_accounts[idx_to_get]

    @blp.response(200)
    def delete(self, id):
        """ Delete a bank account

        -----

        Args:
            id (str): Account uid to delete
        """
        idx = [
            idx
            for idx, account
            in enumerate(bank_accounts)
            if account.id == id
        ]

        if not idx:
            abort(404, message=USER_ERR_3)

        idx_to_remove = next(iter(idx))

        bank_accounts.pop(idx_to_remove)


@blp.route("/bank-accounts/<id>/name")
class BankAccountsName(MethodView):

    @blp.arguments(BankAccountSchema(only=['name']), as_kwargs=True)
    @blp.response(200, BankAccountSchema)
    def patch(self, name, id):
        """ Update the name of a bank account

        -----

        Args:
            name (str): New name of the bank account
            id (str): Account uid to update
        """
        idx = [
            idx
            for idx, account
            in enumerate(bank_accounts)
            if account.id == id
        ]

        if not idx:
            abort(404, message=USER_ERR_3)

        idx_to_update = next(iter(idx))

        bank_accounts[idx_to_update].name = name

        return bank_accounts[idx_to_update]
