# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-14 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
