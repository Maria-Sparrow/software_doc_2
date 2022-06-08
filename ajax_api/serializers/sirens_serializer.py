from rest_framework import serializers

from ajax_api.models.sirens import Sirens


class SirenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sirens
        fields = '__all__'