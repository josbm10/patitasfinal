# Generated by Django 4.0.2 on 2022-03-10 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_adopcion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='mascota',
            field=models.OneToOneField(db_column='mascota_id', on_delete=django.db.models.deletion.CASCADE, to='app.mascotas', verbose_name='Mascota'),
        ),
        migrations.AlterField(
            model_name='adopcion',
            name='user',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usu_id',
            field=models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
