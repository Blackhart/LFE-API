from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.models.dal.budget_category import list_budget_categories
from api.models.dal.budget_category import create_budget_category
from api.models.dal.budget_category import delete_budget_category
from api.models.dal.budget_category import rename_budget_category
from api.models.dal.budget_category import assign_budget_group
from api.models.dal.budget_category import get_budget_category
from api.models.dal.budget_group import get_budget_group
from api.serializers.budget_category import InCreateBudgetCategorySerializer
from api.serializers.budget_category import InRenameBudgetCategorySerializer
from api.serializers.budget_category import InAssignGroupToBudgetCategorySerializer
from api.serializers.budget_category import InDeleteBudgetCategorySerializer
from api.serializers.budget_category import InGetBudgetCategorySerializer
from api.serializers.budget_category import OutBudgetCategorySerializer


@extend_schema(
    summary="Operations on budget categories"
)
class BudgetCategoryList(APIView):
    """
    List all budget categories, or create a new budget category.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetCategorySerializer
        },
        summary="Get all budget categories"
    )
    def get(self, request):
        """ Get all budget categories
        """
        budget_categories = list_budget_categories()

        serializer = OutBudgetCategorySerializer(budget_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InCreateBudgetCategorySerializer,
        responses={
            status.HTTP_201_CREATED: OutBudgetCategorySerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a budget category"
    )
    def post(self, request):
        """ Create a budget category
        """
        serializer = InCreateBudgetCategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        budget_group = get_budget_group(
            serializer.validated_data['budget_group_id']
        )

        budget_category = create_budget_category(
            serializer.validated_data['name'],
            budget_group)

        return Response(OutBudgetCategorySerializer(budget_category).data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Operations on budget categories"
)
class BudgetCategoryUpdate(APIView):
    """
    Update a budget category.
    """

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Delete a budget category"
    )
    def delete(self, request, id):
        """ Delete a budget category
        """
        serializer = InDeleteBudgetCategorySerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        delete_budget_category(serializer.validated_data['id'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetCategorySerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get a budget category"
    )
    def get(self, request, id):
        """ Get a budget category
        """
        serializer = InGetBudgetCategorySerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        budget_category = get_budget_category(serializer.validated_data['id'])

        return Response(OutBudgetCategorySerializer(budget_category).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budget categories"
)
class BudgetCategoryNameUpdate(APIView):
    """
    Update a budget category.
    """

    @extend_schema(
        request=InRenameBudgetCategorySerializer,
        responses={
            status.HTTP_200_OK: OutBudgetCategorySerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Rename a budget category"
    )
    def put(self, request, id):
        """ Rename a budget category
        """
        serializer = InRenameBudgetCategorySerializer(data={**request.data, 'id': id})

        serializer.is_valid(raise_exception=True)

        budget_category = rename_budget_category(
            serializer.validated_data['id'], 
            serializer.validated_data['name']
        )

        return Response(OutBudgetCategorySerializer(budget_category).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budget categories"
)
class BudgetCategoryGroupIdUpdate(APIView):
    """
    Update a budget category.
    """

    @extend_schema(
        request=InAssignGroupToBudgetCategorySerializer,
        responses={
            status.HTTP_200_OK: OutBudgetCategorySerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Overwrite a budget category's budget group ID"
    )
    def put(self, request, id):
        """ Overwrite a budget category's budget group ID
        """
        serializer = InAssignGroupToBudgetCategorySerializer(data={**request.data, 'id': id})

        serializer.is_valid(raise_exception=True)

        budget_category = assign_budget_group(
            serializer.validated_data['id'], 
            serializer.validated_data['budget_group_id']
        )

        return Response(OutBudgetCategorySerializer(budget_category).data, status=status.HTTP_200_OK)
