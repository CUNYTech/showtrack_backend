# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-24 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchList', '0004_auto_20161123_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='show_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='watchList.Show'),
        ),
    ]
