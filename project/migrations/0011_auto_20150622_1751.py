# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_project_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='position',
        ),
        migrations.AddField(
            model_name='contributor',
            name='job',
            field=models.OneToOneField(related_name='contributors', null=True, blank=True, to='project.Job'),
        ),
        migrations.AlterField(
            model_name='request',
            name='job',
            field=models.OneToOneField(related_name='request', null=True, blank=True, to='project.Job'),
        ),
    ]
