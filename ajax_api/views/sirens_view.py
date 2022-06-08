from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, )

from ajax_api.models.sirens import Sirens
from ajax_api.serializers.sirens_serializer import SirenSerializer


class SirensListCreateAPIView(ListCreateAPIView):
    serializer_class = SirenSerializer
    queryset = Sirens.objects.all()


class SirensRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SirenSerializer
    queryset = Sirens.objects.all()