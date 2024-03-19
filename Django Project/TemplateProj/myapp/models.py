from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()