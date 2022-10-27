from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    rol = serializers.PositiveSmallIntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=256)
    avatar = serializers.ImageField(upload_to="avatars/")
    description = serializers.CharField(max_length=100)
