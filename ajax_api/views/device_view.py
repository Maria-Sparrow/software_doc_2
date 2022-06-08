from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, )

from ajax_api.models.device import Device
from ajax_api.serializers.device_serializer import DeviceSerializer


class DeviceListCreateAPIView(ListCreateAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()