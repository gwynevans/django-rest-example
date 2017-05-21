from django.contrib import admin

# Register your models here.
from .models import Task, Location

admin.site.register(Location)
admin.site.register(Task)