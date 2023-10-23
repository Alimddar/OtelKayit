from django import forms

from .models import OtelOda,KonukBilgileri,Reservation


class UpdateRoomDetail(forms.ModelForm):
    
    class Meta:
        model = OtelOda
        fields = ["roomnumber","roomtype","roombadcount","roomclean","roomdefective","roomactive","roomprice","roomproblemreason","roomisempty",]


class UpdateGuestDetail(forms.ModelForm):

    class Meta:

        model = KonukBilgileri
        fields = ["guest_note",]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'checkin_date', 'checkout_date', 'is_confirmed']