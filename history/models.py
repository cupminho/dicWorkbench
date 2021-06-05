from django.db import models

# Create your models here.

class History(models.Model):
    word = models.CharField(max_length=120, null=False)
    original = models.CharField(max_length=120, null=True, blank=True)
    alias = models.CharField(max_length=120, null=True, blank=True)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    area = models.CharField(max_length=120, null=True, blank=True)
    type = models.CharField(max_length=120, null=True, blank=True)
    time = models.CharField (max_length=120, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.word


