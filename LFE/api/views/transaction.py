from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.core.exceptions import IDNotFound
from api.models.dal.transaction import record_transaction
from api.models.dal.transaction import delete_transaction
from api.models.dal.transaction import get_transaction
from api.models.dal.transaction import update_transaction
from api.models.dal.transaction import is_transaction_exists
from api.serializers.transaction import InTransactionSerializer
from api.serializers.transaction import OutTransactionSerializer


@extend_schema(
    summary="Operations on transactions"
)
class TransactionList(APIView):
    """
    List all transactions, or record a new transaction.
    """

    @extend_schema(
        request=InTransactionSerializer,
        responses={
            status.HTTP_201_CREATED: OutTransactionSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Record a transaction"
    )
    def post(self, request):
        """ Record a transaction
        """
        serializer = InTransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        transaction = record_transaction(
            serializer.validated_data['date'],
            serializer.validated_data['label'],
            serializer.validated_data['amount'],
            serializer.validated_data['bank_account']
        )

        return Response(OutTransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Operations on transactions"
)
class TransactionUpdate(APIView):
    """
    Update a transaction.
    """

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Delete a transaction"
    )
    def delete(self, request, id):
        """ Delete a transaction
        """
        if not is_transaction_exists(id):
            raise IDNotFound(id=id)

        delete_transaction(id)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutTransactionSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get a transaction"
    )
    def get(self, request, id):
        """ Get a transaction
        """
        if not is_transaction_exists(id):
            raise IDNotFound(id=id)

        transaction = get_transaction(id)

        return Response(OutTransactionSerializer(transaction).data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InTransactionSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Update a transaction"
    )
    def put(self, request, id):
        """ Update a transaction
        """
        if not is_transaction_exists(id):
            raise IDNotFound(id=id)

        serializer = InTransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        update_transaction(
            id,
            serializer.validated_data['date'],
            serializer.validated_data['label'],
            serializer.validated_data['amount'],
            serializer.validated_data['bank_account']
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
