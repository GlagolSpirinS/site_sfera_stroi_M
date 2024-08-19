from django.contrib import admin
from django.urls import path
from djangoProject import settings
from main import views
from django.conf.urls.static import static
from django.urls import include, re_path
from django.contrib.auth import settings
from django.views.static import serve

from main.views import object_list, apply_for_job

urlpatterns = [
    path('', views.home, name='index'),
    path('personal', views.personal, name='personal'),
    path('job', views.job, name='job'),
    path('company', views.company, name='company'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('place', views.place, name='place'),
    path('buyer', views.buyer, name='buyer'),
    path('partner', views.partner, name='partner'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('objects/', object_list, name='object_list'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('object/<int:id>/', views.object_detail, name='object_detail'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.custom_404'
