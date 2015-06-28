from django.db import models
from django.contrib.auth.models import User
from time import strftime
from general.models import Comment, Tag


class Idea(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.PositiveSmallIntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tagged_ideas')

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


class IdeaLike(models.Model):
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)

    def save(self, *args, **kwargs):
        super(IdeaLike, self).save(*args, **kwargs)
        idea_obj = self.idea
        idea_obj.likes = idea_obj.idealike_set.count()
        idea_obj.save()

    def delete(self, *args, **kwargs):
        super(IdeaLike, self).delete(*args, **kwargs)
        idea_obj = self.idea
        idea_obj.likes = idea_obj.idealike_set.count()
        idea_obj.save()