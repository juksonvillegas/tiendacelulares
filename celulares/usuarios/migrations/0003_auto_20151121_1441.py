# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20151121_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default=b'su casa', max_length=250),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=b'968072613', max_length=9),
        ),
    ]
