# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_contactinfo_experience_project_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='_skill_proficiency',
            field=models.IntegerField(default=5),
        ),
    ]
