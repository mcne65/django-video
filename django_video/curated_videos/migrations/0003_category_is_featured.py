# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curated_videos', '0002_conference_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]