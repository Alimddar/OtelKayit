from django import forms

from .models import OtelOda


class UpdateRoomDetail(forms.ModelForm):


    class Meta:

        model = OtelOda
        fields = "__all__"


