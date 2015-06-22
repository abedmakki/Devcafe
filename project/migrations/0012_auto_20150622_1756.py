# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20150622_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='job',
            field=models.OneToOneField(related_name='contributor', null=True, blank=True, to='project.Job'),
        ),
    ]
