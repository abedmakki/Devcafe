from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    birth_date = models.DateField(blank=True)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=400, null=True)
    slug = models.SlugField(unique=True)

    # Override the __unicode__() method to return out something meaningful!
    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username
