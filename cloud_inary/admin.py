from django.contrib import admin

# Register your models here.
from .models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['image', 'title']
    list_display_links = ['image', 'title']
