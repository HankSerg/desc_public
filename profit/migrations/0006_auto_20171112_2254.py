# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0005_profit_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit',
            name='updated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profit',
            name='category',
            field=models.CharField(blank=True, choices=[('zarplata', 'Зарплата'), ('card', 'На карту'), ('gift', 'Подарки'), ('other', 'Другое')], default='zarplata', help_text='Выберите категорию дохода', max_length=120, null=True),
        ),
    ]
