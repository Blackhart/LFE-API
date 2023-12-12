from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.core.exceptions import IDNotFound
from api.model.dal.budget_category import list_budget_categories
from api.model.dal.budget_category import create_budget_category
from api.model.dal.budget_category import get_budget_category
from api.model.dal.budget_category import delete_budget_category
from api.model.dal.budget_category import rename_budget_category
from api.model.dal.budget_category import assign_budget_group
from api.model.dal.budget_group import is_budget_group_exists
from api.data.constant import USER_ERR_1, USER_ERR_4, USER_ERR_3


blp = Blueprint("Budget Categories",
                __name__,
                description="Operations on budget categories")


class BudgetCategorySchema(Schema):
    """ Schema for a budget category
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    budget_group_id = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)

    @validates('budget_group_id')
    def validate_budget_group_id(self, budget_group_id):
        if not is_budget_group_exists(budget_group_id):
            raise ValidationError(USER_ERR_4)


@blp.route("/budget-categories")
class BudgetCategories(MethodView):

    @blp.response(200, BudgetCategorySchema(many=True))
    def get(self):
        """ Get all budget categories
        """
        return list_budget_categories()

    @blp.arguments(BudgetCategorySchema, as_kwargs=True)
    @blp.response(201, BudgetCategorySchema)
    def post(self, name, budget_group_id):
        """ Create a budget category

        -----

        Args:
            name (str): Name of the category
            budget_group_id (str): Budget group ID to link to
        """
        return create_budget_category(name, budget_group_id)


@blp.route("/budget-categories/<id>")
class BudgetCategoriesByUid(MethodView):

    @blp.response(200, BudgetCategorySchema)
    def get(self, id):
        """ Get a budget category

        -----

        Args:
            id (str): category uid to get
        """
        try:
            return get_budget_category(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)

    @blp.response(200)
    def delete(self, id):
        """ Delete a budget category

        -----

        Args:
            id (str): Budget category uid to delete
        """
        try:
            delete_budget_category(id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budget-categories/<id>/name")
class BudgetCategoriesName(MethodView):

    @blp.arguments(BudgetCategorySchema(only=['name']), as_kwargs=True)
    @blp.response(200, BudgetCategorySchema)
    def patch(self, name, id):
        """ Update the name of a budget category

        -----

        Args:
            name (str): New name of the budget category
            id (str): Budget category uid to update
        """
        try:
            return rename_budget_category(id, name)
        except IDNotFound:
            abort(404, message=USER_ERR_3)


@blp.route("/budget-categories/<id>/budget-group-id")
class BudgetCategoriesName(MethodView):

    @blp.arguments(BudgetCategorySchema(only=['budget_group_id']), as_kwargs=True)
    @blp.response(200, BudgetCategorySchema)
    def patch(self, budget_group_id, id):
        """ Update the group of a budget category

        -----

        Args:
            budget_group_id (str): New group to assign
            id (str): Budget category uid to update
        """
        try:
            return assign_budget_group(id, budget_group_id)
        except IDNotFound:
            abort(404, message=USER_ERR_3)
