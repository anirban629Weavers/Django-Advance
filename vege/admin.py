from django.contrib import admin
from .models import Recipe,Student,StudentID,Department

# Register your models here.
# admin.site.register(Recipe)

@admin.register(Recipe)
class RecipeModel(admin.ModelAdmin):
    list_display = ("recipe_name", "recipe_image")
    list_display_links= ("recipe_name",)
    
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Department)