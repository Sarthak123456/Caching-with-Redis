# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetarApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metar',
            name='scode',
            field=models.TextField(max_length=1000),
        ),
    ]
