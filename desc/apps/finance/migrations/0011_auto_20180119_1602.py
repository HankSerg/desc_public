# Generated by Django 2.0 on 2018-01-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_auto_20180119_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeexpend',
            name='kolvo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
