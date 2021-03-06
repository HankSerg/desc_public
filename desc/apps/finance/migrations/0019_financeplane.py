# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0018_auto_20180323_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancePlane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(blank=True, choices=[('auto', 'Авто'), ('products', 'Продукты'), ('repairs', 'Ремонт'), ('health', 'Здоровье/Аптека'), ('home', 'Предметы в дом'), ('sortir', 'Бытовая химия/расходные'), ('learn', 'Обучение'), ('relax', 'Отдых / Развлечения'), ('other', 'Прочее'), ('mobile', 'Связь / Интернет')], default='home', help_text='Категория расходов', max_length=120, null=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
