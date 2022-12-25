from django.db import models
from django.db.models.fields.files import ImageFieldFile



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

