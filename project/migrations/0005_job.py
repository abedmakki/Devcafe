# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('is_taken', models.BooleanField(default=False)),
                ('issued_to', models.ForeignKey(related_name='jobs', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name='project_jobs', to='project.Project')),
            ],
        ),
    ]
