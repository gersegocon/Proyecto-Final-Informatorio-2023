# Generated by Django 4.2.7 on 2023-11-28 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='viaje',
            name='categoria_viaje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viajes.categoria'),
        ),
    ]