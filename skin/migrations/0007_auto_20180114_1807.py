# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin', '0006_auto_20171223_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='undertone',
            name='skintone',
        ),
        migrations.AlterField(
            model_name='skintype',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='undertone',
            name='image_u',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='undertone',
            name='jewellery',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='undertone',
            name='vein_color',
            field=models.CharField(max_length=100),
        ),
    ]
