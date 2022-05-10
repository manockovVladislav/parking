from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
import json


def statusParking(request):

    # queryset = Book.objects.all().order_by('id').select_related(
    #     'id_author').select_related('id_genre')

    # genre = Genre.objects.all().order_by('id')
    # author = Author.objects.all().order_by('id')
    # comment = Comment.objects.all().order_by('id')
    # # print(queryset.values())
    context = {
        'all_books': None,
        'all_genre': None,
        'all_author': None,
        'all_comment': None,
    }
    return render(request, 'statusParkingTemplates/statusParking.html', context)

def getParkingNumber(request, slug_id):

    context = {
        'slug_id': slug_id,
    }
    return render(request, 'statusParkingTemplates/getParkingNumber.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    return redirect('/')