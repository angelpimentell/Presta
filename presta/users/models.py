from django.db import models


class User(models.Model):
    rol = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to="avatars/")
    description = models.CharField(max_length=100)
