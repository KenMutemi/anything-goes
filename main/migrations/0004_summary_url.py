# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141019_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='url',
            field=models.TextField(default='http://www.example.com'),
            preserve_default=False,
        ),
    ]
