# Generated by Django 4.0.2 on 2022-03-11 22:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_adopcion_mascota_alter_adopcion_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='mascota_img',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/drcas8tkg/image/upload/v1647037043/logoPatitas_Naranja_rbxkqa.png', max_length=255, verbose_name='Imagen'),
        ),
    ]
