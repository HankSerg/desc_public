from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from desc.api.v1.serializers.common import ExpendSerializer
from desc.apps.finance.models import FinanceExpend


class ExpendViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    """
    API для расходов
    Просмотр, добавление, обновление
    """
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination
    serializer_class = ExpendSerializer
    queryset = FinanceExpend.objects.all()

