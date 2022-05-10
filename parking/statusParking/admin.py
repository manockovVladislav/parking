from django.contrib import admin


# Register your models here.

from .models import Parking

class ParkingAdmin(admin.ModelAdmin):
    list_display = ('number_car', 'price','time_start', 'time_end', 'slug_id')
    search_fields = ('number_car', 'price')

admin.site.register(Parking, ParkingAdmin)