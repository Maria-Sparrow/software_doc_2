import csv

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from ajax_api.models.user import User
from ajax_api.serializers.user_serializer import UserSerializer


class UploadDataCSVFile(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        file = request.data.get('user_data')
        file_rows = [row.decode("utf-8") for row in file]
        reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        for user in reader:
            if user:
                request_data = format_data(user)
                create_request_record(request_data)  # METHOD INJECTION
        return Response('Uploaded', status=status.HTTP_201_CREATED)


def format_data(user):
    request_data = {"id": user.pop(0),
                    "full_name": user.pop(0),
                    "email": user.pop(0),
                    "password": user.pop(0)}

    return request_data


def create_request_record(request_data):
    user_serializer = UserSerializer(data=request_data)
    user_serializer.is_valid(raise_exception=True)
    request_obj = user_serializer.save()

    request_obj.save()

    return True
