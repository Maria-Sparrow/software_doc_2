from django.db import models

from ajax_api.models.user import User


class Hubs(models.Model):
    type_hub = models.CharField(max_length=30, null=True)
    features = models.CharField(max_length=40, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"({self.id})Email:{self.features}"
