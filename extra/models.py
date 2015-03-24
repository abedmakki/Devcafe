from django.db import models
from django.contrib.auth import User


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1500)
    # typeflag is set as 0 for Idea Comments, 1 for (Project) Post Comments
    typeflag = models.IntegerField()
    # TODO: Add Post foreign key when Post model is implemented
