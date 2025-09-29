from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(nax_length=100) #longuitud maxima 100 que debe guardar

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    #CASCADE: ELIMINAR EL PRODUCTO
    # PROTECT: LANZA UN ERROR
    # RESTRICT: SOLO ELIMINA SI NO EXISTEN PRODUCTOS
    # SET_NULL: ACTUALIZA EL VALOR
    # SET_DEFAULT: ASIGAN VAL POR DEFECTO
    categoria = models.ForeignKey(Categoria, on_delete=)