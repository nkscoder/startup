# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20170306_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
            preserve_default=False,
        ),
    ]
