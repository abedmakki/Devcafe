from django.contrib import admin
from ideas.models import Idea, IdeaRating, IdeaLike

# Register your models here
admin.site.register(Idea)
admin.site.register(IdeaRating)
admin.site.register(IdeaLike)