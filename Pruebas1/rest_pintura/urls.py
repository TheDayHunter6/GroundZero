from django.urls import path
from .views import lista_pintura, detalle_pintura

app_name = 'rest_pintura'

urlpatterns = [
    path('<id>', lista_pintura, name="lista_pintura"),
    path('<id>/datallepintura', detalle_pintura, name="detalle_pintura"),
]
