# Generated by Django 2.0.8 on 2018-08-05 13:24

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0023_auto_20180805_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='date',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
