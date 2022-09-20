from django.db import models


class Client(models.Model):
    email = models.CharField(max_length=60)
    direction = models.CharField(max_length=80)
    telephone_number = models.PositiveBigIntegerField()
    telephone_ext = models.PositiveSmallIntegerField()
    avatar = models.ImageField(upload_to="avatars/")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.email


