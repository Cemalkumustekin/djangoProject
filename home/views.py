from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render

from home.models import Setting, ContactFormu, ContactFormMessage


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'index'}
    return render(request, 'index.html',context)
def about(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'about'}
    return render(request, 'about.html',context)


def menu(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'menu'}
    return render(request, 'menu.html',context)



def book(request):
    setting = Setting.objects.get(pk=1)
    context={'setting': setting, 'page':'book'}
    return render(request, 'book.html',context)






def book(request):

    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile baglanti kur
            data.name = form.cleaned_data['name']  # formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # verirabanina kaydet
            messages.success(request, "Mesajiniz basari ile gönderilmistir. Tesekkür Ederiz")
            return HttpResponseRedirect('/book')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'book.html', context)




