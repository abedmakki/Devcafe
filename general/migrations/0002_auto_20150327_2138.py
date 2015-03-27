# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=1500)),
                ('typeflag', models.IntegerField()),
                ('idea', models.ForeignKey(to='ideas.Idea')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 3, 27, 19, 38, 30, 198674, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
