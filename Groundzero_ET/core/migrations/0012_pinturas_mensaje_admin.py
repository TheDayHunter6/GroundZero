# Generated by Django 4.0.5 on 2022-07-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_pinturas_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinturas',
            name='mensaje_admin',
            field=models.TextField(blank=True, max_length=300, verbose_name='mensaje admin'),
        ),
    ]