from telnetlib import STATUS
from django.forms import ModelForm,TextInput, Textarea

from django.db import models


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
    smtepemail = models.CharField(max_length=50)
    smtppassword = models.CharField(max_length=150)
    smtpport = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=150)
    instagram = models.CharField(blank=True,max_length=150)
    twitter = models.CharField(blank=True,max_length=150)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    referances = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return str(self.title)

class ContactFormMessage(models.Model):
    STATUS = (
        ('New' , 'New'),
        ('Read' , 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True, max_length=20)
    email= models.CharField(blank=True, max_length=50)
    subject= models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField( max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


    def _str_(self):
        return str(self.name)


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name'   : TextInput(attrs={'class': 'form-control', 'placeholder':'Name & Surname'}),
            'subject'   : TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'message': TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Your Message','rows':'5'}),
        }
