# Generated by Django 4.0.6 on 2024-06-04 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0007_alter_pelicula_director_alter_pelicula_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genero',
            old_name='decripcion',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.director'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.genero'),
        ),
    ]
