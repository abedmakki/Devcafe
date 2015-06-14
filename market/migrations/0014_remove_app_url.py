# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_app_uploaded_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='url',
        ),
    ]
