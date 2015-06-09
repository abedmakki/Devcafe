# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_app_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appcomment',
            old_name='App',
            new_name='app',
        ),
        migrations.RenameField(
            model_name='apprating',
            old_name='App',
            new_name='app',
        ),
    ]
