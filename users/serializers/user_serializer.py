from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    rol = serializers.IntegerField(min_value=0)
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=256)
    avatar = serializers.ImageField()
    description = serializers.CharField(max_length=100)
