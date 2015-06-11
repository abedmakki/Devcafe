# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_auto_20150611_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apptransaction',
            name='unique_id',
            field=models.CharField(unique=True, max_length=30, blank=True),
        ),
    ]
