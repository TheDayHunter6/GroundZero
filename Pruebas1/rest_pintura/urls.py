from django.urls import path
from .views import lista_pintura, detalle_pintura

app_name = 'rest_pintura'

urlpatterns = [
    path('lista_pinturas', lista_pintura, name="lista_pintura"),
    path('detalle_pintura/<id>', detalle_pintura, name="detalle_pintura"),
]
