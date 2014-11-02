# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141021_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='url',
            field=models.TextField(unique=True),
        ),
    ]
