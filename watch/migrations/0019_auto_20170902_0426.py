# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-02 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0018_auto_20170824_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='movement',
            field=models.CharField(choices=[(b'automatic', b'\xe8\x87\xaa\xe5\x8b\x95\xe9\x8c\xb6'), (b'manual', b'\xe6\xa9\x9f\xe6\xa2\xb0\xe9\x8c\xb6')], max_length=50, verbose_name=b'Movement'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='type',
            field=models.CharField(choices=[(b'all', b'\xe7\x94\xb7\xe5\xa5\xb3\xe6\xac\xbe'), (b'men', b'\xe7\x94\xb7\xe6\xac\xbe'), (b'women', b'\xe5\xa5\xb3\xe6\xac\xbe')], max_length=50, verbose_name=b'Type'),
        ),
    ]
