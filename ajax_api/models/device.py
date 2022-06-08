from django.db import models

from ajax_api.models.user import User


class Device(models.Model):
    name = models.CharField(max_length=30, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
