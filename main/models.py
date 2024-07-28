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
    opisaniye = models.TextField(default='SOME STRING')
    usloviya = models.TextField()
    trebovaniya = models.TextField(default='SOME STRING')
    obyazannosti = models.TextField(default='SOME STRING')
    mesto_raboty = models.CharField(max_length=100, default='SOME STRING')
