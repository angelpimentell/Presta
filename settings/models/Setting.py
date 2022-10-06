from django.db import models


class Setting(models.Model):
    company_name = models.CharField(max_length=20)
    company_avatar = models.ImageField(upload_to="avatar/")
    default_currency = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.setting_text
