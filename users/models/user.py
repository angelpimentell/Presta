from django.db import models


class User(models.Model):
    rol = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to="avatars/", null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
