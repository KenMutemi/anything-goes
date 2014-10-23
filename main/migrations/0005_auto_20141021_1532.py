# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_summary_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='title',
            field=models.TextField(),
        ),
    ]
