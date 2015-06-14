# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_remove_app_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='apptransaction',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
