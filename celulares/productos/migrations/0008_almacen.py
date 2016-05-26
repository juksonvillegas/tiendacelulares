# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-26 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
        ('productos', '0007_auto_20160526_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('compra', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
    ]
