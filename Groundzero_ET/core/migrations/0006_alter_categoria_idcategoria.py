# Generated by Django 4.0.5 on 2022-07-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_autor_idautor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria'),
        ),
    ]
