from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Thetare(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
         return '%s -- %s ' % (self.name, self.location)

    def get_absolute_url(self):
       return reverse('basic:th_detail',kwargs={'pk':self.pk})

class Movie(models.Model):
    name=models.CharField(max_length=20)
    thetare=models.ForeignKey(Thetare,on_delete=models.CASCADE,related_name='movies')
    language=models.CharField(max_length=20)

    def __str__(self):
        return self.name
