# Generated by Django 2.0.8 on 2018-08-05 13:13

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0022_homepage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]