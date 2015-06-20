# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20150618_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='issued_to',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='project',
            field=models.ForeignKey(related_name='jobs', to='project.Project'),
        ),
    ]
