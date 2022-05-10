from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Parking(models.Model):
    price = models.CharField(max_length=255, null=True)
    number_car = models.CharField(max_length=12, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug_id = models.SlugField(
        max_length=12, db_index=True, null=True)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(null=True)

    def __str__(self):
        return self.number_car