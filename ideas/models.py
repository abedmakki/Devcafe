from django.db import models
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Idea(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
