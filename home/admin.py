from django.contrib import admin

from foodsdrinks.models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['yemekismi', 'icecekismi']
    list_filter = ['icecekismi','yemekismi']


# Register your models here.
admin.site.register(Category,CategoryAdmin)
