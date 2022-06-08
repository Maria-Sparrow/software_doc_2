from django.db import models
from ajax_api.models.hub import Hubs


class Sensor(models.Model):
    classification = models.CharField(max_length=30, null=True)
    sensitiveElement = models.CharField(max_length=30, null=True)
    typeSensor = models.CharField(max_length=200, null=True)
    batteryLife = models.CharField(max_length=30, null=True)
    hubId = models.ForeignKey(Hubs, on_delete=models.CASCADE)


    def call_product(self):
        return f"You make request to ajax server " \
               f"Product by order:{self.hubId} as {self.classification} {self.sensitiveElement}"


    def __str__(self):
        return f"({self.id})Order:{self.hubId}"


    def set_hub_id(self, data):
        self.hubId = data
        return True
