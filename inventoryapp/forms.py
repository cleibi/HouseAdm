from django import forms
from django.forms import ModelForm
from inventoryapp.models import Room
from django.core import validators

#class Room(forms.Form):
#    name = forms.CharField()


class NewRoomForm(forms.ModelForm):
    class Meta():
        model = Room
        fields = '__all__'
