# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20141023_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
