from django.db import models


class Client(models.Model):
    email = models.CharField(max_length=60)
    direction = models.CharField(max_length=80)
    telephone_number = models.PositiveBigIntegerField()
    telephone_ext = models.PositiveSmallIntegerField()
    avatar = models.ImageField(upload_to="avatars/")
    description = models.CharField(max_length=100)


class PaymentTime(models.Model):
    name = models.CharField(max_length=20)
    measure_type = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()


class Loan(models.Model):
    client = models.ManyToManyField("loans.Client", db_table='loans_clients')
    payment_time = models.OneToOneField("loans.PaymentTime", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    due_amount = models.DecimalField(max_digits=9, decimal_places=2)
    interests = models.DecimalField(max_digits=3, decimal_places=2)
    fee_type = models.PositiveSmallIntegerField()
    start = models.DateField()
    finish = models.DateField(null=True)


class Payment(models.Model):
    loan = models.ForeignKey("loans.Loan", on_delete=models.CASCADE)
    payment_time = models.ForeignKey("loans.PaymentTime", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    delay = models.PositiveSmallIntegerField()
    interests = models.DecimalField(max_digits=3, decimal_places=2)
    interests = models.PositiveSmallIntegerField()
