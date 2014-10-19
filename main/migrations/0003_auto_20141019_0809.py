# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141019_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='fetch_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date'),
        ),
    ]
