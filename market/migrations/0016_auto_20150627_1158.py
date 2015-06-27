# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_apptransaction_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
