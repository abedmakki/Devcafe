from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime


class Project(models.Model):
	PM = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	plan = models.TextField(blank=True)
	logo = models.ImageField(upload_to='project_images', blank=True, null=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title + str(self.PM.pk) + strftime("%Y%m%d%S%M%H"))
		# self.PM = request.user
		super(Project, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
