from rest_framework import serializers

from settings.models.setting import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
