from django.db import router
from django.urls import path, include
from .views import  FormularioViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contacto', FormularioViewset)

app_name = 'api_formulario'

urlpatterns = [

    path('', include(router.urls)),
]
