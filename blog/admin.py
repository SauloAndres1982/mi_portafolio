from django.contrib import admin

from . models import Blog, Opinion

# Register your models here.

admin.site.register(Blog)
admin.site.register(Opinion)