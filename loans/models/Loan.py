from django.db import models


class Loan(models.Model):
    client = models.ManyToManyField("loans.Client", db_table='loans_clients')
    payment_time = models.OneToOneField("loans.PaymentTime", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2)
    due_amount = models.DecimalField(max_digits=11, decimal_places=2)
    interests = models.DecimalField(max_digits=5, decimal_places=2)
    fee_type = models.PositiveSmallIntegerField()
    start = models.DateField()
    finish = models.DateField(null=True)

    def __str__(self):
        return self.client
