from django.contrib import admin
from .models import Person, Driver

# Register your models here.
# admin.site.register(Person)
# admin.site.register(Driver)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car', 'finish_time']