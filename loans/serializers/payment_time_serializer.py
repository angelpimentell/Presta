from rest_framework import serializers

from loans.models.payment_time import PaymentTime


class PaymentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTime
