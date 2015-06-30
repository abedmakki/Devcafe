# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20150627_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default=b'freelancer', max_length=10, choices=[(b'freelancer', b'freelancer'), (b'fulltime', b'fulltime'), (b'parttime', b'parttime'), (b'volunteer', b'volunteer')]),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='profit',
            field=models.CharField(default=b'free', max_length=10, choices=[(b'fixed', b'fixed'), (b'percent', b'percentage'), (b'free', b'free')]),
        ),
        migrations.AddField(
            model_name='job',
            name='profit_value',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=0),
        ),
        migrations.AddField(
            model_name='job',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 13, 14, 24, 640000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
