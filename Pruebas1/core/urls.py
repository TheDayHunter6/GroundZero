from xml.etree.ElementInclude import include
from django.urls import path
from .views import form_delete_pintura, form_pinturas, home, logoutUser, paglogin, pagRegistro, form_modificar_pinturas, artistas, pinturasdemo, compra, formulariofooter
from .views import Pag1, Pag2, Pag3, Pag4, Pag5, Pag6, Pag7, Pag8, Pag9, Pag10, Pag11, Pag12, Pag13, Pag14, Pag15, Pag16, Pag17, Pag18
from cuenta.views import (registro_view, login1)
from rest_pintura.views import(lista_pintura, detalle_pintura)
urlpatterns = [
    path('', home, name="home"),
    path('login/', paglogin, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', pagRegistro, name="registro"),
    path('form-pinturas', form_pinturas, name="form_pinturas"),
    path('form-modificar-pinturas/<id>', form_modificar_pinturas, name="form_modificar_pinturas"),
    path('form-delete-pintura/<id>', form_delete_pintura, name="form_delete_pintura"),
    path('artistas',artistas, name="artistas"),
    path('pinturasdemo',pinturasdemo,name="pinturasdemo"),
    path('compra', compra, name="compra"),
    path('formulariofooter',formulariofooter,name="formulariofooter"),
    path('Pag1',Pag1, name="Pag1"),
    path('Pag2',Pag2, name="Pag2"),
    path('Pag3',Pag3, name="Pag3"),
    path('Pag4',Pag4, name="Pag4"),
    path('Pag5',Pag5, name="Pag5"),
    path('Pag6',Pag6, name="Pag6"),
    path('Pag7',Pag7, name="Pag7"),
    path('Pag8',Pag8, name="Pag8"),
    path('Pag9',Pag9, name="Pag9"),
    path('Pag10',Pag10, name="Pag10"),
    path('Pag11',Pag11, name="Pag11"),
    path('Pag12',Pag12, name="Pag12"),
    path('Pag13',Pag13, name="Pag13"),
    path('Pag14',Pag14, name="Pag14"),
    path('Pag15',Pag15, name="Pag15"),
    path('Pag16',Pag16, name="Pag16"),
    path('Pag17',Pag17, name="Pag17"),
    path('Pag18',Pag18, name="Pag18"),
    path('api/cuenta/', registro_view, name="registro_view"),
    path('api/login/', login1, name="login1"),
    path('api/pintura/', lista_pintura, name='lista_pintura'),
    

    #urls rest
    
]