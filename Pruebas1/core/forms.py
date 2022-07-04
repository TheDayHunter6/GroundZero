from dataclasses import fields
from pyexpat import model
from urllib.parse import ParseResultBytes
from django import forms
from django.forms import ModelForm
from .models import Pinturas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class crearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        
        
        ]

        
class PinturasForm(ModelForm):
    class Meta:
        model = Pinturas
        fields = ['idPintura','nombre_pintura','precio_pintura','autor','categoria']