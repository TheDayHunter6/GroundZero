# Generated by Django 4.0.5 on 2022-07-07 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idAutor', models.IntegerField(primary_key=True, serialize=False, verbose_name='id Autor')),
                ('pnombreAutor', models.CharField(max_length=60, verbose_name='Primer nombre')),
                ('appaternoAutor', models.CharField(max_length=60, verbose_name='Apellido')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('anhio_nac', models.IntegerField(verbose_name='Fecha nacimiento')),
                ('pais', models.CharField(max_length=60, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pinturas',
            fields=[
                ('idPintura', models.IntegerField(primary_key=True, serialize=False, verbose_name='id pintura')),
                ('image', models.ImageField(upload_to='pinturas', verbose_name='imagen')),
                ('destacado', models.BooleanField(verbose_name='destacado')),
                ('nombre_pintura', models.CharField(max_length=20, verbose_name='Nombre Pintura')),
                ('precio_pintura', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
                ('descripcion', models.TextField(blank=True, max_length=200, verbose_name='descripcion')),
                ('fecha_creacion', models.DateField(verbose_name='fecha_creacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]