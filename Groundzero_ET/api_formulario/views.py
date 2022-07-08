from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Contacto
from .serializers import ContactoSerializer
from django.contrib.auth.models import User
from core.models import Pinturas
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.


class FormularioViewset(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class= ContactoSerializer