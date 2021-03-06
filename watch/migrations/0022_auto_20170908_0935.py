# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-08 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0021_auto_20170902_0427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='bracelet_color',
        ),
        migrations.RemoveField(
            model_name='watch',
            name='bracelet_length',
        ),
        migrations.RemoveField(
            model_name='watch',
            name='bracelet_material',
        ),
        migrations.AddField(
            model_name='watch',
            name='case_size',
            field=models.CharField(blank=True, choices=[(b'<26', b'<26 mm'), (b'26-30', b'26-30 mm'), (b'31-35', b'31-35 mm'), (b'36-39', b'36-39 mm'), (b'40-41', b'40-41 mm'), (b'42-43', b'42-43mm'), (b'>44', b'>44 mm')], max_length=50, verbose_name=b'\xe9\x8c\xb6\xe9\x9d\xa2\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='watch',
            name='style',
            field=models.CharField(blank=True, choices=[(b'casual', b'\xe4\xbc\x91\xe9\x96\x92'), (b'military', b'\xe8\xbb\x8d\xe4\xba\x8b'), (b'pilot', b'\xe6\xa9\x9f\xe5\xb8\xab'), (b'sport', b'\xe9\x81\x8b\xe5\x8b\x95'), (b'dive', b'\xe6\xbd\x9b\xe6\xb0\xb4'), (b'dress', b'\xe6\x99\x9a\xe5\xae\xb4'), (b'racing', b'\xe8\xb3\xbd\xe8\xbb\x8a')], max_length=50, verbose_name=b'\xe6\xac\xbe\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='case_material',
            field=models.CharField(max_length=30, verbose_name=b'\xe9\x8c\xb6\xe9\x9d\xa2\xe6\x9d\x90\xe6\x96\x99'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='color',
            field=models.CharField(blank=True, choices=[(b'black', b'\xe9\xbb\x91'), (b'bronze', b'\xe9\x8a\x85'), (b'champagne', b'\xe9\xa6\x99\xe6\xbf\xb1\xe9\x87\x91'), (b'green', b'\xe7\xb6\xa0'), (b'navy', b'\xe6\xb5\xb7\xe8\xbb\x8d\xe8\x97\x8d'), (b'silver', b'\xe9\x8a\x80'), (b'white', b'\xe7\x99\xbd'), (b'beige', b'\xe7\xb1\xb3'), (b'blue', b'\xe8\x97\x8d'), (b'brown', b'\xe5\x95\xa1'), (b'pink', b'\xe7\xb2\x89\xe7\xb4\x85'), (b'black', b'\xe9\xbb\x91'), (b'bronze', b'\xe9\x8a\x85'), (b'champagne', b'\xe9\xa6\x99\xe6\xbf\xb1\xe9\x87\x91'), (b'green', b'\xe7\xb6\xa0'), (b'navy', b'\xe6\xb5\xb7\xe8\xbb\x8d\xe8\x97\x8d'), (b'silver', b'\xe9\x8a\x80'), (b'white', b'\xe7\x99\xbd'), (b'beige', b'\xe7\xb1\xb3'), (b'blue', b'\xe8\x97\x8d'), (b'brown', b'\xe5\x95\xa1'), (b'pink', b'\xe7\xb2\x89\xe7\xb4\x85')], max_length=30, verbose_name=b'\xe9\xa1\x8f\xe8\x89\xb2'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa8\xb1'),
        ),
    ]
