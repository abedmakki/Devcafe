from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime
from general.models import Tag, Comment


class App(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='market_images', blank=True)
    description = models.CharField(max_length=500)
    avg_rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tagged_apps')
    price = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + str(self.owner.pk) + strftime("%Y%m%d%S%M%H"))
        super(App, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class AppRating(models.Model):
    owner = models.ForeignKey(User)
    app = models.ForeignKey(App, related_name='ratings')
    value = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return str(self.value)


class AppComment(Comment):
    app = models.ForeignKey(App, related_name='comments')
    def __unicode__(self):
        return self.text[:20] + ' - by:' + self.owner  