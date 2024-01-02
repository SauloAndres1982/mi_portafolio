from django.contrib import admin
from . models import About, Skills
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(About, ProjectAdmin)
admin.site.register(Skills)