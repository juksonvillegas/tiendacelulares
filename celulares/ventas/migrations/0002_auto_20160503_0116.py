# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-03 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_mayorista'),
        ('productos', '0006_auto_20160327_2224'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('documentado', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='venta_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantida', models.IntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
            ],
        ),
        migrations.AlterField(
            model_name='consignacion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
