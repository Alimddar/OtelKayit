from django.shortcuts import render,redirect

# Api için JsonResponse
from django.http import JsonResponse

# ORM Modellerimiz
from OtelApp.models import *

# Create your views here.

def guestregister(request,odaId):

    room = OtelOda.objects.filter(id = odaId).first()
    
    if request.method == 'POST':
        firstname = request.POST.get('first')
        lastname = request.POST.get('last')
        nationality = request.POST.get('uyruk')
        tcid = request.POST.get('tc')
        passport = request.POST.get('passaport')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        KonukBilgileri.objects.create(room = room, first_name = firstname, last_name = lastname, nationality = nationality, guest_tc = tcid, guest_id = passport, checkin_date = checkin, checkout_date = checkout)
        room.roomisempty = True
        room.save()
        return redirect('odadetay', odaId)
    else:
        return redirect('home')

