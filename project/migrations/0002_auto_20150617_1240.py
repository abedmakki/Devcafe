# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_pm', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=50)),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='project.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='contributer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contributer',
            name='project',
        ),
        migrations.DeleteModel(
            name='Contributer',
        ),
    ]
