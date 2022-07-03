from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

#Modelo para Autores
class Autor(models.Model):
  idAutor = models.IntegerField(primary_key = True, verbose_name = 'id Autor')
  pnombreAutor = models.CharField(max_length = 60, verbose_name = 'Primer nombre')
  appaternoAutor = models.CharField(max_length = 60, verbose_name = 'Apellido')
  edad = models.IntegerField(verbose_name = 'Edad')
  anhio_nac = models.IntegerField(verbose_name = 'Fecha nacimiento') 
  pais = models.CharField(max_length = 60, verbose_name = 'Pais') 

  def __str__(self):
    return self.pnombreAutor

#Modelo para Categorias
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'id de categoria')
  nombreCategoria = models.CharField(max_length = 50, verbose_name = 'Nombre de la categoria')

  def __str__(self):
    return self.nombreCategoria

# Modelo para Pinturas
class Pinturas(models.Model):
  id = models.CharField(max_length = 6, primary_key = True, verbose_name = 'id')
  nombre_pintura = models.CharField(max_length = 20, verbose_name = 'Nombre Pintura')
  precio_pintura = models.IntegerField (null=True, blank =True, verbose_name = 'Precio')
  autor = models.ForeignKey (Autor, on_delete = models.CASCADE)
  categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)


  def __str__(self):
    return self.idPintura 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
