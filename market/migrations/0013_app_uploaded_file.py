# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_auto_20150613_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='uploaded_file',
            field=models.FileField(null=True, upload_to=b'app_files', blank=True),
        ),
    ]
