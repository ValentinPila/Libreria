from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Biblioteca(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=300)
    Telefono = models.CharField(max_length=10)
    HorarioApertura = models.TimeField()
    HorarioCierre = models.TimeField()

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('biblioteca')

class Autor(models.Model):
    Nombre = models.CharField(max_length=100)
    ApellidosP = models.CharField(max_length=100)
    ApellidosM = models.CharField(max_length=100)
    FechaNac = models.DateField()

    Seleccionar = 'Seleccionar'
    Masculino = 'Masculino'
    Femenino = 'Femenino'

    TipoDeGenero = [
        (Seleccionar, 'Seleccionar'),
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
    ]
    Genero = models.CharField(max_length=20, choices=TipoDeGenero, default = 'Seleccionar')

    Edad = models.IntegerField()
    Foto = models.ImageField(upload_to='poster/', blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('autor')

class Editorial(models.Model):
    Nombre = models.CharField(max_length=150)
    FechaCreacion = models.DateField()
    Logo = models.ImageField(upload_to='poster/', blank=True)
    Ubicacion = models.CharField(max_length=300)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('editorial')

class GeneroLiterario(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre


class Libro(models.Model):
    Nombre = models.CharField(max_length=150)
    NumSerie = models.IntegerField()
    Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    Precio = models.IntegerField()
    Genero = models.ForeignKey(GeneroLiterario, on_delete=models.CASCADE)
    Portada = models.ImageField(upload_to='poster/', blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('libro')

class Compras(models.Model):
    NombreUsuario = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    NombreLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreLibro

class Comentarios(models.Model):
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE, related_name='comentarios',)
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('libro_detalle', args=[str(self.libro_id)])