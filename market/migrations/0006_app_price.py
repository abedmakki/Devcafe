# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_app_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
