from django.db import models

# Create your models here.

class Standard(models.Model):
    word = models.CharField(max_length=120, null=False)
    original = models.CharField(max_length=120, null=False)
    definition = models.TextField()

