# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('subscribers', models.PositiveIntegerField(default=0)),
                ('video_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'youtube analytics',
            },
        ),
        migrations.CreateModel(
            name='YouTubeChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel_id', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='youtubeanalytics',
            name='channel',
            field=models.ForeignKey(to='youtubelizr.YouTubeChannel'),
        ),
    ]
