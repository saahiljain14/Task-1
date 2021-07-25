from datetime import date

from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import FixedDeposit, Bullion
from .serializers import FDSerializer, BullionSerializer
# Create your views here.

GOLD_RATE = 4925
SILVER_RATE = 67

class FixedDepositViewSet(viewsets.ModelViewSet):
    '''CRUD operations for Fixed Deposit'''
    serializer_class = FDSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FixedDeposit.objects.filter(created_by = self.request.user)


class BullionViewSet(viewsets.ModelViewSet):
    '''CRUD operations for Bullion'''
    serializer_class = BullionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bullion.objects.filter(created_by = self.request.user)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def CurrentEvaluation(request):
    '''Get current evaluation of current user.'''
    investment = dict()

    fixed_deposit = FixedDeposit.objects.filter(created_by = request.user)
    fd_eval = 0
    for fd_ in list(fixed_deposit):
        delta = min(fd_.maturity_date, date.today()) - fd_.date_of_investment
        fd_amt = fd_.amount_invested + fd_.amount_invested * fd_.annual_roi * (delta.days) / (100 * 365)
        fd_eval = fd_eval + fd_amt
    investment['Fixed Deposit Evaluation'] = fd_eval

    bullion = Bullion.objects.filter(created_by = request.user)
    bullion_eval = 0
    for bullion_ in list(bullion):
        if bullion_.type.lower() == 'gold':
            bullion_amt = bullion_.weight * GOLD_RATE
        elif bullion_.type.lower() == 'silver':
            bullion_amt = bullion_.weight * SILVER_RATE
        bullion_eval = bullion_eval + bullion_amt
    investment['Bullion Evaluation'] = bullion_eval

    return Response(investment)