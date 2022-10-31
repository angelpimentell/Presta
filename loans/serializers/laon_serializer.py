from rest_framework import serializers

from loans.models.loan import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
