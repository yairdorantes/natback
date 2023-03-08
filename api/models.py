from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Producto")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100, verbose_name="Material")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    def __str__(self):
        return self.name

class Insumos(models.Model):
    name = models.CharField(max_length=100, verbose_name="Insumo")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    def __str__(self):
        return self.name
    
class Dessert(models.Model):
    name = models.CharField(max_length=100, verbose_name="Dessert")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    def __str__(self):
        return self.name
    
class Cake(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pastel")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    price = models.FloatField(default=0,verbose_name="Precio")
    weight = models.FloatField(default=0,verbose_name="Peso")
    flavor = models.CharField(max_length=100,verbose_name="Sabor")
    def __str__(self):
        return self.name
    