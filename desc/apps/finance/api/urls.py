from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = 'finance'

router = routers.DefaultRouter()
router.register('finance', views.ExpendViewSet)

urlpatterns = [
    path('expenses/', views.FinanceExpendListView.as_view(),name='finance_expend_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        # path('expense/', ExpenseSingle.as_view()),
    # path('expense/', ExpenseSingle.as_view()),
    path('', include(router.urls)),
]
