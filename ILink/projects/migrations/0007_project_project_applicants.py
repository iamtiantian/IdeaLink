# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-19 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20160518_0619'),
        ('projects', '0006_auto_20160518_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_applicants',
            field=models.ManyToManyField(related_name='projects_project_applicant_related', to='accounts.Account'),
        ),
    ]
