from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=80, null=False)
    password = models.CharField(max_length=40, null=False)

    def __str__(self):
        return f"({self.id})Email:{self.email}"


