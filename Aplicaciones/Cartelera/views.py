from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Pelicula, Director, Pais, Cine
from django.contrib import messages
#IMPORTACIONES PARA CORREO ELECTRONICO
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse

#importaciones prueba para cine
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def home(request):
    return render(request,"home.html")

# Listado de Géneros
def listadoGeneros(request):
    generos = Genero.objects.all()
    return render(request, "listadoGeneros.html", {'generos': generos})

# Se recibe el id para eliminar un género
def eliminarGeneros(request, id):
    genero = get_object_or_404(Genero, id=id)
    genero.delete()
    messages.success(request, 'Género eliminado exitosamente.')
    return redirect('listadoGeneros')

# Renderizando formulario de nuevo género
def nuevoGenero(request):
    return render(request, "nuevoGenero.html")

# Insertando datos en géneros
def guardarGenero(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        estado = request.POST.get('estado') == 'True'  # Convertir a booleano
        foto = request.FILES.get('foto')
        
        if not nombre or estado is None:  # Asegúrate de que 'nombre' y 'estado' están presentes
            messages.error(request, 'Nombre y Estado son requeridos.')
            return redirect('nuevoGenero')
        
        # Crear una nueva instancia de Genero
        nuevoGenero = Genero(
            nombre=nombre,
            descripcion=descripcion,
            estado=estado,
            foto=foto
        )
        nuevoGenero.save()
        messages.success(request, "Género registrado exitosamente.")
        return redirect('listadoGeneros')
    
    # Para solicitudes GET, muestra el formulario
    return render(request, 'nuevoGenero.html')

# Renderizando formulario de actualización de género
def editarGenero(request, id):
    generoEditar = get_object_or_404(Genero, id=id)
    return render(request, 'editarGenero.html', {'generoEditar': generoEditar})

# Actualizar datos del género en la BDD
def procesoActualizarGeneros(request, id):
    if request.method == 'POST':
        generoConsultado = get_object_or_404(Genero, id=id)
        
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        estado = request.POST.get('estado') == 'True'  # Convertir a booleano
        
        if not nombre or estado is None:  # Asegúrate de que 'nombre' y 'estado' están presentes
            messages.error(request, 'Nombre y Estado son requeridos.')
            return redirect('editarGenero', id=id)
        
        generoConsultado.nombre = nombre
        generoConsultado.descripcion = descripcion
        generoConsultado.estado = estado
        
        # Actualiza solo si se subieron nuevos archivos
        foto = request.FILES.get('foto')
        if foto:
            generoConsultado.foto = foto
        
        generoConsultado.save()
        messages.success(request, 'Género actualizado exitosamente.')
        return redirect('listadoGeneros')
    else:
        messages.error(request, 'Error al actualizar el género.')
        return redirect('listadoGeneros')
    

# Listado de Directores
def listadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directores})

# Se recibe el id para eliminar un director
def eliminarDirector(request, id):
    directorEliminar = get_object_or_404(Director, id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

# Renderizando formulario de nuevo director
def nuevoDirector(request):
    return render(request, "nuevoDirector.html")

# Insertando datos en directores
def guardarDirector(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        apellido = request.POST.get('apellido')
        nombre = request.POST.get('nombre')
        gmail = request.POST.get('gmail')
        estado_str = request.POST.get('estado')  # 'True' o 'False'
        estado = estado_str == 'True'  # Convertir a booleano

        portada = request.FILES.get('portada')  # Puede ser None si no se carga una nueva fotografía

        Director.objects.create(
            dni=dni,
            apellido=apellido,
            nombre=nombre,
            gmail=gmail,
            estado=estado,
            portada=portada
        )

        messages.success(request, 'Director guardado exitosamente.')
        return redirect('listadoDirectores')
    else:
        messages.error(request, 'Error al guardar el director.')
        return redirect('listadoDirectores')

# Renderizando formulario de actualización de director
def editarDirector(request, id):
    directorEditar = get_object_or_404(Director, id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

# Actualizar datos del director en la BDD
def procesoActualizarDirector(request, id):
    if request.method == 'POST':
        directorConsultado = get_object_or_404(Director, id=id)
        directorConsultado.dni = request.POST['dni']
        directorConsultado.apellido = request.POST['apellido']
        directorConsultado.nombre = request.POST['nombre']
        directorConsultado.gmail = request.POST.get('gmail', '')

        # Convertir el estado de cadena a booleano
        estado_str = request.POST.get('estado', 'True')  # Por defecto 'True' si no se proporciona valor
        directorConsultado.estado = estado_str == 'True'
        
        portada = request.FILES.get('portada')
        if portada:
            directorConsultado.portada = portada
        
        directorConsultado.save()
        messages.success(request, 'Director actualizado exitosamente.')
        return redirect('listadoDirectores')
    else:
        messages.error(request, 'Error al actualizar el director.')
        return redirect('listadoDirectores')
    
    

# Listado de Países
def listadoPaises(request):
    paises = Pais.objects.all()
    return render(request, "listadoPaises.html", {'paises': paises})

# Se recibe el id para eliminar un país
def eliminarPais(request, id):
    paisEliminar = get_object_or_404(Pais, id=id)
    paisEliminar.delete()
    messages.success(request, "País eliminado exitosamente.")
    return redirect('listadoPaises')

# Renderizando formulario de nuevo país
def nuevoPais(request):
    return render(request, "nuevoPais.html")

# Insertando datos en países
def guardarPais(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        continente = request.POST['continente']
        capital = request.POST['capital']
        
        nuevoPais = Pais.objects.create(
            nombre=nombre, continente=continente, capital=capital
        )
        messages.success(request, "País registrado exitosamente.")
        return redirect('listadoPaises')

# Renderizando formulario de actualización de país
def editarPais(request, id):
    paisEditar = get_object_or_404(Pais, id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

# Actualizar datos del país en la BDD
def procesoActualizarPais(request, id):
    if request.method == 'POST':
        paisConsultado = get_object_or_404(Pais, id=id)
        paisConsultado.nombre = request.POST['nombre']
        paisConsultado.continente = request.POST['continente']
        paisConsultado.capital = request.POST['capital']
        
        paisConsultado.save()
        messages.success(request, 'País actualizado exitosamente.')
        return redirect('listadoPaises')
    else:
        messages.error(request, 'Error al actualizar el país.')
        return redirect('listadoPaises')




#Renderizando el template de ListadoCines
def listadoCines(request):
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
        
        
#Directores
def listadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directores})

def gestionDirectores(request):
    return render(request, 'gestionDirectores.html')

@csrf_exempt
def guardarDirector(request):
    if request.method == 'POST':
        nom = request.POST.get("nombre")
        ape = request.POST.get("apellido")
        email = request.POST.get("email")
        nuevoDirector = Director.objects.create(nombre=nom, apellido=ape, email=email)
        return JsonResponse({
            'estado': True,
            'mensaje': 'Director registrado exitosamente.'
        })
        
        
        
#************************************************************************************************
# Listado de Películas
def listadoPeliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculas})

# Gestionar Películas
def gestionPeliculas(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'gestionPeliculas.html', {'generos': generos, 'directores': directores})

# Crear nueva película
@csrf_exempt
def guardarPelicula(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        duracion = request.POST.get('duracion')
        sinopsis = request.POST.get('sinopsis')
        genero_id = request.POST.get('genero')
        director_id = request.POST.get('director')
        publicado = 'publicado' in request.POST
        fecha_publicacion = request.POST.get('fecha_publicacion')

        if not all([titulo, duracion, sinopsis, genero_id, director_id, fecha_publicacion]):
            return JsonResponse({
                'estado': False,
                'mensaje': 'Todos los campos son requeridos.'
            })

        try:
            genero = Genero.objects.get(id=genero_id)
            director = Director.objects.get(id=director_id)
        except Genero.DoesNotExist or Director.DoesNotExist:
            return JsonResponse({
                'estado': False,
                'mensaje': 'Género o director no encontrado.'
            })

        Pelicula.objects.create(
            titulo=titulo,
            duracion=duracion,
            sinopsis=sinopsis,
            genero=genero,
            director=director,
            publicado=publicado,
            fecha_publicacion=fecha_publicacion
        )
        
        return JsonResponse({
            'estado': True,
            'mensaje': 'Película registrada exitosamente.'
        })

# Editar película
def editarPelicula(request, id):
    peliculaEditar = get_object_or_404(Pelicula, id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'editarPelicula.html', {'peliculaEditar': peliculaEditar, 'generos': generos, 'directores': directores})

# Actualizar datos de la película en la BDD
@csrf_exempt
def procesoActualizarPelicula(request, id):
    if request.method == 'POST':
        peliculaConsultada = get_object_or_404(Pelicula, id=id)
        titulo = request.POST.get('titulo')
        duracion = request.POST.get('duracion')
        sinopsis = request.POST.get('sinopsis')
        genero_id = request.POST.get('genero')
        director_id = request.POST.get('director')
        publicado = 'publicado' in request.POST
        fecha_publicacion = request.POST.get('fecha_publicacion')

        if not all([titulo, duracion, sinopsis, genero_id, director_id, fecha_publicacion]):
            return JsonResponse({
                'estado': False,
                'mensaje': 'Todos los campos son requeridos.'
            })

        try:
            genero = Genero.objects.get(id=genero_id)
            director = Director.objects.get(id=director_id)
        except Genero.DoesNotExist or Director.DoesNotExist:
            return JsonResponse({
                'estado': False,
                'mensaje': 'Género o director no encontrado.'
            })

        peliculaConsultada.titulo = titulo
        peliculaConsultada.duracion = duracion
        peliculaConsultada.sinopsis = sinopsis
        peliculaConsultada.genero = genero
        peliculaConsultada.director = director
        peliculaConsultada.publicado = publicado
        peliculaConsultada.fecha_publicacion = fecha_publicacion
        peliculaConsultada.save()

        return JsonResponse({
            'estado': True,
            'mensaje': 'Película actualizada exitosamente.'
        })

# Eliminar una película
@csrf_exempt
def eliminarPelicula(request, id):
    try:
        peliculaEliminar = Pelicula.objects.get(id=id)
        peliculaEliminar.delete()
        return JsonResponse({
            'estado': True,
            'mensaje': 'Película eliminada exitosamente.'
        })
    except Pelicula.DoesNotExist:
        return JsonResponse({
            'estado': False,
            'mensaje': 'Película no encontrada.'
        })