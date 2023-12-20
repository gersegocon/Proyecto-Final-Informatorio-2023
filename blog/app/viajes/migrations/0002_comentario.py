# Generated by Django 4.2.7 on 2023-12-19 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=50)),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='viajes.viaje')),
            ],
        ),
    ]
