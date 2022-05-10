from django.urls import path
from .views import *

urlpatterns = [
    path('', registrations),
    path('registrPerson/', registrPerson),
    path('registrCheckClone/', registrCheckClone),
    path('enterSite/', enterSite),
]