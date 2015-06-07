from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime
from general.models import Comment, Tag


class Idea(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    avg_rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tagged_ideas')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.owner.pk) + strftime("%Y%m%d%S%M%H"))
        super(Idea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class IdeaComment(Comment):
    # idea = models.ForeignKey(Idea)
    idea = models.ForeignKey(Idea, related_name='comments')

    def __unicode__(self):
        return self.text[:20] + ' - by:' + self.owner


class IdeaRating(models.Model):
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea, related_name='ratings')
    value = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return str(self.value)