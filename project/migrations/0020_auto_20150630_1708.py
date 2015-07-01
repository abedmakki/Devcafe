# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20150630_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='profit',
            field=models.CharField(default=b'free', null=True, max_length=10, choices=[(b'fixed', b'fixed'), (b'percentage', b'percentage'), (b'free', b'free')]),
        ),
    ]
