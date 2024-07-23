from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='index'),
    path('personal', views.personal, name='personal'),
    path('job', views.job, name='job'),

    path('place', views.place, name='place'),
    path('partner', views.partner, name='partner'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
]
