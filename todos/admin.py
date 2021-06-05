from django.contrib import admin

# Register your models here.

from .models import Todo, Option

admin.site.register(Todo)
admin.site.register(Option)
