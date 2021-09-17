from __future__ import unicode_literals
from django.conf import settings
from datetime import date

from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from desc.apps.auto.models import Auto

# Задаём значения для SELECT
CATEGORY_CHOICES = (
    ('auto', 'Авто'),
    ('products', 'Продукты'),
    ('repairs', 'Ремонт'),
    ('health', 'Здоровье/Аптека'),
    ('utility', 'Коммунальные'),
    ('home', 'Предметы в дом'),
    ('sortir', 'Бытовая химия/расходные'),
    ('learn', 'Обучение'),
    ('relax', 'Отдых / Развлечения'),
    ('mobile', 'Связь / Интернет'),
    ('clothes', 'Одежда / Обувь'),
    ('other', 'Прочее'),
)


class FinanceExpend(models.Model):
    """ Модель для записи расходов """
    name = models.CharField(max_length=120)  # tovar
    category = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        help_text=_('Выберите категорию')
    )
    timestamp = models.DateField(auto_now_add=False, auto_now=False)  # pdate
    updated = models.DateField(auto_now_add=True)  # Обновление записи
    kolvo = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)  # сумма
    total = models.DecimalField(max_digits=8, decimal_places=2)  # сумма
    files = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Строка расхода"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('finance-detail', kwargs={'pk': self.pk})

    @property
    def title(self):
        return self.name


# Задаём значения для SELECT
TYPE_CHOICES = (
    ('zarplata', 'Зарплата'),
    ('card', 'На карту'),
    ('gift', 'Подарки'),
    ('other', 'Другое')
)


class FinanceProfit(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        choices=TYPE_CHOICES,
        help_text=_('Выберите категорию дохода'),
        default='zarplata'
    )
    timestamp = models.DateField(auto_now_add=False, auto_now=False)
    updated = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)

# Задаём значения для SELECT
PLAN_CHOICES = (
    ('auto', 'Авто'),
    ('products', 'Продукты'),
    ('repairs', 'Ремонт'),
    ('health', 'Здоровье/Аптека'),
    ('home', 'Предметы в дом'),
    ('sortir', 'Бытовая химия/расходные'),
    ('learn', 'Обучение'),
    ('relax', 'Отдых / Развлечения'),
    ('other', 'Прочее'),
    ('mobile', 'Связь / Интернет'),
)


class FinancePlane(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        choices=PLAN_CHOICES,
        help_text=_('Категория расходов'),
        default='home'
    )
    description = models.CharField(
        max_length=500,
        help_text=_('Описание')
    )
    timestamp = models.DateField(
        auto_now_add=False,
        auto_now=False,
        default=date.today)
    updated = models.DateField(
        auto_now_add=True
    )  # Обновление записи

    def __str__(self):
        return str(self.name)


class HomePage(Page):
    body = RichTextField(blank=True)

    template = 'home_page.html'

    content_panels = Page.content_panels + [

        FieldPanel('body', classname="full")
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),

    ]
