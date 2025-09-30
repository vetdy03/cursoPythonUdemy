from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from .models import Producto
#productos

# Create your views here.
def index(request):
    productos = Producto.objects.all().values() # si quetremos ver en un json debemos usar values()

    # print(productos)
    return JsonResponse(list(productos), safe=False) # si no es un diccionario poner safe en false 
