from rest_framework import serializers

from ajax_api.models.sensor import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'