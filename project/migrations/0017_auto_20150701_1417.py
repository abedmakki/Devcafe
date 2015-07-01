# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20150627_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default=b'freelancer', max_length=10, null=True, choices=[(b'freelancer', b'freelancer'), (b'fulltime', b'fulltime'), (b'parttime', b'parttime'), (b'volunteer', b'volunteer')]),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='profit',
            field=models.CharField(default=b'free', max_length=10, null=True, choices=[(b'fixed', b'fixed'), (b'percentage', b'percentage'), (b'free', b'free')]),
        ),
        migrations.AddField(
            model_name='job',
            name='profit_value',
            field=models.DecimalField(default=0, null=True, max_digits=4, decimal_places=0),
        ),
        migrations.AddField(
            model_name='job',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=stdimage.models.StdImageField(null=True, upload_to=b'project_images', blank=True),
        ),
    ]
