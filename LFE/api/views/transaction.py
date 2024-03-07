from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.models.dal.transaction import record_transaction
from api.models.dal.transaction import delete_transaction
from api.models.dal.transaction import get_transaction
from api.models.dal.transaction import update_transaction
from api.models.dal.bank_account import get_bank_account
from api.serializers.transaction import InCreateTransactionSerializer
from api.serializers.transaction import InDeleteTransactionSerializer
from api.serializers.transaction import InGetTransactionSerializer
from api.serializers.transaction import InUpdateTransactionSerializer
from api.serializers.transaction import OutTransactionSerializer


@extend_schema(
    summary="Operations on transactions"
)
class TransactionList(APIView):
    """
    List all transactions, or record a new transaction.
    """

    @extend_schema(
        request=InCreateTransactionSerializer,
        responses={
            status.HTTP_201_CREATED: OutTransactionSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Record a transaction"
    )
    def post(self, request):
        """ Record a transaction
        """
        serializer = InCreateTransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bank_account = get_bank_account(
            serializer.validated_data['bank_account_id']
        )

        transaction = record_transaction(
            serializer.validated_data['date'],
            serializer.validated_data['label'],
            serializer.validated_data['amount'],
            bank_account
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
        serializer = InDeleteTransactionSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        delete_transaction(serializer.validated_data['id'])

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
        serializer = InGetTransactionSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        transaction = get_transaction(serializer.validated_data['id'])

        return Response(OutTransactionSerializer(transaction).data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InCreateTransactionSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Update a transaction"
    )
    def put(self, request, id):
        """ Update a transaction
        """
        serializer = InUpdateTransactionSerializer(
            data={**request.data, 'id': id})

        serializer.is_valid(raise_exception=True)

        bank_account = get_bank_account(
            serializer.validated_data['bank_account_id']
        )

        update_transaction(
            id,
            serializer.validated_data['date'],
            serializer.validated_data['label'],
            serializer.validated_data['amount'],
            bank_account
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
