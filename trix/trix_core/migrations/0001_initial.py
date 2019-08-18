# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-25 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, help_text='User is active? Inactive users can not log in.', verbose_name='Is active?')),
                ('is_admin', models.BooleanField(default=False, help_text='User is superuser? Superusers have full access to the admin UI.', verbose_name='Is superuser?')),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['email'],
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(help_text='Write the assignment here.', verbose_name='Assignment text')),
                ('solution', models.TextField(blank=True, default=b'', help_text='If you want your students to be able to view a suggested solution, write the solution here.', verbose_name='Solution')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('lastupdate_datetime', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
            ],
            options={
                'ordering': ['-lastupdate_datetime'],
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignments',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=b'', verbose_name='Description')),
            ],
            options={
                'ordering': ['course_tag'],
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='HowSolved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('howsolved', models.CharField(choices=[(b'bymyself', 'Solved by myself'), (b'withhelp', 'Solved with help')], max_length=10)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trix_core.Assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permalink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=b'', max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, default=b'', verbose_name='Description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trix_core.Course', verbose_name='Course')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Permalink',
                'verbose_name_plural': 'Permalinks',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(blank=True, choices=[(b'', 'No category'), (b'c', 'Course'), (b'p', 'Period')], default=b'', max_length=1)),
            ],
            options={
                'ordering': ['tag'],
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='permalink',
            name='tags',
            field=models.ManyToManyField(to='trix_core.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='course',
            name='active_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active_period_set', to='trix_core.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='course_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_set', to='trix_core.Tag'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='tags',
            field=models.ManyToManyField(to='trix_core.Tag', verbose_name='Tags'),
        ),
    ]