from rest_framework import serializers

from desc.apps.finance.models import FinanceExpend


class ExpendSerializer(serializers.ModelSerializer):
    """
        Сериализатор для расходов
    """
    class Meta:
        model = FinanceExpend
        fields = '__all__'
