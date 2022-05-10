from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    fio = models.CharField(max_length=255)
    number_car = models.CharField(max_length=12, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio
