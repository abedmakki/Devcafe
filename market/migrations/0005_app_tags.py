# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        ('market', '0004_appcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_apps', to='general.Tag', blank=True),
        ),
    ]
