# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_idealike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
