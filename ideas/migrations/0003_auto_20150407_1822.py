# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_ideacomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomment',
            name='idea',
            field=models.ForeignKey(related_name='comments', to='ideas.Idea'),
            preserve_default=True,
        ),
    ]
