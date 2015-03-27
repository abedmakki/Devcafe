from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
	PM = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	plan = models.TextField()
	logo = models.ImageField(upload_to='projects_images', blank=True)
	slug = models.SlugField(unidue=True)

	def __unicode__(self):
        return self.title