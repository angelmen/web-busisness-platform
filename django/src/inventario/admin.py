from django.contrib import admin

# Register your models here.
from .models import Articulo, Articulo_Venta

admin.site.register(Articulo)
admin.site.register(Articulo_Venta)
