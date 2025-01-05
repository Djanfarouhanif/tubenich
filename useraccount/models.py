from django.db import models
from django.contrib.auth.models import User,  AbstractUser
from django.conf import settings

userModels = User()
#user c'est le models par default de django
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(default=None , upload_to="profile")

    def __str__(self):
        return self.user.username