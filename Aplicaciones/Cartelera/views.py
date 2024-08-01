from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Pelicula, Director, Pais, Cine
from django.contrib import messages
#IMPORTACIONES PARA CORREO ELECTRONICO
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from django.http import HttpResponse, JsonResponse

#importaciones prueba para cine
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
def home(request):
    return render(request,"home.html")
# ---------------------------------------------------------------------GENEROS------------------------------------------------------------
#Renderizando el template de ListadoGeneros
def ListadoGeneros(request):
    generos=Genero.objects.all()
    return render(request,"listadoGeneros.html", {'generos': generos})

#Se recibe el id para eliminar un genro
def eliminarGenero(request, id):
    generoEliminar=Genero.objects.get(id=id) #el primer id representa el modelo la base de datos, el segundo id representa el parametro
    generoEliminar.delete()
    messages.success(request,"Género eliminado exitosamente.")
    return redirect('listadoGeneros')
#Renderizando formulario de nuevo genero
def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

#Insertando generos en la base de datos
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request,"Género registrado exitosamente.")
    return redirect('listadoGeneros')

# Renderizando formulario de actualización
def editarGenero(request, id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html' ,{'generoEditar':generoEditar})

#Actualizando los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    foto=request.FILES.get("foto")
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    if foto:
        generoConsultado.foto = foto
    generoConsultado.save()
    messages.success(request,"Género actualizado exitosamente.")
    return redirect('listadoGeneros')


# ---------------------------------------------------------------------PELICULAS------------------------------------------------------------
# Renderizando el template de ListadoPeliculas
def ListadoPeliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculas})

# Renderizando el template de Gestión de Peliculas
def gestionPeliculas(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'gestionPeliculas.html', {'generos': generos, 'directores': directores})

# Insertando película mediante AJAX en la base de datos
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



#Se recibe el id para eliminar una pelicula
def eliminarPelicula(request, id):
    peliculaEliminar=Pelicula.objects.get(id=id) #el primer id representa el modelo la base de datos, el segundo id representa el parametro
    peliculaEliminar.delete()
    messages.success(request,"Película eliminada exitosamente.")
    return redirect('listadoPeliculas')


# Renderizando formulario de actualización
def editarPelicula(request, id):
    peliculaEditar=Pelicula.objects.get(id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request,'editarPelicula.html' ,{
        'peliculaEditar':peliculaEditar,
        'generos': generos,
        'directores': directores
    })

#Actualizando los nuevos datos en la BDD
def procesarActualizacionPelicula(request):
    id=request.POST['id']
    titulo = request.POST['titulo']
    duracion = request.POST['duracion']
    sinopsis = request.POST['sinopsis']
    genero_id = request.POST['genero']
    director_id = request.POST['director']
    portada=request.FILES.get("portada")
    peliculaConsultada=Pelicula.objects.get(id=id)
    peliculaConsultada.titulo = titulo
    peliculaConsultada.duracion = duracion
    peliculaConsultada.sinopsis = sinopsis
    
    # Actualizar claves foráneas
    peliculaConsultada.genero = Genero.objects.get(id=genero_id)
    peliculaConsultada.director = Director.objects.get(id=director_id)

    if portada:
        peliculaConsultada.portada = portada
    peliculaConsultada.save()
    messages.success(request,"Pelicula actualizada exitosamente.")
    return redirect('listadoPeliculas')

# ---------------------------------------------------------------------PAISES------------------------------------------------------------
#Renderizando el template de ListadoPaises
def ListadoPaises(request):
    paises=Pais.objects.all()
    return render(request,"listadoPaises.html", {'paises': paises})

#Se recibe el id para eliminar un país
def eliminarPais(request, id):
    paisEliminar=Pais.objects.get(id=id) #el primer id representa el modelo la base de datos, el segundo id representa el parametro
    paisEliminar.delete()
    messages.success(request,"País eliminado exitosamente.")
    return redirect('listadoPaises')
#Renderizando formulario de nuevo pais
def nuevoPais(request):
    return render(request, 'nuevoPais.html')

#Insertando paises en la base de datos
def guardarPais(request):
    nom=request.POST["nombre"]
    con=request.POST["continente"]
    cap=request.POST["capital"]
    nuevoPais=Pais.objects.create(nombre=nom, continente=con, capital=cap)
    messages.success(request,"País registrado exitosamente.")
    return redirect('listadoPaises')

# Renderizando formulario de actualización
def editarPais(request, id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html' ,{'paisEditar':paisEditar})

#Actualizando los nuevos datos en la BDD
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,"País actualizado exitosamente.")
    return redirect('listadoPaises')


# --------------------------------------------------------------DIRECTORES------------------------------------------------------
# Renderizando el template de ListadoDirectores
def ListadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directores})

def gestionDirectores(request):
    return render(request, 'gestionDirectores.html')

# Insertando director mediante AJAX en la base de datos
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

#--------------------------------------------------------------------


#--------------------------------------FUNCION para gestionar el CRUD de cine---------------
#Renderizando el template de ListadoCines
def ListadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines': cines})

def gestionCines(request):
    return render(request, 'gestionCines.html')

#insertando cine mediante AJAX en la base de datos
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
#--------------------------------------CORREO ELECTRONICO---------------

def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
            '',
            ["javierguala07@gmail.com"],
            reply_to=[email])
            
            try:
                email.send()

                return redirect("/correo/?valido")
            except:
                return redirect("/correo/?novalido")
           
    return render(request, "correo.html", {'miFormulario':formulario_contacto})