from rest_framework import serializers

from ajax_api.models.hub import Hubs


class HubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hubs
        fields = '__all__'
