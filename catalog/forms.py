
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms


class RenewBookForm(forms.Form):
    """
        Form for a librarian to renew books.
        Форма доступная для библиотекаря для обновления книг
    """
    renewal_date = forms.DateField(help_text="Введите дату примерно 4 недели(по умолчанию 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # проверка того, что дата не выходит за нижнюю границу (не в прошлом)
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # проверка того, что дата не выходит за верхнюю границу (+4 недели)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Ошибка в дате - новая дата не может быть позже 4 недель'))

        # помните, что всегда надо возвращать очищенные данные

        return data
