# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0008_app_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_id', models.CharField(max_length=30)),
                ('home_no', models.CharField(max_length=11)),
                ('phone_no', models.CharField(max_length=11)),
                ('delivery_address', models.CharField(max_length=300)),
                ('delivery_time', models.DateTimeField()),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='transactions',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apptransaction',
            name='app',
            field=models.ForeignKey(to='market.App'),
        ),
        migrations.AddField(
            model_name='apptransaction',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
