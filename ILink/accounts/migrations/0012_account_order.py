# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-04 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20160518_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
