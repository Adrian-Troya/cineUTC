from django.urls import path
from . import views

# Rutas
urlpatterns = [
    # Página principal
    path('home/', views.home, name='home'),
    
    # Géneros
     path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGeneros/<id>/', views.eliminarGeneros, name='eliminarGeneros'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>/', views.editarGenero, name='editarGenero'),
    path('procesoActualizarGeneros/<id>/', views.procesoActualizarGeneros, name='procesoActualizarGeneros'),

    # Países
    path('listadoPaises/', views.listadoPaises, name='listadoPaises'),
    path('eliminarPais/<int:id>/', views.eliminarPais, name='eliminarPais'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<int:id>/', views.editarPais, name='editarPais'),
    path('procesoActualizarPais/<int:id>/', views.procesoActualizarPais, name='procesoActualizarPais'),

    # Películas
    path('listadoPeliculas/', views.listadoPeliculas, name='listadoPeliculas'),
    path('gestionPeliculas/', views.gestionPeliculas, name='gestionPeliculas'),
    path('guardarPelicula/', views.guardarPelicula, name='guardarPelicula'),
    path('editarPelicula/<int:id>/', views.editarPelicula, name='editarPelicula'),
    path('procesoActualizarPelicula/<int:id>/', views.procesoActualizarPelicula, name='procesoActualizarPelicula'),
    path('eliminarPelicula/<int:id>/', views.eliminarPelicula, name='eliminarPelicula'),

    # Cines
    path('listadoCines/', views.listadoCines, name='listadoCines'),
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    
    #Directores con lo fecth
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('gestionDirectores/', views.gestionDirectores, name='gestionDirectores'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('eliminarDirector/<int:id>/', views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('editarDirector/<int:id>/', views.editarDirector, name='editarDirector'),
    path('procesoActualizarDirector/<int:id>/', views.procesoActualizarDirector, name='procesoActualizarDirector'),

]
