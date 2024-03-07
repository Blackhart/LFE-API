from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.models.dal.budget import list_budgets
from api.models.dal.budget import create_budget
from api.models.dal.budget import delete_budget
from api.models.dal.budget import rename_budget
from api.models.dal.budget import get_budget
from api.models.dal.budget import list_budget_groups_by_budget
from api.serializers.budget import InCreateBudgetSerializer
from api.serializers.budget import InDeleteBudgetSerializer
from api.serializers.budget import InGetBudgetSerializer
from api.serializers.budget import InListBudgetGroupsByBudgetSerializer
from api.serializers.budget import InRenameBudgetSerializer
from api.serializers.budget import OutBudgetSerializer
from api.serializers.budget_group import OutBudgetGroupSerializer


@extend_schema(
    summary="Operations on budgets"
)
class BudgetList(APIView):
    """
    List all budgets, or create a new budget.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetSerializer
        },
        summary="Get all budgets"
    )
    def get(self, request):
        """ Get all budgets
        """
        budgets = list_budgets()

        serializer = OutBudgetSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InCreateBudgetSerializer,
        responses={
            status.HTTP_201_CREATED: OutBudgetSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a budget"
    )
    def post(self, request):
        """ Create a budget
        """
        serializer = InCreateBudgetSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        budget = create_budget(serializer.validated_data['name'])

        return Response(OutBudgetSerializer(budget).data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Operations on budgets"
)
class BudgetUpdate(APIView):
    """
    Update a budget.
    """

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Delete a budget"
    )
    def delete(self, request, id):
        """ Delete a budget
        """
        serializer = InDeleteBudgetSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        delete_budget(serializer.validated_data['id'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get a budget"
    )
    def get(self, request, id):
        """ Get a budget
        """
        serializer = InGetBudgetSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        budget = get_budget(serializer.validated_data['id'])

        return Response(OutBudgetSerializer(budget).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budgets"
)
class BudgetNameUpdate(APIView):
    """
    Update a budget.
    """

    @extend_schema(
        request=InCreateBudgetSerializer,
        responses={
            status.HTTP_200_OK: OutBudgetSerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Rename a budget"
    )
    def put(self, request, id):
        """ Rename a budget
        """
        serializer = InRenameBudgetSerializer(data={**request.data, 'id': id})

        serializer.is_valid(raise_exception=True)

        budget = rename_budget(
            serializer.validated_data['id'],
            serializer.validated_data['name']
        )

        return Response(OutBudgetSerializer(budget).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budgets"
)
class BudgetGroupsByBudget(APIView):
    """
    List all budget groups linked to a budget.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetGroupSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get all budget groups linked to a budget"
    )
    def get(self, request, id):
        """ Get all budget groups linked to a budget
        """
        serializer = InListBudgetGroupsByBudgetSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        budget_groups = list_budget_groups_by_budget(
            serializer.validated_data['id'])

        serializer = OutBudgetGroupSerializer(budget_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
