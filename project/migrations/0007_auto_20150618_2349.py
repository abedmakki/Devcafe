# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='contributor',
            name='position',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
