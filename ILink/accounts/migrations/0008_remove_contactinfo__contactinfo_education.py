# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20160503_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='_contactinfo_education',
        ),
    ]