# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curated_videos', '0004_auto_20161121_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='github_handle',
            field=models.URLField(blank=True, max_length=1500, null=True),
        ),
    ]
