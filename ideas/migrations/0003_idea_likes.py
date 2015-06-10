# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_idea_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
