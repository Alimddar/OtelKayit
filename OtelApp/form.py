from django import forms

from .models import OtelOda


class UpdateRoomDetail(forms.ModelForm):


    class Meta:

        model = OtelOda
        fields = ["roomnumber","roomtype","roombadcount","roomclean","roomdefective","roomactive","roomprice","roomproblemreason","roomisempty"]


