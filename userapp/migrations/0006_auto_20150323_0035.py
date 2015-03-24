# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0005_auto_20150322_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('country', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
