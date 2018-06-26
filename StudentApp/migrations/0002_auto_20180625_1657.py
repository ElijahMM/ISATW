# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.AlterField(
            model_name='student',
            name='specializations',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.Specializare'),
        ),
    ]
