# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchList', '0007_auto_20161129_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='progress',
        ),
    ]
