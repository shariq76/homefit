from django.contrib import admin
from .models import *


# Register your models here.
class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'stock', 'price']

admin.site.register(Category, CatAdmin)
admin.site.register(Products, ProdAdmin)
