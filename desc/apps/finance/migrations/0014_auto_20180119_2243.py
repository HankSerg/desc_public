# Generated by Django 2.0 on 2018-01-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_auto_20180119_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeexpend',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]