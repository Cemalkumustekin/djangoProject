from django.db import models

from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    yemekismi = models.CharField(max_length=30)
    icecekismi = models.CharField(max_length=30)
    aciklama = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    parent=models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.yemekismi





class foodsdrinks(models.Model):
    STATUS = (
        ('True' , 'Evet'),
        ('False' , 'Hayır'),
    )
    category= models.ForeignKey(Category, on_delete=models.CASCADE)#relation with category table
    yemekismi = models.CharField(max_length=30)
    icecekismi = models.CharField(max_length=30)
    aciklama = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount=models.IntegerField()
    detail=RichTextUploadingField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Images(models.Model):
    foodsrinks=models.ForeignKey(foodsdrinks,on_delete=models.CASCADE)
    yemekismi = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

