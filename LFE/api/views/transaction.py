from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.models.dal.transaction import record_transaction
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
            serializer.validated_data['bank_account_id']
        )

        return Response(OutTransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
