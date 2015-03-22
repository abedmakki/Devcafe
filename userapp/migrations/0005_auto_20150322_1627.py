# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20150319_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
