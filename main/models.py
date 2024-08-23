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
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_ready = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image2 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image3 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image4 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image5 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image6 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image7 = models.ImageField(upload_to='objectImg/', blank=True, null=True)
    image8 = models.ImageField(upload_to='objectImg/', blank=True, null=True)


class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partnerImg/')

class applicant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    description = models.TextField()
    job_name = models.CharField(max_length=100, default='SOME STRING')
