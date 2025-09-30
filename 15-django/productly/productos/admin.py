from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
