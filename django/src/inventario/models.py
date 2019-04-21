from django.db import models

# Create your models here.
class Articulo(models.Model):
    codigoProducto = models.CharField(max_length=8)
    nombreProducto = models.CharField(max_length=30)
    costo = models.DecimalField(decimal_places=2, max_digits=15)
    precio = models.DecimalField(decimal_places=2, max_digits=15)
    existencias = models.PositiveSmallIntegerField()
    ubicacion = models.CharField(max_length=50)

class Articulo_Venta(models.Model):
    codigoProducto = models.CharField(max_length=8)
    nombreProducto = models.CharField(max_length=30)
    costo = models.DecimalField(decimal_places=2, max_digits=15)
    precio = models.DecimalField(decimal_places=2, max_digits=15)
    existencias = models.PositiveSmallIntegerField()
    ubicacion = models.CharField(max_length=50)
