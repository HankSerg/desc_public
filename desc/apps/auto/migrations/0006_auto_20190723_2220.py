# Generated by Django 2.2 on 2019-07-23 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_auto_20190723_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='action',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
