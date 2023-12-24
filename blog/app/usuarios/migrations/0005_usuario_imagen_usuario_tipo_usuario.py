# Generated by Django 4.2.7 on 2023-12-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_usuario_destinos_guardados_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='default-user.png', upload_to='usuarios'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('Colaborador', 'Colaborador'), ('Visitante', 'Visitante'), ('Miembro', 'Miembro'), ('Superusuario', 'Superusuario')], default='Miembro', max_length=20),
        ),
    ]