from rest_framework import serializers
from django.contrib.auth.models import User

from desc.apps.finance.models import FinanceExpend

class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")

class ExpensesSerializers(serializers.ModelSerializer):
    """ Сериализация всех расходов"""

    class Meta:
        model = FinanceExpend
        fields = '__all__'


class SingleSerializers(serializers.ModelSerializer):
    """Сериализация записи расходов"""
    # user = UserSerializer()

    class Meta:
      model = FinanceExpend
      fields = '__all__'
