# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('page_likes', models.PositiveIntegerField(default=0)),
                ('new_likes', models.PositiveIntegerField(default=0)),
                ('reach', models.PositiveIntegerField(default=0)),
                ('people_engaged', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'facebook analytics',
            },
        ),
        migrations.CreateModel(
            name='FacebookObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='facebookanalytics',
            name='object',
            field=models.ForeignKey(to='facebooklizr.FacebookObject'),
        ),
    ]
