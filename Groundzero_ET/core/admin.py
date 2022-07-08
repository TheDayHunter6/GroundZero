from django.contrib import admin
from .models import Pinturas, Categoria, Contacto

# Register your models here.

admin.site.register(Pinturas)
admin.site.register(Categoria)
admin.site.register(Contacto)