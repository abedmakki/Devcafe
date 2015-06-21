# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 8, 59, 55, 87000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
