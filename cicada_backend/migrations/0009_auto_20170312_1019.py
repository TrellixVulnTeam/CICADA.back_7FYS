# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cicada_backend', '0008_component_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cicada_backend.Profile'),
        ),
    ]
