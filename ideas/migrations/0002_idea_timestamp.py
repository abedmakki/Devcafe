# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 12, 27, 34, 93589, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
