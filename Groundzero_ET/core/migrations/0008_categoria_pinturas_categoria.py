# Generated by Django 4.0.5 on 2022-07-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_pinturas_categoria_delete_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.AddField(
            model_name='pinturas',
            name='categoria',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]
