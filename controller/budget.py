from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.controller.bank_account import BankAccountSchema
from api.controller.budget_group import BudgetGroupSchema
from api.core.exceptions import IDNotFound
from api.model.dal.budget import list_budgets
from api.model.dal.budget import create_budget
from api.model.dal.budget import get_budget
from api.model.dal.budget import delete_budget
from api.model.dal.budget import rename_budget
from api.model.dal.budget import get_linked_bank_accounts
from api.model.dal.budget import get_linked_budget_groups
from api.data.constant import USER_ERR_1, USER_ERR_3


blp = Blueprint("Budgets",
                __name__,
                description="Operations on budgets")


class BudgetSchema(Schema):
    """ Schema for a budget
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)


@blp.route("/budgets")
class Budgets(MethodView):

    @blp.response(200, BudgetSchema(many=True))
    def get(self):
        """ Get all budgets
        """
        return list_budgets()

    @blp.arguments(BudgetSchema, as_kwargs=True)
    @blp.response(201, BudgetSchema)
    def post(self, name):
        """ Create a budget

        -----

        Args:
            name (str): Name of the budget
        """
        return create_budget(name)


@blp.route("/budgets/<id>")
class BudgetsByUid(MethodView):

    @blp.response(200, BudgetSchema)
    def get(self, id):
        """ Get a budget

        -----

        Args:
            id (str): Budget uid to get
        """
        try:
            return get_budget(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)

    @blp.response(200)
    def delete(self, id):
        """ Delete a budget

        -----

        Args:
            id (str): Budget uid to delete
        """
        try:
            delete_budget(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budgets/<id>/name")
class BudgetsName(MethodView):

    @blp.arguments(BudgetSchema(only=['name']), as_kwargs=True)
    @blp.response(200, BudgetSchema)
    def patch(self, name, id):
        """ Update the name of a budget

        -----

        Args:
            name (str): New name of the budget
            id (str): Budget uid to update
        """
        try:
            return rename_budget(id, name)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budgets/<id>/bank-accounts")
class BankAccountsByBudget(MethodView):

    @blp.response(200, BankAccountSchema(many=True))
    def get(self, id):
        """ Return all linked bank accounts

        -----

        Args:
            id (str): Budget uid
        """
        try:
            return get_linked_bank_accounts(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budgets/<id>/budget-groups")
class BudgetGroupsByBudget(MethodView):

    @blp.response(200, BudgetGroupSchema(many=True))
    def get(self, id):
        """ Return all linked budget groups

        -----

        Args:
            id (str): Budget uid
        """
        try:
            return get_linked_budget_groups(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)
