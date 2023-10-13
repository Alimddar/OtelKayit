from django.db import models

# User modelini çek
from django.contrib.auth.models import User


# Create your models here.
class OtelYonetim(models.Model):
    owner = models.ForeignKey(User, verbose_name=("Otel Sahibi"), on_delete=models.CASCADE)
    title = models.CharField(("Otel Adı"), max_length=100)
    image = models.ImageField(("Otel Logosu"), upload_to="Logo", height_field=None, width_field=None, max_length=None)
    address = models.CharField(("Otel Adresi"), max_length=150)
    badcount = models.IntegerField(("Otel Yatak Sayısı"))

    def __str__(self) -> str:
        return self.title
    
class OtelOda(models.Model):
    otel = models.ForeignKey(OtelYonetim, verbose_name=("Otelin Adı"), on_delete=models.CASCADE)
    roomnumber = models.IntegerField(("Oda Numarası"), default=1)
    roomtype = models.CharField(("Oda Tipi"),max_length=50)
    roombadcount = models.IntegerField(("Oda Yatak Sayısı"))
    roomclean = models.BooleanField(("Oda Temiz Mi?"), default=True)
    roomdefective = models.BooleanField(("Oda Arızalı Mı?"), default=False)
    roomactive = models.BooleanField(("Odayı Kapat!"), default=False)
    roomprice = models.IntegerField(("Odanın Fiyatı"))
    roomproblemreason = models.TextField(("Odanın Problemi Nedir?"), blank=True)
    roomisempty = models.BooleanField(("Oda Dolu Mu?"),default=True)

    def __str__(self) -> str:
        return self.roomtype

class KonukBilgileri(models.Model):
    room = models.ForeignKey(OtelOda, verbose_name=("Oda Tipi"), on_delete=models.CASCADE)
    first_name = models.CharField(("Konaklayan Adı"), max_length=50)
    last_name = models.CharField(("Konaklayan Soyadı"), max_length=50)
    nationality = models.CharField(("Konuk Uyruğu"), max_length=50)
    guest_tc = models.CharField(("Konuk Tc Numarası"), default="11 karakterlidir" ,max_length=11)
    guest_id = models.CharField(("Konaklayan Passaport ID"), max_length=50, blank=True)
    checkin_date = models.DateField(("Giriş Tarihi"), auto_now=False, auto_now_add=False)
    checkout_date = models.DateField(("Çıkış Tarihi"), auto_now=False, auto_now_add=False, blank=True)


    def __str__(self) -> str:
        return self.first_name
    


class Muhasebe(models.Model):
    date = models.DateField(("Tarih"), auto_now_add=True)
    room = models.ForeignKey(OtelOda, verbose_name=("Oda"), on_delete=models.CASCADE)
    guest = models.ForeignKey(KonukBilgileri, verbose_name=("Müşteri"), on_delete=models.CASCADE)
    calculate = models.DecimalField(("Fatura Tutarı"), max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.date
        
    def ucret_hesapla(self):
        fiat = self.room.roomprice
        self.calculate = fiat
        self.save()