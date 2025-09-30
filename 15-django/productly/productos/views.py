from django.http import HttpResponse #, JsonResponse

from django.shortcuts import render
from .models import Producto
#productos

# Create your views here.
def index(request):
    productos = Producto.objects.all() # si quetremos ver en un json debemos usar values()

    return render(
        request, 
        'index.html',
        context={'productos':productos}
    )










# # print(productos)
 # return JsonResponse(list(productos), safe=False) # si no es un diccionario poner safe en false 
