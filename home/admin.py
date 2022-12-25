from django.contrib import admin

from foodsdrinks.models import Category, foodsdrinks, Images
from home.models import Setting


class foodsdrinksImageInline(admin.TabularInline):
    model= Images
    extra= 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['yemekismi','icecekismi']
    list_filter = ['icecekismi','yemekismi']

class foodsdrinksAdmin(admin.ModelAdmin):
    list_display = ['yemekismi', 'category', 'price'  , 'amount', 'image' ,'icecekismi']
    list_filter = ['icecekismi', 'yemekismi']
    inlines = [foodsdrinksImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['yemekismi'  , 'foodsdrinks', 'image']





# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(foodsdrinks,foodsdrinksAdmin)
admin.site.register(Setting)
