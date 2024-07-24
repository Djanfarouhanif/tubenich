from django.db import models
from django.contrib.auth.models import User

userModels = User()

class Student(models.Model):
    user = models.Model(userModels, on_delete=models.CASCADE)
    langage = models.CharField(max_length=90)

    def __str__(self):
        return self.user.username