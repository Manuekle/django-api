from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'createdAt']
    list_filter = ['createdAt']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Product, ProductAdmin)