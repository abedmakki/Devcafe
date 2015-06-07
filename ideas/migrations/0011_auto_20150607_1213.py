# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0010_auto_20150607_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='idea',
            name='rating',
        ),
        migrations.AddField(
            model_name='idearating',
            name='idea',
            field=models.ForeignKey(to='ideas.Idea'),
        ),
        migrations.AddField(
            model_name='idearating',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
