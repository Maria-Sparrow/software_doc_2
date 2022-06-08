from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, )

from ajax_api.models.hub import Hubs
from ajax_api.serializers.hub_serializer import HubsSerializer


class HubsListCreateAPIView(ListCreateAPIView):
    serializer_class = HubsSerializer
    queryset = Hubs.objects.all()


class HubsRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HubsSerializer
    queryset = Hubs.objects.all()
