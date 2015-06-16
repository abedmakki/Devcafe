# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_auto_20150611_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'market_images', blank=True),
        ),
    ]
