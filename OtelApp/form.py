from django import forms

from .models import OtelOda,KonukBilgileri


class UpdateRoomDetail(forms.ModelForm):
    
    class Meta:
        model = OtelOda
        fields = ["roomnumber","roomtype","roombadcount","roomclean","roomdefective","roomactive","roomprice","roomproblemreason","roomisempty",]


class UpdateGuestDetail(forms.ModelForm):

    class Meta:

        model = KonukBilgileri
        fields = ["guest_note",]