from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pinturas
from .forms import  crearUsuario, subirPintura, modificarPintura, ContactoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



# Create your views here.

def home(request):
    return render(request,'core/index.html')

def administrador(request):
    return render(request,'core/administrador.html')

def pinturas(request):
    pinturas = Pinturas.objects.all()
    data = {
        'pinturas': pinturas
    }
    return render(request, 'core/pinturas.html', data)

def mis_pinturas(request):
    pinturas = Pinturas.objects.all()
    data = {
        'pinturas': pinturas
    }
    return render(request,'core/mis-pinturas.html', data)

def subir_pintura(request):    
    form = subirPintura()
    
    if request.method== 'POST':
        form = subirPintura(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')
    context = {'form':form} 
    return render(request, 'core/subirpintura.html', context)

def contacto(request):
    form = ContactoForm()
   
    if request.method== 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')
    context = {'formcontacto':form} 
    return render(request, 'core/contacto.html', context)

def modificar_pintura(request,id):
    pinturas = get_object_or_404(Pinturas, idPintura=id)
    form = modificarPintura()
    data ={
        'form': modificarPintura(instance=pinturas)
    }

    if request.method== 'POST':
        form = modificarPintura(data=request.POST, instance=pinturas, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('admin-pinturas')
    
    return render(request, 'core/modificarpintura.html', data)

def eliminar_pintura(request,id):
    pinturas = get_object_or_404(Pinturas, idPintura=id)
    pinturas.delete()
    return redirect ('admin-pinturas')
    

def admin_pinturas(request):
    return render(request,'core/admin_pinturas.html')

def admin_contacto(request):
    return render(request,'core/admin_contacto.html')

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




