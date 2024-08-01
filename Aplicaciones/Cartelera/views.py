from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Pelicula, Director, Pais, Cine
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

# ---------------------------------------------------------------------GENEROS------------------------------------------------------------
def ListadoGeneros(request):
    generos = Genero.objects.all()
    return render(request, "listadoGeneros.html", {'generos': generos})

def eliminarGenero(request, id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Género eliminado exitosamente.")
    return redirect('listadoGeneros')

def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Género registrado exitosamente.")
    return redirect('listadoGeneros')

def editarGenero(request, id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar': generoEditar})

def procesarActualizacionGenero(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    foto = request.FILES.get("foto")
    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    if foto:
        generoConsultado.foto = foto
    generoConsultado.save()
    messages.success(request, "Género actualizado exitosamente.")
    return redirect('listadoGeneros')

# ---------------------------------------------------------------------PELICULAS------------------------------------------------------------
def ListadoPeliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculas})

def gestionPeliculas(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'gestionPeliculas.html', {'generos': generos, 'directores': directores})

@csrf_exempt
def guardarPelicula(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        duracion = request.POST.get("duracion")
        sinopsis = request.POST.get("sinopsis")
        genero_id = request.POST.get("genero")
        director_id = request.POST.get("director")
        portada = request.FILES.get("portada")

        genero = Genero.objects.get(id=genero_id)
        director = Director.objects.get(id=director_id)

        nuevaPelicula = Pelicula.objects.create(
            titulo=titulo,
            duracion=duracion,
            sinopsis=sinopsis,
            genero=genero,
            director=director,
            portada=portada
        )

        return JsonResponse({
            'estado': True,
            'mensaje': 'Película registrada exitosamente.'
        })

def eliminarPelicula(request, id):
    peliculaEliminar = Pelicula.objects.get(id=id)
    peliculaEliminar.delete()
    messages.success(request, "Película eliminada exitosamente.")
    return redirect('listadoPeliculas')

def editarPelicula(request, id):
    peliculaEditar = Pelicula.objects.get(id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'editarPelicula.html', {
        'peliculaEditar': peliculaEditar,
        'generos': generos,
        'directores': directores
    })

def procesarActualizacionPelicula(request):
    id = request.POST['id']
    titulo = request.POST['titulo']
    duracion = request.POST['duracion']
    sinopsis = request.POST['sinopsis']
    genero_id = request.POST['genero']
    director_id = request.POST['director']
    portada = request.FILES.get("portada")
    peliculaConsultada = Pelicula.objects.get(id=id)
    peliculaConsultada.titulo = titulo
    peliculaConsultada.duracion = duracion
    peliculaConsultada.sinopsis = sinopsis
    peliculaConsultada.genero = Genero.objects.get(id=genero_id)
    peliculaConsultada.director = Director.objects.get(id=director_id)

    if portada:
        peliculaConsultada.portada = portada
    peliculaConsultada.save()
    messages.success(request, "Pelicula actualizada exitosamente.")
    return redirect('listadoPeliculas')

# ---------------------------------------------------------------------PAISES------------------------------------------------------------
def ListadoPaises(request):
    paises = Pais.objects.all()
    return render(request, "listadoPaises.html", {'paises': paises})

def eliminarPais(request, id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "País eliminado exitosamente.")
    return redirect('listadoPaises')

def nuevoPais(request):
    return render(request, 'nuevoPais.html')

def guardarPais(request):
    nom = request.POST["nombre"]
    con = request.POST["continente"]
    cap = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nom, continente=con, capital=cap)
    messages.success(request, "País registrado exitosamente.")
    return redirect('listadoPaises')

def editarPais(request, id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

def procesarActualizacionPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    paisConsultado = Pais.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, "País actualizado exitosamente.")
    return redirect('listadoPaises')

# --------------------------------------------------------------DIRECTORES------------------------------------------------------
def ListadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directores})

def gestionDirectores(request):
    return render(request, 'gestionDirectores.html')

@csrf_exempt
def guardarDirector(request):
    if request.method == 'POST':
        dni = request.POST.get("dni")
        apellido = request.POST.get("apellido")
        nombre = request.POST.get("nombre")
        foto = request.FILES.get("foto")
        nuevoDirector = Director.objects.create(dni=dni, apellido=apellido, nombre=nombre, foto=foto)
        return JsonResponse({
            'estado': True,
            'mensaje': 'Director registrado exitosamente.'
        })

# --------------------------------------FUNCION para gestionar el CRUD de cine---------------
def ListadoCines(request):
    cines = Cine.objects.all()
    return render(request, "listadoCines.html", {'cines': cines})

def gestionCines(request):
    return render(request, 'gestionCines.html')

@csrf_exempt
def guardarCine(request):
    if request.method == 'POST':
        nom = request.POST.get("nombre")
        dir = request.POST.get("direccion")
        tel = request.POST.get("telefono")
        nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
        return JsonResponse({
            'estado': True,
            'mensaje': 'Cine registrado exitosamente.'
        })
