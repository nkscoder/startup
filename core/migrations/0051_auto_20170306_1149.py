# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20170306_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='industry',
            field=models.CharField(choices=[('Healthcare', 'Healthcare'), ('FinTech', 'FinTech'), ('Logistics', 'Logistics')], max_length=100),
        ),
    ]
