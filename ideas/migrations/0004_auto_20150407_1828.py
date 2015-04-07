# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150407_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomment',
            name='idea',
            field=models.ForeignKey(to='ideas.Idea'),
            preserve_default=True,
        ),
    ]
