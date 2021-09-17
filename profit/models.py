from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import get_default_timezone
# TODO переписать всё в finance profit - почистить лишнее

# Задаём значения для SELECT
CATEGORY_CHOICES = (
    ('zarplata', 'Зарплата'),
    ('card', 'На карту'),
    ('gift', 'Подарки'),
    ('other', 'Другое')
)


# Create your models here.
class Profit(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        help_text=_('Выберите категорию дохода'),
        default='zarplata'
    )
    timestamp = models.DateField(auto_now_add=False, auto_now=False)
    updated = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)