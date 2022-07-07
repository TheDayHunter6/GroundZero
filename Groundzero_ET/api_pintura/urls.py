from django.db import router
from django.urls import path, include
from .views import lista_pintura, detalle_pintura, PinturaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pinturas', PinturaViewset)

app_name = 'api_pintura'

urlpatterns = [
    path('lista_pinturas', lista_pintura, name="lista_pintura"),
    path('detalle_pintura/<id>', detalle_pintura, name="detalle_pintura"),
    path('', include(router.urls)),
]
