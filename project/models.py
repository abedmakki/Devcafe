from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField


class Project(models.Model):
    PM = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    plan = models.TextField(blank=True, null=True)
    #logo = models.ImageField(upload_to='project_images', blank=True, null=True)
    logo = StdImageField(upload_to='project_images', blank=True, variations={'thumbnail': (100, 75)})
    timestamp = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    project = models.ForeignKey(Project, related_name='posts')
    text = models.TextField(blank=True)

    def __unicode__(self):
        return self.text


class Contributor(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project, related_name='contributors')
    is_pm = models.BooleanField(default=False)
    # position = models.CharField(max_length=100, blank=True, null=True)
    job = models.OneToOneField('Job', blank=True, null=True)

    def __unicode__(self):
        return self.user.username + ', Contributor to: ' + self.project.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    issued_to = models.ForeignKey(Contributor, related_name='tasks')
    project = models.ForeignKey(Project, related_name='project_tasks')
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title + ', for: ' + \
            self.project.title + ', ' + str(self.is_done)


class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    issued_to = models.ForeignKey(User, null=True, blank=True)
    project = models.ForeignKey(Project, related_name='jobs')
    is_taken = models.BooleanField(default=False)
    time_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)

    freelancer = 'freelancer';fulltime = 'fulltime';parttime = 'parttime';volunteer = 'volunteer'
    typeChoices = ((freelancer, 'freelancer'),(fulltime, 'fulltime'),(parttime, 'parttime'),(volunteer, 'volunteer'))

    job_type = models.CharField(choices=typeChoices , default=freelancer , max_length=10)

    fixed = 'fixed'; percentage = 'percentage'; free='free'
    profit_choices = ((fixed, 'fixed'),(percentage, 'percentage'),(free, 'free'))

    profit = models.CharField(choices=profit_choices , default=free ,max_length=10)
    profit_value = models.DecimalField(max_digits=4 , decimal_places=0 ,default=0)

    def __unicode__(self):
        return self.project.title + ', Announced For: ' + self.name


class Request(models.Model):
    owner = models.ForeignKey(User)
    job = models.ForeignKey(Job, related_name='job_requests', blank=True, null=True)

    def __unicode__(self):
        return self.owner.username + ', Applied for: ' + self.job.name
