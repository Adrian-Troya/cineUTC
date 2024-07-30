# Generated by Django 4.0.6 on 2024-06-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0010_rename_genero_p_pelicula_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='generos'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='portada',
            field=models.FileField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
