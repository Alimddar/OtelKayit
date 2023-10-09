from django.db import models

# ValidatorError
from django.core.exceptions import ValidationError

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
    roomtype = models.CharField(("Oda Tipi"),max_length=50)
    roombadcount = models.IntegerField(("Oda Yatak Sayısı"))
    roomprice = models.IntegerField(("Odanın Fiyatı"))
    roomactive = models.BooleanField(("Oda Aktif Mi?"), default=True)
    roomproblemreason = models.TextField(("Odanın Problemi Nedir?"), blank=True)

    def __str__(self) -> str:
        return self.roomtype
    

def integer_length(value):
    if not (11 <= value < 12):
        raise ValidationError("11 Haneli Olmak Zorundadır!")

class KonukBilgileri(models.Model):
    room = models.ForeignKey(OtelOda, verbose_name=("Oda Tipi"), on_delete=models.CASCADE)
    first_name = models.CharField(("Konaklayan Adı"), max_length=50)
    last_name = models.CharField(("Konaklayan Soyadı"), max_length=50)
    nationality = models.CharField(("Konuk Uyruğu"), max_length=50)
    guest_tr_id = models.IntegerField(("Konaklayan Tc Kimlik Numarası"), validators=[integer_length])
    guest_id = models.CharField(("Konaklayan Passaport ID"), max_length=50, blank=True)
    checkin_date = models.DateField(("Giriş Tarihi"), auto_now=False, auto_now_add=False)
    checkout_date = models.DateField(("Çıkış Tarihi"), auto_now=False, auto_now_add=False, blank=True)

    def __str__(self) -> str:
        return self.first_name