# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20170301_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectName',
            field=models.CharField(default='ejfhje', max_length=100),
            preserve_default=False,
        ),
    ]
