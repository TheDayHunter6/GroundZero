from django.contrib import admin
from .models import Pinturas, Autor, Categoria, Contacto

# Register your models here.

admin.site.register(Pinturas)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Contacto)