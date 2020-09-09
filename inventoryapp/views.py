from django.shortcuts import render
from django.http import HttpResponse
from inventoryapp.models import Hsection,Room,Item
from . import forms
from inventoryapp.forms import NewRoomForm

# Create your views here.
def index(request):

    return render(request,'inventoryapp/index.html')


def rooms(request):

    form = NewRoomForm()

    if request.method == 'POST':
        form = NewRoomForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request,'inventoryapp/form_hsection.html',{'form':form})
