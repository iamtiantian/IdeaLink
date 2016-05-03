# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160503_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='_contactinfo_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='_contactinfo_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='_contactinfo_education',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='_contactinfo_gender',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='_contactinfo_birthdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='_contactinfo_cellphone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='_contactinfo_email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='_contactinfo_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
