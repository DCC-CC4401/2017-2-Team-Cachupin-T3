# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cholitos_law', '0003_auto_20170927_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
