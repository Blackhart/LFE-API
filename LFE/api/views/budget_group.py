from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.core.exceptions import IDNotFound
from api.models.dal.budget_group import list_budget_groups
from api.models.dal.budget_group import create_budget_group
from api.models.dal.budget_group import delete_budget_group
from api.models.dal.budget_group import rename_budget_group
from api.models.dal.budget_group import get_budget_group
from api.models.dal.budget_group import is_budget_group_exists
from api.models.dal.budget_group import list_budget_categories_by_budget_group
from api.serializers.budget_group import InBudgetGroupSerializer
from api.serializers.budget_group import InBudgetGroupNameUpdateSerializer
from api.serializers.budget_group import OutBudgetGroupSerializer
from api.serializers.budget_category import OutBudgetCategorySerializer


@extend_schema(
    summary="Operations on budget groups"
)
class BudgetGroupList(APIView):
    """
    List all budget groups, or create a new budget group.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetGroupSerializer
        },
        summary="Get all budget groups"
    )
    def get(self, request):
        """ Get all budget groups
        """
        budget_groups = list_budget_groups()

        serializer = OutBudgetGroupSerializer(budget_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InBudgetGroupSerializer,
        responses={
            status.HTTP_201_CREATED: OutBudgetGroupSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a budget group"
    )
    def post(self, request):
        """ Create a budget group
        """
        serializer = InBudgetGroupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        budget_group = create_budget_group(
            serializer.validated_data['name'],
            serializer.validated_data['budget'])

        return Response(OutBudgetGroupSerializer(budget_group).data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Operations on budget groups"
)
class BudgetGroupUpdate(APIView):
    """
    Update a budget group.
    """

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Delete a budget group"
    )
    def delete(self, request, id):
        """ Delete a budget group
        """
        if not is_budget_group_exists(id):
            raise IDNotFound(id=id)

        delete_budget_group(id)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetGroupSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get a budget group"
    )
    def get(self, request, id):
        """ Get a budget group
        """
        if not is_budget_group_exists(id):
            raise IDNotFound(id=id)

        budget_group = get_budget_group(id)

        return Response(OutBudgetGroupSerializer(budget_group).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budget groups"
)
class BudgetGroupNameUpdate(APIView):
    """
    Update a budget group.
    """

    @extend_schema(
        request=InBudgetGroupNameUpdateSerializer,
        responses={
            status.HTTP_200_OK: OutBudgetGroupSerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Rename a budget group"
    )
    def put(self, request, id):
        """ Rename a budget group
        """
        serializer = InBudgetGroupNameUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        if not is_budget_group_exists(id):
            raise IDNotFound(id=id)

        budget_group = rename_budget_group(
            id, serializer.validated_data['name'])

        return Response(OutBudgetGroupSerializer(budget_group).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on budget groups"
)
class BudgetCategoriesByBudgetGroup(APIView):
    """
    List all budget categories linked to a budget group.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBudgetCategorySerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get all budget categories linked to a budget group"
    )
    def get(self, request, id):
        """ Get all budget categories linked to a budget group
        """
        if not is_budget_group_exists(id):
            raise IDNotFound(id=id)

        budget_categories = list_budget_categories_by_budget_group(id)

        serializer = OutBudgetCategorySerializer(budget_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
