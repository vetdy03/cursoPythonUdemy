from django.contrib import admin
from .models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en',)
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
