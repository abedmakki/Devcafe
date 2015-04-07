# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0002_auto_20150327_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
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
            model_name='ideacomment',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='ideacomment',
            name='owner',
        ),
        migrations.DeleteModel(
            name='IdeaComment',
        ),
    ]
