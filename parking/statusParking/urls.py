from django.urls import path
from .views import *

urlpatterns = [
    path('', statusParking, name='statusParking'),
    path('getParkingNumber/<slug:slug_id>/', getParkingNumber),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]