# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150403_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(upload_to=b'project_images', blank=True),
            preserve_default=True,
        ),
    ]
