from django.contrib import admin
from .models import *


# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ToDo._meta.fields if field.name != 'user']


admin.site.register(ToDo)