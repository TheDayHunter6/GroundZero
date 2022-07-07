from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Pinturas
from .forms import  crearUsuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def home(request):
    return render(request,'core/index.html')

def paglogin(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect (home)
        else:
            messages.error(request,'Usuario o contraseña no existen')
    context= {'page': page}
    return render(request,'core/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def pagRegistro(request):
    form = crearUsuario()
    if request.method == 'POST':
        form = crearUsuario(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ocurrio un error en el registro')
    return render(request, 'core/login.html', {'form': form})

@permission_classes((IsAuthenticated))
def artistas(request):
    return render(request,'core/artistas.html')

def pinturas(request):
    pinturas = Pinturas.objects.all()
    data = {
        'pinturas': pinturas
    }
    return render(request, 'core/pinturas.html', data)

def pinturas2(request):
    pinturas = Pinturas.objects.all()
    data = {
        'pinturas': pinturas
    }
    return render(request, 'core/pinturas copy.html', data)

def compra(request):
    return render(request, 'core/compra.html')

def formulariofooter(request):
    return render(request, 'core/formulariofooter.html')


def listapinturas(request):
    lista = Pinturas.objects.all()
    contexto = {
        'Pinturas': lista,
    }
    return render(request, 'core/index.html', contexto)