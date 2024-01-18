from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.core.exceptions import IDNotFound
from api.models.dal.bank_account import list_bank_accounts
from api.models.dal.bank_account import create_bank_account
from api.models.dal.bank_account import delete_bank_account
from api.models.dal.bank_account import rename_bank_account
from api.models.dal.bank_account import get_bank_account
from api.models.dal.bank_account import is_bank_account_exists
from api.serializers.bank_account import InBankAccountSerializer
from api.serializers.bank_account import InBankAccountNameUpdateSerializer
from api.serializers.bank_account import OutBankAccountSerializer


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

        serializer = OutBankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=InBankAccountSerializer,
        responses={
            status.HTTP_201_CREATED: OutBankAccountSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Create a bank account"
    )
    def post(self, request):
        """ Create a bank account
        """
        serializer = InBankAccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        bank_account = create_bank_account(
            serializer.validated_data['name'], 
            serializer.validated_data['type'], 
            serializer.validated_data['balance'], 
            serializer.validated_data['budget_id'])

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
        if not is_bank_account_exists(id):
            raise IDNotFound(id=id)

        delete_bank_account(id)

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
        if not is_bank_account_exists(id):
            raise IDNotFound(id=id)

        bank_account = get_bank_account(id)

        return Response(OutBankAccountSerializer(bank_account).data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Operations on bank accounts"
)
class BankAccountNameUpdate(APIView):
    """
    Update a bank account.
    """

    @extend_schema(
        request=InBankAccountNameUpdateSerializer,
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
        serializer = InBankAccountNameUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        if not is_bank_account_exists(id):
            raise IDNotFound(id=id)

        bank_account = rename_bank_account(
            id, serializer.validated_data['name'])

        return Response(OutBankAccountSerializer(bank_account).data, status=status.HTTP_200_OK)
