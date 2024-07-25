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
    old_work = models.CharField(max_length=100)
    busyness = models.CharField(max_length=100)
    chart = models.CharField(max_length=100)
    remote_work = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False)
    underworking = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False)
    table = models.TextField(max_length=255)
    description = models.TextField()
