# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0002_auto_20171112_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profit',
            name='total',
        ),
    ]
