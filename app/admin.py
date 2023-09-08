from django.contrib import admin
from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'number_of_solved', 'ball', 'created')
    list_display_links = ('id', 'user', 'number_of_solved')
