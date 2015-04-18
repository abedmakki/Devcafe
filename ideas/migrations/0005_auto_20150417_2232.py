# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20150407_1740'),
        ('ideas', '0004_auto_20150407_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=models.ManyToManyField(to='general.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='ideacomment',
            name='idea',
            field=models.ForeignKey(related_name='comments', to='ideas.Idea'),
        ),
    ]
