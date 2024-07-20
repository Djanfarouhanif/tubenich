from django.db import models

# Create your models here.

class Tube(models.Model):
    title = models.CharField(max_length=255)
    video = models.URLField()

    def __str__(self):
        return self.title
