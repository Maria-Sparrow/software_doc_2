from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, )
from rest_framework.response import Response

from ajax_api.models.hub import Hubs
from ajax_api.models.user import User
from ajax_api.serializers.hub_serializer import HubsSerializer
from ajax_api.serializers.user_serializer import UserSerializer


class HubsListCreateAPIView(ListCreateAPIView):
    serializer_class = HubsSerializer
    queryset = Hubs.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        user_id = int(request_data.pop('userId')[0])
        request_obj.user = User.objects.get(id=user_id)  # PROPERTY INJECTION
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class HubsRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HubsSerializer
    queryset = Hubs.objects.all()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()