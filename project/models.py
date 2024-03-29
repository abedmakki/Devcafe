from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime


class Project(models.Model):
    PM = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    plan = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='project_images', blank=True, null=True)
    # slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title + str(self.PM.pk) + strftime("%Y%m%d%S%M%H"))
        # self.PM = request.user
        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    project = models.ForeignKey(Project, related_name='posts')
    text = models.TextField(blank = True)

    def __unicode__(self):
        return self.text


class Contributor(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project, related_name='contributors')
    is_pm = models.BooleanField(default=False)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.user.username + ', Contributor to: ' + self.project.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    issued_to = models.ForeignKey(Contributor, related_name='tasks')
    project = models.ForeignKey(Project, related_name='project_tasks')
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title + ', for: ' + str(self.project.title) + ', ' + str(self.is_done) 


class Job(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	issued_to = models.ForeignKey(User, related_name='jobs')
	project = models.ForeignKey(Project, related_name='project_jobs')
	is_taken = models.BooleanField(default=False)
