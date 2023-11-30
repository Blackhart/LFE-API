import uuid

from data.constant import SUPPORTED_BANK_ACCOUNT_TYPE, USER_ERR_1, USER_ERR_2, USER_ERR_3
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError
from model.db import accounts
from model.poco.account import Account


blp = Blueprint("Accounts",
                __name__,
                description="Operations on bank accounts")


class AccountSchema(Schema):
    """ Schema for a bank account
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    balance = fields.Float(required=True)
    
    @validates('name')
    def validate_name(self, name):
        if not name:
            raise ValidationError(USER_ERR_2)
    
    @validates('type')
    def validate_type(self, type):
        if type not in SUPPORTED_BANK_ACCOUNT_TYPE:
            raise ValidationError(USER_ERR_1)


@blp.route("/accounts")
class Accounts(MethodView):

    @blp.response(200, AccountSchema(many=True))
    def get(self):
        """ Get all bank accounts
        """
        return accounts

    @blp.arguments(AccountSchema, as_kwargs=True)
    @blp.response(201, AccountSchema(only=["id"]))
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
            account_data (dict): Account data
        """
        account = Account(
            id=uuid.uuid4().hex,
            name=name,
            type=type,
            balance=balance
        )

        accounts.append(account)

        return account


@blp.route("/accounts/<account_uid>")
class AccountsByUid(MethodView):
    
    @blp.arguments(AccountSchema(only=['name']), as_kwargs=True)
    @blp.response(200, AccountSchema)
    def patch(self, name, account_uid):
        """ Update the name of a bank account

        -----

        Args:
            name (str): New name of the bank account
            account_uid (str): Account uid to update
        """
        idx = [idx for idx, account in enumerate(accounts) if account.id == account_uid]
        
        if not idx:
            abort(404, message=USER_ERR_3)
            
        idx_to_update = next(iter(idx))
            
        accounts[idx_to_update].name = name
        
        return accounts[idx_to_update]
    
    
    @blp.response(200)
    def delete(self, account_uid):
        """ Delete a bank account

        -----

        Args:
            account_uid (str): Account uid to delete
        """
        idx = [idx for idx, account in enumerate(accounts) if account.id == account_uid]
        
        if not idx:
            abort(404, message=USER_ERR_3)
        
        idx_to_remove = next(iter(idx))
        
        accounts.pop(idx_to_remove)