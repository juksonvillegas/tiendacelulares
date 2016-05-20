# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-20 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20160504_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta_detalle',
            old_name='cantida',
            new_name='cantidad',
        ),
        migrations.AlterField(
            model_name='consignacion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
