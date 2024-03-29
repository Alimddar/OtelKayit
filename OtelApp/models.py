from django.db import models

from django.core import validators

from datetime import date

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
    roomnumber = models.IntegerField(("Oda Numarası"), default=1)
    roomtype = models.CharField(("Oda Tipi"),max_length=50)
    roombadcount = models.IntegerField(("Oda Yatak Sayısı"), default=1, validators=[validators.MinValueValidator(1, message="En Az Bir Yatak Olmalıdır!"),validators.MaxValueValidator(6, message="6 Yataktan Daha Fazla Ekleyemezsin!")])
    roomclean = models.BooleanField(("Oda Temiz Mi?"), default=True)
    roomdefective = models.BooleanField(("Oda Arızalı Mı?"), default=False)
    roomactive = models.BooleanField(("Odayı Kapat!"), default=False)
    roomprice = models.IntegerField(("Odanın Fiyatı"), default=0, blank=True)
    roomproblemreason = models.TextField(("Odanın Problemi Nedir?"), blank=True)
    roomisempty = models.BooleanField(("Oda Dolu Mu?"), default=False)
    roomreserved = models.BooleanField(("Oda Rezerve Edildi Mi?"), default=False)

    def __str__(self) -> str:
        return str((self.roomnumber))

class KonukBilgileri(models.Model):
    otel = models.ForeignKey(OtelYonetim, verbose_name=("Otel"), on_delete=models.CASCADE)
    room = models.ForeignKey(OtelOda, verbose_name=("Oda Tipi"), on_delete=models.CASCADE)
    first_name = models.CharField(("Konaklayan Adı"), max_length=50)
    last_name = models.CharField(("Konaklayan Soyadı"), max_length=50)
    nationality = models.CharField(("Konuk Uyruğu"), max_length=50)
    guest_tc = models.CharField(("Konuk Tc Numarası"), max_length=11, blank=True)
    guest_id = models.CharField(("Konaklayan Passaport ID"), max_length=50, blank=True)
    checkin_date = models.DateField(("Giriş Tarihi"), auto_now=False, auto_now_add=False)
    checkout_date = models.DateField(("Çıkış Tarihi"), auto_now=False, auto_now_add=False, blank=True)
    guest_note = models.TextField(("Müşteri İçin Not"), blank=True)


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

class Reservation(models.Model):
    guest = models.ForeignKey(KonukBilgileri, verbose_name=("Konaklayan"), on_delete=models.CASCADE)
    room = models.ForeignKey(OtelOda, verbose_name=("Oda"), on_delete=models.CASCADE)
    checkin_date = models.DateField(("Giriş Tarihi"))
    checkout_date = models.DateField(("Çıkış Tarihi"))
    is_confirmed = models.BooleanField(default=False)  

    class Meta:
        unique_together = ('room', 'checkin_date', 'checkout_date') 
    
    def __str__(self) -> str:
        return f"Reservation for {self.guest.first_name} in Room {self.room.roomnumber} from {self.checkin_date} to {self.checkout_date}"

    def save(self, *args, **kwargs):
        if not self.is_room_available():
            raise ValidationError('Seçilen tarihlerde oda müsait değil!')
        super().save(*args, **kwargs)

    def is_room_available(self):
        overlapping_reservations = Reservation.objects.filter(
            room=self.room,
            checkin_date__lte=self.checkout_date,
            checkout_date__gte=self.checkin_date
        ).exclude(id=self.id)
        return overlapping_reservations.count() == 0