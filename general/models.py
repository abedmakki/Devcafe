from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    owner = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1500)

    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
