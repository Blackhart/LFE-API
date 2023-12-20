from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.controller.budget_category import BudgetCategorySchema
from api.core.exceptions import IDNotFound
from api.model.dal.budget import is_budget_exists
from api.model.dal.budget_group import list_budget_groups
from api.model.dal.budget_group import create_budget_group
from api.model.dal.budget_group import get_budget_group
from api.model.dal.budget_group import delete_budget_group
from api.model.dal.budget_group import rename_budget_group
from api.model.dal.budget_group import get_linked_categories
from api.data.constant import USER_ERR_1, USER_ERR_3, USER_ERR_5


blp = Blueprint("Budget Groups",
                __name__,
                description="Operations on budget groups")


class BudgetGroupSchema(Schema):
    """ Schema for a budget group
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    budget_id = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)

    @validates('budget_id')
    def validate_budget_id(self, budget_id):
        if not is_budget_exists(budget_id):
            raise ValidationError(USER_ERR_5)


@blp.route("/budget-groups")
class BudgetGroups(MethodView):

    @blp.response(200, BudgetGroupSchema(many=True))
    def get(self):
        """ Get all budget groups
        """
        return list_budget_groups()

    @blp.arguments(BudgetGroupSchema, as_kwargs=True)
    @blp.response(201, BudgetGroupSchema)
    def post(self, name, budget_id):
        """ Create a budget group

        -----

        Args:
            name (str): Name of the group
        """
        return create_budget_group(name, budget_id)


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


@blp.route("/budget-groups/<id>/categories")
class CategoriesByBudgetGroup(MethodView):

    @blp.response(200, BudgetCategorySchema(many=True))
    def get(self, id):
        """ Return all the assigned categories

        -----

        Args:
            id (str): Budget group uid
        """
        try:
            return get_linked_categories(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)
