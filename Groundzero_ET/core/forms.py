from dataclasses import fields
from pyexpat import model
from urllib.parse import ParseResultBytes
from django import forms
from django.forms import ModelForm
from .models import Contacto, Pinturas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class crearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        
        
        ]


class subirPintura(ModelForm):

    class Meta:
        model = Pinturas
        fields = ['image', 'nombre_pintura', 'autor', 'precio_pintura','descripcion','fecha_creacion']

class modificarPintura(ModelForm):

    class Meta:
        model = Pinturas
        fields = ['image', 'nombre_pintura', 'autor', 'precio_pintura','descripcion','fecha_creacion', 'destacado','aprobada','mensaje_admin']


class ContactoForm(ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'