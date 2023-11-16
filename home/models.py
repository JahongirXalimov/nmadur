from django.db import models

class Phone(models.Model):
   nomi = models.CharField(max_length=100)
   rangi = models.CharField(max_length=100)
   narxi = models.CharField(max_length=100)

   def __str__(self):
       return self.nomi
