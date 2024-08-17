from django.db import models
class ObjectMain(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
class Managers(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
class Jobs(models.Model):
    name = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    trebuyemyy_opyt_raboty = models.CharField(max_length=100)
    zanyatost = models.CharField(max_length=100)
    grafik = models.CharField(max_length=100)
    udalonnayarabota = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False)
    kratkoye_opisaniye = models.TextField(max_length=255)
    usloviya = models.TextField()
    trebovaniya = models.TextField(default='SOME STRING')
    obyazannosti = models.TextField(default='SOME STRING')
    mesto_raboty = models.CharField(max_length=100, default='SOME STRING')

class Object(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='objectImg/')
    description = models.TextField()
    is_ready = models.BooleanField(default=False)  # Новое булевое поле

class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partnerImg/')

class applicant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    description = models.TextField()
    job_name = models.CharField(max_length=100, default='SOME STRING')
