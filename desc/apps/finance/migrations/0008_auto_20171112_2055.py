# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20171027_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeexpend',
            name='category',
            field=models.CharField(blank=True, choices=[('auto', 'Авто'), ('products', 'Продукты'), ('repairs', 'Ремонт'), ('health', 'Здоровье/Аптека'), ('home', 'Предметы в дом'), ('learn', 'Обучение')], help_text='Выберите категорию', max_length=120, null=True),
        ),
    ]
