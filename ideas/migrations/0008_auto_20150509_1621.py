# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0007_auto_20150509_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_ideas', to='general.Tag', blank=True),
        ),
    ]
