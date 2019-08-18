# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-08-18 19:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('trix_core', '0004_user_fix'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ManyToManyField(blank=True, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='solution',
            field=models.TextField(blank=True, default='', help_text='If you want your students to be able to view a suggested solution, write the solution here.', verbose_name='Solution'),
        ),
        migrations.AlterField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='howsolved',
            name='howsolved',
            field=models.CharField(choices=[('bymyself', 'Solved by myself'), ('withhelp', 'Solved with help')], max_length=10),
        ),
        migrations.AlterField(
            model_name='permalink',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='permalink',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.CharField(blank=True, choices=[('', 'No category'), ('c', 'Course'), ('p', 'Period')], default='', max_length=1),
        ),
    ]