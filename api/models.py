from django.db import models
# Create your models here.

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    compression_level = models.IntegerField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)