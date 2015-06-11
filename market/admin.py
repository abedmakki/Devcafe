from django.contrib import admin
from market.models import App, AppRating, AppTransaction

# Register your models here
admin.site.register(App)
admin.site.register(AppRating)
admin.site.register(AppTransaction)