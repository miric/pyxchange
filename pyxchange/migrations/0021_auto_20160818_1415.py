# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyxchange', '0020_auto_20160818_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(default='3jdeaE', max_length=6, unique=True),
        ),
    ]
