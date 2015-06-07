# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0009_auto_20150607_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='rating_no',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='rating_total',
        ),
        migrations.AddField(
            model_name='idea',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
