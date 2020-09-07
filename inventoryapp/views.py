from django.shortcuts import render
from django.http import HttpResponse
from inventoryapp.models import Hsection,Room,Item

# Create your views here.
def index(request):
    itemlist = Item.objects.order_by('room')
    items_dict = {'items_list':itemlist}
    return render(request,'inventoryapp/index.html',context=items_dict)
