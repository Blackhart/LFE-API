import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, validates, ValidationError

from api.model.db import expense_groups
from api.model.poco.expense_group import ExpenseGroup
from api.data.constant import USER_ERR_1, USER_ERR_3


blp = Blueprint("Expense Groups",
                __name__,
                description="Operations on expense groups")


class ExpenseGroupSchema(Schema):
    """ Schema for an expense group
    """
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if not name or not name.strip():
            raise ValidationError(USER_ERR_1)


@blp.route("/expense-groups")
class ExpenseGroups(MethodView):

    @blp.arguments(ExpenseGroupSchema, as_kwargs=True)
    @blp.response(201, ExpenseGroupSchema(only=["id"]))
    def post(self, name):
        """ Create an expense group

        An expense group has 1 attribute:
            1. A name

        Attributes:

        1. Group Name

        The group name is defined by the user. It allows the user to easily identify the group.

        -----

        Args:
            name (str): Name of the group
        """
        group = ExpenseGroup(
            id=uuid.uuid4().hex,
            name=name
        )

        expense_groups.append(group)

        return group


@blp.route("/expense-groups/<id>")
class ExpenseGroupsByUid(MethodView):

    @blp.response(200, ExpenseGroupSchema)
    def get(self, id):
        """ Get an expense group

        -----

        Args:
            id (str): group uid to get
        """
        idx = [
            idx
            for idx, group
            in enumerate(expense_groups)
            if group.id == id
        ]

        if not idx:
            abort(404, message=USER_ERR_3)

        idx_to_get = next(iter(idx))

        return expense_groups[idx_to_get]
