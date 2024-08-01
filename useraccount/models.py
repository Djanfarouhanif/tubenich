from django.db import models
from django.contrib.auth.models import User,  AbstractUser
from django.conf import settings

userModels = User()
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    langage = models.CharField(max_length=90)
    profile_image = models.ImageField(default="" , uploade_to="profile")

    def __str__(self):
        return self.user.username