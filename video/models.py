from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField() # L'URL YOUTUBE
    order = models.IntegerField() # L'ordre de la vidéo

    def __str__(self):
        return self.title


class VideoProgress(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} {'completed' if self.is_completed else 'Not Completed'}"
 
