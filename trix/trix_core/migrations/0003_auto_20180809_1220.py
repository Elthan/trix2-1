# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trix_core', '0002_assignment_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='howsolved',
            name='solved_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Solved'),
        ),
        migrations.AddField(
            model_name='user',
            name='consent_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]