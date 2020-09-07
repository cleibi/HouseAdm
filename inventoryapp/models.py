from django.db import models

# Create your models here.
class Hsection(models.Model):
    hsection_name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.hsection_name

class Room(models.Model):
    tipo = models.ForeignKey(Hsection,on_delete=models.CASCADE)
    room_name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.room_name

class Item(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=256,unique=True)
    #qtd = models.IntegerField(verbose_name=Quantidade)

    def __str__(self):
        return str(self.item_name)
