from django.contrib import admin
from .models import *
# Register your models here.
# recipe < Content

class ContentInline(admin.TabularInline) : 
    model = Content

class RecipeAdmin(admin.ModelAdmin):
    inlines =[ContentInline, ]

class ContentAdmin(admin.ModelAdmin):
    list_display =['title']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Content, ContentAdmin)