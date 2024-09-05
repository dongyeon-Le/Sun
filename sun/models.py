from django.db import models

class Register(models.Model):
    UserId = models.CharField(max_length=50)
    UserPassword = models.CharField(max_length=50)
    UserName = models.CharField(max_length=10)
    UserEmail = models.CharField(max_length=50)
    UserPhone = models.CharField(max_length=50)
    UserAddress = models.CharField(max_length=50)