# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2024-05-06 13:21
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0007_auto_20240506_1128'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='licence',
            managers=[
                ('polymorphic_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
