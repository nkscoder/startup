# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170124_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdipp',
            name='dipp',
            field=models.IntegerField(unique=True),
        ),
    ]
