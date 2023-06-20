from django.db import models
# Create your models here.

class Image(models.Model):
    image = models.ImageField()
    # image = models.FilePathField()

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)