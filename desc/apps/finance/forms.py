from django import forms
from django.forms import ModelForm
from .models import FinanceExpend
from django.core.exceptions import ValidationError
from desc.apps.auto.models import Auto
from django.forms.widgets import SplitDateTimeWidget
from django.utils.translation import ugettext_lazy as _
import datetime


# Называем поля по своему TODO добавить проверку clean
class FinanceCreateForm(ModelForm):


    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    timestamp = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'datepicker', 'placeholder': 'Дата покупки','autocomplete':'off'}))


    total = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Итого','autocomplete':'off'}))

    autoqueryset = Auto.objects.all()
    auto = forms.ModelChoiceField(queryset=autoqueryset, required=False)
    #
    class Meta:
        model = FinanceExpend
        fields = [
            'name',
            'timestamp',
            'category',
            'auto',
            'total',
            'files'
        ]
        labels = {
            'name': _('Название'),
            'timestamp': _('Дата покупки'),
            'category': _('Категория'),
            'total': _('Всего'),
            'files': _('Файлы'),
        }
        help_texts = {
            'files': _('Квитанции об оплате'),
            'auto': _('Квитанции об оплате'),
        }

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super(FinanceCreateForm, self).__init__(*args, **kwargs)


class DateInput(forms.DateInput):
    input_type = 'date'


class FinanceFilterSingleDateForm(forms.Form):
    single_date = forms.DateField(widget=forms.DateInput(attrs={
    'class': 'datepicker', 'placeholder': 'Дата покупки','autocomplete': 'off'}))

    def clean_single_date(self):
        data = self.cleaned_data['single_date']

        # проверка того, что дата не выходит за нижнюю границу (не в прошлом)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Ошибка в дате - новая дата не может быть позже 4 недель'))

        return data

class SearchForm(forms.Form):
    # Добавим для осуществления поиска по формам
    query = forms.CharField()
