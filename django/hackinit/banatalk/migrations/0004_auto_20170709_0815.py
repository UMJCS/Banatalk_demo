# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-09 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banatalk', '0003_auto_20170709_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eat',
            name='time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='Datetime',
            field=models.CharField(max_length=50),
        ),
    ]
