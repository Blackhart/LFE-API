from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.core.exceptions import IDNotFound
from api.model.dal.bank_account import create_bank_account
from api.model.dal.bank_account import delete_bank_account
from api.model.dal.bank_account import rename_bank_account
from api.model.dal.bank_account import get_bank_account
from api.model.dal.bank_account import list_bank_accounts
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
        return list_bank_accounts()

    @blp.arguments(BankAccountSchema, as_kwargs=True)
    @blp.response(201, BankAccountSchema)
    def post(self, name, type, balance):
        """ Create a bank account

        -----

        Args:
            name (str): Name of the bank account
            type (str): Type of the bank account
            balance (float): Starting balance of the bank account
        """
        return create_bank_account(name, type, balance)


@blp.route("/bank-accounts/<id>")
class BankAccountsByUid(MethodView):

    @blp.response(200, BankAccountSchema)
    def get(self, id):
        """ Get a bank account

        -----

        Args:
            id (str): Account uid to get
        """
        try:
            account = get_bank_account(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)

        return account

    @blp.response(200)
    def delete(self, id):
        """ Delete a bank account

        -----

        Args:
            id (str): Account uid to delete
        """
        try:
            delete_bank_account(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


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
        try:
            return rename_bank_account(id, name)
        except IDNotFound:
            abort(404, message=USER_ERR_3)
