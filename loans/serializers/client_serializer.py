from rest_framework import serializers

from loans.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
