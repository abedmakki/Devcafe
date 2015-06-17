# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AlterField(
            model_name='project',
            name='plan',
            field=models.TextField(null=True, blank=True),
        ),
    ]
