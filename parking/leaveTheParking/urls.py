from django.urls import path
from .views import *

urlpatterns = [
    path('', leaveTheParking, name='leaveTheParking'),
    path('payParking/', payParking),
]