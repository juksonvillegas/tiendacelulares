# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default=datetime.datetime(2015, 11, 21, 19, 39, 46, 643117, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=2, max_length=9),
            preserve_default=False,
        ),
    ]
