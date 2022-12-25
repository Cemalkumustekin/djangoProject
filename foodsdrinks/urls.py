from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),

]