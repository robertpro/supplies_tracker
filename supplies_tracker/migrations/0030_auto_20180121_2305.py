# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-21 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0029_auto_20180119_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_storage',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
