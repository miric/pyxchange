# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyxchange', '0024_auto_20160818_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.CharField(help_text='Up to 500 characters', max_length=500, verbose_name='Description'),
        ),
    ]