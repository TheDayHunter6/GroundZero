from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

#Modelo para Categorias
class Categoria(models.Model):
  idCategoria = models.AutoField(primary_key = True, verbose_name = 'id de categoria')
  nombreCategoria = models.CharField(max_length = 50, verbose_name = 'Nombre de la categoria')

  def __str__(self):
    return self.nombreCategoria

# Modelo para Pinturas
class Pinturas(models.Model):
  idPintura = models.AutoField( primary_key = True, verbose_name = 'id pintura')
  image = models.ImageField(upload_to='pinturas', verbose_name='imagen')
  destacado = models.BooleanField(default=False,verbose_name="destacado")
  aprobada = models.BooleanField(default=False,verbose_name="aprobada")
  categoria = models.ForeignKey(Categoria, default=True, on_delete = models.CASCADE)
  nombre_pintura = models.CharField(max_length = 20, verbose_name = 'Nombre Pintura')
  precio_pintura = models.IntegerField (null=True, blank =True, verbose_name = 'Precio')
  autor = models.ForeignKey (User, on_delete = models.CASCADE)
 
  descripcion = models.TextField(max_length=300, blank= True, verbose_name='descripcion')
  fecha_creacion = models.DateField(verbose_name='fecha_creacion')
  
  

  def __str__(self):
    return self.nombre_pintura

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)