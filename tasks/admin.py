from django.contrib import admin
from .models import Category, Task

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
 
 
@admin.register(Task)
class Admin(admin.ModelAdmin):
    list_display = ['title','category', 'complited']
    search_fields = ['title', 'created_at', 'complited'] 
         
    