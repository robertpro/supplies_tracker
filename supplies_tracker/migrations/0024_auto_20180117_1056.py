# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 10:56
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0023_auto_20180117_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='space',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever'),
        ),
    ]