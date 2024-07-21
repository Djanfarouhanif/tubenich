from django.db import models

# Create your models here.

class Youtubeur(models.Model):
    username = models.CharField(max_length=255)
    view = models.CharField(max_length=50)
    follower_number = models.CharField(max_length=50)

    def __srt__(self):
        return self.username
#Video de plus d'une heure
class Video_long_format(models.Model):
    account_user  = models.ForeignKey(Youtubeur, one_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    video_long_format = models.URLField()
    thumbnails = models.URLField()
    descriptipn = models.TextField()
    programing_langage = models.CharField(max_length=100)

    def __str__(self):
        return self.account_user.username

#Video de petit formt moin d' une heure
class Video_petit_format(models.Model):
    account_user = models.ForeignKey(Youtubeur, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.URLField()
    thumbnails = models.URLField()
    description = models.TextField()
    programing_langage = models.CharField(max_length=100)

    def __str__(self):
        return self.account_user.username

#Les video en forme de formation
class Video_list(models.Model):
    account_user = models.ForeignKey(Youtubeur, on_delete=models.CASCADE)
    list_video = models.URLField()
    programming_langage = models.CharFeild(max_length=100)

    def __str__(self):
        return self.account_user.username

