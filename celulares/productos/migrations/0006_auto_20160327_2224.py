# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-28 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20160326_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='barras',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
