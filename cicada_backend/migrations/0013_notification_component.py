# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cicada_backend', '0012_remove_notification_components'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='component',
            field=models.ManyToManyField(through='cicada_backend.UserComponentNotificationResponse', to='cicada_backend.Component'),
        ),
    ]
