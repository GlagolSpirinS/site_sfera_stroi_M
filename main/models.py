from django.db import models


class ObjectMain(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


class Managers(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
