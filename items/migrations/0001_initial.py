# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('body', models.CharField(blank=True, default='', max_length=1024)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Location')),
            ],
        ),
    ]
