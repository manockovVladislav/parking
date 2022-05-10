from time import time
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from statusParking.models import Parking
from .models import Person
import json
import random
import string

def registrations(request):
    return render(request, 'registrationTemplates/registrations.html')

def registrCheckClone(request):

    success = 'success'

    if request.POST:
        data_check_arr = request.POST.dict()
        name = data_check_arr.get('personLogin')

        try:
            nameBoolean = User.objects.get(username=name)
        except:
            nameBoolean = None

        print(nameBoolean)
        if nameBoolean:
            success = 'error'

    response_object = {
        'status': success
    }
    return HttpResponse(json.dumps(response_object), content_type="application/json")

def registrPerson(request):

    success = 'success'

    if request.POST:
        data_arr = request.POST.dict()

        login_person = data_arr.get('login')
        password_person = data_arr.get('password')
        
        user = User.objects.create_user(
            login_person,None, password_person)

        user_id = user.pk
        user_fio = data_arr.get('fioPerson')
        user_number_car = data_arr.get('number')

        person = Person()
        person.fio = user_fio
        person.number_car = user_number_car
        person.user_id = user_id
        person.save()

        # login(request, user)

    response_object = {
        'status': success
    }
    return HttpResponse(json.dumps(response_object), content_type="application/json")


def enterSite(request):

    status = 'error'
    if request.POST:
        data = request.POST.dict()
        status = 'success'
        user_number_car = data.get('numberCarUser')

        try:
            persons = Person.objects.get(number_car=user_number_car)
        except:
            persons = None

        try:
            parking_car_now = Parking.objects.get(number_car=user_number_car, time_end=None)
        except:
            parking_car_now = None
            
        
        if parking_car_now:
            status = 'car_parking_now'
            response_object = {
                'status': status
            }
            return HttpResponse(json.dumps(response_object), content_type="application/json")

        if persons:
            parking = Parking()
            parking.number_car = user_number_car
            slug_id = generate_alphanum_random_string(12)
            parking.slug_id = slug_id
            parking.user_id = persons.user_id
            parking.save()
            
        response_object = {
            'status': status,
            'slug_id': slug_id
        }
        return HttpResponse(json.dumps(response_object), content_type="application/json")
    response_object = {
        'status': status
    }
    return HttpResponse(json.dumps(response_object), content_type="application/json")


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(
        random.sample(letters_and_digits, length))
    return rand_string