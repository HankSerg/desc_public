# Generated by Django 2.0.8 on 2018-09-20 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_action'),
        ('finance', '0024_auto_20180805_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeexpend',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto.Auto'),
        ),
    ]
