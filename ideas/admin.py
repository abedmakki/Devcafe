from django.contrib import admin
from ideas.models import Idea, IdeaRating

# Register your models here
admin.site.register(Idea)
admin.site.register(IdeaRating)