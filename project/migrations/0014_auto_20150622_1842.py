# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20150622_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='job',
            field=models.ForeignKey(related_name='job_requests', blank=True, to='project.Job', null=True),
        ),
    ]
