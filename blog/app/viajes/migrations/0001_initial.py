# Generated by Django 4.2.7 on 2023-12-12 22:21

import app.viajes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('resumen', models.CharField(max_length=200, null=True, verbose_name='Resumen')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('contenido', models.TextField(verbose_name='Texto')),
                ('imagenes', models.ImageField(upload_to='viajes')),
                ('autor', models.ForeignKey(default=app.viajes.models.Viaje.default_autor, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria_viaje', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viajes.categoria')),
            ],
        ),
    ]
