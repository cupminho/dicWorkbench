from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=120, null=False)
    author = models.CharField(max_length=20, null=False)
    file = models.FileField(upload_to='text/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} / {self.title} / {self.author}'
