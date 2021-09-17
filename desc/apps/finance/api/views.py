from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from ..models import FinanceExpend
from .serializers import FinanceExpendSerializer, ExpendSerializer


class FinanceExpendListView(generics.ListAPIView):
    queryset = FinanceExpend.objects.all()
    serializer_class = FinanceExpendSerializer

class ExpendViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinanceExpend.objects.all()
    serializer_class = ExpendSerializer

class Expenses(APIView):
    """ Список расходов общий """
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        today = datetime.date.today()
        now_year = date(today, 'Y')

        # Расходы за этот месяц
        expenses_from_year = FinanceExpend.objects.filter(timestamp__year=now_year)

        expenses = expenses_from_year.order_by('-timestamp')[:30]
        # TODO EDIT THIS TO FILTER LIMIT

        # expenses = FinanceExpend.objects.all()
        serializer = ExpensesSerializers(expenses, many=True)
        return Response({"data": serializer.data})

class ExpenseSingle(APIView):
    """Одна запись расходов"""
    permission_classes = [permissions.AllowAny]
#     permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        id = request.GET.get("id")
        obj = FinanceExpend.objects.get(id=id)
        serializer = SingleSerializers(obj)
        return Response({"data": serializer.data})
