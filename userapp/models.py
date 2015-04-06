from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import strftime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    birth_date = models.DateField(blank=True , null=True)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=400, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.user.username + str(self.user.pk) + strftime("%Y%m%d%S%M%H"))
                super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username
