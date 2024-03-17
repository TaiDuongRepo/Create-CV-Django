from django.contrib import admin

from .models import Person, Skills

# Register your models here.
admin.site.register(Person)
admin.site.register(Skills)