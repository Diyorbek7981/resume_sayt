from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_display_links = ['name', 'email', 'subject']
    list_filter = ['name', 'subject']
    search_fields = ['name']


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'proect']
    list_display_links = ['name', 'phone', 'proect']

# @admin.register(HomeModel)
# class HomeModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'content']
#     list_display_links = ['title', 'content']

@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['year','title']
    list_display_links =  ['year','title']

@admin.register(SkilModel)
class SkilModelAdmin(admin.ModelAdmin):
    list_display = ['skil_name','percent']
    list_display_links = ['skil_name','percent']

@admin.register(ServisModel)
class ServisModelAdmin(admin.ModelAdmin):
    list_display = ['icon', 'profession']
    list_display_links = ['icon', 'profession']

