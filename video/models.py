from django.db import models

# Create your models here.

class Video_long_format(models.Model):
    title = models.CharField(max_length=255)
    video_long_format = models.URLField()
    minature = models.URLField()
    

    def __str__(self):
        return self.title
class Video_petit_format(models.Model):
    title = models.CharField(max_length=255)
    video = models.URLField()
    minature = models.URLField()

    def __str__(self):
        return self.title
