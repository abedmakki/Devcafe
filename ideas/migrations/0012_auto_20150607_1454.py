# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0011_auto_20150607_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='idearating',
            name='idea',
            field=models.ForeignKey(related_name='ratings', to='ideas.Idea'),
        ),
    ]
