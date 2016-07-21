# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-26 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0007_auto_20160526_0042'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nota', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Compra_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
    ]