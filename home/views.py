from django.shortcuts import render

from home.models import Setting, ContactFormu, ContactFormMessage


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'home'}
    return render(request, 'index.html',context)
def about(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'about'}
    return render(request, 'about.html',context)
def book(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'book'}
    return render(request, 'book.html',context)

def menu(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'menu'}
    return render(request, 'menu.html',context)

def index(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'index'}
    return render(request, 'index.html',context)

