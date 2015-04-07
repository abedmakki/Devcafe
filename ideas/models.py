from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime


class Idea(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.owner.pk) + strftime("%Y%m%d%S%M%H"))
        super(Idea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
