# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20150622_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='job',
            field=models.OneToOneField(related_name='job_request', null=True, blank=True, to='project.Job'),
        ),
    ]
