from django.db import models
from django.contrib.auth.models import User
from ideas.models import Idea


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()


class IdeaComment(models.Model):
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1500)
    # typeflag is set as 0 for Idea Comments, 1 for (Project) Post Comments
    typeflag = models.IntegerField()
    # TODO: Add Post foreign key when Post model is implemented
