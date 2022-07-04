from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Pinturas
from .forms import PinturasForm, crearUsuario
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

def pinturasdemo(request):
    return render(request, 'core/pinturasdemo.html')

def compra(request):
    return render(request, 'core/compra.html')

def formulariofooter(request):
    return render(request, 'core/formulariofooter.html')

def Pag1(request):
    return render(request,'core/Pag1.html')

def Pag2(request):
    return render(request,'core/Pag2.html')

def Pag3(request):
    return render(request,'core/Pag3.html')

def Pag4(request):
    return render(request,'core/Pag4.html')

def Pag5(request):
    return render(request,'core/Pag5.html')

def Pag6(request):
    return render(request,'core/Pag6.html')

def Pag7(request):
    return render(request,'core/Pag7.html')

def Pag8(request):
    return render(request,'core/Pag8.html')

def Pag9(request):
    return render(request,'core/Pag9.html')

def Pag10(request):
    return render(request,'core/pag10.html')

def Pag11(request):
    return render(request,'core/Pag11.html')

def Pag12(request):
    return render(request,'core/Pag12.html')

def Pag13(request):
    return render(request,'core/Pag13.html')

def Pag14(request):
    return render(request,'core/Pag14.html')

def Pag15(request):
    return render(request,'core/Pag15.html')

def Pag16(request):
    return render(request,'core/Pag16.html')

def Pag17(request):
    return render(request,'core/Pag17.html')

def Pag18(request):
    return render(request,'core/Pag18.html')




def form_pinturas(request):
    contexto = { 
        'form': PinturasForm(),
        }
    if request.method=='POST':
        formulario=PinturasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form-pinturas.html', contexto)

def form_modificar_pinturas(request, id):
    pintura = Pinturas.objects.get(idPintura=id)
    contexto = { 
        'form': PinturasForm(instance=pintura),
        }
    if request.method=='POST':
        formulario=PinturasForm(data=request.POST, instance=pintura)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form-modificar-pinturas.html', contexto)

def form_delete_pintura(request, id):
    pintura = Pinturas.objects.get(idPintura=id)
    pintura.delete()
    return redirect(to="home")

def listapinturas(request):
    lista = Pinturas.objects.all()
    contexto = {
        'Pinturas': lista,
    }
    return render(request, 'core/index.html', contexto)