from django.contrib import admin
from project.models import Project

# Register your models here
# Add in this class to customized the Admin Interface
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Project, ProjectAdmin)
#admin.site.register(Project)