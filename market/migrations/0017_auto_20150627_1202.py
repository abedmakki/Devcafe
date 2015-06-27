# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_auto_20150627_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.CharField(max_length=20),
        ),
    ]
