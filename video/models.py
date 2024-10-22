from django.db import models


class Youtubeur(models.Model):
    username = models.CharField(max_length=255)
    follower = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

    def __srt__(self):
        return self.username
#Video de plus d'une heure
class Video_long_format(models.Model):
    accountUser  = models.ForeignKey(Youtubeur, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    videoId = models.URLField()
    thumbnails = models.URLField()
    description = models.TextField()
    programingLangage = models.CharField(max_length=100)
    

    def __str__(self):
        return self.accountUser.username

#Video de petit formt moin d' une heure
class Video_petit_format(models.Model):
    accountUser = models.ForeignKey(Youtubeur, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    videoId = models.URLField()
    thumbnails = models.URLField()
    description = models.TextField()
    programingLangage = models.CharField(max_length=100)
    #Voire si c'est quelle basse faut utiliser variable ou condition etc...abs
    # levle = models.CharField(max_length=100)

    def __str__(self):
        return self.accountUser.username

#Les video en forme de formation
class Video_list(models.Model):
    account_user = models.ForeignKey(Youtubeur, on_delete=models.CASCADE)
    list_video = models.URLField()
    programmingLangage = models.CharField(max_length=100)

    def __str__(self):
        return self.accountUser.username

