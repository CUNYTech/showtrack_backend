# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='progress',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
