# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_auto_20150627_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
