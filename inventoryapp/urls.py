from django.conf.urls import url
from inventoryapp import views

urlpatterns = [
    url('',views.index,name='index')
]
