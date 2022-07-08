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
  mensaje_admin = models.TextField(max_length=300, blank= True, verbose_name='mensaje admin')
  categoria = models.ForeignKey(Categoria, default=True, on_delete = models.CASCADE)
  nombre_pintura = models.CharField(max_length = 20, verbose_name = 'Nombre Pintura')
  precio_pintura = models.IntegerField (null=True, blank =True, verbose_name = 'Precio')
  autor = models.ForeignKey (User, on_delete = models.CASCADE)
  descripcion = models.TextField(max_length=300, blank= True, verbose_name='descripcion')
  fecha_creacion = models.DateField(verbose_name='fecha_creacion')
  
  def __str__(self):
    return self.nombre_pintura


opciones_consulta= [
  [0,"consulta"],
  [1,"reclamo"],
  [2,"sugerencia"],
  [3,"felicitaciones"],

]
#Modelo para Formulario
class Contacto(models.Model):
  nombre = models.CharField(max_length=50)
  correo = models.EmailField()
  tipo_consulta = models.IntegerField(choices=opciones_consulta)
  mensaje = models.TextField()
  avisos = models.BooleanField()

  def __str__(self):
    return self.nombre

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)