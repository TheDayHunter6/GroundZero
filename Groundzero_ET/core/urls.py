from xml.etree.ElementInclude import include
from django.urls import path
from .views import home, logoutUser, paglogin, pagRegistro,  artistas, pinturas, pinturas2, compra, formulariofooter

#from cuenta.views import (registro_view, login1)
from api_pintura.views import(lista_pintura, detalle_pintura)
urlpatterns = [
    path('', home, name="home"),
    path('login/', paglogin, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', pagRegistro, name="registro"),
    
    path('artistas',artistas, name="artistas"),
    path('pinturas',pinturas,name="pinturas"),
    path('pinturas2',pinturas2,name="pinturas2"),
    path('compra', compra, name="compra"),
    path('formulariofooter',formulariofooter,name="formulariofooter"),
    #path('api/cuenta/', registro_view, name="registro_view"),
    #path('api/login/', login1, name="login1"),
    
    

    #urls rest
    
]