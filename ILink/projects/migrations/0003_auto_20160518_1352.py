# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160518_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
        ),
    ]