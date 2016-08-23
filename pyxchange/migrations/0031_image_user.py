# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pyxchange', '0030_auto_20160819_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]