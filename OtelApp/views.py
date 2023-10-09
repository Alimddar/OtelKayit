from django.shortcuts import render,redirect


# Django user modelini al
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Single MiddleWare
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            giris = authenticate(request, username = username, password = password)

            if giris is not None:
                login(request,giris)
                # Değişecek Otelin Kendisine Girecek
                return redirect('oteldashboard')
            else:
                return redirect('home')
        else:
            return redirect('home')

    return render(request, "index.html")


@login_required(login_url="home")
def otel(request):

    return render(request, "otel.html")



# 404 sayfası için
def hatasayfasi(request):

    return render(request, '404.html')