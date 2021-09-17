from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from ..models import FinanceExpend

class FinanceExpendSerializer(serializers.ModelSerializer):
    """ сериализация всех расходов """
    class Meta:
        model = FinanceExpend
        fields = '__all__'

class ExpendSerializer(serializers.ModelSerializer):
    """ сериализация всех расходов """
    class Meta:
        model = FinanceExpend
        fields = '__all__'
