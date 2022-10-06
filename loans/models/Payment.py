from django.db import models


class Payment(models.Model):
    loan = models.ForeignKey("loans.Loan", on_delete=models.CASCADE)
    payment_time = models.ForeignKey("loans.PaymentTime", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateField()
    delay = models.PositiveSmallIntegerField()
    interests = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.loan
