# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150617_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(related_name='contributors', to='project.Project'),
        ),
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(related_name='posts', to='project.Project'),
        ),
    ]
