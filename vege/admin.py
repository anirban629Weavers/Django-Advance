from django.contrib import admin
from .models import Recipe

# Register your models here.
# admin.site.register(Recipe)

@admin.register(Recipe)
class Student(admin.ModelAdmin):
    list_display = ("recipe_name", "recipe_image")
    list_display_links= ("recipe_name",)