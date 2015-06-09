# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_remove_app_avg_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
    ]
