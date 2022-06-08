from rest_framework import serializers

from ajax_api.models.device import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
