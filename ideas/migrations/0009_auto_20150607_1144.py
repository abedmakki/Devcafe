# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0008_auto_20150509_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='rating',
        ),
        migrations.AddField(
            model_name='idea',
            name='rating_no',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='rating_total',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
