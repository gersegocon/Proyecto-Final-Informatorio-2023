# Generated by Django 4.2.7 on 2023-11-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('contenido', models.TextField(verbose_name='Texto')),
                ('imagenes', models.ImageField(upload_to='viajes')),
            ],
        ),
    ]