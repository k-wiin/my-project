from django.db import models

# Create your models here.
class student(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    mobile_number = models.CharField(max_length=255)