from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.core.exceptions import IDNotFound
from api.models.dal.budget import list_budgets
from api.models.dal.budget import create_budget
from api.models.dal.budget import delete_budget
from api.models.dal.budget import rename_budget
from api.models.dal.budget import get_budget
from api.models.dal.budget import is_budget_exists
from api.models.dal.budget import list_bank_accounts_by_budget
from api.models.dal.budget import list_budget_groups_by_budget
from api.models.dal.budget import list_transactions_by_budget
from api.serializers.budget import InBudgetSerializer
from api.serializers.budget import OutBudgetSerializer
from api.serializers.bank_account import OutBankAccountSerializer
from api.serializers.budget_group import OutBudgetGroupSerializer
from api.serializers.transaction import OutTransactionsByBudgetSerializer

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
        request=InBudgetSerializer,
        responses={
            status.HTTP_201_CREATED: OutBudgetSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a budget"
    )
    def post(self, request):
        """ Create a budget
        """
        serializer = InBudgetSerializer(data=request.data)

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
        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        delete_budget(id)

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
        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        budget = get_budget(id)

        return Response(OutBudgetSerializer(budget).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budgets"
)
class BudgetNameUpdate(APIView):
    """
    Update a budget.
    """

    @extend_schema(
        request=InBudgetSerializer,
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
        serializer = InBudgetSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        budget = rename_budget(id, serializer.validated_data['name'])

        return Response(OutBudgetSerializer(budget).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budgets"
)
class BankAccountsByBudget(APIView):
    """
    List all bank accounts linked to a budget.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBankAccountSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get all bank accounts linked to a budget"
    )
    def get(self, request, id):
        """ Get all bank accounts linked to a budget
        """
        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        bank_accounts = list_bank_accounts_by_budget(id)

        serializer = OutBankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        budget_groups = list_budget_groups_by_budget(id)

        serializer = OutBudgetGroupSerializer(budget_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budgets"
)
class TransactionsByBudget(APIView):
    """
    List all transactions linked to a budget.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutTransactionsByBudgetSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get all transactions linked to a budget"
    )
    def get(self, request, id):
        """ Get all transactions linked to a budget
        """
        if not is_budget_exists(id):
            raise IDNotFound(id=id)

        transactions = list_transactions_by_budget(id)

        serializer = OutTransactionsByBudgetSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)