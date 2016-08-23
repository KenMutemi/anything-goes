# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_summary_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='fetch_date',
            new_name='last_update',
        ),
    ]
