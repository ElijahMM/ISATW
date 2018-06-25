# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProfessorApp', '0003_auto_20180625_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update_at')),
            ],
        ),
    ]
