# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_apptransaction_baid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apptransaction',
            old_name='baid',
            new_name='paid',
        ),
    ]
