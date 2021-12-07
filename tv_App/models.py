from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    release = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
