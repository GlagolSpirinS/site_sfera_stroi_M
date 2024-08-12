from django.contrib import admin
from django.urls import path
from djangoProject import settings
from main import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('personal', views.personal, name='personal'),
    path('job', views.job, name='job'),
    path('company', views.company, name='company'),
    path('place', views.place, name='place'),
    path('partner', views.partner, name='partner'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
