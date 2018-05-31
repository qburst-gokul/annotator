# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('share', models.BooleanField(default=False)),
                ('thumbnail', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=50)),
                ('screen', models.CharField(blank=True, max_length=10)),
                ('density', models.CharField(blank=True, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]