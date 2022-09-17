from django.db import models


class PaymentTime(models.Model):
    name = models.CharField(max_length=20)
    measure_type = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.paymenttime_text
