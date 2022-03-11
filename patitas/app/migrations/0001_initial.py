# Generated by Django 4.0.2 on 2022-03-07 16:28

import cloudinary.models
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
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(default='', max_length=100, verbose_name='Titulo')),
                ('blog_fech', models.DateTimeField(auto_now=True, verbose_name='Publicacion')),
                ('blog_img', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='Portada')),
                ('blog_hty', models.TextField(verbose_name='Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('mascota_nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mascota_est', models.CharField(choices=[('false', 'DISPONIBLE'), ('true', 'NO DISPONIBLE')], max_length=20, verbose_name='Estado de Adopcion')),
                ('mascota_img', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='Imagen')),
                ('mascota_age', models.IntegerField(default=0, verbose_name='Edad')),
                ('mascota_sex', models.CharField(choices=[('HEMBRA', 'HEMBRA'), ('MACHO', 'MACHO')], max_length=10, verbose_name='Sexo')),
                ('mascota_act', models.CharField(choices=[('ALTO', 'ALTO'), ('MEDIO', 'MEDIO'), ('BAJO', 'BAJO')], max_length=10, verbose_name='Nivel de Actividad')),
                ('mascota_hair', models.CharField(choices=[('CORTO', 'CORTO'), ('LARGO', 'LARGO')], max_length=10, verbose_name='Pelo')),
                ('mascota_tall', models.CharField(choices=[('PEQUEÑO', 'PEQUEÑO'), ('MEDIANO', 'MEDIANO'), ('GRANDE', 'GRANDE')], max_length=10, verbose_name='Tamaño')),
                ('mascota_hty', models.TextField(verbose_name='Historia')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20, unique=True)),
                ('usu_id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('adopcion_id', models.AutoField(primary_key=True, serialize=False)),
                ('adopcion_fech', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('mascota', models.OneToOneField(db_column='mascota_id', on_delete=django.db.models.deletion.RESTRICT, to='app.mascotas', verbose_name='Mascota')),
                ('user', models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.RESTRICT, to='app.cliente', to_field='usu_id', verbose_name='Usuario')),
            ],
        ),
    ]
