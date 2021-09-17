# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-02 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20171112_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeexpend',
            name='category',
            field=models.CharField(blank=True, choices=[('auto', 'Авто'), ('products', 'Продукты'), ('repairs', 'Ремонт'), ('health', 'Здоровье/Аптека'), ('home', 'Предметы в дом'), ('sortir', 'Бытовая химия/проч'), ('learn', 'Обучение'), ('relax', 'Отдых / Развлечения'), ('other', 'Прочее')], help_text='Выберите категорию', max_length=120, null=True),
        ),
    ]
