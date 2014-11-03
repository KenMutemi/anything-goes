# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='fetch_date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 19), verbose_name=b'date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='summary',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
