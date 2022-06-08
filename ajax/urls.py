"""ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ajax_api.views.csv_view import UploadDataCSVFile
from ajax_api.views.device_view import DeviceListCreateAPIView, DeviceRetrieveUpdateAPIView
from ajax_api.views.hub_view import HubsListCreateAPIView, HubsRetrieveUpdateAPIView
from ajax_api.views.sensor_view import SensorListCreateAPIView, SensorRetrieveUpdateAPIView
from ajax_api.views.sirens_view import SirensListCreateAPIView, SirensRetrieveUpdateAPIView
from ajax_api.views.user_view import UserListCreateAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hubs/', HubsListCreateAPIView.as_view()),
    path('hubs/<int:pk>/', HubsRetrieveUpdateAPIView.as_view()),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),

    path('sirens/', SirensListCreateAPIView.as_view()),
    path('sirens/<int:pk>/', SirensRetrieveUpdateAPIView.as_view()),

    path('sensor/', SensorListCreateAPIView.as_view()),
    path('sensor/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),

    path('device/', DeviceListCreateAPIView.as_view()),
    path('device/<int:pk>/', DeviceRetrieveUpdateAPIView.as_view()),

    path('test_csv/', UploadDataCSVFile.as_view()),
]
