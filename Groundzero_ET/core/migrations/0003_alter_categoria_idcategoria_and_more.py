# Generated by Django 4.0.5 on 2022-07-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pinturas_aprobada_alter_pinturas_destacado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id de categoria'),
        ),
        migrations.AlterField(
            model_name='pinturas',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, verbose_name='descripcion'),
        ),
    ]
