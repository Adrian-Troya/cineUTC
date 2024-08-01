#configurando redireccionanmiento
from django.urls import path

from . import views
urlpatterns = [
    path('home/',views.home),
    #-----------------------------------------GENEROS--------------------------------------------------
    path('listadoGeneros/', views.ListadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>', views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>', views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/', views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    #-----------------------------------------PELICULAS--------------------------------------------------
    path('listadoPeliculas/', views.ListadoPeliculas, name='listadoPeliculas'),
    path('eliminarPelicula/<id>', views.eliminarPelicula, name='eliminarPelicula'),
    path('gestionPeliculas/', views.gestionPeliculas, name='gestionPeliculas'),
    path('guardarPelicula/', views.guardarPelicula, name='guardarPelicula'),
    path('editarPelicula/<id>', views.editarPelicula, name='editarPelicula'),
    path('procesarActualizacionPelicula/', views.procesarActualizacionPelicula, name='procesarActualizacionPelicula'),
    #-----------------------------------------DIRECTORES--------------------------------------------------
    path('listadoDirectores/', views.ListadoDirectores, name='listadoDirectores'),
    path('gestionDirectores/', views.gestionDirectores, name='gestionDirectores'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    #-----------------------------------------PAISES--------------------------------------------------
    path('listadoPaises/', views.ListadoPaises, name='listadoPaises'),
    path('eliminarPais/<id>', views.eliminarPais, name='eliminarPais'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<id>', views.editarPais, name='editarPais'),
    path('procesarActualizacionPais/', views.procesarActualizacionPais, name='procesarActualizacionPais'),

    #-----------------------------------------GESTION CINES--------------------------------------------------
    path('listadoCines/', views.ListadoCines, name='listadoCines'),
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    #-----------------------------------------CORREO ELECTRONICO--------------------------------------------------
    path('correo/', views.correo, name='correo')
]
