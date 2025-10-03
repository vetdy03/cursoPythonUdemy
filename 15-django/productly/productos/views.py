from django.http import Http404, HttpResponse #, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
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


def detalle(request, producto_id):
    producto =  get_object_or_404(Producto, id=producto_id)
    producto= Producto.objects.get(id=producto_id)
    return render(
        request, 
        'detalle.html',
        context={'producto':producto})

def formulario(request): # GET y POST esto es un formulario
    form = ProductoForm()
    return render (
        request,
        'producto_form.html',
        {'form': form}
    )






# # print(productos)
 # return JsonResponse(list(productos), safe=False) # si no es un diccionario poner safe en false 
