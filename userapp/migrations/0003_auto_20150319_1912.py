# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20150319_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
    ]
