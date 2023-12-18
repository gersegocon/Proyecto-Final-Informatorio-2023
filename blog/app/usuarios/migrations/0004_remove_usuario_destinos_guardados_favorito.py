# Generated by Django 4.2.7 on 2023-12-17 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
        ('usuarios', '0003_remove_usuario_favoritos_usuario_destinos_guardados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='destinos_guardados',
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_guardado', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viajes.viaje')),
            ],
        ),
    ]
