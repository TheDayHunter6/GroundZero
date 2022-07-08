from xml.etree.ElementInclude import include
from django.urls import path
from .views import admin_contacto, administrador, home, logoutUser, paglogin, pagRegistro,  artistas, pinturas, pinturas2, compra, formulariofooter,subir_pintura, mis_pinturas, admin_pinturas, modificar_pintura, eliminar_pintura, administrador, contacto
from django.conf import settings
from django.conf.urls.static import static

#from cuenta.views import (registro_view, login1)
from api_pintura.views import(lista_pintura, detalle_pintura)

urlpatterns = [
    path('', home, name="home"),
    path('login/', paglogin, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', pagRegistro, name="registro"),
    path('administrador', administrador, name="administrador"),
    path('artistas',artistas, name="artistas"),
    path('pinturas',pinturas,name="pinturas"),
    path('pinturas2',pinturas2,name="pinturas2"),
    path('compra', compra, name="compra"),
    path('formulariofooter',formulariofooter,name="formulariofooter"),
    path('subir_pintura/',subir_pintura,name="subir pintura"),
    path('mis-pinturas',mis_pinturas,name="mis-pinturas"),
    path('modificar-pinturas/<id>/',modificar_pintura,name="modificar-pinturas"),
    path('eliminar-pinturas/<id>/',eliminar_pintura,name="eliminar-pinturas"),
    path('admin-pinturas',admin_pinturas,name="admin-pinturas"),
    path('admin-contacto',admin_contacto,name="admin-contacto"),
    path('contacto',contacto,name="contacto"),
    
    #path('api/cuenta/', registro_view, name="registro_view"),
    #path('api/login/', login1, name="login1"),
    
    

    #urls rest
    
]