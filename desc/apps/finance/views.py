from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, Max, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import get_language, activate
from django.template.defaultfilters import date
from django.urls import reverse
from django.http import Http404
from django.utils.translation import ugettext_lazy as _

import datetime
# from datetime import date


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.postgres.search import SearchVector
from .forms import FinanceCreateForm, FinanceFilterSingleDateForm, SearchForm
from desc.apps.finance.models import FinanceExpend, FinanceProfit

from desc.apps.finance.serializers import (SingleSerializers, ExpensesSerializers)

from .mixins import AjaxFormMixin

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


class FinanceCreateView(AjaxFormMixin, CreateView):
    form_class = FinanceCreateForm
    template_name = 'finance/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()

        return super(FinanceCreateView, self).form_valid(form)


class FinanceUpdateView(AjaxFormMixin, UpdateView):
    form_class = FinanceCreateForm
    template_name = 'finance/form.html'

    def get_queryset(self):
        return FinanceExpend.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(FinanceUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context


class FinanceDeleteView(DeleteView):
    #model = FinanceExpend

   def delete(self, request, *args, **kwargs):
   #    self.object = self.get_object()

    success_url = '/finance/'
# def finance_createview(request):
#     form = FinanceCreateForm()
#
#     if request.method == "POST":
#         print("post data")
#
#         form = FinanceCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # instance = FinanceExpend(file_field=request.FILES['files'])
#             # instance.save()
#             # handle_uploaded_file(request.FILES['file'])
#             # obj = FinanceExpend.objects.create(
#             #     name=form.cleaned_data.get('name'),
#             #     category=form.cleaned_data.get('category'),
#             #     timestamp=form.cleaned_data.get('timestamp'),
#             #     kolvo=form.cleaned_data.get('kolvo'),
#             #     total=form.cleaned_data.get('total'),
#             #     file=request.FILES['files']
#             #
#             # )
#             # return reverse('finance-detail', kwargs={'id': id})
#             return HttpResponseRedirect('/finance/')
#
#         if form.errors:
#             print(form.errors)
#
#         # name = request.POST.get('name')
#         # name = request.POST.get('name')
#         # name = request.POST.get('name')
#     template_name = 'finance/form.html'
#     context = {"form": form}
#     return render(request, template_name, context)


def handle_uploaded_file(f):
    with open('test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def home(request):
#     context = {
#         "html_var": "context variable"
#     }
#     return render(request, "base.html", context)

User = get_user_model()


class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'home.html'
        context = {
            'customers': '10'
        }
        return render(request, template_name, context)

class ArifmView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'arifmetika.html'
        context = { }
        return render(request, template_name, context)

class Arifm2View(View):
    def get(self, request, *args, **kwargs):
        template_name = 'arifmetika2.html'
        context = { }
        return render(request, template_name, context)

class Arifm2classView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'arifmetika2class.html'
        context = { }
        return render(request, template_name, context)

class RussView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'russ.html'
        context = { }
        return render(request, template_name, context)

class GirlsView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'girls.html'
        context = { }
        return render(request, template_name, context)

class TrudView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'trud1.html'
        context = { }
        return render(request, template_name, context)

class DetsadView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'detsad.html'
        context = { }
        return render(request, template_name, context)


def get_data(request, *args, **kwargs):
    # ip = request.META['REMOTE_ADDR']
    data = {
        "sales": 100,
        "customers": 10
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    # TODO добавить finance profit

    def get(self, request, format=None):
        import datetime
        now = datetime.date.today()
        # текущий год
        now_year = now.year
        # прошлый год
        last_year = now.year - 1

        year = FinanceExpend.objects.filter(timestamp__year=now_year)
        data_last_year = FinanceExpend.objects.filter(timestamp__year=last_year)
        # новый массив со значениями за текущий год
        now_year_arr = []
        # новый массив со значениями за прошлый год
        last_year_arr = []
        # получим данные за 12 месяцев для каждого случая
        for x in range(1, 13):
            now_year_arr.append(year.filter(timestamp__month=x).aggregate(total=Sum('total'))['total'])
            last_year_arr.append(data_last_year.filter(timestamp__month=x).aggregate(total=Sum('total'))['total'])

        # qs_count = User.objects.all().count()
        # Заголовки для графика
        labels = [
            "Январь", "Февраль", "Март", "Апрель",
            "Май", "Июнь", "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь"]

        data = {
            "labels": labels,
            "default": now_year_arr,
            "last_year": last_year_arr
        }
        return Response(data)


class FinanceDetailView(DetailView):
    queryset = FinanceExpend.objects.all()


def finance_detailview(request, id):
    template_name = 'finance/finance_detail.html'
    obj = FinanceExpend.objects.get(id=id)
    # print(obj)
    context = {
        "object": obj
    }
    return render(request, template_name, context)


class FinanceStatisticView(View):

    # model = FinanceExpend
    # template_name = 'statistic.html'

    # def get(self, request, *args):
    #     return FinanceExpend.objects.filter(timestamp__range=["2019-07-26", "2019-08-05"]).aggregate(Sum('total'))


    def get(self, request, *args, **kwargs):
        # данные за период отпуска
        q = FinanceExpend.objects.filter(timestamp__range=["2019-07-26", "2019-08-05"])
        sum = q.aggregate(Sum('total'))
        template_name = 'statistic.html'

        context = {
            "sum": sum
        }
        return render(request, template_name, context)


def finance_listview(request):
    # русский
    activate('ru')
    get_language()

    today = datetime.date.today()
    # Этот месяц
    # nowMonth = date(today, 'F')
    # nowMonth = date(today, 'F')
    # Месяц числом
    numMonth = date(today, 'm')
    # Этот год числом
    now_year = date(today, 'Y')

    # print(numMonth)
    # TODO Переписать используя наработки. Возможно используя API chart

    # расходы на автомобили (все) за всё время:
    all_auto = FinanceExpend.objects.filter(category='auto').aggregate(Sum('total'))
    patriot_all = FinanceExpend.objects.filter(auto__name='UAZ PATRIOT').aggregate(Sum('total'))
    vesta_all = FinanceExpend.objects.filter(auto__name='Lada Vesta').aggregate(Sum('total'))
    # Этот год
    # последние 30 записей за этот год
    year = FinanceExpend.objects.filter(timestamp__year=now_year)
    # Расходы за этот месяц
    sum_today_month = year.filter(timestamp__month=numMonth)
    aggr_today = sum_today_month.aggregate(Sum('total'))
    year16 = FinanceExpend.objects.filter(timestamp__year=2016)
    year17 = FinanceExpend.objects.filter(timestamp__year=2017)
    year18 = FinanceExpend.objects.filter(timestamp__year=2018)
    year19 = FinanceExpend.objects.filter(timestamp__year=2019)
    year20 = FinanceExpend.objects.filter(timestamp__year=2020)
    year21 = FinanceExpend.objects.filter(timestamp__year=2021)
    month1 = year.filter(timestamp__month=1)
    month2 = year.filter(timestamp__month=2)
    month3 = year.filter(timestamp__month=3)
    month4 = year.filter(timestamp__month=4)
    month5 = year.filter(timestamp__month=5)
    month6 = year.filter(timestamp__month=6)
    month7 = year.filter(timestamp__month=7)
    month8 = year.filter(timestamp__month=8)
    month9 = year.filter(timestamp__month=9)
    month10 = year.filter(timestamp__month=10)
    month11 = year.filter(timestamp__month=11)
    month12 = year.filter(timestamp__month=12)

    month1_expend = month1.aggregate(Sum('total'))
    month2_expend = month2.aggregate(Sum('total'))
    month3_expend = month3.aggregate(Sum('total'))
    month4_expend = month4.aggregate(Sum('total'))
    month5_expend = month5.aggregate(Sum('total'))
    month6_expend = month6.aggregate(Sum('total'))
    month7_expend = month7.aggregate(Sum('total'))
    month8_expend = month8.aggregate(Sum('total'))
    month9_expend = month9.aggregate(Sum('total'))
    month10_expend = month10.aggregate(Sum('total'))
    month11_expend = month11.aggregate(Sum('total'))
    month12_expend = month12.aggregate(Sum('total'))

    all = FinanceExpend.objects.all()
    maximum = year.aggregate(Max('total'))
    queryset = year.order_by('-timestamp')[:30]
    total_sum = year.aggregate(Sum('total'))
    sum16 = year16.aggregate(Sum('total'))
    sum17 = year17.aggregate(Sum('total'))
    sum18 = year18.aggregate(Sum('total'))
    sum19 = year19.aggregate(Sum('total'))
    sum20 = year20.aggregate(Sum('total'))
    sum21 = year21.aggregate(Sum('total'))
    # print(sum16)
    all_sum = all.aggregate(Sum('total'))
    # средний чек за весь период
    avg = FinanceExpend.objects.aggregate(total_avg=Avg('total'))
    # queryset = FinanceExpend.objects.all().order_by('-updated')
    context = {
        "object_list": queryset,
        "avg": avg,
        "maximum": maximum,
        "total": total_sum,
        "all_sum": all_sum,
        'sum16': sum16,
        'sum17': sum17,
        "sum18": sum18,
        "sum19": sum19,
        "sum20": sum20,
        "sum21": sum21,
        "numMonth": numMonth,
        "sumTodayMonth": aggr_today,
        'month1_expend': month1_expend,
        'month2_expend': month2_expend,
        'month3_expend': month3_expend,
        'month4_expend': month4_expend,
        'month5_expend': month5_expend,
        'month6_expend': month6_expend,
        'month7_expend': month7_expend,
        'month8_expend': month8_expend,
        'month9_expend': month9_expend,
        'month10_expend': month10_expend,
        'month11_expend': month11_expend,
        'month12_expend': month12_expend,
        'all_auto_expend': all_auto,
        'patriot_all': patriot_all,
        'vesta_all': vesta_all
    }
    template_name = 'finance/finance_list.html'
    return render(request, template_name, context)


def finance_listview_auto(request, *args, **kwargs):
    #  Выборка по категории Авто
    template_name = 'finance/finance_list.html'
    # последние 30 записей за этот год
    year = FinanceExpend.objects.filter(timestamp__year=2017)
    maximum = year.aggregate(Max('total'))
    queryset = year.order_by('-timestamp')[:30]
    total_sum = year.aggregate(Sum('total'))
    # средний чек за весь период
    avg = FinanceExpend.objects.aggregate(total_avg=Avg('total'))

    # queryset = FinanceExpend.objects.all().order_by('-updated')
    context = {
        "object_list": queryset,
        "avg": avg,
        "maximum": maximum,
        "total": total_sum
    }
    return render(request, template_name, context)


def all_finance_listview(request, *args, **kwargs):
    # скопировать и зафильтровать на пример так:
    # query = FinanceExpend.objects.filter(timestamp=date(2018,12,31))
    #  используем пагинацию
    template_name = 'finance/finance_list_all.html'
    # year = FinanceExpend.objects.filter(timestamp__year=2017)
    queryset = FinanceExpend.objects.all().order_by('-timestamp')
    # print(queryset)
    paginator = Paginator(queryset, 20)

    page = request.GET.get('page')
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    return render(request, template_name, {'object_list': obj})


def finance_listview_date(request, year, month, date, *args, **kwargs):
    # TODO доработать с формой
    # скопировать и зафильтровать на пример так:
    # query = FinanceExpend.objects.filter(timestamp=date(2018,12,31))
    #  используем пагинацию
    template_name = 'finance/finance_list_all.html'
    # year = FinanceExpend.objects.filter(timestamp__year=2017)
    # Год
    # req_year = year
    # newString = "%year - ем %s" % year
    # timeformat = year + '-' + month + '-' + date
    dt =  datetime.date(year,month,date)
    queryset = FinanceExpend.objects.filter(timestamp=dt)
    # queryset = FinanceExpend.objects.all().order_by('-timestamp')
    # print(queryset)
    if request.method == 'POST':
        form = FinanceFilterSingleDateForm(request.POST)

        if form.is_valid():
            reqyear = form.cleaned_data['single_date'].year
            reqmonth = form.cleaned_data['single_date'].month
            reqdate = form.cleaned_data['single_date'].day

            url = '/finance/date/%d/%d/%d/' % (reqyear, reqmonth, reqdate)

            return HttpResponseRedirect(url)
    else:
        form = FinanceFilterSingleDateForm(request.GET)

    paginator = Paginator(queryset, 20)

    page = request.GET.get('page')
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    return render(request, template_name, {'form': form, 'object_list': obj})


def finance_listview_date_form(request, *args, **kwargs):
    # скопировать и зафильтровать на пример так:
    # query = FinanceExpend.objects.filter(timestamp=date(2018,12,31))
    #  используем пагинацию
    template_name = 'finance/finance_listview_date_form.html'

    if request.method == 'POST':
      form = FinanceFilterSingleDateForm(request.POST)

      if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
         reqyear = form.cleaned_data['single_date'].year
         reqmonth = form.cleaned_data['single_date'].month
         reqdate = form.cleaned_data['single_date'].day
        #
         # string = reqyear + '/' + reqmonth  + '/' + '/'+ reqdate +'/'

         url = '/finance/date/%d/%d/%d/' % (reqyear, reqmonth, reqdate)

         # redirect to a new URL
         return HttpResponseRedirect(url)
      # else:
        # Do something in case if form is not valid
        # raise form.ValidationError("You have forgotten about Fred!")
        # raise Http404

        # form = FinanceFilterSingleDateForm(request.POST)
    else:
        prop_date = datetime.date.today()
        form = FinanceFilterSingleDateForm(initial={'single_date': prop_date,})
    #   'single_date'  2019-03-21
    return render(request, template_name, {'form': form})


#class RestaurantListView(ListView):
    #template_name = 'restaurants/restaurants_list.html'

    # def get_queryset(self):
    #     slug = self.kwargs.get("slug")
    #     if slug:
    #         queryset = RestaurantLocation.objects.filter(
    #             Q(category__iexact=slug) |
    #             Q(category__icontains=slug))
    #     else:
    #         queryset = RestaurantLocation.objects.all()
        #return render()
from django.conf import settings

class ProfitListView(ListView):
    model = FinanceProfit
    template_name = 'profit/profit_list.html'
    paginate_by = 20
    # Сделать расходы за текущий месяц
    # и добавить переменную
    # aggr_today - расходы за этот месяц
    # вывести доходы за текущий месяц переменная profit_month
    # queryset = year.order_by('-timestamp')[:30]

    def get_context_data(self, **kwargs):
        import datetime
        now = datetime.date.today()
        now_year = now.year
        now_month = now.month
        profitlist = FinanceProfit.objects.filter(timestamp__year=now_year).order_by('-timestamp')[:30]
        expend_month = FinanceExpend.objects.filter(timestamp__year=now_year,timestamp__month=now_month).aggregate(total=Sum('total'))['total']
        profit_month = FinanceProfit.objects.filter(timestamp__year=now_year,timestamp__month=now_month).aggregate(total=Sum('total'))['total']
        if profit_month  and expend_month :
                difference = profit_month-expend_month
        else:
            difference = 0
        # передаём данные в шаблон
        context = {
            'aggr_today': expend_month,
            'profit_month': profit_month,
            'profitlist': profitlist,
            'profitdiff': difference
        }
        return context

     # def get_queryset(self):
     #     year = FinanceProfit.objects.filter(timestamp__year=2019).order_by('-timestamp')[:30]
     #     queryset = year.order_by('-timestamp')[:30]
     #     return queryset

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = FinanceExpend.objects.annotate(
            search = SearchVector('name', 'category'),
        ).filter(search=query)
        return render(request, 'finance/search.html', {'form': form,
                                                        'query': query,
                                                        'results': results})
