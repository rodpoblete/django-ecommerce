import os
from django.db import models


# Create your models here.
class juguetes(models.Model):
    Producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)
    stock = models.CharField(max_length=4)

    def __str__(self):
        return "{}".format(self.Producto)


class electro(models.Model):
    Producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)
    stock = models.CharField(max_length=4)

    def generaNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'electronica'
        nombre = "{}".format(extension)
        return os.path.join(ruta,nombre)
    
    foto = models.ImageField(upload_to=generaNombre, null=True, default='electronica/electro.png')

    def __str__(self):
        return "{}".format(self.Producto)


class ropa(models.Model):
    Producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    stock = models.CharField(max_length=4)

    def __str__(self):
        return "{}".format(self.Producto)