from django.shortcuts import render,redirect


# Django user modelini al
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Kendi Modellerimizi Dahil Edelim
from .models import *

# Single MiddleWare
from django.contrib.auth.decorators import login_required

# Message
from django.contrib import messages


# Form.py çek
from .form import *



# Create your views here.
def index(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            giris = authenticate(request, username = username, password = password)

            if giris is not None:
                login(request,giris)
                # Message Geç
                messages.success(request,"Giriş Başarılı")
                # Yönlendir
                return redirect('oteldashboard')
            else:
                messages.error(request,'Kullanıcı Adı veya Şifre Hatalı!')
                return redirect('home')
        else:
            messages.warning(request,"Boş Alanları Doldurunuz.")
            return redirect('home')

    return render(request, "index.html")



@login_required(login_url="home")
def otel(request):

    context = {}

    odalar = OtelOda.objects.filter(otel__owner = request.user).all()
    
    context['odalar'] = odalar

    return render(request, "otel.html", context)


@login_required(login_url="home")
def blokaj(request):

    return render(request, "blokaj.html")


@login_required(login_url="home")
def muhasebe(request):
    
    return render(request, "muhasebe.html")


@login_required(login_url="home")
def detailroom(request,odaId):

    context = {}

    room = OtelOda.objects.filter(id = odaId).first()
    context['odalar'] = room

    # Formu fronta yollayacağız
    roomForm = UpdateRoomDetail(instance = room)
    context['form'] = roomForm

    musteri = KonukBilgileri.objects.filter(room = room).all()
    context['musteriler'] = musteri


    if request.method == "POST":
        updateRoom = UpdateRoomDetail(request.POST,instance = room)
        if updateRoom.is_valid():
            updateRoom.save()
            return redirect('odadetay', odaId)
        else:
            return redirect('404')
    return render(request, 'roomdetail.html', context)


@login_required(login_url="home")
def detailguest(request, musteriId):

    context = {}

    musteri = KonukBilgileri.objects.filter(id = musteriId).first()
    context['kisi'] = musteri

    musteriBilgiForm = UpdateGuestDetail(instance = musteri)
    context['musteriform'] = musteriBilgiForm

    if request.method == "POST":
        guncelle = UpdateGuestDetail(request.POST, instance = musteri)
        if guncelle.is_valid():
            guncelle.save()
            return redirect('musteridetay', musteriId)
        else:
            return redirect('404')

    return render(request, 'guestdetail.html', context)

# 404 sayfası için
def hatasayfasi(request):

    return render(request, '404.html')