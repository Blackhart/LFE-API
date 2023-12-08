from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.core.exceptions import IDNotFound
from api.model.dal.budget_group import list_budget_groups
from api.model.dal.budget_group import create_budget_group
from api.model.dal.budget_group import get_budget_group
from api.model.dal.budget_group import delete_budget_group
from api.model.dal.budget_group import rename_budget_group
from api.data.constant import USER_ERR_1, USER_ERR_3


blp = Blueprint("Budget Groups",
                __name__,
                description="Operations on budget groups")


class BudgetGroupSchema(Schema):
    """ Schema for a budget group
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)


@blp.route("/budget-groups")
class BudgetGroups(MethodView):

    @blp.response(200, BudgetGroupSchema(many=True))
    def get(self):
        """ Get all budget groups
        """
        return list_budget_groups()

    @blp.arguments(BudgetGroupSchema, as_kwargs=True)
    @blp.response(201, BudgetGroupSchema)
    def post(self, name):
        """ Create a budget group

        -----

        Args:
            name (str): Name of the group
        """
        return create_budget_group(name)


@blp.route("/budget-groups/<id>")
class BudgetGroupsByUid(MethodView):

    @blp.response(200, BudgetGroupSchema)
    def get(self, id):
        """ Get a budget group

        -----

        Args:
            id (str): group uid to get
        """
        try:
            return get_budget_group(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)

    @blp.response(200)
    def delete(self, id):
        """ Delete a budget group

        -----

        Args:
            id (str): Budget group uid to delete
        """
        try:
            delete_budget_group(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budget-groups/<id>/name")
class BudgetGroupsName(MethodView):

    @blp.arguments(BudgetGroupSchema(only=['name']), as_kwargs=True)
    @blp.response(200, BudgetGroupSchema)
    def patch(self, name, id):
        """ Update the name of a budget group

        -----

        Args:
            name (str): New name of the budget group
            id (str): Budget group uid to update
        """
        try:
            return rename_budget_group(id, name)
        except IDNotFound:
            abort(404, message=USER_ERR_3)
