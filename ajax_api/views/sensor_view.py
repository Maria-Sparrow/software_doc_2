from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, )
from rest_framework.response import Response

from ajax_api.models.hub import Hubs
from ajax_api.models.sensor import Sensor
from ajax_api.serializers.sensor_serializer import SensorSerializer


class SensorListCreateAPIView(ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        hub_id = int(request_data.pop('hubId')[0])
        print(hub_id)
        hub_obj = Hubs.objects.get(id=hub_id)
        request_obj.set_hub_id(hub_obj)  # INTERFACE INJECTION
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class SensorRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
