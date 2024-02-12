from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from api.models.dal.report import get_net_worth_report
from api.serializers.net_worth_report import outNetWorthReportSerializer
from api.serializers.transaction import InReportTransactionSerializer


@extend_schema(
    summary="Operations on reports"
)
class NetWorthReport(APIView):
    """
    Get net worth report.
    """

    @extend_schema(
        parameters=[InReportTransactionSerializer],
        responses={
            status.HTTP_200_OK: outNetWorthReportSerializer,
            status.HTTP_400_BAD_REQUEST: None
        },
        summary="Get net worth report"
    )
    def get(self, request):
            """
            Retrieves the net worth report based on the provided query parameters.

            Args:
                request (HttpRequest): The HTTP request object.

            Returns:
                Response: The serialized net worth report data.

            Raises:
                ValidationError: If the provided query parameters are invalid.
            """
            serializer = InReportTransactionSerializer(data=request.query_params)

            serializer.is_valid(raise_exception=True)

            daily, monthly, yearly = get_net_worth_report(
                serializer.validated_data.get('bank_accounts', []),
                serializer.validated_data.get('start_date', None),
                serializer.validated_data.get('end_date', None)
            )

            serializer = outNetWorthReportSerializer({
                'daily': dict(zip(daily.index.astype(str), daily.values)),
                'monthly': dict(zip(monthly.index.astype(str), monthly.values)),
                'yearly': dict(zip(yearly.index.astype(str), yearly.values))
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
