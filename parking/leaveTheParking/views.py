from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from statusParking.models import Parking
from datetime import *
import math
import json


def leaveTheParking(request):
    context = {
        'all': None,
    }
    return render(request, 'leaveTheParkingTemplates/leaveTheParking.html', context)

def payParking(request):
    status = "error"

    if request.POST:
        data = request.POST.dict()
        status = 'success'
        user_number_talon = data.get('numberTalon')
        print(data)
        try:
            current_parking = Parking.objects.get(slug_id=user_number_talon, time_end=None)
        except:
            current_parking = None
        
        print(current_parking)
        if current_parking:
            today = datetime.now(timezone.utc)
            current_parking.time_end  = today
            delta = today - current_parking.time_start
            minutes = delta.seconds / 60
            
            current_parking.price = int(minutes)
            current_parking.save()

            response_object = {
                'status': status,
                'price': int(minutes)
            }
            return HttpResponse(json.dumps(response_object), content_type="application/json")
