from xml.etree.ElementInclude import include
from django.urls import path
from .views import home, logoutUser, paglogin, pagRegistro,  artistas, pinturas, pinturas2, compra, formulariofooter,subir_pintura, mis_pinturas, admin_pinturas
from django.conf import settings
from django.conf.urls.static import static

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
    path('subir_pintura/',subir_pintura,name="subir pintura"),
    path('mis-pinturas',mis_pinturas,name="mis-pinturas"),
    path('admin-pinturas',admin_pinturas,name="admin-pinturas"),
    
    #path('api/cuenta/', registro_view, name="registro_view"),
    #path('api/login/', login1, name="login1"),
    
    

    #urls rest
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)