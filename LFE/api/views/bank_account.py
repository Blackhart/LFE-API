from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.core.date import get_current_date
from api.models.dal.bank_account import list_bank_accounts
from api.models.dal.bank_account import create_bank_account
from api.models.dal.bank_account import delete_bank_account
from api.models.dal.bank_account import rename_bank_account
from api.models.dal.bank_account import get_bank_account
from api.models.dal.bank_account import get_bank_account_balance
from api.models.dal.bank_account import list_transactions_by_bank_account
from api.models.dal.transaction import record_transaction
from api.serializers.bank_account import InCreateBankAccountSerializer
from api.serializers.bank_account import InRenameBankAccountSerializer
from api.serializers.bank_account import InDeleteBankAccountSerializer
from api.serializers.bank_account import InGetBankAccountSerializer
from api.serializers.bank_account import InListTransactionsByBankAccountSerializer
from api.serializers.bank_account import OutBankAccountSerializer
from api.serializers.transaction import OutTransactionSerializer


@extend_schema(
    summary="Operations on bank accounts"
)
class BankAccountList(APIView):
    """
    List all bank accounts, or create a new bank account.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBankAccountSerializer
        },
        summary="Get all bank accounts"
    )
    def get(self, request):
        """ Get all bank accounts
        """
        bank_accounts = list_bank_accounts()
        
        for bank_account in bank_accounts:
            bank_account.balance = get_bank_account_balance(bank_account.id)

        serializer = OutBankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InCreateBankAccountSerializer,
        responses={
            status.HTTP_201_CREATED: OutBankAccountSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a bank account"
    )
    def post(self, request):
        """ Create a bank account
        """
        serializer = InCreateBankAccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bank_account = create_bank_account(
            serializer.validated_data['name'],
            serializer.validated_data['type'])
        
        if serializer.validated_data['balance'] > 0:
            record_transaction(
                date=get_current_date(), 
                label="Initial deposit", 
                amount=serializer.validated_data['balance'], 
                bank_account=bank_account
            )
        
        bank_account.balance = serializer.validated_data['balance']

        return Response(OutBankAccountSerializer(bank_account).data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Operations on bank accounts"
)
class BankAccountUpdate(APIView):
    """
    Update a bank account.
    """

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Delete a bank account"
    )
    def delete(self, request, id):
        """ Delete a bank account
        """
        serializer = InDeleteBankAccountSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        delete_bank_account(serializer.validated_data['id'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutBankAccountSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get a bank account"
    )
    def get(self, request, id):
        """ Get a bank account
        """
        serializer = InGetBankAccountSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)

        bank_account = get_bank_account(serializer.validated_data['id'])
        
        bank_account.balance = get_bank_account_balance(bank_account.id)

        return Response(OutBankAccountSerializer(bank_account).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on bank accounts"
)
class BankAccountNameUpdate(APIView):
    """
    Update a bank account.
    """

    @extend_schema(
        request=InRenameBankAccountSerializer,
        responses={
            status.HTTP_200_OK: OutBankAccountSerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Rename a bank account"
    )
    def put(self, request, id):
        """ Rename a bank account
        """
        serializer = InRenameBankAccountSerializer(data={**request.data, 'id': id})

        serializer.is_valid(raise_exception=True)

        bank_account = rename_bank_account(
            serializer.validated_data['id'], 
            serializer.validated_data['name']
        )
        
        bank_account.balance = get_bank_account_balance(bank_account.id)

        return Response(OutBankAccountSerializer(bank_account).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on bank accounts"
)
class TransactionsByBankAccount(APIView):
    """
    List all transactions by bank account.
    """

    @extend_schema(
        responses={
            status.HTTP_200_OK: OutTransactionSerializer,
            status.HTTP_404_NOT_FOUND: None
        },
        summary="Get all transactions by bank account"
    )
    def get(self, request, id):
        """ Get all transactions by bank account
        """
        serializer = InListTransactionsByBankAccountSerializer(data={'id': id})

        serializer.is_valid(raise_exception=True)
        
        transactions = list_transactions_by_bank_account(serializer.validated_data['id'])

        serializer = OutTransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
