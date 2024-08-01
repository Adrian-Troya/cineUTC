from django.db import models

# Creando un modelo Genero: Terror, Comedia
#indentacion espacio que deja los atributos con la class.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True) 
    foto = models.ImageField(upload_to='generos/fotos/', blank=True, null=True)
    #Cambiar la estructura de 
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)    
    
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    gmail = models.EmailField(max_length=254, blank=True, null=True)  # Nuevo campo
    estado = models.BooleanField(default=True)
    portada = models.ImageField(upload_to='directores/', blank=True, null=True)

    def __str__(self):
        fila = "{0}: {1} - {2}  {3} - {4}"
        return fila.format(self.id, self.dni, self.apellido, self.nombre, self.estado)

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=150)
    continente=models.CharField(max_length=150)
    capital=models.CharField(max_length=150)
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.continente,self.capital)
    
class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE) #llamando a la clave primaria de Género y traba con funcion casacada
    director=models.ForeignKey(Director, on_delete=models.CASCADE) #llamamos a la calve primaria de Director y traba con funcion casacada.
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.titulo) #self referenciando a la clase y toma los atributos
    
# Nuevo modelo de Cine para gestionar 
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=250)
    telefono=models.CharField(max_length=150, default='')
    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id,self.nombre, self.direccion, self.telefono) #self referenciando a la clase y toma los atributos
    