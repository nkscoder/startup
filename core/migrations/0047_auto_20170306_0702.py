# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20170306_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='Category',
            new_name='SubCategory',
        ),
    ]