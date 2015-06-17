# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150617_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('is_done', models.BooleanField(default=False)),
                ('issued_to', models.ForeignKey(related_name='tasks', to='project.Contributor')),
                ('project', models.ForeignKey(related_name='project_tasks', to='project.Project')),
            ],
        ),
    ]
