# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-01 20:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_cliente_mayorista'),
        ('productos', '0006_auto_20160327_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preventa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime(2016, 4, 1, 15, 49, 59, 298499))),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
    ]
