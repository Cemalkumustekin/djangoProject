from telnetlib import STATUS


from django.db import models


class Setting(models.Model):
    STATUS=(
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver= models.CharField(max_length=20)
    smtepemail = models.CharField(max_length=1)
    smtppassword = models.CharField(max_length=150)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    aboutus = models.TextField()
    referances = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return str(self.aciklama)














