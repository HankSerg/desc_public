from django.urls import path
from desc.apps.finance.views import *

urlpatterns = [
    path('', finance_listview, name='finance-list'),
    path('profit/', ProfitListView.as_view()),
    path('all/', all_finance_listview),
    path('stat/', FinanceStatisticView.as_view()),
    path('all(<int:page>+)/', all_finance_listview),
    path('create/', FinanceCreateView.as_view(), name='finance-create'),

    path('<int:pk>/update/', FinanceUpdateView.as_view(), name='finance-update'),
    path('<int:pk>/delete/', FinanceDeleteView.as_view(), name='finance-delete'),
    path('<int:pk>/', FinanceDetailView.as_view(), name='finance-detail'),


    # выборка по дате
    # path('date/$', finance_listview_date),
    path('date/', finance_listview_date_form, name='finance-date'),
    path('date/<int:year>/<int:month>/<int:date>/', finance_listview_date),
    path('search/', post_search, name='post_search'),

# Далее описание API
    # path('expenses/', Expenses.as_view()),
    # path('expense/', ExpenseSingle.as_view()),
    # path('expense/', ExpenseSingle.as_view()),
]
