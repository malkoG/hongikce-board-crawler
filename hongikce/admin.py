from django.contrib import admin

from .models import Category, Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_number' ,'title', 'description', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('board_type', 'board_url')