from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView
from django.db.models import Avg, Max, Sum
from django.template.defaultfilters import date
from django.utils import timezone

from .models import Profit
# эксперимент с ajax
from .forms import JoinForm
from .mixins import AjaxFormMixin


from desc.apps.finance.models import FinanceExpend


class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = 'forms/ajax.html'
    success_url = '/form-success/'


class ProfitListView(ListView):
    template_name = 'profit/profit_list.html'

    def get_queryset(self):
        year = Profit.objects.filter(timestamp__year=2018)
        queryset = year
        return queryset

    def get_context_data(self, **kwargs):
        import datetime
        today = datetime.date.today()

        # Месяц числом
        num_month = date(today, 'm')

        # доходы за год
        profit_year = Profit.objects.filter(timestamp__year=2018)

        # расходы за год
        expend_year = FinanceExpend.objects.filter(timestamp__year=2018)

        # доходы за месяц
        sum_profit_month = profit_year.filter(timestamp__month=num_month)
        # итого доходы за месяц
        prof_aggr_today = sum_profit_month.aggregate(Sum('total'))['total__sum']

        # расходы за этот месяц
        sum_today_month = expend_year.filter(timestamp__month=num_month)
        # итого расходы за месяц
        expend_month = sum_today_month.aggregate(Sum('total'))['total__sum']

        # разница доходы - расходы

        difference = prof_aggr_today - expend_month

        context = super(ProfitListView, self).get_context_data(**kwargs)
        context['aggr_today'] = expend_month
        context['profit_month'] = prof_aggr_today
        context['difference'] = difference
        return context


class ProfitDetailView(DetailView):
    def get_queryset(self):
        return Profit.objects.filter(user=self.request.user)


class ProfitCreateView(CreateView):
    def get_queryset(self):
        return Profit.objects.filter(user=self.request.user)


class ProfitUpdateView(UpdateView):
    def get_queryset(self):
        return Profit.objects.filter(user=self.request.user)
