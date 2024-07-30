# Generated by Django 4.0.6 on 2024-06-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0004_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=250)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sinopsis', models.TextField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.director')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.genero')),
            ],
        ),
    ]
